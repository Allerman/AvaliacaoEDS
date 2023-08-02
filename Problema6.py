# Como ficaria o seu código, caso os procedimentos médicos fosses
# carregados a partir de uma API REST/JSON em vez de um arquivo CSV?

#importei dados falsos do jsonplaceholder.

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

url_api = 'https://jsonplaceholder.typicode.com/posts'

nome_tabela_destino = 'procedimentosSus_t2'

# Obter os dados da API em formato JSON
dados_json = obter_dados_da_api(url_api)

# Converter os dados JSON para DataFrame usando pandas
dados_df = pd.DataFrame(dados_json)


with mysql.connector.connect(**db_config) as conn:
    with conn.cursor() as cursor:
        try:
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS `{nome_tabela_destino}` (
                userId INT,
                id INT,
                title VARCHAR(255),
                body TEXT
            )
            """
            cursor.execute(create_table_query)

            # Início da transação
            conn.autocommit = False

            for indice, linha in dados_df.iterrows():
                # Verificar e tratar dados nulos
                user_id = linha['userId'] if not pd.isna(linha['userId']) else None
                post_id = linha['id'] if not pd.isna(linha['id']) else None
                title = linha['title'] if not pd.isna(linha['title']) else None
                body = linha['body'] if not pd.isna(linha['body']) else None

                query = f"INSERT INTO `{nome_tabela_destino}` (userId, id, title, body) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (user_id, post_id, title, body))

            # Confirmação
            conn.commit()

            # Log de sucesso
            print("Dados importados com sucesso!")

        except Exception as e:
            # Rollback em caso de erro
            conn.rollback()
            # Log de erro
            print(f"Erro ao importar os dados: {str(e)}")

