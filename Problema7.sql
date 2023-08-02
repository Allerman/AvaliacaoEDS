-- Dado que um atendimento médico pode ter vários diagnósticos, como
-- você modelaria essas duas tabelas no banco de dados de staging?

-- Tabela de ATENDIMENTO
CREATE TABLE stg_prontuario.ATENDIMENTO (
  id INT AUTO_INCREMENT PRIMARY KEY,
  tipo_atendimento CHAR(1),
  detalhe_atendimento VARCHAR(255)
);

-- Tabela de DIAGNOSTICO
CREATE TABLE stg_prontuario.DIAGNOSTICO (
  id INT AUTO_INCREMENT PRIMARY KEY,
  descricao VARCHAR(255),
  cod_CID CHAR(4)
);

-- Tabela intermediária para relacionar PACIENTE, ATENDIMENTO e DIAGNOSTICO
CREATE TABLE stg_prontuario.DIAGNOSTICO_PACIENTE (
  paciente_id INT,
  atendimento_id INT,
  data_atendimento DATE,
  diagnostico_id INT,
  PRIMARY KEY (paciente_id, atendimento_id, diagnostico_id) -- Definindo a chave primária composta
);

-- Adicionando as FKs
ALTER TABLE stg_prontuario.DIAGNOSTICO_PACIENTE
ADD CONSTRAINT fk_diagPaciente_paciente
FOREIGN KEY (paciente_id) REFERENCES stg_prontuario.PACIENTE(id);

ALTER TABLE stg_prontuario.DIAGNOSTICO_PACIENTE
ADD CONSTRAINT fk_diagPaciente_atendimento
FOREIGN KEY (atendimento_id) REFERENCES stg_prontuario.ATENDIMENTO(id);

ALTER TABLE stg_prontuario.DIAGNOSTICO_PACIENTE
ADD CONSTRAINT fk_diagPaciente_diagnostico
FOREIGN KEY (diagnostico_id) REFERENCES stg_prontuario.DIAGNOSTICO(id);
