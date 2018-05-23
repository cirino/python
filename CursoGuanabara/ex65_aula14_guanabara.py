print('''
    Exercício 65 da aula 14 de Python
    Curso do Guanabara
    Day 23 Code Python - 22/05/2018
''')

print('Média, maior e menor número')
print('-=' * 20)

resp = 's'
media = soma = qtd = maior = menor = 0

while resp in 'sS':
    n = int(input('Digite o número: '))
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    soma += n
    qtd += 1
    if qtd == 1:
        maior = menor = qtd
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / qtd

print('-=' * 20)
print('Você digitou {} números e a média foi {:.2f}.'.format(qtd, media))
print('O maior número é o {} e o menor é o {}'.format(maior, menor))

print('FIM')
print('-=' * 20)
