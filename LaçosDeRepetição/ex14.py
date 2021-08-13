# Apresentar como resultado o valor do fatorial dos ímpares de 1 a 10


for i in range(1, 11):
    aux = i
    result = 1
    if i % 2 != 0:
        while i >= 2:
            result *= i
            i -= 1
        print(f'Fatorial de {aux} = {result}')

