from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users", 
                   tags=["users"])
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
# Operación GET
@router.get("/")
async def users():
  return users_list

# path
@router.get("/{id}", response_model=User)
async def user(id: int):
  return search_user(id)
  
# query
@router.get("/", response_model=User)
async def user(id: int):
  return search_user(id)

# Operación POST
@router.post("/", response_model=User, status_code=201)
async def new_user(user: User):
  if type(search_user(user.id)) == User or type(search_user_url(user.url)) == User:
    raise HTTPException(status_code=204, detail="El usuario ya existe.")
  else:
    users_list.append(user)
    return search_user(user.id)

# Operación PUT
@router.put("/", response_model=User)
async def update_user(user: User):
  found = False
  for index, saved_user in enumerate(users_list):
    if saved_user.id == user.id:
      users_list[index] = user
      found = True
  if not found:
    return {"error": "No se ha actualizado el usuario."}
  else:
    return user
  
# Operación DELETE
@router.delete("/{id}")
async def delete_user(id: int):
  found = False
  for index, saved_user in enumerate(users_list):
    if saved_user.id == id:
      del users_list[index]
      found = True
  if not found:
    return {"error": "No se ha eliminado el usuario."}
  else:
    return users_list

def search_user(id: int):
  users = filter(lambda user: user.id == id, users_list)
  try:
    return list(users)[0]
  except:
    return {"error": "No se ha encontrado el usuario."}
  
def search_user_url(url: str):
  users = filter(lambda user: user.url == url, users_list)
  try:
    return list(users)[0]
  except:
    return {"error": "No se ha encontrado la url."}