from fastapi import FastAPI
import json
import os

app = FastAPI()
DATA_FILE = "data.json"

# Si no existe el archivo JSON, se crea con una lista vacía
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.get("/")
def home():
    return {"message": "API en Vercel sin SQLite"}

@app.get("/users")
def get_users():
    with open(DATA_FILE, "r") as f:
        users = json.load(f)
    return {"users": users}

@app.post("/users")
def add_user(nombre: str, email: str):
    with open(DATA_FILE, "r") as f:
        users = json.load(f)

    # Verificar si el email ya existe
    for user in users:
        if user["email"] == email:
            return {"error": "El email ya está registrado"}

    # Agregar nuevo usuario
    new_user = {"nombre": nombre, "email": email}
    users.append(new_user)

    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

    return {"message": "Usuario agregado", "nombre": nombre, "email": email}
