from time import sleep

print("""
    Aula 06 de Python
    Curso da Solyd
    Day 20 Code Python - 19/05/2018
""")

lista = ['lu', 'mi']                           #LISTA (ORDENADA)

tupla = ('li', 'mi')                           #TUPLA

dicionario = {'nome': 'lu', 'idade' : 5}       #DICIONARIO (CHAVE E VALOR)

conjunto = {'lu', 'mi', 'dag', 'lu', 'mi'}     #CONJUNTO (SOMENTE O VALOR - AGRUPA - SEM REPETIÇÕES)

print(lista[0])
print(tupla[1])

if 'lu' in dicionario.values():
    print('Está no dicionário.')

conjunto.add('python')    
print(conjunto)
