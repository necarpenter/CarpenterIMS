from sqlalchemy.orm import deferred
from sqlalchemy.sql.sqltypes import LargeBinary
from sqlalchemy.util.langhelpers import hybridproperty
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Base = declarative_base()


class User(Base):
    __tablename__ = "User"
    Email = Column(String(255), primary_key=True)
    Password = Column(String(255))
