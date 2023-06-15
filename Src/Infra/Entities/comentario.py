from sqlalchemy import Column, Text, Integer, ForeignKeyConstraint
from Src.Infra.Configs.base import Base


class Comentario(Base):
    __tablename__ = 'comentario'
    __table_args__ = (
        ForeignKeyConstraint(
            ("usuario_id",), ["usuario.id"],
            name="fk_comentario_usuario"
        ),
        ForeignKeyConstraint(
            ("tarefa_id",), ["tarefa.id"],
            name="kf_comentario_tarefa"
        )
    )

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    texto = Column(Text, nullable=False)

    usuario_id = Column(Integer, nullable=False)
    tarefa_id = Column(Integer, nullable=False)
