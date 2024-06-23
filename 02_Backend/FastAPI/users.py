from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# Inicia el server: uvicorn users:app --reload

class User(BaseModel):
  id: int
  name: str
  surname: str
  url: str
  age: int

users_list = [
  User(id=0, name="Diego", surname="Chiapa", url="diegochiapa.com.ar", age=32),
  User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
  User(id=2, name="Haakon", surname="Dahlberg", url="https://haakon.com", age=33)
]

@app.get("/users")
async def users():
  return users_list

# path
@app.get("/user/{id}")
async def user(id: int):
  return search_user(id)
  
# query
@app.get("/user/")
async def user(id: int):
  return search_user(id)

def search_user(id: int):
  users = filter(lambda user: user.id == id, users_list)
  try:
    return list(users)[0]
  except:
    return {"error": "No se ha encontrado el usuario."}