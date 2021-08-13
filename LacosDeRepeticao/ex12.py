# Efetuar a leitura de 10 valores numericos e apresentar o somatório e a media dos valores lidos


soma = 0
counter = 1

while counter < 11:
    x = int(input(f'Digite o {counter}º valor: '))
    soma += x
    counter += 1

print(f'A soma dos valores lidos é {soma} e a média é {soma/10}')

