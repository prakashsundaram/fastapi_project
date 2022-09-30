from fastapi import FastAPI
from Booking import models
from .Booking.database import engine
from .Booking.routers import user

app = FastAPI()

@app.get('/')
def index():
    return "Hello Prakash!"

app.include_router(user.router)

models.Base.metadata.create_all(engine)
