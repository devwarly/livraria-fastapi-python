from pydantic import BaseModel, Field

class LivroBase(BaseModel):
    titulo: str = Field(min_length=3, max_length=100)
    autor: str = Field(min_length=3, max_length=100)
    ano_publicacao: int | None = None

class LivroCreate(LivroBase):
    pass

class LivroResponse(LivroBase):
    id: int

    class Config:
        from_attributes = True