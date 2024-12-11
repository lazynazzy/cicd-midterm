# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Helloooo, World!!!!!!!"}


@app.get("/health")
def health_check():
    return {"status": "OK"}
