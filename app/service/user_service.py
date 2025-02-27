from app.models.User import User
from app.config.database import SessionLocal
import bcrypt

class User_service():
  
  def __init__(self):
     db = SessionLocal()
     self.db = db
     
  def create_user(self, name:str, username:str, email:str, password:str):
    encode_pass = self.encode_pass(password)
    
    new_user = User(
      name=name,
      username=username,
      password=encode_pass,
      email = email
    )
    self.db.add(new_user)
    self.db.commit()
    self.db.refresh(new_user)
    return new_user
  
  @staticmethod
  def encode_pass(password:str) -> str:
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pass.decode('utf-8')
  
  @staticmethod
  def verify_pass(stored_hash:str, password:str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))
  
  def get_user_by_username(self, username:str):
    return self.db.query(User).filter(User.username == username).first()
  
  def get_user_by_email(self, email:str):
    return self.db.query(User).filter(User.email == email).first()