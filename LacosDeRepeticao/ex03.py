# Apresentar o total da soma dos 100 primeiros números inteiros

counter = 0
soma = 0


while counter <= 100:
    soma += counter
    counter += 1


print(f'A soma dos 100 primeiros números inteiros é igual a {soma}')
