# Extreme Digital Solutions 🖥️
Este repositório contém uma série de códigos SQL e Python desenvolvidos como parte da avaliação para a 
Extreme Digital Solutions. Os códigos foram criados para demonstrar habilidades em programação e engenharia de dados.

## Sumário
- [Problemas](#problemas)
  - [Problema 1](#problema-1)
  - [Problema 2](#problema-2)
  - [Problema 3](#problema-3)
  - [Problema 10](#problema-10)
- [Agradecimento](#agradecimento)
- [Autor](#autor)

# Problemas

## Problema 1
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


## Problema 2
Este código foi feito para copiar os dados dos schemas dos hospitais para a nova tabela de pacientes no schema `stg_prontuario`.
Descidir fazer uma Procedure para automatizar esse processo.
#### como usar
Primeiro voce deve fazer um git clone ou copiar o script:
   ```
git clone https://github.com/Allerman/AvaliacaoEDS.git
```
Depois voce deve rodar o script em seu terminal Mysql (talvez seja necessario ajustar, colocando a rota do arquivo. Assim que for executado e a procedure criada vamos para o proximo passo):
```
source Problema2.sql
```
Agora basta chamar a procedure, e ela fara a copia/transporte dos dados.
Ademais, se novos dados foram adicionados nos hospitais eles também poderao ser copiados/transportados apenas chamando a procedure novamente:
   ```
CALL transferir_dados_pacientes();
   ```

## Problema 3

Este codigo verifica na tabela `stg_prontuario.PACIENTE` a quantidade de dados duplicados com base nos campos: 
   * nome,
   * dt_nascimento,
   * cpf
   * nome_mae

Foi utilizado JOIN para combinar os resultados da tabela stg_prontuario.PACIENTE `p`, com os resultados da subquery `d`, onde a subquery foi usada para calcular a quantidade de dados duplicados com base nos campos citados acima.


## Problema 4
Neste codigo o objetivo foi retornar, para cada conjunto de pacientes repetidos, somente o que tem a data de atualização mais recente.
Foi criado uma tabela temporária chamada `duplicadas`. E a subconsulta dentro do WITH é responsável por selecionar os campos:
* nome,
* dt_nascimento,
* cpf,
* nome_mae,
* data de atualização mais recente (MAX(dt_atualizacao)) de cada grupo. 

Ademais, a cláusula *GROUP BY* agrupa os registros com base nos campos citados a cima, menos a `dt_atualizacao`. 
Já a cláusula *HAVING* seleciona apenas os grupos que têm mais de uma ocorrência, ou seja, os duplicados.
O motivo para usar o *WITH* nesse código foi para otimizar a consulta, torná-la mais legível, organizada e evitando repetiçoes na subquery.


## Problema 5
Aqui partimos para o python, neste codigo, estou pegando um arquivo .CSV com alguns procedimentos medicos, que estao separados em duas colunas:
* codigo,
* descricao

O codigo esta bem organizado e com funçoes/variaveis bem descritivas, como `db_config` que esta armazenando as configuraçoes para a conexao com o banco de dados. 


Importei a biblioteca **pandas**, que é usada para manipulação de dados em formato tabular, como o arquivo CSV, e a biblioteca **mysql.connector** que é usada para a conexão e interação com o banco de dados MySQL. <br>
Criei as variaveis contendo os caminhos para o arquivo .CSV e para a tabela(que nao foi criada anteriormente, contudo sera a partir da execuçao do script).


O código estabelece a conexão com o banco de dados MySQL usando o *with* statement. Esse contexto gerenciado garante que a conexão seja aberta e fechada automaticamente, mesmo em caso de erros. 
Sobre a criação da tabela, é criada no banco de dados MySQL com base nos dados do arquivo CSV. O comando `CREATE TABLE` é usado para criar a tabela, especificando os nomes das colunas e os tipos de dados para cada coluna (no caso, codigo como BIGINT e descricao como VARCHAR(255)).


Inserção dos dados na tabela é feita com o comando INSERT INTO, os dados do DataFrame `dados_csv` são inseridos na tabela criada. E é utilizada a técnica de *Bulk Insert* (executemany) para melhorar o desempenho, inserindo várias linhas em uma única operação.
O commit() é chamado para efetivar as alteraçoes. Caso ocorra algum erro durante a importação dos dados, uma mensagem de erro é exibida. 


*Por fim o script termina sua execução e a conexão com o banco de dados é automaticamente encerrada pelo contexto gerenciado (with).*

## Problema 6
Este codigo tem a mesma inteçao que o do problema 5, contudo os dados estao vindo de uma API REST/JSON.

`obter_dados_da_api(url)` É uma função que recebe uma URL como parâmetro e faz uma requisição HTTP GET à API usando a biblioteca requests. Se a resposta da API for bem-sucedida (código de status 200), a função retorna os dados no formato JSON. Caso contrário, uma exceção é levantada.

`url_api` é a URL da API que será consultada para obter os dados.


`with mysql.connector.connect(**db_config) as conn: with conn.cursor() as cursor:` estabelece uma conexão com o banco de dados MySQL usando o contexto gerenciado (with). O contexto gerenciado garante que a conexão seja aberta e fechada automaticamente.

conn.autocommit = False define que a transação não será autoconfirmada para que possa ser feito o commit ao final da inserção dos dados. Caso ocorra algum erro durante a inserção, é possível realizar o rollback.

O loop `for indice, linha in dados_df.iterrows():` itera sobre cada linha do DataFrame dados_df.
No loop, os dados de cada linha do DataFrame são verificados e tratados para evitar a inserção de valores nulos no banco de dados.

query = f"INSERT INTO {nome_tabela_destino} (userId, id, title, body) VALUES (%s, %s, %s, %s)" é a query SQL usada para inserir os dados na tabela do banco de dados. E depois com o cursor.execute(...), a query é executada, e os valores são passados como parâmetros para serem inseridos na tabela.

Ao final do loop, a transação é confirmada com `conn.commit()`.
> Se ocorrer algum erro durante a importação dos dados, é realizado um rollback para desfazer todas as inserções feitas no banco de dados.

## Problema 7
Esse código cria um esquema de banco de dados com três tabelas relacionadas: ATENDIMENTO, DIAGNOSTICO e DIAGNOSTICO_PACIENTE. Essas tabelas permitem o armazenamento de informações sobre atendimentos médicos, diagnósticos e pacientes, estabelecendo as relações corretas entre elas para garantir a integridade dos dados.

Tendo em vista ao que foi solicitado no desafio iniciei criando as duas tabelas, onde a `ATENDIMENTO` contem os tipo_atendimento(I=Internação, U=Urgência e A=Ambulatório) e detalhe_atendimento ("Cirurgia cardiovasculvar").
 `DIAGNOSTICO` possue descricao ("Diabetes") e cod_CID ("E10").

 Por fim, realizei a relaçao dessas duas tabelas e a de `PACIENTE`. Com a tabela `DIAGNOSTICO_PACIENTE`, contendo:
* paciente_id 
* atendimento_id
* data_atendimento
* diagnostico_id
> Também defini a PRIMARY KEY composta (paciente_id, atendimento_id, diagnostico_id)

Após a criaçao, adicionei as Foreign keys 🔑.

## Problema 8
Baseado no codigo passado, este calcula a média do número de diagnósticos por atendimento do tipo 'U' (atendimentos urgentes) na tabela `DIAGNOSTICO_PACIENTE` e `ATENDIMENTO`.

   A subquery *(SELECT atendimento_id, COUNT(diagnostico_id) AS num_diagnosticos ...)* é usada para obter o número de diagnósticos em cada atendimento do tipo 'U'. Isso é feito através do JOIN entre as tabelas `DIAGNOSTICO_PACIENTE` e `ATENDIMENTO`, e usando a coluna atendimento_id como critério de junção. 


O COUNT(diagnostico_id) conta quantos registros de diagnóstico estão associados a cada atendimento.

A cláusula *WHERE a.tipo_atendimento* = 'U' filtra apenas os atendimentos do tipo 'U', ou seja, os atendimentos urgentes.

 A cláusula GROUP BY *atendimento_id* agrupa os resultados pela coluna atendimento_id, o que permite que o COUNT seja calculado para cada atendimento individualmente.


 A consulta externa **SELECT ROUND(AVG(num_diagnosticos), 2)...** calcula a média do número de diagnósticos por atendimento do tipo 'U' usando a função *AVG* aplicada à coluna num_diagnosticos. O *ROUND(2)* arredonda o resultado para duas casas decimais, tornando a média mais legível.

*Assim, o código fornece a média do número de diagnósticos por atendimento do tipo 'U' no sistema.*

### Problema 9
Esse código é uma função Python que verifica a viabilidade de uma prescrição médica em relação ao estoque de medicamentos disponíveis. O programa solicita ao usuário que insira a prescrição de medicamentos, o estoque de medicamentos e o medicamento que deseja verificar a viabilidade. Em seguida, ele utiliza a biblioteca collections para contar a frequência de cada medicamento na prescrição e no estoque.

A função **verificar_viabilidade** recebe três parâmetros:

> prescricao: A prescrição médica, representada por uma sequência de caracteres, onde cada letra representa um medicamento e a frequência de cada letra representa a dose desse medicamento. Essa sequência é convertida para letras maiúsculas usando prescricao.upper() para padronização.

> estoque: O estoque de medicamentos, também representado por uma sequência de caracteres, onde cada letra representa um medicamento disponível em estoque. Essa sequência também é convertida para letras maiúsculas usando estoque.upper() para padronização.

> medicamento_verificar: O medicamento que deseja verificar a viabilidade, representado por uma única letra que corresponde ao medicamento.

O código então utiliza a classe *Counter da biblioteca collections* para contar a frequência de cada medicamento tanto na prescrição quanto no estoque, criando os dicionários *freq_prescricao* e *freq_estoque*.

Em seguida, a função verifica se o medicamento_verificar consta na prescrição e se está disponível em estoque, comparando as frequências nos dicionários. Se o medicamento não constar na prescrição ou não estiver disponível em estoque, a função retorna a mensagen.


No final, a função **main()** é responsável por receber as entradas do usuário, converter as sequências para letras maiúsculas e chamar a função verificar_viabilidade, exibindo o resultado.


## Problema 10
Esse código é um script Python que cria um gráfico de barras para visualizar a quantidade de atendimentos médicos realizados por dia, usando os dados armazenados na tabela `DIAGNOSTICO_PACIENTE`. Ele utiliza as bibliotecas `matplotlib.pyplot` e `mysql.connector` para gerar o gráfico.

**A função `obter_dados_atendimento()`:**
   - É responsável por se conectar ao banco de dados, executar as consultas SQL necessárias e obter os dados de atendimento.
   - O uso do `with` statement garante que a conexão será automaticamente fechada após o uso.
   - A função executa duas consultas SQL no banco de dados:
     - A primeira consulta obtém todas as datas únicas de atendimento da tabela `DIAGNOSTICO_PACIENTE`, armazenando-as em uma lista chamada `lista_datas_atendimento`.
     - A segunda consulta obtém a quantidade de atendimentos para cada data de atendimento, armazenando essas quantidades na lista `qtd_p_dia`.
   - A função retorna as listas `lista_datas_atendimento` e `qtd_p_dia`.

**Criação do gráfico de barras:**
   - Utilizando a biblioteca `matplotlib.pyplot`, é criado um gráfico de barras com os dados obtidos anteriormente.
   - O comando `plt.figure(figsize=(12, 6))` define o tamanho da figura do gráfico.
   - `plt.bar(lista_datas_atendimento, qtd_p_dia, color='blue')` cria as barras do gráfico, usando as datas de atendimento como o eixo x e a quantidade de atendimentos como o eixo y. As barras são coloridas de azul.
   - `plt.xlabel('Data de Atendimento')` e `plt.ylabel('Quantidade de Atendimentos')` definem os rótulos dos eixos x e y, respectivamente.
   - `plt.title('Quantidade de Atendimentos Médicos por Dia')` define o título do gráfico.
   - `plt.xticks(rotation=45)` define a rotação dos rótulos no eixo x para facilitar a leitura das datas.
   - `plt.tight_layout()` ajusta automaticamente o espaçamento dos elementos no gráfico para evitar sobreposições.
   - `plt.show()` exibe o gráfico.

## Outra forma de resolver o problema 10
   Este codigo tem a mesma intençao do ultimo, contudo, conta quantos atendimentos ocorreram em cada mês e cria um gráfico de barras para mostrar a quantidade de atendimentos médicos por mês. Isso permite visualizar a distribuição dos atendimentos ao longo do ano e identificar padrões sazonais ou variações no volume de atendimentos em diferentes meses.

# Agradecimento
Agradeço à equipe da Extreme Digital Solutions pela oportunidade de participar do processo seletivo. Foi uma experiência valiosa e desafiadora que me permitiu demonstrar minhas habilidades e comprometimento com a área de engenharia de dados. 😎

# Autor
Thayssa A. Silva
