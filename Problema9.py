# você deve escrever um programa em Python que verifique a viabilidade de
# uma prescrição, dado o estado do estoque naquele momento.
# A entrada do seu programa deve ser duas sequências de caracteres. A
# primeira sequência indica quais medicamentos foram prescritos e a
# segunda quais medicamentos estão no estoque. Em ambas as
# sequencias, cada letra representa um medicamento

def verificar_viabilidade(prescricao, estoque):
	freq_prescricao = {}
	freq_estoque = {}
    
	for medicamento in prescricao:
    	freq_prescricao[medicamento] = freq_prescricao.get(medicamento, 0) + 1
    
	for medicamento in estoque:
    	freq_estoque[medicamento] = freq_estoque.get(medicamento, 0) + 1

	for medicamento, frequencia_prescricao in freq_prescricao.items():
    	if medicamento not in freq_estoque or frequencia_prescricao > freq_estoque[medicamento]:
        	return False

	return True

# exemplo:
print(verificar_viabilidade('a', 'b'))  # Saída: False
print(verificar_viabilidade('aa', 'aab')) # Saída: True

