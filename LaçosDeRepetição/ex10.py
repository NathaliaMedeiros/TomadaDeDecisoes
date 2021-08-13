"""
Efetuar o cálculo e apresentar o somatóprio do numero de grãos de trigo que se pode obter num tabulero de xadrez,
obedecendo à seguinte regra: colocar um grão de trigo no primeiro quadro e nos seguintes, o dobro do anterior.
"""

counter = total = 0
anterior = atual = 1


while counter < 64:
    if counter == 0:
        print(f'Casa 1: 1 grão')
        total = atual
    else:
        atual *= 2 * anterior
        total += atual
        print(f'Casa {counter + 1}: {atual} grãos')
    counter += 1


print(f'Total de grãos de 64 casas: {total}')

