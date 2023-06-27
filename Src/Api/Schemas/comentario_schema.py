from pydantic import BaseModel, Extra


class Comentario(BaseModel):
    texto: str
    tarefa_id: int

    class Config:
        extra = Extra.allow


class ComentarioResponse(Comentario):
    usuario_id: int
    id: int

    class Config:
        orm_mode = True


class ComentarioViewResponse(BaseModel):
    id: int
    usuario_id: int
    funcao: str
    nome_login: str
    texto: str

    class Config:
        orm_mode = True


class ComentarioUpdate(BaseModel):
    texto: str
