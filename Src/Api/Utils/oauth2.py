from datetime import datetime, timedelta

from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from Src.Api.Schemas import token_schema
from Src.Infra.Repository.usuario_repository import UsuarioRepository

# SECRET_KEY
# Algoritimo
# Tempo de Expiracao

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3000


def criar_acesso_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded


def verificar_token_de_acesso(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        usuario_id = payload.get("usuario_id")

        if usuario_id is None:
            raise credentials_exception

        token_data = token_schema.TokenData(id=usuario_id)

        return token_data
    except JWTError:
        raise credentials_exception


def get_usuario_atual(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Não foi possível validar as credenciais",
                                          headers={"WWW-Authenticate": "Bearer"})

    token = verificar_token_de_acesso(token, credentials_exception)

    usuario = UsuarioRepository.select(token.id)

    return usuario
