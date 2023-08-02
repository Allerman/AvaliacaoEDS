-- Dado que um atendimento médico pode ter vários diagnósticos, como
-- você modelaria essas duas tabelas no banco de dados de staging?

CREATE TABLE stg_prontuario.ATENDIMENTO (
  id INT AUTO_INCREMENT PRIMARY KEY,
  tipo_atendimento CHAR(2),
  detalhe_atendimento VARCHAR(255)
);

CREATE TABLE stg_prontuario.DIAGNOSTICO (
  id INT AUTO_INCREMENT PRIMARY KEY,
  descricao VARCHAR(255),
  cod_CID VARCHAR(10)
);

-- Relacionando as duas tabelas:
CREATE TABLE stg_prontuario.DIAGNOSTICO_PACIENTE (
  paciente_id INT,
  atendimento_id INT,
  data_atendimento DATE,
  diagnostico_id INT
);

-- Adicionando as FKs:
ALTER TABLE stg_prontuario.DIAGNOSTICO_PACIENTE
ADD CONSTRAINT fk_diagPaciente_pacientId
FOREIGN KEY (paciente_id) REFERENCES stg_prontuario.PACIENTE(id);

ALTER TABLE stg_prontuario.DIAGNOSTICO_PACIENTE
ADD CONSTRAINT fk_diagPaciente_atendId
FOREIGN KEY (atendimento_id) REFERENCES stg_prontuario.ATENDIMENTO(id);

ALTER TABLE stg_prontuario.DIAGNOSTICO_PACIENTE
ADD CONSTRAINT fk_diagPaciente__diagId
FOREIGN KEY (diagnostico_id) REFERENCES stg_prontuario.DIAGNOSTICO(id);
