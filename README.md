# FastAPI Template Project

## Requisitos do Back-End

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).

## Desenvolvimento local no Back-End

* Inicie com Docker Compose:

```bash
docker-compose up -d
```

* Agora você pode abrir seu navegador e interagir com as URLs a seguir:

Adminer, uma ferramenta para gerenciar conteúdo em bancos de dados: http://localhost:8080/

Documentação interativa automática com Swagger UI: http://localhost:8000/docs

**Note**: The first time you start your stack, it might take a minute for it to be ready. While the backend waits for the database to be ready and configures everything. You can check the logs to monitor it.

Para verificar os logs, execute:

```bash
docker-compose logs
```

Para verificar os logs de um serviço específico, adicione o nome do serviço, por exemplo:

```bash
docker-compose logs backend
```

If your Docker is not running in `localhost` (the URLs above wouldn't work) check the sections below on **Development with Docker Toolbox** and **Development with a custom IP**.
