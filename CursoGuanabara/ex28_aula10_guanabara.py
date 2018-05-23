print("""
    Exercício 28 da aula 10 de Python
    Curso do Guanabara
    Day 7 Code Python - 06/05/2018
""")

from random import randint
from time import sleep

numero = int(input('Adivinhe o número: '))
computador = randint(0, 5)

print('-=-'*30)
sleep(2)

if numero == computador:
    print('Acertou, Uhuuu: {}'.format(numero))
else:
    print('Pensei no número {} e o computador escolheu {}'.format(numero, computador))
