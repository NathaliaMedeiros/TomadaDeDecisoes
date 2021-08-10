# Ler cinco valores inteiros, identificar e apresentar o maior e o menor valor informado.


for i in range(1, 6):
    x = int(input(f'Digite o {i}º valor: '))
    if i == 1:
        menor = maior = x
    elif x < menor:
        menor = x
    elif x > maior:
        maior = x

print(menor, maior)

