from sqlalchemy import Column, ForeignKey, Integer, String, Table, ARRAY
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.projects.Project_document import Project_Document
import bcrypt

class User(Base):
  __tablename__ = "user"
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  name = Column(String, nullable=False)
  username = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)
  email = Column(String, nullable=False)
  friends = Column(ARRAY(Integer))
  invites = Column(ARRAY(Integer))
  
  teams = []
  my_friends = []
  projects_videos = []
  projects_paints = []
  
  friends = relationship(
        "User",
        secondary=friends,
        primaryjoin=id == friends.c.user_id,
        secondaryjoin=id == friends.c.friend_id,
        backref="friends_list"
  )
  
  def encode_pass(password:String):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pass.decode("utf-8")
  
  def verify_pass(stored_hash:str, password:str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))