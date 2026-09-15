from abc import ABC, abstractmethod
from datetime import datetime
from nicegui import ui

class Produto():
    def __init__(self, nome, codigo, preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade

    def avisarFalta(self):
        if self.quantidade <= 0: return f"{self.nome} esgotado!"
        elif self.quantidade <= 5: return f"{self.nome} acabando!"

    def getInformacoes(self): 
        return self.codigo, self.preco

    def __str__(self): return f'Nome: {self.nome} - Código: {self.codigo} - Preço: R${self.preco}:.2f'
   
class Movimentacao(ABC): # compra e venda
    def __init__(self, codigo, *args):
        self.codigo = codigo
        self.produtos = [*args]
        self.preco_final = calcularPrecoFinal()
        tempo = datetime.now() # pega a data e hora da venda
        self.data = tempo.strftime('%d/%m/%Y %H:%M')

    @abstractmethod
    def calcularPrecoFinal(self): pass

class Venda(Movimentacao):
    def __init__(self, codigo, *args):
        super().__init__(codigo, *args)
        
    def calcularPrecoFinal(self):
        preco_final = 0
        for i in self.produtos:
            preco_final += i.preco
        return preco_final

class Compra(Movimentacao):
    def __init__(self, codigo, *args):
        super().__init__(codigo, *args)

    def calcularPrecoFinal(self):
        preco_final = 0
        for i in self.produtos:
            preco_final += i.preco
        return preco_final

class Conta():
    def __init__(self, descricao, valor, vencimento):
        self.descricao = descricao
        self.valor = valor
        self.vencimento = vencimento

    def avisarVencimento(self):
        tempo = datetime.now()
        if self.vencimento == tempo.strftime('%d/%m/%Y'):
            return f"{self.descricao} vence hoje!"

    def getInformacoes(self):
        return self.descricao, self.valor
