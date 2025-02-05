from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = []  # Lista en memoria (se reinicia con cada despliegue)

class User(BaseModel):
    nombre: str
    email: str

@app.get("/")
def home():
    return {"message": "API en Vercel"}

@app.get("/users")
def get_users():
    return {"users": users}

@app.post("/users")
def add_user(user: User):
    for existing_user in users:
        if existing_user["email"] == user.email:
            return {"error": "El email ya está registrado"}

    new_user = {"nombre": user.nombre, "email": user.email}
    users.append(new_user)

    return {"message": "Usuario agregado", "user": new_user}
