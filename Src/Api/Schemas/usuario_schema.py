from pydantic import BaseModel


class Usuario(BaseModel):
    nome: str
    sobrenome: str
    nome_login: str
    senha_hash: str
    funcao_id: int


class UsuarioResponse(Usuario):
    id: int

    class Config:
        orm_mode = True


class UsuarioLogin(BaseModel):
    nome_login: str
    senha_hash: str
