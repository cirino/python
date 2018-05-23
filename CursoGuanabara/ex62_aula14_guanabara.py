print('''
    Exercício 62 da aula 14 de Python
    Curso do Guanabara
    Day 23 Code Python - 22/05/2018
''')

print('Gerador de PA - Iniciando com 10 termos')
print('-=' * 15)

primeira = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeira
cont = 1
total = 0
continuar = 10

while continuar != 0:
    total += continuar
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')
    print('-=' * 15)
    continuar = int(input('Quantos termos a mais? Ou 0 (zero) para sair... '))

print('-=' * 15)
print('\nProgreção finalizada com {} termos mostrados.'.format(total))
