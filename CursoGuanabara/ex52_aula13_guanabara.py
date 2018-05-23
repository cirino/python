print('''
    Exercício 52 da aula 13 de Python
    Curso do Guanabara
    Day 22 Code Python - 21/05/2018
''')

num = int(input('Número inteiro: '))
cont = 0

for n in range(1, num + 1):
    if num % n == 0:
        cont += 1

if cont == 2:
    print('Número primo. cont: {}'.format(cont), end=' -> ')

print('FIM')
