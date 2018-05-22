from datetime import date

print('''
    Exercício 54 da aula 13 de Python
    Curso do Guanabara
    Day 22 Code Python - 21/05/2018
''')

hoje = date.today().year
maior = 0
menor = 0

for n in range(1, 4):
    nasc = int(input('Ano de nascimento: '))
    if nasc < (hoje - 18):
        maior += 1
    else:
        menor += 1

print('\nmaior de idade:', maior)
print('menor de idade', menor)

print('FIM')
