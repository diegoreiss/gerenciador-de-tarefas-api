from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    token_de_acesso: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
