
from fastapi import APIRouter
from app.models.DTO.team.teamPostDTO import TeamPostDTO
from app.service.team_service import Team_Service

team_service = Team_Service()
team_controller = APIRouter()

class Team_Controller():
  
  @team_controller.post("/team/new_team")
  def create_team(team: TeamPostDTO):
    new_team = team_service.create_team(team)
    return {"message": "Deu boa", "team": new_team}
  
  @team_controller.put("/team/update/{team_id}")
  def update_team(team: TeamPostDTO, team_id: int):
    team = team_service.update_team(team, team_id)
    if not team:
      return {"message":"Time não encontrado"}
    return {"message": "Deu boa", "team": team}
  
  @team_controller.delete("/team/delete/{team_id}")
  def delete_team(team_id: int):
    if team_service.delete_team(team_id) != None:
      return {"message":"Time deletado"}
    return {"message":"Time não encontrado"}
  
  @team_controller.get("/team/{team_id}")
  def get_team_by_id(team_id: int):
    team = team_service.get_team_by_id(team_id)
    if not team:
      return {"message":"Time não encontrado"}
    return {"message": "Deu boa", "team": team}
  