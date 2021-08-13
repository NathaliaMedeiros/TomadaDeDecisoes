# efetuar a leitura de 15 valores numericos inteiros e no final apresente o somatório do fatoria de cada valor lido

counter = 1
result = 1

while counter < 16:
    x = int(input('Digite um valor para obter seu fatorial: '))
    print(f'O fatorial de {x} é ', end='')
    while x > 1:
        result *= x
        x -= 1
    print(result, end='')
    print()
    print('=-' * 30)
counter += 1

