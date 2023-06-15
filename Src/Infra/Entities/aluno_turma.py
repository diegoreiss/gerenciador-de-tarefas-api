from sqlalchemy import Column, Integer, ForeignKeyConstraint
from Src.Infra.Configs.base import Base


class AlunoTurma(Base):
    __tablename__ = 'aluno_turma'
    __table_args__ = (
        ForeignKeyConstraint(
            ("usuario_aluno_id",), ["usuario.id"],
            name="fk_usuario_aluno_turma"
        ),
        ForeignKeyConstraint(
            ("turma_id", ), ["turma.id"],
            name="fk_turma_aluno_turma"
        )
    )

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    usuario_aluno_id = Column(Integer, nullable=False)
    turma_id = Column(Integer, nullable=False)
