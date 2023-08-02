-- Supondo que você identificou duplicatas no problema anterior, escreva
-- uma consulta em SQL que retorne, para cada conjunto de pacientes
-- repetidos, somente o que tem a data de atualização mais recente.

SELECT p.nome, p.dt_nascimento, p.cpf, p.nome_mae, p.dt_atualizacao
FROM stg_prontuario.PACIENTE p
INNER JOIN (
    SELECT nome, dt_nascimento, cpf, nome_mae, MAX(dt_atualizacao) AS max_data_atualizacao
    FROM stg_prontuario.PACIENTE
    GROUP BY nome, dt_nascimento, cpf, nome_mae
    HAVING COUNT(*) > 1
) AS duplicatas ON p.nome = duplicatas.nome
                AND p.dt_nascimento = duplicatas.dt_nascimento
                AND p.cpf = duplicatas.cpf
                AND p.nome_mae = duplicatas.nome_mae
                AND p.dt_atualizacao = duplicatas.max_data_atualizacao;
