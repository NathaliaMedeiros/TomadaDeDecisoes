# Apresentar os resultados da soma e média aritmetica dos valores pares situados entre 50 e 70

counter = 50
soma = valores = 0

while counter <= 70:
    if counter % 2 == 0:
        soma += counter
        valores += 1
    counter += 1


print(f'A soma dos {valores} valores pares entre 50 e 70 é {soma}. A média é igual a {soma / valores}')


