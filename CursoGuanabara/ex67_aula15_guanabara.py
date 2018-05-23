print('''
    Exercício 67 da aula 15 de Python
    Curso do Guanabara
    Day 24 Code Python - 23/05/2018
''')

print('Tabuada')
print('-=' * 23)

cont = soma = 0

while True:
    n = int(input('Digite um número para ver a tabuada [Negativo parar o programa]: '))

    if n < 0:
        break

    for t in range(1, 11):
        print(f'{n} * {t} = {n * t}')

    print('-=' * 20)

print('FIM')
print('-=' * 20)
