from fastapi import FastAPI

app = FastAPI()
users = []  # Lista en memoria (se reinicia con cada despliegue)

@app.get("/")
def home():
    return {"message": "API en Vercel"}

@app.get("/users")
def get_users():
    return {"users": users}

@app.post("/users")
def add_user(nombre: str, email: str):
    for user in users:
        if user["email"] == email:
            return {"error": "El email ya está registrado"}

    new_user = {"nombre": nombre, "email": email}
    users.append(new_user)

    return {"message": "Usuario agregado", "nombre": nombre, "email": email"}
