from pydantic import BaseModel

class TeamPostDTO(BaseModel):
  name : str
  users : list = []
  projects : list = []