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

produtos = []
def cadastrarProduto(nome, codigo, preco, quantidade):
    produtos.append(Produto(nome, codigo, int(preco), int(quantidade)))
    ui.notify('Produto Cadastrado!', type='positive', timeout=3000)

def listarProdutos():
    for i in produtos:
        with ui.card():
            ui.label(i.nome)

with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'): # menu de cima
    ui.label('LEET Empresas')
    ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')


with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer: # menu da direita
    ui.label('Opções:')  
    with ui.expansion('Produtos', icon='inventory_2').style('background-color: #00FFFF'): # não funciona ainda
        for i in produtos:
            ui.label(i.nome)
    # ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')

with ui.row(): # para cadastrar produtos
    ui.label('Cadastrar Produto')
    nome = ui.input(label='Nome:').props('square outlined dense').classes('shadow-lg')
    codigo = ui.input(label='Código:').props('square outlined dense').classes('shadow-lg')
    preco = ui.input(label='Preço:').props('square outlined dense').classes('shadow-lg')
    quantidade = ui.input(label='Quantidade:').props('square outlined dense').classes('shadow-lg')
    ui.button('Cadastrar', on_click=lambda: cadastrarProduto(nome.value, codigo.value, preco.value, quantidade.value))


ui.run()