"""
Ler um valor numerico inteiro positivo ou negativo e apresentar o valor lido como sendo um valor positivo, ou seja, se
o valor lido for menor ou igual a 0, ele deve ser multiplicado por -1
"""

x = int(input('Digite um número: '))

if x < 0:
    x = x * -1

print(x)

