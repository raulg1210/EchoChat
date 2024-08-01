from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from src.models.messageModel import Message
from src.schemas.message_schemas import UpdateMessage, CreateMessage

class MessageService:
    def get_all_messages(self, db: Session) -> List[Message]:
        return db.query(Message).all()
    
    def get_message_by_id(self, db: Session, id: int) -> Message:
        return db.query(Message).filter(Message.id == id).first()
    
    def create_message(self, db: Session, message: CreateMessage) -> Message:
        new_message = Message(
            content=message.content,
            sender_id=message.sender_id,
            receiver_id=message.receiver_id,
            created_at=datetime.now()
        )
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        return new_message
    
    def update_message(self, db: Session, id: int, message: UpdateMessage) -> Message:
        message_to_update = db.query(Message).filter(Message.id == id).first()
        message_to_update.content = message.content
        db.commit()
        db.refresh(message_to_update)
        return message_to_update
    
    def delete_message(self, db: Session, id: int) -> Message:
        message_to_delete = db.query(Message).filter(Message.id == id).first()
        db.delete(message_to_delete)
        db.commit()
        return message_to_delete