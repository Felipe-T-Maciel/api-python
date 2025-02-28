from app.config.database import engine, Base
from app.models.User import User # type: ignore
from app.models.projects.Project_document import Project_Document # type: ignore
from app.models.projects.Project_video import Project_Video # type: ignore
from app.models.projects.Project_paint import Project_Paint # type: ignore
from app.models.Team import Team # type: ignore


def configure_all():
  Base.metadata.create_all(bind=engine)