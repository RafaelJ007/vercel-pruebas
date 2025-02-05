from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Conectar a la base de datos SQLite y crear la tabla si no existe
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()  # Llamamos a la función para inicializar la BD

@app.get("/")
def home():
    return {"message": "API con SQLite en Vercel"}

@app.get("/users")
def get_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = [{"id": row[0], "nombre": row[1], "email": row[2]} for row in cursor.fetchall()]
    conn.close()
    return {"users": users}

@app.post("/users")
def add_user(nombre: str, email: str):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (nombre, email) VALUES (?, ?)", (nombre, email))
        conn.commit()
        conn.close()
        return {"message": "Usuario agregado", "nombre": nombre, "email": email}
    except sqlite3.IntegrityError:
        return {"error": "El email ya está registrado"}
