from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from Src.Infra.Configs.base import Base
from Src.Infra.Configs.config_database import ConfigDatabase

from Src.Infra.Entities import (
    funcao, usuario, turma,
    aluno_turma, professor_turma, tarefa,
    comentario
)


class DBConnectionHandler:
    def __init__(self):
        self.__engine = DBConnectionHandler.__create_engine()
        self.session = None
        self.__create_database()

    def __create_database(self):
        engine_url = self.__engine.url

        if not database_exists(engine_url):
            print('sem banco de dados, criando database')
            create_database(engine_url)

            print('criando tabela')
            self.__create_table()

    def __create_table(self):
        Base.metadata.create_all(bind=self.__engine, checkfirst=True)

    @staticmethod
    def __create_engine():
        configuration = ConfigDatabase()
        string_connection = configuration.get_string_connection()

        return create_engine(string_connection, echo=True)

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
