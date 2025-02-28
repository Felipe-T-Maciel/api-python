from app.config.database import SessionLocal
from app.models.DTO.team.teamPostDTO import TeamPostDTO
from app.models.Team import Team

class Team_Service():
  
  def __init__(self):
    db = SessionLocal()
    self.db = db
  
  def create_team(self, team: TeamPostDTO):
    new_team = Team(
      name=team.name
    )
    self.db.add(new_team)
    self.db.commit()
    self.db.refresh(new_team)
    return new_team
  
  def get_team_by_id(self, team_id: int):
    return self.db.query(Team).filter(Team.id == team_id).first()
  
  def update_team(self, team: TeamPostDTO, team_id: int):
    old_team = self.get_team_by_id(team_id)
    for(key, value) in vars(team).items():
      if value is not None:
        setattr(old_team, key, value)
    
    self.db.add(old_team)
    self.db.commit()
    self.db.refresh(old_team)
    return old_team
  
  def delete_team(self, team_id: int):
    team = self.get_team_by_id(team_id)
    if not team:
      return None
    
    self.db.delete(team)
    self.db.commit()
    return team