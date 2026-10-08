from fastapi import FastAPI
from app.database.conection import engine
from app.routers import livros
from app.database.models import Base
from fastapi.middleware.cors import CORSMiddleware 

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(livros.router)


@app.get("/") 
async def home():
    return {"message": "Bem-vindo à API de livros!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)