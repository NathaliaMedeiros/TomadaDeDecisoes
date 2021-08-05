"""
Ler os valores de quatro notas escolares de um aluno. Calcular a média aritmética e apresentar a mensagem 'APROVADO'
se media >= 5;
Caso contrário, apresentar a msg 'REPROVADO'. Informar junto com cada mensagem o valor da média obtida.
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

res = (n1 + n2 + n3 + n4) / 4

if res >= 5:
    print(f'Nota {res} - APROVADO')
else:
    print(f'Nota {res} - REPROVADO')


