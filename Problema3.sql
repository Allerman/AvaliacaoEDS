-- Escreva uma consulta em SQL que retorne os pacientes duplicados na
-- tabela PACIENTE do schema stg_prontuario, caso existam.

SELECT p.nome, p.dt_nascimento, p.cpf, p.nome_mae, p.dt_atualizacao, d.quantidade_duplicados
FROM stg_prontuario.PACIENTE p
JOIN (
    SELECT nome, dt_nascimento, cpf, nome_mae, COUNT(*) AS quantidade_duplicados
    FROM stg_prontuario.PACIENTE
    GROUP BY nome, dt_nascimento, cpf, nome_mae
    HAVING COUNT(*) > 1
) d ON p.nome = d.nome AND p.dt_nascimento = d.dt_nascimento AND p.cpf = d.cpf AND p.nome_mae = d.nome_mae;
