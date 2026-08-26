from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello Word!"}

@app.get("/saudacao")
async def saudacao(string: str):
    return {"message": f"Olá {string}, seja bem vindo(a)!"}