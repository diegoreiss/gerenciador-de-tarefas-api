from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from Src.Infra.Configs.base import Base


class Turma(Base):
    __tablename__ = "turma"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(60), nullable=False)

    usuarios = relationship("usuario", secondary="aluno_tarefa", backref="turma")
