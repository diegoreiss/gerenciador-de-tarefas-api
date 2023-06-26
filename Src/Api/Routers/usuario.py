from typing import List

from fastapi import APIRouter, status, HTTPException, Depends

from Src.Api.Schemas import usuario_schema
from Src.Api.Utils import password_utils, oauth2
from Src.Api.Utils.directory_utils import DirectoryUtils
from Src.Infra.Repository.usuario_repository import UsuarioRepository

router = APIRouter(prefix='/usuario', tags=['usuario'])


@router.get('/', response_model=List[usuario_schema.UsuarioResponse])
def get_usuarios():
    usuarios = UsuarioRepository.select_all()

    return usuarios


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=usuario_schema.UsuarioResponse)
def create_usuario(usuario: usuario_schema.Usuario):
    hashed_password = password_utils.hash_password(usuario.senha_hash)
    usuario.senha_hash = hashed_password

    try:
        new_usuario = UsuarioRepository.insert(**usuario.dict())
        professor_path = ["api_files", "professor", str(new_usuario.id).zfill(5), "tarefa"]
        directory_utils = DirectoryUtils(professor_path)

        match new_usuario.funcao_id:
            case 2:
                directory_utils.criar_diretorio()

        return new_usuario

    except BaseException as e:
        if "Duplicate entry" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Nome de usuário '{usuario.nome_login}' ja em uso!!!")
        elif "Can't connect" in str(e):
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                detail="Sem conexão com o banco de dados do sitema")


@router.get('/{id}', response_model=usuario_schema.UsuarioResponse)
def get_usuario(id: int):
    response = UsuarioRepository.select(id)

    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Usuário com o id {id} inexistente.')

    return response


@router.get('/atual/', response_model=usuario_schema.UsuarioResponse)
def get_usuario_atual(usuario_atual=Depends(oauth2.get_usuario_atual)):
    return usuario_atual
