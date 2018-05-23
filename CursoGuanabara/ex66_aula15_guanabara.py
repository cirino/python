print('''
    Exercício 66 da aula 15 de Python
    Curso do Guanabara
    Day 24 Code Python - 23/05/2018
''')

print('Somando em loop')
print('-=' * 20)

cont = soma = 0

while True:
    n = int(input('Digite um número [999 parar o programa]: '))

    if n == 999:
        break

    soma += n
    cont += 1

print('-=' * 20)
print(f'{cont} números digitados, e a soma é {soma}')

print('FIM')
print('-=' * 20)
