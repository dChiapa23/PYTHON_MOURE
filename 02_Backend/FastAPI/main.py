from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
  return "Hola FastAPI"
# url local: http://127.0.1:8000/

@app.get("/url")
async def url():
  return {"url_curso":"https://mouredev.com/python"}
# url local: http://127.0.1:8000/url

# Iniciar el server: uvicorn main:app --reload
# Detener el server: ctrl + c

# Documentacion con SWAGGER: http://127.0.0.1:8000/docs
# Documentacion con REDOCLY: http://127.0.0.1:8000/redoc
