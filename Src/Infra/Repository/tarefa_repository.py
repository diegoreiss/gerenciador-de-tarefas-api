from Src.Infra.Configs.connection import DBConnectionHandler
from Src.Infra.Entities.tarefa import Tarefa


class TarefaRepository:
    @staticmethod
    def select_all():
        with DBConnectionHandler() as db:
            return db.session.query(Tarefa).all()

    @staticmethod
    def select_all_by_id_user(usuario_autor_id: int):
        with DBConnectionHandler() as db:
            return db.session.query(Tarefa).filter(Tarefa.usuario_autor_id == usuario_autor_id).all()

    @staticmethod
    def select(id):
        with DBConnectionHandler() as db:
            return db.session.query(Tarefa).filter(Tarefa.id == id).first()

    @staticmethod
    def insert(**kwargs) -> Tarefa:
        with DBConnectionHandler() as db:
            data_insert = Tarefa(**kwargs)

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
            tarefa = db.session.query(Tarefa).filter(Tarefa.id == id)

            if tarefa.first() is None:
                return 404

            try:
                tarefa.delete(synchronize_session=False)
                db.session.commit()
            except BaseException as e:
                raise e

    @staticmethod
    def update(id: int, **kwargs):
        with DBConnectionHandler() as db:
            tarefa_query = db.session.query(Tarefa).filter(Tarefa.id == id)

            if tarefa_query.first() is None:
                return 404

            try:
                tarefa_query.update(kwargs, synchronize_session=False)

                updated_tarefa = tarefa_query.first()

                db.session.commit()
                db.session.refresh(updated_tarefa)

                return updated_tarefa

            except BaseException as e:
                raise e

    @staticmethod
    def update_anexo(id: int, anexo):
        print('entrei no update_anexo')
        with DBConnectionHandler() as db:
            tarefa_query = db.session.query(Tarefa).filter(Tarefa.id == id)

            if tarefa_query.first() is None:
                return 404

            try:
                tarefa_query.update({"anexo": anexo})

                updated_tarefa = tarefa_query.first()

                db.session.commit()
                db.session.refresh(updated_tarefa)

                return updated_tarefa

            except BaseException as e:
                raise e
