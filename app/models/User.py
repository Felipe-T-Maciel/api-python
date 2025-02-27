from sqlalchemy import Column, Integer, String, ARRAY
from app.config.database import Base
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