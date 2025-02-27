from fastapi import FastAPI
from app.config.configuration import configure_all
from app.routes import router
from app.controller.user_controller import userController

app = FastAPI()
app.include_router(router=userController)
configure_all()

@app.get("/")
def main():
  return{"message": "Hello World"}