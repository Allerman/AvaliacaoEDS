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

### Problema 3

Este codigo verifica na tabela `stg_prontuario.PACIENTE` a quantidade de dados duplicados com base nos campos: 
   * nome,
   * dt_nascimento,
   * cpf
   * nome_mae

Foi utilizado JOIN para combinar os resultados da tabela stg_prontuario.PACIENTE `p`, com os resultados da subquery `d`, onde a subquery foi usada para calcular a quantidade de dados duplicados com base nos campos citados acima.


### Problema 4
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


### Problema 5
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

### Problema 6
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

### Problema 7


### Problema 8


### Problema 9


### Problema 10
