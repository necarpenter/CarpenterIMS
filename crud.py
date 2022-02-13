from models.user import User
from sqlalchemy.orm import Session

def get_user(db:Session, user_email:str) -> User:
    return db.query(User).filter(User.Email == user_email).first()