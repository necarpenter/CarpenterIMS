from sqlalchemy.orm import deferred
from sqlalchemy.sql.sqltypes import LargeBinary, Float
from sqlalchemy.util.langhelpers import hybridproperty
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Base = declarative_base()


class Product(Base):
    __tablename__ = "Product"
    Id = Column(Integer, primary_key=True)
    Name = Column(String(255))
    UPC = Column(String(255))

    items = relationship("Product_Item", backref='Product')


class Product_Item(Base):
    __tablename__ = "Product_Item"
    Id = Column(Integer, primary_key=True)
    ProductId = Column(Integer, ForeignKey(Product.Id))
    Qty = Column(Float)
