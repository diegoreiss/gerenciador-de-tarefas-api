from fastapi import FastAPI
from Src.Api.Routers import usuario, auth, tarefa, comentario

app = FastAPI()
app.include_router(usuario.router)
app.include_router(tarefa.router)
app.include_router(comentario.router)
app.include_router(auth.router)


@app.get('/')
def root():
    return {'message': 'Cavalo de padeiro'}
