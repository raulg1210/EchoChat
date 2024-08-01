from src.db.base import Base
from src.db.connection import engine
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from src.models.userModel import User
from src.schemas.user_schemas import UpdateUser, CreateUser

class UserService:
    def get_all_users(self, db: Session) -> List[User]:
        return db.query(User).all()
    
    def get_user_by_username(self, db: Session, username: str) -> User:
        return db.query(User).filter(User.username == username).first()
    
    def create_user(self, db: Session, user: CreateUser) -> User:
        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=user.hashed_password,
            created_at=datetime.now()
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    def update_user(self, db: Session, username: str, user: UpdateUser) -> User:
        user_to_update = db.query(User).filter(User.username == username).first()
        user_to_update.name = user.name
        user_to_update.email = user.email
        user_to_update.hashed_password = user.hashed_password
        user_to_update.updated_at = datetime.now()
        db.commit()
        db.refresh(user_to_update)
        return user_to_update
    
    def delete_user(self, db: Session, username: str) -> User:
        user_to_delete = db.query(User).filter(User.username == username).first()
        db.delete(user_to_delete)
        db.commit()
        return user_to_delete