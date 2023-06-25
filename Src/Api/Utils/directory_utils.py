import os
import shutil


class DirectoryUtils:
    def __init__(self, caminho: list):
        super().__init__()
        self.cwd = os.getcwd()
        self.dir_path = os.path.join(self.cwd, *caminho)

    def criar_diretorio(self, folders_into=None):
        if folders_into is None:
            folders_into = []

        if os.path.exists(self.dir_path):
            try:
                shutil.rmtree(self.dir_path)
            except BaseException as e:
                print(e)

        os.makedirs(self.dir_path)

        for folder in folders_into:
            os.makedirs(os.path.join(self.dir_path, folder))

    def remover_diretorio(self):
        if os.path.exists(self.dir_path):
            try:
                shutil.rmtree(self.dir_path)
            except BaseException as e:
                print(e)

    def remover_itens_diretorio(self):
        for file in os.listdir(self.dir_path):
            file_path = os.path.join(self.dir_path, file)

            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except BaseException as e:
                print(e)
