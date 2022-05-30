from core.crud import *
from datetime import timedelta, datetime
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi import HTTPException, status
from models.user import User
from passlib.hash import pbkdf2_sha256

def attempt_login(form, db, Authorize):
    """Attempts to log user in and set JWT token when successful. 
    Assumes basic form validation has already occurred."""
    email = form.username
    pwd = form.password
    foundUser = get_user(db, email)
    if not foundUser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    if checkPassword(pwd, foundUser.Password):
        return create_tokens(foundUser, Authorize)
    else:
        print('Bad Password')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
def create_tokens(user: User, Authorize):
    access_token = Authorize.create_access_token(subject=user.Email)
    refresh_token = Authorize.create_refresh_token(subject=user.Email)
    print(access_token)
    print(refresh_token)
    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)
    return access_token, refresh_token



def hash(pwd) -> str:
    return pbkdf2_sha256.hash(pwd)

def checkPassword(pwd, hashed) -> bool:
    return pbkdf2_sha256.verify(pwd, hashed)