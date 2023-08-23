from fastapi import FastAPI
from deta import Deta

deta = Deta()

db = deta.Base("simple_db")

app = FastAPI()

@app.get("/")
def root():
    db.put({"value": "Hello world!"}, "my-key")
    return "Hello from Space! 🚀"
