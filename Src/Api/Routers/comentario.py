from typing import List
from fastapi import APIRouter, status, HTTPException, Depends, Response
from Src.Api.Schemas import comentario_schema
from Src.Api.Utils import oauth2
from Src.Infra.Repository.comentario_repository import ComentarioRepository

router = APIRouter(prefix="/comentario", tags=["comentario"])


@router.get("/{tarefa_id}", response_model=List[comentario_schema.ComentarioViewResponse])
def get_comentarios_by_id_tarefa(tarefa_id: int, usuario_atual=Depends(oauth2.get_usuario_atual)):
    comentarios = ComentarioRepository.select_all_by_tarefa_id(tarefa_id)

    return [comentario_schema.ComentarioViewResponse(id=comentario[0], usuario_id=comentario[1], funcao=comentario[2],
                                                     nome_login=comentario[3], texto=comentario[4])
            for comentario in comentarios]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=comentario_schema.ComentarioResponse)
def create_comentario(comentario: comentario_schema.Comentario, usuario_atual=Depends(oauth2.get_usuario_atual)):
    comentario.usuario_id = usuario_atual.id
    new_comentario = ComentarioRepository.insert(**comentario.dict())

    return new_comentario


@router.put("/{id}")
def update_comentario(id: int, comentario: comentario_schema.ComentarioUpdate,
                      usuario_atual=Depends(oauth2.get_usuario_atual)):
    comentario_updated = ComentarioRepository.update(id, **comentario.dict())

    if comentario_updated == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"comentario com o id {id} inexistente")

    return comentario_updated


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comentario(id: int, usuario_atual=Depends(oauth2.get_usuario_atual)):
    comentario = ComentarioRepository.delete(id)

    if comentario == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Comentario com id {id} inexistente.")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
