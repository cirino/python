from random import randint

print('''
    Exercício 68 da aula 15 de Python
    Curso do Guanabara
    Day 24 Code Python - 23/05/2018
''')

print('Jogo de Par ou Ímpar')
print('-=' * 23)

vitorias = 0

while True:
    jogador = int(input('Digite um número: '))

    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I] ? ')).upper().strip()[0]

    print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {total} e deu ', end='')
    print('PAR' if total % 2 == 0 else 'ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU')
            vitorias += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU')
            vitorias += 1
        else:
            print('VOCÊ PERDEU')
            break

    print('\nJogando novamente...')
    print('-=' * 20)


print(f'GAME OVER. Você venceu {vitorias} vezes.')

print('FIM')
print('-=' * 20)
