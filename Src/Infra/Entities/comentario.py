from sqlalchemy import Column, Text, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from Src.Infra.Configs.base import Base


class Comentario(Base):
    __tablename__ = 'comentario'
    __table_args__ = (
        ForeignKeyConstraint(
            ("tarefa_id",), ["tarefa.id"],
            name="fk_comentario_tarefa", ondelete="CASCADE"
        ),
        ForeignKeyConstraint(
            ("usuario_id",), ["usuario.id"],
            name="fk_comentario_usuario", ondelete="CASCADE"
        )
    )

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    texto = Column(Text, nullable=False)

    tarefa_id = Column(Integer, nullable=False)
    usuario_id = Column(Integer, nullable=False)

    tarefa_parent = relationship("Tarefa", back_populates="comentario_children")
    usuario_parent = relationship("Usuario", back_populates="comentario_children")
