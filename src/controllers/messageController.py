from src.db.connection import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.services.messageService import MessageService
from src.schemas.message_schemas import CreateMessage, UpdateMessage

router = APIRouter()

messageService = MessageService()

@router.get("/messages")
def get_all_messages(db: Session = Depends(get_db)):
    return messageService.get_all_messages(db)  

@router.get("/messages/{id}")
def get_message_by_id(id: int, db: Session = Depends(get_db)):
    return messageService.get_message_by_id(db, id)

@router.post("/messages")
def create_message(message: CreateMessage, db: Session = Depends(get_db)):
    return messageService.create_message(db, message)

@router.put("/messages/{id}")
def update_message(id: int, message: UpdateMessage, db: Session = Depends(get_db)):
    return messageService.update_message(db, id, message)

@router.delete("/messages/{id}")
def delete_message(id: int, db: Session = Depends(get_db)):
    return messageService.delete_message(db, id)

