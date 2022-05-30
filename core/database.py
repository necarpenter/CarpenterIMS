from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json



credsfile = open('./core/dbcreds.json')
creds = json.load(credsfile)
engine = create_engine(f"{creds['engine']}://{creds['username']}:{creds['password']}@{creds['host']}/{creds['database']}?charset={creds['charset']}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()