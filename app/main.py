from fastapi import FastAPI
from app.configuration import configure_all
from app.routes import router

app = FastAPI()
app.include_router(router=router)
configure_all()

@app.get("/")
def main():
  return{"message": "Hello World"}