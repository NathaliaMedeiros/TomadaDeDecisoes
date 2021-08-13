# Escreva um programa que apresente a série de Fibonacci até o 15º termo -> 1, 1, 2, 3, 5, 8, 13, 21, 34

counter = 1
a = b = 1
res = 0

print('Sequência de Fibonacci ')
while counter < 16:
    if counter == 1 or counter == 2:
        print(f'{counter}º termo: {a}')
    else:
        res = a + b
        print(f'{counter}º termo: {res}')
        b = a
        a = res
    counter += 1

