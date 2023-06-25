from sqlalchemy.exc import IntegrityError
from Src.Infra.Configs.connection import DBConnectionHandler
from Src.Infra.Entities.usuario import Usuario


class UsuarioRepository:
    @staticmethod
    def select_all():
        with DBConnectionHandler() as db:
            return db.session.query(Usuario).all()

    @staticmethod
    def select(id: int):
        with DBConnectionHandler() as db:
            return db.session.query(Usuario).filter(Usuario.id == id).first()

    @staticmethod
    def insert(**kwargs) -> Usuario:
        with DBConnectionHandler() as db:
            try:
                data_insert = Usuario(**kwargs)
                db.session.add(data_insert)
                db.session.commit()
                db.session.refresh(data_insert)

                return data_insert
            except IntegrityError as e:
                raise e
            except BaseException as e:
                raise e

    @staticmethod
    def delete(id: int):
        with DBConnectionHandler() as db:
            usuario = db.session.query(Usuario).filter(Usuario.id == id)

            if usuario.first() is None:
                return 404

            usuario.delete(synchronize_session=False)
            db.session.commit()

    @staticmethod
    def update(id: int, usuario: Usuario) -> int | Usuario:

        with DBConnectionHandler() as db:
            usuario_query = db.session.query(Usuario).filter(Usuario.id == id)

            if usuario_query.first() is None:
                return 404

            try:
                usuario_query.update(usuario.dict(), synchronize_session=False)
                db.session.commit()
            except BaseException as e:
                raise e

            return usuario_query.first()

    @staticmethod
    def get_usuario_by_nome_login(nome_login: str) -> int | Usuario:
        with DBConnectionHandler() as db:
            usuario_query = db.session.query(Usuario).filter(Usuario.nome_login == nome_login).first()

            if not usuario_query:
                return 404

            return usuario_query
