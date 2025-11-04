from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    ENVIRONMENT = os.getenv('ENVIRONMENT')
    DB_HOST = os.getenv('DB_HOST')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    DB_PORT = os.getenv('DB_PORT')

    return {"message": f"Hello FastAPI! I'm from env {ENVIRONMENT}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": 10, "query": q}
