from fastapi import Form
from pydantic import BaseModel


class ProductForm(BaseModel):
    name: str
    price: float

    class Config:
        orm_mode = True

    @classmethod
    def as_form(
            cls,
            name: str = Form(...),
            price: int = Form(...)
    ):
        return cls(name=name,price=price)