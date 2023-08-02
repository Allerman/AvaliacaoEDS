# Como ficaria o seu código, caso os procedimentos médicos fosses
# carregados a partir de uma API REST/JSON em vez de um arquivo CSV?

#inportei dados falsos do jsonplaceholder.

import pandas as pd
import mysql.connector
import requests
def obter_dados_da_api(url):
	response = requests.get(url)
	if response.status_code == 200:
    	return response.json()
	else:
    	raise Exception(f"Erro ao obter dados da API. Status code: {response.status_code}")

db_config = {
	'host': 'localhost',
	'database': 'stg_procedimentos',
	'user': 'urgot',
	'password': ' ',
}

# URL da API JSONPlaceholder para obter os dados desejados para teste
url_api = 'https://jsonplaceholder.typicode.com/posts'

nome_tabela_destino = 'procedimentosSus_t2'

# obter os dados da API em formato JSON
dados_json = obter_dados_da_api(url_api)

# converter os dados JSON para DataFrame usando pandas
dados_df = pd.DataFrame(dados_json)

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

try:
	create_table_query = f"""
	CREATE TABLE IF NOT EXISTS {nome_tabela_destino} (
    	userId INT,
    	id INT,
    	title VARCHAR(255),
    	body TEXT
	)
	"""
	cursor.execute(create_table_query)

	for indice, linha in dados_df.iterrows():
    	query = f"INSERT INTO {nome_tabela_destino} (userId, id, title, body) VALUES (%s, %s, %s, %s)"
    	cursor.execute(query, (linha['userId'], linha['id'], linha['title'], linha['body']))

	conn.commit()

	print("Dados importados com sucesso!")

except Exception as e:
	print(f"Erro ao importar os dados: {str(e)}")
finally:
	cursor.close()
	conn.close()
