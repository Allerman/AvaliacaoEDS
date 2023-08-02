# Utilizando Python, crie uma visualização que indique a quantidade de
# atendimentos médicos por dia. A entrada de seu programa deve ser uma
# lista de datas, onde cada data representa um atendimento que ocorreu
# naquele dia. Cole abaixo o código fonte de seu programa e exemplos de
# visualizações para diferentes entradas.

import matplotlib.pyplot as plt
import mysql.connector

def obter_dados_atendimento():
	db_config = {
    	'host': 'localhost',
    	'database': 'stg_prontuario',
    	'user': 'urgot',
    	'password': '',
	}

	with mysql.connector.connect(**db_config) as conn, conn.cursor() as cursor:
    	# Obter as datas de atendimento
    	query = "SELECT DISTINCT data_atendimento FROM DIAGNOSTICO_PACIENTE"
    	cursor.execute(query)
    	lista_datas_atendimento = [str(data[0]) for data in cursor.fetchall()]

    	# Obter as quantidades de atendimentos por dia
    	qtd_p_dia = []
    	for data in lista_datas_atendimento:
        	query = f"SELECT COUNT(*) FROM DIAGNOSTICO_PACIENTE WHERE data_atendimento = '{data}'"
        	cursor.execute(query)
        	resultado = cursor.fetchone()
        	quantidade_atendimentos = resultado[0]
        	qtd_p_dia.append(quantidade_atendimentos)

	return lista_datas_atendimento, qtd_p_dia

lista_datas_atendimento, qtd_p_dia = obter_dados_atendimento()

# Gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(lista_datas_atendimento, qtd_p_dia, color='blue')
plt.xlabel('Data de Atendimento')
plt.ylabel('Quantidade de Atendimentos')
plt.title('Quantidade de Atendimentos Médicos por Dia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
