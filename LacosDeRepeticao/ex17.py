"""
Elaborar um programa que possibilite calcular a area total de uma residencia. Solicitar a entrada do nome do cômodo,
largura e comprimento dele. Caso queira parar o programa, entrar com a palavra 'nao'
"""

total = 0
teste = True

while teste:
    comodo = input('Digite o nome do cômodo ou "nao" para encerrar: ')
    if comodo == 'nao':
        teste = False
    else:
        largura = float(input(f'Qual a largura de {comodo}? '))
        comprimento = float(input(f'Qual o comprimento de {comodo}? '))
        print()
        area = largura * comprimento
        total += area

print(f'A casa possui área total igual a {total} m³')

