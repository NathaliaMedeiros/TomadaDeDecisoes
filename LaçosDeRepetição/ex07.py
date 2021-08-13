# Elaborar um programa que apresente como resultado o valor de uma potencia de base qualuqer elevada a um expoente

base = int(input('Digite o valor da base: '))
expoente = int(input('Digite o valor do expoente: '))

counter = 0
result = 1

while counter < expoente:
    result *= base
    counter += 1

print(f'{base} ^ {expoente} = {result}')

