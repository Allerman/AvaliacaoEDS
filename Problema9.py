# você deve escrever um programa em Python que verifique a viabilidade de
# uma prescrição, dado o estado do estoque naquele momento.
# A entrada do seu programa deve ser duas sequências de caracteres. A
# primeira sequência indica quais medicamentos foram prescritos e a
# segunda quais medicamentos estão no estoque. Em ambas as
# sequencias, cada letra representa um medicamento

from collections import Counter

def verificar_viabilidade(prescricao, estoque, medicamento_verificar):
    prescricao = prescricao.upper() 
    estoque = estoque.upper()

    freq_prescricao = Counter(prescricao)
    freq_estoque = Counter(estoque)

    if medicamento_verificar.upper() not in freq_prescricao:
        return "Medicamento não consta na prescrição."

    if medicamento_verificar.upper() not in freq_estoque or freq_prescricao[medicamento_verificar.upper()] > freq_estoque[medicamento_verificar.upper()]:
        return "Medicamento indisponível no estoque."

    return "Medicamento disponível no estoque."

def main():
    prescricao = input("Insira a prescrição de medicamentos separada por espaços: ")
    estoque = input("Insira o estoque de medicamentos separado por espaços: ")
    medicamento_verificar = input("Digite o medicamento que deseja verificar a viabilidade: ")

    prescricao = prescricao.upper() 
    estoque = estoque.upper()

    resultado = verificar_viabilidade(prescricao, estoque, medicamento_verificar)
    print(resultado)

if __name__ == "__main__":
    main()
