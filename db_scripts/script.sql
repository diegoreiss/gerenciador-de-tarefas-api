SET NAMES utf8;

DROP TABLE IF EXISTS funcao;
CREATE TABLE IF NOT EXISTS funcao(
    id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL
);

DROP TABLE IF EXISTS usuario;
CREATE TABLE IF NOT EXISTS usuario(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(40) NOT NULL,
    sobrenome VARCHAR(40) NOT NULL,
    nome_login VARCHAR(60) UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    funcao_id INTEGER NOT NULL,

    CONSTRAINT fk_usuario_funcao
	   FOREIGN KEY (funcao_id)
	   REFERENCES funcao(id)
	   ON DELETE CASCADE
);


DROP TABLE IF EXISTS tarefa;
CREATE TABLE IF NOT EXISTS tarefa(
    id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(60) NOT NULL,
    descricao TEXT NULL,
    status ENUM("ativo", "inativo") DEFAULT ("ativo"),
    prioridade ENUM("alta", "media", "baixa") DEFAULT ("alta"),
    anexo TEXT NULL,
    usuario_autor_id INTEGER NOT NULL,

    CONSTRAINT fk_tarefa_usuario
        FOREIGN KEY (usuario_autor_id)
        REFERENCES usuario(id)
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS comentario;
CREATE TABLE IF NOT EXISTS comentario(
    id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    texto TEXT NOT NULL,
    tarefa_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,

    CONSTRAINT fk_comentario_tarefa
        FOREIGN KEY (tarefa_id)
        REFERENCES tarefa(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_comentario_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuario(id)
        ON DELETE CASCADE
);


INSERT INTO
    funcao(nome)
VALUES
    ('aluno'), ('professor');
