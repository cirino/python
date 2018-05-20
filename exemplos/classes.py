class Margarida:
    def _init_(self):
        print("init da Margarida")
        self.responsavel = "Tia Margarida"

    def criancas(self):
        print("Lalá, Lelé e Lili")

class Donald:
    def _init_(self):
        print("init do Donald")
        self.responsavel = "Tio Donald"

    def criancas(self):
        print("Huguinho, Zezinho e Luizinho")

    def amigos(self):
        print("Mickey e Pateta")


class Sobrinha(Donald, Margarida):
    def _init_(self):
        super()._init_()

    def todos(self):
        super().criancas()
        super().amigos()
        Margarida.criancas(self)

lulu = Sobrinha()
lulu.todos()
