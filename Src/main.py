from fastapi import FastAPI
from Src.Api.Routers import usuario, auth

app = FastAPI()
app.include_router(usuario.router)
app.include_router(auth.router)


@app.get('/')
def root():
    return {'message': 'Cavalo de padeiro'}
