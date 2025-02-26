from sqlalchemy import Column, String, Integer, ForeignKey, Table
from app.database import Base
from sqlalchemy.orm import relationship


class Project_Paint(Base):
  __tablename__ = "project_paint"
  id = Column(Integer, autoincrement=True, primary_key=True, index=True)
  name = Column(String, nullable=False)

  projects_paints = Table(
    "projects_paints_User",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("project_id", Integer, ForeignKey("project_paint.id"), primary_key=True)
  )
  
  projects_paints = Table(
    "projects_paints_Teams",
    Base.metadata,
    Column("team_id", Integer, ForeignKey("team.id"), primary_key=True),
    Column("project_id", Integer, ForeignKey("project_paint.id"), primary_key=True)
  )