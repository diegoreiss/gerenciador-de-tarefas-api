from Src.Infra.Configs.connection import DBConnectionHandler
from Src.Infra.Entities.comentario import Comentario
from Src.Infra.Entities.usuario import Usuario
from Src.Infra.Entities.funcao import Funcao


class ComentarioRepository:
    @staticmethod
    def select_all_by_tarefa_id(tarefa_id: int):
        with DBConnectionHandler() as db:
            return (db.session
                    .query(Comentario.id, Comentario.usuario_id, Funcao.nome, Usuario.nome_login, Comentario.texto)
                    .join(Usuario, Comentario.usuario_id == Usuario.id)
                    .join(Funcao, Usuario.funcao_id == Funcao.id)
                    .filter(Comentario.tarefa_id == tarefa_id)
                    .all()
                    )

    @staticmethod
    def insert(**kwargs):
        with DBConnectionHandler() as db:
            data_insert = Comentario(**kwargs)

            try:
                db.session.add(data_insert)
                db.session.commit()
                db.session.refresh(data_insert)

                return data_insert
            except BaseException as e:
                raise e

    @staticmethod
    def delete(id: int):
        with DBConnectionHandler() as db:
            comentario = db.session.query(Comentario).filter(Comentario.id == id)

            if comentario.first() is None:
                return 404

            try:
                comentario.delete(synchronize_session=False)
                db.session.commit()
            except BaseException as e:
                raise e

    def update(id: int, **kwargs):
        with DBConnectionHandler() as db:
            comentario_query = db.session.query(Comentario).filter(Comentario.id == id)

            if comentario_query.first() is None:
                return 404

            try:
                comentario_query.update(kwargs, synchronize_session=False)

                updated_comentario = comentario_query.first()

                db.session.commit()
                db.session.refresh(updated_comentario)

                return updated_comentario

            except BaseException as e:
                raise e
