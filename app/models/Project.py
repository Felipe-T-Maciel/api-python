from sqlalchemy import Column, String, Integer, ForeignKey, Table
from app.database import Base
from sqlalchemy.orm import relationship


class Project_Document(Base):
  id = Column(Integer, autoincrement=True, primary_key=True, index=True)
  name = Column(String, nullable=False)
  