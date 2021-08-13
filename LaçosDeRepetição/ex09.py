# Apresentar os valores de conversão de graus Celsius em Fahrenheit, de 10 em 10, iniciando a contagem em 10 graus.


celsius = 10

while celsius <= 200:
    fahrenheit = (9 * celsius + 160) / 5
    print(f'{celsius}ºC é igual a {fahrenheit}ºF')
    celsius += 10

