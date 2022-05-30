from typing import List
from typing import Optional
from sqlalchemy import false, true
from models.product import Product
from fastapi import Request
from sqlalchemy.orm import Session
import core.crud as crud


class ProductForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.id: Optional[int] = None
        self.name: Optional[str] = None
        self.upc: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.id = form.get("id")
        self.name = form.get("name")
        self.upc = form.get("upc")

    async def load_data_with_product(self, Prod: Product):
        self.id = Prod.Id
        self.name = Prod.Name
        self.upc = Prod.UPC

    async def empty_form(self):
        print(self.name)
        if not self.name and not self.upc:
            return true
        return false

    async def is_valid(self):
        if not self.name:
            self.errors.append("Name is required")
        if not self.upc:
            self.errors.append("UPC is required")
        if not self.errors:
            return True
        return False

    async def saveProduct(self, db: Session):
        prod: Product = crud.get_product(db, self.id)
        prod.Name = self.name
        prod.UPC = self.upc
        db.add(prod)
