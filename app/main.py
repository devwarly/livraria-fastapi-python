from fastapi import FastAPI, HTTPException

Livros = [
    "Robbit", "O Senhor dos Anéis", "Java - Do básico ao avançado", "Gabriel no páis das maravilhas"
]

app = FastAPI()


@app.get("/") 
async def home():
    return {"message": "Bem-vindo à API de livros!"}

@app.get("/livros")
async def listar_livros():
    return {"Livros: ": Livros}

@app.post("/livros")
async def adicionar_livro(livro: str):
    Livros.append(livro)
    return {"message": "Livro adicionado com sucesso", "livros": Livros}

@app.put("/livros/{index}")
async def atualizar_livro(index: int, new_livro: str):

    if index > len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    Livros[index] = new_livro
    return {"message": "Livro autualizado com sucesso!", "livros": Livros}

@app.delete("/livros/{index}")
async def deletar_livro(index: int):
    if index > len(Livros) or index < 0:
            raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    Livros.pop(index)
    return {"message": "Livro Deletado com sucesso!", "livros": Livros}




