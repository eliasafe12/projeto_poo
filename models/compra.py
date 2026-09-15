from models.movimentacao import Movimentacao
class Compra(Movimentacao):
    def __init__(self, codigo, *args):
        super().__init__(codigo, *args)

    def calcularPrecoFinal(self):
        preco_final = 0
        for i in self.produtos:
            preco_final += i[2]
        return preco_final
