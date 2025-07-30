from pydantic import BaseModel, EmailStr
from datetime import datetime

class EventCreate(BaseModel):
    name: str
    location: str
    start_time: datetime
    end_time: datetime
    max_capacity: int

class EventOut(BaseModel):
    id: int
    name: str
    location: str
    start_time: datetime
    end_time: datetime
    max_capacity: int

    class Config:
        orm_mode = True

class AttendeeCreate(BaseModel):
    name: str
    email: EmailStr

class AttendeeOut(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
