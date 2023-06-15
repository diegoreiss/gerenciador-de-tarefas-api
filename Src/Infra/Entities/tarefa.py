import enum
from sqlalchemy import Column, Integer, String, Enum, Text, ForeignKeyConstraint, text
from Src.Infra.Configs.base import Base


class Status(enum.Enum):
    ativo = "ativo"
    inativo = "inativo"


class Tarefa(Base):
    __tablename__ = "tarefa"
    __table_args__ = (
        ForeignKeyConstraint(
            ("turma_id",), ["turma.id"],
            name="fk_tarefa_turma"
        ),
    )

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = Column(String(60), nullable=False)
    descricao = Column(Text, nullable=True)
    status = Column(Enum(Status), server_default=text("'ativo'"))

    turma_id = Column(Integer, nullable=False)
