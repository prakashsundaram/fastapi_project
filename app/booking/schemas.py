from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    phonenumber: Optional[str]=None
    gender: Optional[int]=None
    password: str
    class Config:
        orm_mode = True

