from sqlalchemy import Column, String, Integer, Text, ForeignKeyConstraint
from Src.Infra.Configs.base import Base


class Usuario(Base):
    __tablename__ = "usuario"
    __table_args__ = (
        ForeignKeyConstraint(
            ("funcao_id",), ["funcao.id"],
            name="fk_usuario_funcao"
        ),
    )

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(40), nullable=False)
    sobrenome = Column(String(40), nullable=False)
    nome_login = Column(String(60), unique=True, nullable=False)
    senha_hash = Column(Text, nullable=False)

    funcao_id = Column(Integer, nullable=False)
