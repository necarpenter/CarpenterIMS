import bcrypt

def hash(pwd) -> str:
    return bcrypt.hashpw(pwd, bcrypt.gensalt())

def checkPassword(pwd, hashed) -> bool:
    return bcrypt.checkpw(pwd, hashed)