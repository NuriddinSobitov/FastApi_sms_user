from faker import Faker
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from database import get_db
from forms import ProductForm
from hashing import Hasher
from celery_tasks.send_email import send_verification_email

api = APIRouter()
@api.post('/add_user')
async def generate_fake_users(
        n: int,
        db: Session = Depends(get_db),
):
    faker = Faker()
    users = []
    for _ in range(n):  # CLIENT
        users.append(
            models.Users(
                name=faker.name(),
                email=faker.email(),
                password=Hasher.get_password_hash('1')
            )
        )
    db.add_all(users)
    db.commit()
    db.close()




@api.post('/add_product')
async def add_product(
        db: Session = Depends(get_db),
        form: ProductForm = Depends(ProductForm.as_form)
):
    data = form.dict(exclude_none=True)
    product = models.Products(**data)
    db.add(product)
    db.commit()
    product = form.name
    users = db.query(models.Users).all()
    for i in users:
        send_verification_email.delay(i,product)
    return 'zor'


