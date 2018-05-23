from time import sleep
import sys

print('''
    Aula 08 de Python
    Curso da Solyd
    Day 21 Code Python - 20/05/2018
''')

argumentos = sys.argv

def soma(n1 = 0, n2 = 0):
    return n1 + n2

def sub(n1 = 0, n2 = 0):
    return n1 - n2

if len(argumentos) > 1 and len(argumentos) <= 4:
    if (argumentos[1]) == 'help':
        print('''
            Ajuda do Cirino:
                argumentos:
                soma num1 num2 => retorna a soma de num1 + num2
                sub  num1 num2 => retorna a subtração de num1 - num2
        ''')

    elif len(argumentos) <= 3:
        print('Passe os 3 argumentos, ou help para ajuda')

    elif len(argumentos[3]) > 0:
        if argumentos[1] == 'soma':
            calc = soma(float(argumentos[2]), float(argumentos[3]))
        elif argumentos[1] == 'sub':
            calc = sub(float(argumentos[2]), float(argumentos[3]))
        else:
            calc = 'Algo errado ...'
        print('Calculando...')
        sleep(1)
        print(calc)
else:
    print('Vixe, que erro loko véio. Passe help no parâmetro para rodar certinho a parada.')

print('FIM')
