from pydantic import BaseModel
from typing import Optional

class UpdateUser(BaseModel):
    username: Optional[str]
    email: Optional[str]
    hashed_password: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True
        
class CreateUser(BaseModel):
    username: Optional[str]
    email: Optional[str]
    hashed_password: Optional[str]

    class Config:
        orm_mode = True
