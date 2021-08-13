"""
 Efetuar a leitura sucessiva de valores numéricos e apresentar o somatório, média e total de valores lidos.
 O programa deve fazer a leitura dos valores enquanto eles forem positivos. Parar quando entrar um valor negativo
"""

soma = total = x = 0

while x >= 0:
    x = int(input('Digite um valor: '))
    if x >= 0:
        soma += x
        total += 1
    else:
        break

print(f'A soma dos {total} valores é {soma}. A média é {soma/total}')

