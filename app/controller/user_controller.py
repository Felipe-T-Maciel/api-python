from app.models.User import User
from app.service.user_service import User_service
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.models.DTO.UserPostDTO import UserPostDTO
from app.config.database import SessionLocal

userController = APIRouter()
user_service = User_service()

class User_Controller():
  
  
  @userController.post("/user/new_user")
  def create_user(user: UserPostDTO):
    existing_user = user_service.get_user_by_username(username=user.username)
    if existing_user:
      return {"message":"Usuário já existe"}
    
    existing_user = user_service.get_user_by_email(email=user.email)
    if existing_user:
      return {"message":"Usuário já existe"}
    
    new_user = user_service.create_user(name=user.name, username=user.username, email=user.email, password=user.password)
    return {"message": "Deu boa", "user": new_user}
  
  @userController.get("/user/update")
  def update_user(user: UserPostDTO):
    
    return {"message":"Teste"}