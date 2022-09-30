from fastapi import APIRouter, Depends
from app.Booking import database
from app.Booking.database import get_db
from fastapi import APIRouter, status
from app.Booking import schemas, models
from sqlalchemy.orm import Session
from app.Booking.repository import user

get_db= database.get_db

router = APIRouter()

@router.post('/user', status_code=status.HTTP_201_CREATED)
def create(request: schemas.User, db:Session = Depends(get_db)):
    return user.create(request, db)

