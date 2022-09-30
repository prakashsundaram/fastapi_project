from enum import Enum
from sqlalchemy.orm import Session
from app.Booking import schemas, models, hashing
from fastapi import HTTPException, status
import re
from datetime import datetime


email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_regex = '^\\+?[1-9][0-9]{7,14}$'

class genderEnum(Enum):
    Male = 1
    Female = 2
    Others = 3

def gender(gen: int):
    for i in range(len(genderEnum)):
        if i==gen:
            return genderEnum(i).name

def create(request: schemas.User, db: Session):
    users = db.query(models.User).filter(models.User.email == request.email).first()
    if users:
        raise HTTPException(status_code=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Email address already exists")
    
    if not (re.fullmatch(email_regex, request.email)):
        raise HTTPException(status_code=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Invalid e-mail")
    
    if request.gender not in [1,2,3]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Enter 1 if male, 2 if female, 3 if others")
    user_phonenumber = db.query(models.User).filter(models.User.phonenumber == request.phonenumber).first()
    if user_phonenumber:
        raise HTTPException(status_code=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Phone number already exists")
    
    if not(re.fullmatch(phone_regex, request.phonenumber)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid phone number")
    
    
    new_user = models.User(name = request.name, email = request.email, phonenumber=request.phonenumber, gender=gender(request.gender), password = hashing.Hash.rpassword(request.password), is_active = 1, is_deleted = 0, created_timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), updated_timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user