# Agora vamos precisar importar para nosso schema de staging todos os
# procedimentos médicos cadastrados no SIGTAP (Sistema de
# Gerenciamento da Tabela de Procedimentos, Medicamentos e OPM do
# SUS). Para tal, escreva um código em Python que leia um arquivo CSV e
# grave seu conteúdo em uma tabela do nosso banco de dados.

#importei dados alternativos aos do SIGTAP, pois estava ocorendo erros de download dos arquivos .csv 

import pandas as pd
import mysql.connector

# Dados para conexão com o db
db_config = {
    'host': 'localhost',
    'database': 'stg_procedimentos',
    'user': 'urgot',
    'password': '',
}

caminho_arquivo_csv = '/home/user/Downloads/procedimentosSus.csv'
nome_tabela_destino = 'procedimentosSus'

# Leitura do arquivo CSV usando pandas
dados_csv = pd.read_csv(caminho_arquivo_csv, encoding='utf-8', sep=',')

# Conexão com o db no MySQL usando contexto gerenciado (with)
with mysql.connector.connect(**db_config) as conn:
    with conn.cursor() as cursor:
        try:
            # Utilização de parâmetros para o nome da tabela no comando CREATE TABLE
            create_table_query = "CREATE TABLE IF NOT EXISTS `{}` (codigo BIGINT, descricao VARCHAR(255))".format(nome_tabela_destino)
            cursor.execute(create_table_query)

            # Utilização de Bulk Insert para melhorar o desempenho
            insert_query = f"INSERT INTO `{nome_tabela_destino}` (codigo, descricao) VALUES (%s, %s)"
            data_to_insert = [(row['codigo'], row['descricao']) for _, row in dados_csv.iterrows()]
            cursor.executemany(insert_query, data_to_insert)

            # efetivar as alterações no banco de dados
            conn.commit()

            # Log de sucesso
            print("Dados importados com sucesso!")

        except Exception as e:
            # Log de erro
            print(f"Erro ao importar os dados: {str(e)}")
