from src.services.userService import UserService
from src.db.connection import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.user_schemas import CreateUser, UpdateUser

router = APIRouter()
userService = UserService()

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    return userService.get_all_users(db)

@router.get("/users/{username}")
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return userService.get_user_by_username(db, username)

@router.post("/users")
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    return userService.create_user(db, user)

@router.put("/users/{username}")
def update_user(username: str, user: dict, db: Session = Depends(get_db)):
    return userService.update_user(db, username, user)

@router.delete("/users/{username}")
def delete_user(username: str, db: Session = Depends(get_db)):
    return userService.delete_user(db, username)