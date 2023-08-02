# Extreme Digital Solutions
Este repositório contém uma série de códigos SQL e Python desenvolvidos como parte da avaliação para a 
Extreme Digital Solutions. Os códigos foram criados para demonstrar habilidades em programação e engenharia de dados.

## Problemas

### Problema 1
Este código implementa uma função chamada `verificar_viabilidade` que verifica se uma prescrição de medicamentos é viável com base no estoque disponível. O usuário deve inserir duas sequências de caracteres separadas por espaços: a primeira sequência indica quais medicamentos foram prescritos e a segunda indica quais medicamentos estão no estoque. Cada letra representa um medicamento e a frequência de cada letra representa a dose desse medicamento. O código realiza a contagem dos medicamentos nas sequências usando a classe `Counter` do módulo `collections` e, em seguida, verifica se o medicamento desejado está presente na prescrição e se há quantidade suficiente dele no estoque. A saída do código informa se o medicamento é viável, se está indisponível no estoque ou se não consta na prescrição.

### `prescricao-estoque/verificar_viabilidade_input.py`
Este código é uma versão aprimorada do anterior, adicionando uma interface de input para o usuário. Ele permite que o usuário insira as sequências de medicamentos diretamente durante a execução do programa, tornando o processo de verificação mais interativo e amigável.

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
