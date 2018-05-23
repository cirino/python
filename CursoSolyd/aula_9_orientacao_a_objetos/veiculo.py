print('''
    Aula 09 de Python
    Curso da Solyd
    Day 22 Code Python - 21/05/2018
''')

class Veiculo:
    def __init__(self, cor, marca, rodas, tanque):
        self.cor = cor
        self.marca = marca
        self.rodas =  rodas
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros
