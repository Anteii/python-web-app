from fastapi import FastAPI, middleware
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

middleware = [
    Middleware(CORSMiddleware, 
               allow_origins=["http://localhost:8080"],
               allow_credentials=True,
               allow_methods=["*"],
               allow_headers=["*"]
    )
]

app = FastAPI(middleware=middleware)

@app.get("/")
def index():
    return {"message": "Hello Docker World!"}