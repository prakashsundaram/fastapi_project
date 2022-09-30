from sqlalchemy import Integer, String, Column, DateTime
from app.booking.database import Base
from app.booking.repository.user import gender

class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phonenumber = Column(String, unique=True)
    gender = Column(String)    
    password = Column(String)
    is_active = Column(Integer)
    is_deleted = Column(Integer)
    created_timestamp = Column(DateTime)
    updated_timestamp = Column(DateTime)