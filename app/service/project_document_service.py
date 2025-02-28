from app.config.database import SessionLocal
from app.models.DTO.project_document import ProjectDocumentDTO_Post
from app.models.projects.Project_document import Project_Document

class Project_Document_Service():
  
  def __init__(self):
    db = SessionLocal()
    self.db = db
    
  def create_project_document(self, project_document: ProjectDocumentDTO_Post):
    new_project_document = Project_Document(
      name=project_document.name,
      type=project_document.type
    )
    self.db.add(new_project_document)
    self.db.commit()
    self.db.refresh(new_project_document)
    return new_project_document