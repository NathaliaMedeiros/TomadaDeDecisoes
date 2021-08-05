"""
Ler três valores numéricos e fazer o calculo da equação completa de segundo grau, utilizando Baskara.
Considerar delta < 0, > 0 e = 0. A, B e C devem ser diferentes de 0.
"""
import math
x1 = x2 = 0


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a ==  0 or b == 0 or c == 0:
    print('Não é possível proseguir com a equação.')
else:
    delta = b * b - (4 * a * c)
    print(delta)

    if delta < 0:
        print('Não há raíz real')
    else:
        x1 = ((-b + math.sqrt(delta)) / (2 * a))
        x2 = ((-b - math.sqrt(delta)) / (2 * a))

    if delta == 0:
        print(f'A raíz é {x1}')
    else:
        print(f'Raíz 1 é {x1} e raíz 2 é {x2}')

