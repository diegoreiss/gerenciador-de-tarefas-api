SET NAMES utf8;

DROP TABLE IF EXISTS funcao;
CREATE TABLE IF NOT EXISTS funcao(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL
);

DROP TABLE IF EXISTS usuario;
CREATE TABLE IF NOT EXISTS usuario(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(40) NOT NULL,
    sobrenome VARCHAR(40) NOT NULL,
    nome_login VARCHAR(60) NOT NULL,
    senha_hash TEXT NOT NULL,
    funcao_id INT NOT NULL,

    CONSTRAINT fk_usuario_funcao
	   FOREIGN KEY (funcao_id)
	   REFERENCES funcao(id)
);

DROP TABLE IF EXISTS turma;
CREATE TABLE IF NOT EXISTS turma(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL
);

DROP TABLE IF EXISTS professor_turma;
CREATE TABLE IF NOT EXISTS professor_turma(
    usuario_professor_id INT NOT NULL,
    turma_id INT NOT NULL,

    CONSTRAINT fk_usuario_professor_turma
        FOREIGN KEY (usuario_professor_id)
        REFERENCES usuario(id),
    
    CONSTRAINT fk_turma_turma_professor
        FOREIGN KEY (turma_id)
        REFERENCES turma(id)
);

DROP TABLE IF EXISTS aluno_turma;
CREATE TABLE IF NOT EXISTS aluno_turma(
    usuario_aluno_id INT NOT NULL,
    turma_id INT NOT NULL,

    CONSTRAINT fk_usuario_aluno_turma
        FOREIGN KEY (usuario_aluno_id)
        REFERENCES usuario(id),
    
    CONSTRAINT fk_turma_aluno_turma
        FOREIGN KEY (turma_id)
        REFERENCES turma(id)
);

DROP TABLE IF EXISTS tarefa;
CREATE TABLE IF NOT EXISTS tarefa(
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(60) NOT NULL,
    descricao TEXT NULL,
    status ENUM("Ativo", "Inativo") DEFAULT ("Ativo"),
    id_turma INT NOT NULL,

    CONSTRAINT fk_tarefa_turma
        FOREIGN KEY (id_turma)
        REFERENCES turma(id)
);

DROP TABLE IF EXISTS comentario;
CREATE TABLE IF NOT EXISTS comentario(
    id INT PRIMARY KEY AUTO_INCREMENT,
    texto TEXT NOT NULL,
    id_usuario INT NOT NULL,
    id_tarefa INT NOT NULL,

    CONSTRAINT fk_comentario_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuario(id),

    CONSTRAINT fk_comentario_tarefa
        FOREIGN KEY (id_tarefa)
        REFERENCES tarefa(id)
);


INSERT INTO
    funcao(nome)
VALUES
    ('Aluno'), ('Professor');

INSERT INTO
    turma(nome)
VALUES
  ('Programação Orientada a Objetos'),
  ('Desenvolvimento Destkop'),
  ('CRUD');
