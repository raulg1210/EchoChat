from pydantic import BaseModel
from typing import Optional

class UpdateMessage(BaseModel):
    content: Optional[str]
    
    class Config:
        orm_mode = True
        
class CreateMessage(BaseModel):
    content: str
    sender_id: int
    receiver_id: int