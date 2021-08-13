# Efetuar a leitura de valores positivos inteiros até que um valor negativo seja informado. Apresentar o maior e menor


menor = maior = counter = 0
teste = True


while teste:
    x = int(input('Digite um número: '))
    if counter == 0:
        menor = maior = x
    elif  x < menor:
        menor = x
    elif x > maior:
        maior = x
    counter += 1

    if x < 0:
        teste = False


print(f'Menor: {menor}. Maior: {maior}')

