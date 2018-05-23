from time import sleep

print('''
    Exercício 59 da aula 14 de Python
    Curso do Guanabara
    Day 23 Code Python - 22/05/2018
''')

primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))

opcao = 0

while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

    opcao = int(input('Qual a sua opção? '))
    sleep(0.5)

    if opcao == 1:
        print('A soma de {} e {} é {}'.format(primeiro, segundo, primeiro + segundo))
    elif opcao == 2:
        print('A multiplição de {} e {} é {}'.format(primeiro, segundo, primeiro * segundo))
    elif opcao == 3:
        if primeiro > segundo:
            print('Entre {} e {} o maior é {}'.format(primeiro, segundo, primeiro))
        elif primeiro < segundo:
            print('Entre {} e {} o menor é {}'.format(primeiro, segundo, segundo))
        else:
            print('{} e {} são iguais'.format(primeiro, segundo))
    elif opcao == 4:
        primeiro = int(input('Primeiro número: '))
        segundo = int(input('Segundo número: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-='*16)

    sleep(1)
print('Fim do programa.')
