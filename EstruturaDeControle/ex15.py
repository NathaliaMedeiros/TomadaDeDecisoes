"""
Ler e apresentar nome e sexo de uma pessoa e apresentar como saida uma das seguintes msgs: 'Ilmo. Sr' ou 'Ilma. Sra'
"""

nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo (M/F):')
sexo = sexo.upper()

if 'F' in sexo:
    print(f'Olá, Sra. {nome.capitalize()}')
else:
    print(f'Olá, Sr. {nome.capitalize()}')

