from typing import List
from fastapi import APIRouter, status, HTTPException, Response
from Src.Api.Schemas import usuario_schema
from Src.Api.Utils import password_utils
from Src.Infra.Repository.usuario_repository import UsuarioRepository

router = APIRouter(prefix='/usuario', tags=['usuarios'])


@router.get('/', response_model=List[usuario_schema.UsuarioResponse])
def get_usuarios():
    usuarios = UsuarioRepository.select_all()

    return usuarios


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=usuario_schema.UsuarioResponse)
def create_usuario(usuario: usuario_schema.Usuario):
    print('entrei no endpoint')
    hashed_password = password_utils.hash_password(usuario.senha_hash)
    usuario.senha_hash = hashed_password

    new_usuario = UsuarioRepository.insert(**usuario.dict())

    return new_usuario


@router.get('/{id}', response_model=usuario_schema.UsuarioResponse)
def get_usuario(id: int):
    response = UsuarioRepository.select(id)

    if response == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Usuário com o id {id} inexistente.')

    return Response(status_code=status.HTTP_201_CREATED)
