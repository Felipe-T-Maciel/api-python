from sqlalchemy import Column, Table, String, Integer, ForeignKey
from app.database import Base

class Team(Base):
  __tablename__ = "team"
  id = Column(Integer, autoincrement=True, primary_key=True)
  name = Column(String)
  users = []
  projects = []
  
  teams = Table(
    "teams_users",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("team_id", Integer, ForeignKey("team.id"), primary_key=True)
  )
  