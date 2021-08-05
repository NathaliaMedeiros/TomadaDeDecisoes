# Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'{n1} - {n2} = {n1 - n2}')
else:
    print(f'{n2} - {n1} = {n2 - n1}')

