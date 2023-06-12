from sqlalchemy import Column, String, Integer
from Src.Infra.Configs.base import Base


class Funcao(Base):
    __tablename__ = 'funcao'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(30), nullable=False)
