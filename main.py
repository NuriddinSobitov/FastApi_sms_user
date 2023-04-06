from fastapi import FastAPI

import models
from celery_utils import create_celery
from database import engine
from routers import api

app = FastAPI()

app.celery_app = create_celery()
celery = app.celery_app


@app.on_event('startup')
async def startup_event():
    # models.Base.metadata.drop_all(engine)
    # models.Base.metadata.create_all(engine)
    app.include_router(router=api)
