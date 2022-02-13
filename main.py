from fastapi import FastAPI, Request, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
import json
from fastapi.templating import Jinja2Templates
from LoginForm import LoginForm
templates = Jinja2Templates(directory="templates")
from database  import SessionLocal, engine
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
import security
from pydantic import BaseModel

# Dependency

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    # Configure application to store and get JWT from cookies
    authjwt_token_location: set = {"cookies"}
    # Disable CSRF Protection for this example. default is True
    authjwt_cookie_csrf_protect: bool = False

@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": '1234'})

@app.get("/login")
async def login(request: Request):
        return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    form = LoginForm(request)
    await form.load_data()

    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login Successful :)")

            response = templates.TemplateResponse("login.html", form.__dict__)

            access_token, refresh_token  = security.attempt_login(form, db, Authorize) 
            response.set_cookie(
                key="access_token_cookie", value=f"{access_token}", httponly=True
            )      

            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("login.html", form.__dict__)
    return templates.TemplateResponse("login.html", form.__dict__)

@app.get('/user')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}