from app.config.database import engine, Base
from app.models.User import User
from app.models.projects.Project_document import Project_Document
from app.models.projects.Project_video import Project_Video
from app.models.projects.Project_paint import Project_Paint
from app.models.Team import Team

def configure_all():
  Base.metadata.create_all(bind=engine)