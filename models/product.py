from sqlalchemy.orm import deferred
from sqlalchemy.sql.sqltypes import LargeBinary
from sqlalchemy.util.langhelpers import hybridproperty
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref, attribute_mapped_collection
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import PasswordUtil

Base = declarative_base()

class Product(Base):
    __tablename__ = "Product"
    Id = Column(int, primary_key=True)
    Name = Column(String(255))
    UPC = Column(String(255))
    
    items = relationship(
        "Product_Item",
        cascade="all, delete-orphan",
        backref=backref("parent", remote_side=id),
        collection_class=attribute_mapped_collection("name"),
    )
