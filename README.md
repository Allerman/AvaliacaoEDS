# Extreme Digital Solutions
Este repositório contém uma série de códigos SQL e Python desenvolvidos como parte da avaliação para a 
Extreme Digital Solutions. Os códigos foram criados para demonstrar habilidades em programação e engenharia de dados.

## Problemas

### Problema 1
Este código cria uma tabela chamada `PACIENTE`, no schema `stg_prontuario` para abrigar os dados dos pacientes dos hospitais:
* stg_hospital_a
* stg_hospital_b
* stg_hospital_c

Que também estao armazenados em uma tabela `PACIENTE` em seus respectivos schemas. Os seus campos sao padroes, portanto o CREATE foi feito baseando-se nas colunas e informaçoes que foram passadas para nao haver divergencias de dados.
   ```
id int
nome varchar
dt_nascimento date
cpf int
nome_mae varchar
dt_atualizacao timestamp Date
   ```


### Problema 2
Este código foi feito para copiar os dados dos schemas dos hospitais para a nova tabela de pacientes no schema `stg_prontuario`.
Descidir fazer uma Procedure para automatizar esse processo.
#### como usar
Primeiro voce deve fazer um git clone para obter o script
Sendo assim, se mais dados foram adicionados nos hospitais eles poderao ser copiados/transportados com apenas uma linha de codigo, sendo ela a chamada da procedure:
   ```
CALL transferir_dados_pacientes();
   ```

## Como utilizar

1. Clone o repositório em seu ambiente local usando o comando:
   ```
   git clone https://github.com/seu-usuario/prescricao-estoque.git
   ```

2. Acesse a pasta do projeto:
   ```
   cd prescricao-estoque
   ```

3. Execute o código `verificar_viabilidade.py` ou `verificar_viabilidade_input.py`:
   ```
   python verificar_viabilidade.py
   ```
   ou
   ```
   python verificar_viabilidade_input.py
   ```

4. Siga as instruções apresentadas na tela para inserir as prescrições e estoque de medicamentos e verificar a viabilidade de uma prescrição específica.

## Observações
- Os códigos foram desenvolvidos para a avaliação da Extreme Digital Solutions e têm o objetivo de demonstrar habilidades em programação e engenharia de dados.

- O código `verificar_viabilidade_input.py` é uma versão aprimorada com interface de input para inserção das sequências de medicamentos. Escolha um dos dois códigos para executar, de acordo com sua preferência.

- As sequências de medicamentos devem ser inseridas separadas por espaços.

- O código utiliza a classe `Counter` do módulo `collections`, portanto, certifique-se de possuir a biblioteca padrão do Python instalada.

- Lembre-se de inserir apenas caracteres válidos (letras do alfabeto) nas sequências de medicamentos. O código atual não faz validação de entrada.

Espero que este repositório atenda às expectativas da avaliação da Extreme Digital Solutions. Se você tiver alguma dúvida ou precisar de mais informações, não hesite em entrar em contato. Boa avaliação!
