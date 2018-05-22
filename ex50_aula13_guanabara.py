print('''
    Exercício 50 da aula 13 de Python
    Curso do Guanabara
    Day 22 Code Python - 21/05/2018
''')

soma = 0

for n in range(1, 7):
    num = int(input('Numero: '))

    if num % 2 == 0:
        soma += num

print('Soma dos pares: {}'.format(soma))
