from pydantic import BaseModel

class ProjectDocumentDTO_Post(BaseModel):
  name : str
  type : str