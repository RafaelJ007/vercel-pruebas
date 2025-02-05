from fastapi import FastAPI
import json
import os

app = FastAPI()

DATA_FILE = "data.json"

# Función para leer los datos almacenados
def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"items": []}

# Función para escribir datos en el archivo
def write_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@app.get("/")
def read_root():
    return {"message": "API en Vercel con FastAPI"}

@app.get("/items")
def get_items():
    return read_data()

@app.post("/items")
def add_item(item: dict):
    data = read_data()
    data["items"].append(item)
    write_data(data)
    return {"message": "Item agregado", "data": item}
