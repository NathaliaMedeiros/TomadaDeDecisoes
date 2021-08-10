# Ler quatro valores numéricos inteiros e apresentar os valores que são divisíveis por 2 ou 3


for i in range(1, 5):
    x = int(input(f'Digite o {i}º valor: '))
    if x % 2 == 0 or x % 3 == 0:
        print(f'O número {i} é divisível por 2 ou 3')
        print()

