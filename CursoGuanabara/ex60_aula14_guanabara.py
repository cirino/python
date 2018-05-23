from time import sleep

print('''
    Exercício 60 da aula 14 de Python
    Curso do Guanabara
    Day 23 Code Python - 22/05/2018
''')

numero = int(input('Número: '))
#fat = 1
fat = numero
opcao = numero

print('Calculando {}! = '.format(numero), end='')

while opcao > 0:
    sleep(0.1)

    print('{}'.format(opcao), end='')
    print(' x ' if opcao > 1 else ' = ', end='')

    #fat *= opcao
    opcao -= 1

    if opcao != 0:
       fat *= opcao

print(fat)

print('-='*16)
print('Fim do programa.')
