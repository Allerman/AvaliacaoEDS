# Agora vamos precisar importar para nosso schema de staging todos os
# procedimentos médicos cadastrados no SIGTAP (Sistema de
# Gerenciamento da Tabela de Procedimentos, Medicamentos e OPM do
# SUS). Para tal, escreva um código em Python que leia um arquivo CSV e
# grave seu conteúdo em uma tabela do nosso banco de dados.

#inportei dados alternativos aos do SIGTAP, pois estava ocorendo erros de download dos arquivos .csv 

import pandas as pd
import mysql.connector

# dados para conexão com o db
db_config = {
	'host': 'localhost',
	'database': 'stg_procedimentos',
	'user': 'urgot',
	'password': ' ',
}

caminho_arquivo_csv = '/home/hermes/Downloads/procedimentosSus.csv'

nome_tabela_destino = 'procedimentosSus'

# leitura do arquivo CSV usando pandas
dados_csv = pd.read_csv(caminho_arquivo_csv, encoding='utf-8', sep=',')

# conexão com o db no MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

try:
	create_table_query = f"""
	CREATE TABLE IF NOT EXISTS {nome_tabela_destino} (
    	codigo BIGINT,
    	descricao VARCHAR(255)
	)
	"""
	cursor.execute(create_table_query)

	# gravação dos dados na tabela
	for indice, linha in dados_csv.iterrows():
    	query = f"INSERT INTO {nome_tabela_destino} (codigo, descricao) VALUES (%s, %s)"
    	cursor.execute(query, (linha['codigo'], linha['descricao']))

	conn.commit()

	print("Dados importados com sucesso!")

except Exception as e :
	print(f"Erro ao importar os dados: {str(e)}")
finally:

	cursor.close()
	conn.close()

