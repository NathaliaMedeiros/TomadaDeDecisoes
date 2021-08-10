"""
Ler 3 valores e apresentá-los dispostos em ordem crescente. Utilizar a propriedade distributiva e troca de valores
entre variáveis
"""

a = int(input())
b = int(input())
c = int(input())

aux = 0

if c < b:
    aux = c
    c = b
    b = aux

if b < a:
    aux = b
    b = a
    a = aux

if c < b:
    aux = c
    c = b
    b = aux

print(a, b, c)

