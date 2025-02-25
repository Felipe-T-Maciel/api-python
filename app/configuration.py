from app.database import engine, Base
from app.models.User import User
from app.models.Project import Project_Document

def configure_all():
  Base.metadata.create_all(bind=engine)