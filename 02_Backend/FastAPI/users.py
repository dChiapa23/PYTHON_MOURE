from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# Inicia el server: uvicorn users:app --reload

class User(BaseModel):
  name: str
  surname: str
  url: str
  age: int

users_list = [User(name="Diego", surname="Chiapa", url="diegochiapa.com.ar", age=32),
         User(name="Brais", surname="Moure", url="https://moure.dev", age=35),
         User(name="Haakon", surname="Dahlberg", url="https://haakon.com", age=33)]

@app.get("/users")
async def users():
  return users_list