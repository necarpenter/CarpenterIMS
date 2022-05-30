from typing import List
from typing import Optional
from sqlalchemy import false, true

from fastapi import Request
import core.crud as crud

class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.email: Optional[str] = None
        self.username: Optional[str] = None
        self.password: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.email = form.get("email")
        self.username = form.get("email")
        self.password = form.get("password")

    async def empty_form(self):
        print(self.username)
        if not self.username and not self.password:
            return true
        return false

    async def is_valid(self):
        if not self.username or not (self.username.__contains__("@")):
            self.errors.append("Email is required")
        if not self.password or not len(self.password) >= 4:
            self.errors.append("A valid password is required")
        if not self.errors:
            return True
        return False
    async def check_user(self):
        crud.get_user()