from fastapi import APIRouter, status, HTTPException, Response
from Src.Api.Schemas import usuario_schema
from Src.Api.Utils.password_utils import verify_password
from Src.Infra.Repository.usuario_repository import UsuarioRepository

router = APIRouter(tags=['Autenticação'])


@router.post('/login')
def login(user_credentials: usuario_schema.UsuarioLogin):
    usuario = UsuarioRepository.get_usuario_by_nome_login(user_credentials.nome_login)

    if usuario == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Credenciais Inválidas')

    if not verify_password(user_credentials.senha_hash, usuario.senha_hash):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Credenciais Inválidas')

    # criar um token

    # retornar o token

    return {"token example": "your token"}
