-- Escreva um comando SQL que crie uma
-- tabela chamada PACIENTE, no schema stg_prontuario, para abrigar os
-- dados de pacientes de todos os hospitais.

CREATE TABLE stg_prontuario.PACIENTE (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    dt_nascimento DATE,
    cpf int,
    nome_mae VARCHAR(100),
    dt_atualizacao TIMESTAMP
);



-- Alternativa melhorada, apenas para exemplo:
CREATE TABLE stg_prontuario.PACIENTE (
    paciente_id BIGINT PRIMARY KEY,
    nome VARCHAR(100),
    dt_nascimento DATE,
    cpf VARCHAR(11) UNIQUE,
    nome_mae VARCHAR(100),
    dt_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
