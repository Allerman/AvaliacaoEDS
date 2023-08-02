-- Baseado na sua resposta para o Problema 7 e sabendo que existem três
-- tipos de atendimentos na base de dados (I=Internação, U=Urgência e
-- A=Ambulatório), escreva uma consulta em SQL que retorne a
-- quantidade média de diagnósticos dos atendimentos do tipo U.

SELECT ROUND(AVG(num_diagnosticos), 2) AS media_diagnosticos_tipo_U
FROM (
	SELECT atendimento_id, COUNT(diagnostico_id) AS num_diagnosticos
	FROM stg_prontuario.DIAGNOSTICO_PACIENTE dp
	JOIN stg_prontuario.ATENDIMENTO a ON dp.atendimento_id = a.id
	WHERE a.tipo_atendimento = 'U'
	GROUP BY atendimento_id
) AS contagem;
