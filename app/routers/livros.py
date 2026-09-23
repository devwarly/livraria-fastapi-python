from fastapi import APIRouter, HTTPException
from app.schemas.livro import LivroSchema
from app.database.conection import SessionLocal
from app.database.models import LivroModel
from app.schemas.livro import LivroCreate
from app.database.conection import get_db
from app.services import livro_service

router = APIRouter(
    prefix="/livros",
    tags=["livros"],
)

'''

Livros = [
     LivroSchema(id=1, titulo="O senhor dos anéis", autor="SR. Warly Martins", ano_publicacao=2005),
     LivroSchema(id=2, titulo="Java do Básico ao avançado", autor="SR. Warly Martins", ano_publicacao=2022),
]

'''

@router.get("/")
async def listar_livros(
    db:Session = Depends(get_db)
):
    return livro_service.listar_livros(db)



'''@router.post("/livros")
async def adicionar_livro(livro: LivroSchema):
    Livros.append(livro)
    return {"message": "Livro adicionado com sucesso", "livros": Livros}'''

@router.post("/")
async def adicionar_livro(livro: LivroCreate):
    db = SessionLocal()

    novo_livro = LivroModel(
        titulo = livro.titulo,
        autor = livro.autor,
        ano_publicacao = livro.ano_publicacao
    )

    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    db.close()
    return {"message": "Livro adicionado com sucesso."}

'''@router.put("/livros/{index}")
async def atualizar_livro(index: int, new_livro: LivroSchema):

    if index > len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    Livros[index] = new_livro
    return {"message": "Livro autualizado com sucesso!", "livros": Livros}

@router.delete("/livros/{index}")
async def deletar_livro(index: int):
    if index > len(Livros) or index < 0:
            raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    Livros.pop(index)
    return {"message": "Livro Deletado com sucesso!", "livros": Livros}'''


