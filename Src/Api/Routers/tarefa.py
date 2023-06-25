import os
from typing import Annotated, List
from fastapi import APIRouter, status, HTTPException, Response, UploadFile, Form, Depends
from fastapi.responses import FileResponse
from Src.Api.Schemas import tarefa_schema
from Src.Api.Utils import oauth2
from Src.Api.Utils.directory_utils import DirectoryUtils
from Src.Infra.Repository.tarefa_repository import TarefaRepository

router = APIRouter(prefix='/tarefa', tags=['tarefa'])


@router.get("/usuario/atual/", response_model=List[tarefa_schema.TarefaResponse])
def get_tarefas_usuario_atual(usuario_atual=Depends(oauth2.get_usuario_atual)):
    try:
        tarefas_usuario_atual = TarefaRepository.select_all_by_id_user(usuario_atual.id)

        return tarefas_usuario_atual
    except BaseException as e:
        print(e)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=tarefa_schema.TarefaResponse)
def create_tarefa(titulo: Annotated[str, Form()], descricao: Annotated[str, Form()], status: Annotated[str, Form()],
                  prioridade: Annotated[str, Form()], has_anexo: bool = False, file: UploadFile | None = None,
                  usuario_atual=Depends(oauth2.get_usuario_atual)):
    tarefa_form = {
        "titulo": titulo,
        "descricao": descricao,
        "status": status,
        "prioridade": prioridade,
        "usuario_autor_id": usuario_atual.id
    }

    new_tarefa = TarefaRepository.insert(**tarefa_form)

    nome_dir_atual = os.path.basename(os.getcwd())
    user_dir = str(usuario_atual.id).zfill(5)
    tarefa_dir = str(new_tarefa.id).zfill(5)

    tarefa_path = ["api_files", "professor", user_dir, "tarefa", tarefa_dir]
    directory_utils = DirectoryUtils(tarefa_path)
    directory_utils.criar_diretorio(folders_into=["anexo", "entregas"])

    if has_anexo:
        anexo_path = ["api_files", "professor", user_dir, "tarefa", tarefa_dir, "anexo", file.filename]
        cwd_anexo = os.path.join(os.getcwd(), *anexo_path)

        with open(cwd_anexo, "wb+") as file_obj:
            file_obj.write(file.file.read())

        posicao = cwd_anexo.index(nome_dir_atual)
        caminho_relativo = cwd_anexo[posicao + len(nome_dir_atual) + 1:].replace("\\", "/")

        new_tarefa = TarefaRepository.update_anexo(new_tarefa.id, caminho_relativo)

    return new_tarefa


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_tarefa(id: int, usuario_atual=Depends(oauth2.get_usuario_atual)):
    response = TarefaRepository.delete(id)

    if response == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Tarefa com id {id} inexistente.')

    user_dir = str(usuario_atual.id).zfill(5)
    tarefa_dir = str(id).zfill(5)
    tarefa_path = ["api_files", "professor", user_dir, "tarefa", tarefa_dir]
    print(tarefa_path)
    directory_utils = DirectoryUtils(tarefa_path)
    directory_utils.remover_diretorio()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}', response_model=tarefa_schema.TarefaResponse)
def update_tarefa(id: int, titulo: Annotated[str, Form()], descricao: Annotated[str, Form()],
                  status: Annotated[str, Form()], prioridade: Annotated[str, Form()], has_anexo: bool = False,
                  file: UploadFile | None = None, usuario_atual=Depends(oauth2.get_usuario_atual)):
    tarefa_form = {
        "titulo": titulo,
        "descricao": descricao,
        "status": status,
        "prioridade": prioridade,
    }

    if has_anexo:
        print("tem anexo")
        user_dir = str(usuario_atual.id).zfill(5)
        tarefa_dir = str(id).zfill(5)
        tarefa_anexo_path = ["api_files", "professor", user_dir, "tarefa", tarefa_dir, "anexo"]

        directory_utils = DirectoryUtils(tarefa_anexo_path)
        directory_utils.remover_itens_diretorio()
        tarefa_anexo_path.append(file.filename)

        cwd_anexo = os.path.join(os.getcwd(), *tarefa_anexo_path)

        with open(cwd_anexo, "wb+") as file_obj:
            file_obj.write(file.file.read())

        nome_dir_atual = os.path.basename(os.getcwd())
        posicao = cwd_anexo.index(nome_dir_atual)
        caminho_relativo = cwd_anexo[posicao + len(nome_dir_atual) + 1:].replace("\\", "/")

        tarefa_form["anexo"] = caminho_relativo

    print("vou atualizar")
    response = TarefaRepository.update(id, **tarefa_form)

    if response == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Tarefa com id {id} inexistente.')

    print("vou retornar")
    return response


@router.get('/download/')
def download_anexo(file_path: str, usuario_atual=Depends(oauth2.get_usuario_atual)):
    full_file_path = os.path.join(os.getcwd(), *file_path.split("/"))
    file_name = file_path.split("/")[-1]

    if not os.path.exists(full_file_path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Anexo não encontrado")

    return FileResponse(path=full_file_path, media_type='application/octet-stream', filename=file_name)
