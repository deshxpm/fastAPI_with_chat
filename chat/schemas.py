from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

class MessageCreate(BaseModel):
    receiver_id: int
    message: str

class MessageResponse(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    message: str
