-- Escreva um comando SQL que possa ser utilizado para copiar os dados
-- dos schemas dos hospitais para a nova tabela de pacientes que você
-- criou no schema stg_prontuario.

-- Opção manual, para inserção “única”:
INSERT INTO stg_prontuario.PACIENTE (id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao)
SELECT id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao
FROM stg_hospital_a.PACIENTE;

INSERT INTO stg_prontuario.PACIENTE (id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao)
SELECT id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao
FROM stg_hospital_b.PACIENTE;

INSERT INTO stg_prontuario.PACIENTE (id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao)
SELECT id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao
FROM stg_hospital_c.PACIENTE;


-- Opção automatizada, se for necessário a adição frequente de novos pacientes dos hospitais ao stg_prontuario:
DELIMITER $$
CREATE PROCEDURE transferir_dados_pacientes()
BEGIN

	INSERT INTO stg_prontuario.PACIENTE (id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao)
	SELECT hA.id, hA.nome, hA.dt_nascimento, hA.cpf, hA.nome_mae, hA.dt_atualizacao
	FROM stg_hospital_a.PACIENTE hA
	WHERE NOT EXISTS (
    	SELECT 1
    	FROM stg_prontuario.PACIENTE p
    	WHERE p.id = hA.id
	);

	INSERT INTO stg_prontuario.PACIENTE (id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao)
	SELECT hB.id, hB.nome, hB.dt_nascimento, hB.cpf, hB.nome_mae, hB.dt_atualizacao
	FROM stg_hospital_b.PACIENTE hB
	WHERE NOT EXISTS (
    	SELECT 1
    	FROM stg_prontuario.PACIENTE p
    	WHERE p.id = hB.id
	);

	INSERT INTO stg_prontuario.PACIENTE (id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao)
	SELECT hC.id, hC.nome, hC.dt_nascimento, hC.cpf, hC.nome_mae, hC.dt_atualizacao
	FROM stg_hospital_c.PACIENTE hC
	WHERE NOT EXISTS (
    	SELECT 1
    	FROM stg_prontuario.PACIENTE p
    	WHERE p.id = hC.id
	);
END $$
DELIMITER ;

-- Procedure criada, basta chama-lá com: 
CALL transferir_dados_pacientes();

