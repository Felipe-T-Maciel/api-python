from pydantic import BaseModel, EmailStr

class UserPostDTO(BaseModel):
  name : str
  username : str
  email : str
  password : str