CREATE TABLE tarefa(
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(60) NOT NULL,
    descricao TEXT NULL,
    status ENUM("Ativo", "Inativo") NOT NULL DEFAULT "Ativo"
    id_comentario INT NULL

    CONSTRAINT FK_tarefa_comentario
        FOREIGN KEY (id_comentario)
        REFERENCES comentario(id)
);

CREATE TABLE comentario(
    id INT PRIMARY KEY AUTO_INCREMENT,
    texto TEXT NOT NULL,
    id_tarefa INT NOT NULL,

    CONSTRAINT FK_comentario_tarefa
        FOREIGN KEY (id_tarefa)
        REFERENCES tarefa(id)
);
