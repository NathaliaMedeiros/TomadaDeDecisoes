# Elaborar um programa que apresente a soma dos valores ímpares entre 1 e 500

counter = 1
soma = 0


while counter <= 500:
    if counter % 2 != 0:
        soma += counter
    counter += 1


print(f'A soma dos valores ímpares entre 1 e 500 é igual a {soma}')

