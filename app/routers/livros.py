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
async def adicionar_livro(livro: LivroCreate, db: Session = Depends(get_db)):
    return livro_service.adicinar_livro(livro, db)

@router.put("/livros/{index}")
async def atualizar_livro(index: int, livro: LivroCreate, db: Session = Depends(get_db)):

    livro_db = livro_service.atualizar_livro(index, livro, db)

    if not livro_db:
         raise HTTPException(status_code=404, detail="Livro não encontrado")

    return livro_db

@router.delete("/livros/{index}")
async def deletar_livro(index: int, db: Session = Depends(get_db)):
    removido = livro_service.remover_livro(index, db)

    db.close()

    if not removido:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    return {
        "message": "Livro removido com sucesso!!"
    }


