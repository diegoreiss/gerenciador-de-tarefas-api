from sqlalchemy import Column, Integer, ForeignKeyConstraint
from Src.Infra.Configs.base import Base


class ProfessorTurma(Base):
    __tablename__ = 'professor_turma'
    __table_args__ = (
        ForeignKeyConstraint(
            ("usuario_professor_id",), ["usuario.id"],
            name="fk_usuario_professor_turma"
        ),
        ForeignKeyConstraint(
            ("turma_id", ), ["turma.id"],
            name="fk_turma_professor_turma"
        )
    )

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    usuario_professor_id = Column(Integer, nullable=False)
    turma_id = Column(Integer, nullable=False)
