from time import sleep

print('''
    Aula 07 de Python
    Curso da Solyd
    Day 21 Code Python - 20/05/2018
''')

def contador():
    qtdLetras = len(str(input('Qual a palavra ou frase? ')).strip())
    return qtdLetras

qtdContar = int(input('Quantos caracteres deve ter? '))

total = contador() 

print('\nContando...')
sleep(0.5)

if total == qtdContar:
    print('Tem o tamanho dos seus Sonhos xD =>', total )
else:
    print('Xii, tem um tamanho diferente hehehe =>', total)
