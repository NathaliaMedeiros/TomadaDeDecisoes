# Apresentar os resultados de uma tabuada de um número qualquer

numero = int(input('Qual tabuada deseja obter o resultado? '))

counter = 0

while counter <= 10:
    print(f'{numero} x {counter} = {numero * counter}')
    counter += 1
