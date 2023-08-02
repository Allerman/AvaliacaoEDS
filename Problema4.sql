-- Supondo que você identificou duplicatas no problema anterior, escreva
-- uma consulta em SQL que retorne, para cada conjunto de pacientes
-- repetidos, somente o que tem a data de atualização mais recente.

WITH duplicatas AS (
    SELECT nome, dt_nascimento, cpf, nome_mae, MAX(dt_atualizacao) AS max_data_atualizacao
    FROM stg_prontuario.PACIENTE
    GROUP BY nome, dt_nascimento, cpf, nome_mae
    HAVING COUNT(*) > 1
)
SELECT p.nome, p.dt_nascimento, p.cpf, p.nome_mae, p.dt_atualizacao
FROM stg_prontuario.PACIENTE p
INNER JOIN duplicatas d ON p.nome = d.nome
                             AND p.dt_nascimento = d.dt_nascimento
                             AND p.cpf = d.cpf
                             AND p.nome_mae = d.nome_mae
                             AND p.dt_atualizacao = d.max_data_atualizacao;
