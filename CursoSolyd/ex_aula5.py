from time import sleep

print("""
    Exercício da aula 05 de Python
    Curso da Solyd
    Day 20 Code Python - 19/05/2018
""")

qtd_pessoas = int(input('Quantas pessoas serão convidadas para a festa? '))

lista_convidados = []

while len(lista_convidados) < qtd_pessoas:
    lista_convidados.append((input('Qual o nome do convidado? ').strip()))
    print('Adicionando...\n')
    sleep(0.5)

print('Lista de convidados:')
print(lista_convidados)
