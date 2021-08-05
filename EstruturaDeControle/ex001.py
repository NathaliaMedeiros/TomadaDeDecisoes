"""
Ler 3 valores para o lado de um triângulo
Verificar se cada lado é menor que a soma dos outros 2.
Verificar se é escaleno, isósceles ou equilátero.
Caso os dados não caracterizem um triângulo, informar na tela
"""

a = float(input('Insira o valor do primeiro lado do triângulo: '))
b = float(input('Insira o valor do segundo lado do triângulo: '))
c = float(input('Insira o valor do terceiro lado do triângulo: '))


if a < (b + c) and b < (a + c) and c < (b + a):
    if a == b == c:
        print('TRIÂNGULO EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('TRIÂNGULO ISÓSCELES')
    else:
        print('TRIÂNGULO ESCALENO')
else:
    print('Não configura um triângulo!')

