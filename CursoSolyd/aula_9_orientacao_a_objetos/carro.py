from veiculo import Veiculo

print('''
    Aula 09 de Python
    Curso da Solyd
    Day 22 Code Python - 21/05/2018
''')

class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, marca, 4, tanque)

    def abastecer(self, litros):
        if (self.tanque + litros) > 50:
            print('Tanque não tem a capacidade solicitada')
        else:
            self.tanque += litros
