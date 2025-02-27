from sqlalchemy import Column, String, Integer, ForeignKey, Table
from app.config.database import Base


class Project_Video(Base):
  __tablename__ = "project_video"
  id = Column(Integer, autoincrement=True, primary_key=True, index=True)
  name = Column(String, nullable=False)
  type = Column(String, nullable=False, insert_default="Video")
  
  projects_videos = Table(
    "projects_videos_User",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("project_id", Integer, ForeignKey("project_video.id"), primary_key=True)
  )
  
  projects_videos = Table(
    "projects_videos_Team",
    Base.metadata,
    Column("team_id", Integer, ForeignKey("team.id"), primary_key=True),
    Column("project_id", Integer, ForeignKey("project_video.id"), primary_key=True)
  )