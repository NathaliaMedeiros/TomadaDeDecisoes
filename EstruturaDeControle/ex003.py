"""
Ler um número inteiro qualquer N
Calcular o resto da divisão de N por 4
Calcular o resto da divisão de N por 5
Verificar se ambas as variáveis possuem o valor zero, se sim, apresentar a variável N, se não, apresentar a mensagem:
'Não é divisível por 4 e 5'
"""

n = int(input('Digite um número inteiro: '))

r4 = n % 4
r5 = n % 5

if r4 == r5 == 0:
    print(n)
else:
    print('Não é divisível por 4 e 5')

