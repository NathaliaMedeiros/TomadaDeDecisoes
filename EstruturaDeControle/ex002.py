"""
Desenvolver um programa que leia um valor numérico inteiro e apresente-o caso seja divisível por 4 e 5
"""

x = int(input('Digite um número: '))

if x % 20 == 0:
    print(f'O número {x} é divisível por 4 e 5')
else:
    print(f'O número {x} não é divisível por 4 e 5')

