"""
Ler os valores de quatro notas escolares de um aluno. Calcular a média aritmética e apresentar a mensagem “Aprovado”
se a média obtida for maior ou igual a 7; caso contrário, o programa deve solicitar a nota de exame do aluno e calcular
uma nova média aritmética entre a nota de exame com a primeira média aritmética. Se o valor da nova média for maior ou
igual a 5 apresentar a mensagem “Aprovado em exame”; caso contrário, apresentar a mensagem “Reprovado”.
Informar junto com cada mensagem o valor da média obtida
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

res = (n1 + n2 + n3 + n4) / 4

if res >= 7:
    print(f'Média {res} - APROVADO')
else:
    print('Não atingiu a média')
    exame = int(input('Digite a nota de exame: '))
    NovaMedia = (res + exame) / 2
    if NovaMedia >= 5:
        print(f'Média {NovaMedia} - Aprovado em exame')
    else:
        print(f'Média {NovaMedia} - Reprovado')

