from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from app.database import Base
import bcrypt

friends = Table(
    "friends",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("friend_id", Integer, ForeignKey("user.id"), primary_key=True)
)

class User(Base):
  __tablename__ = "user"
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  name = Column(String, nullable=False)
  username = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)
  email = Column(String, nullable=False)
  friends = relationship(
        "User",
        secondary=friends,
        primaryjoin=id == friends.c.user_id,
        secondaryjoin=id == friends.c.friend_id,
        backref="friends_list"
  )
  projects_documents = Table(
    "projects_document",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("project_id", Integer, ForeignKey("project.id"), primary_key=True)
  )
  
  def encode_pass(password:String):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pass.decode("utf-8")
  
  def verify_pass(stored_hash:str, password:str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))