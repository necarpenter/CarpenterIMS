from tokenize import Double
from sqlalchemy.orm import deferred
from sqlalchemy.sql.sqltypes import LargeBinary
from sqlalchemy.util.langhelpers import hybridproperty
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref, attribute_mapped_collection
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import PasswordUtil
from models.product import Product
Base = declarative_base()

class Product_Item(Base):
    __tablename__ = "Product_Item"
    Id = Column(int, primary_key=True)
    ProductId = Column(int, ForeignKey(Product.id))
    Qty = Column(Double)
    