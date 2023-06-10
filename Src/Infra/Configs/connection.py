from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from .base import Base
from .config_database import config_database


class DBConnectionHandler:
    __CONNECTION_STRING = config_database()

    def __init__(self):
        self.__engine = create_engine(DBConnectionHandler.__CONNECTION_STRING)
        self.session = None
        self.__create_database()

    def __create_database(self):
        engine_url = self.__engine.url

        if not database_exists(engine_url):
            create_database()
            self.__create_table()

    def __create_table(self):
        Base.metadata.create_all(bind=self.__engine, checkfirst=True)

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
