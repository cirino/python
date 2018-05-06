print("""
    Exercício 24 da aula 09 de Python
    Curso do Guanabara
    Day 7 Code Python - 06/05/2018
""")

cidade = str(input('Qual cidade você nasceu: ')).strip()

#a primeira é "santo"
print(cidade.lower().split()[0] == 'santo')

#a primeira começa com "santo..."
print(cidade[:5].lower() == 'santo')