from fastapi import FastAPI, Request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi.responses import HTMLResponse
import json
from fastapi.templating import Jinja2Templates
import LoginForm

credsfile = open('dbcreds.json')
creds = json.load(credsfile)
engine = create_engine(f"{creds['engine']}://{creds['username']}:{creds['password']}@{creds['host']}/{creds['database']}?charset={creds['charset']}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

templates = Jinja2Templates(directory="templates")

Base = declarative_base()

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": '1234'})


@app.get("/login/")
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})