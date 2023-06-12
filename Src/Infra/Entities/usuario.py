from sqlalchemy import Column, String, Integer, Text, ForeignKey
from Src.Infra.Configs.base import Base
from Src.Infra.Entities.funcao import Funcao


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(40), nullable=False)
    sobrenome = Column(String(40), nullable=False)
    nome_login = Column(String(60), unique=True, nullable=False)
    senha_hash = Column(Text, nullable=False)

    funcao_id = Column(Integer, ForeignKey("funcao.id"), nullable=False)
