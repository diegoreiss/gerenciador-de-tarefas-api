from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Src.Api.Utils import password_utils, oauth2
from Src.Infra.Repository.usuario_repository import UsuarioRepository

router = APIRouter(tags=['Autenticação'])


@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    usuario = None
    try:
        usuario = UsuarioRepository.get_usuario_by_nome_login(user_credentials.username)
    except BaseException as e:
        print(e)
        if "Can't connect" in str(e):
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                detail="Sem conexão com o banco de dados do sitema")

    if usuario in (404, None) or not password_utils.verify_password(user_credentials.password, usuario.senha_hash):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Credenciais Inválidas")

    dados_para_o_token = {"usuario_id": usuario.id}
    token_de_acesso = oauth2.criar_acesso_token(data=dados_para_o_token)

    return {"access_token": token_de_acesso, "token_type": "Bearer"}
