"""
Ler um valor numerico inteiro que esteja na faixa de valores de 1 ate 9. O programa deve apresentar a mensagem
'O valor está na faixa permitada' caso o número seja de 1 a 9, caso contrário, apresentar 'O valor está fora da faixa'
"""

x = int(input('Digite um valor: '))

if 1 <= x <= 9:
    print('O valor está dentro da faixa permitida')
else:
    print('O valor não está dentro da faixa permitida')
