from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from Src.Infra.Configs.base import Base


class Funcao(Base):
    __tablename__ = "funcao"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(30), nullable=False)

    usuario_children = relationship("Usuario", back_populates="funcao_parent")
