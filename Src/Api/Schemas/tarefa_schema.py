from typing import Optional
from pydantic import BaseModel, Extra
from Src.Infra.Entities.tarefa import Status, Prioridade


class Tarefa(BaseModel):
    titulo: str
    descricao: str
    status: Status
    prioridade: Prioridade
    anexo: Optional[str] = None


class TarefaResponse(Tarefa):
    id: int
    usuario_autor_id: int

    class Config:
        orm_mode = True


class TarefaResponseAluno(BaseModel):
    nome_completo_autor: str
    tarefa: TarefaResponse

    class Config:
        orm_mode = True


class TarefaUpdate(BaseModel):
    titulo: str
    descricao: str
    status: Status
    prioridade: Prioridade

    class Config:
        extra = Extra.allow
