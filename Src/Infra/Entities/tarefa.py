import enum
from sqlalchemy import Column, Integer, String, Enum, Text, ForeignKeyConstraint, text
from sqlalchemy.orm import relationship
from Src.Infra.Configs.base import Base


class Status(enum.Enum):
    ativo = "ativo"
    inativo = "inativo"


class Prioridade(enum.Enum):
    alta = "alta"
    media = "media"
    baixa = "baixa"


class Tarefa(Base):
    __tablename__ = "tarefa"
    __table_args__ = (
        ForeignKeyConstraint(
            ("usuario_autor_id",), ["usuario.id"],
            name="fk_tarefa_usuario", ondelete="CASCADE"
        ),
    )

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = Column(String(60), nullable=False)
    descricao = Column(Text, nullable=True)
    status = Column(Enum(Status), server_default=text("'ativo'"))
    prioridade = Column(Enum(Prioridade), server_default=text("'alta'"))
    anexo = Column(Text, nullable=True)

    usuario_autor_id = Column(Integer, nullable=False)

    usuario_parent = relationship("Usuario", back_populates="tarefa_children")
    comentario_children = relationship("Comentario", back_populates="tarefa_parent")
