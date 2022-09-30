from fastapi import FastAPI
from .booking import models
from .booking.database import engine
from .booking.routers import user

app = FastAPI()

@app.get('/')
def index():
    return "Hello Prakash!"

app.include_router(user.router)

models.Base.metadata.create_all(engine)
