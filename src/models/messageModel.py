from sqlalchemy import Column, Integer, String, DateTime
from src.db.base import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, nullable=False)
    receiver_id = Column(Integer, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    
    def __repr__(self):
        return f"Message(id={self.id!r}, message={self.content!r}), sender_id={self.sender_id!r}, receiver_id={self.receiver_id!r}"