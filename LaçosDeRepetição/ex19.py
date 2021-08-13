# Apresentar o resultado inteiro da divisao de dois numeros quaisquer. NÃO utilizar o DIV

x = int(input('Digite um numero: '))
y = int(input('Digite outro numero: '))

quociente = 0

if y > x:
    print('Não há resultado inteiro')
else:
    while x >= y:
        if x >= y:
            quociente += 1
            x -= y

    print(quociente)

