from models.carrinho.carrinho import Carrinho

class Usuario():
    def __init__(self, contato, senha):
        self._contato = contato
        self._nome_de_usuario = self._contato.get_email()
        self._senha = senha
        self._carrinho_de_compras = Carrinho()
    
    def adicionar_compra_carrinho(self, item):
        self._carrinho_de_compras.adicionar_item(item)
    
    def remover_compra_carrinho(self, item):
        self._carrinho_de_compras.remover_item(item)
    
    def get_contato(self):
        return self._contato
    
    def get_nome_de_usuario(self):
        return self._nome_de_usuario
        
    def get_senha(self):
        return self._senha

    def get_carrinho_de_compras(self):
        return self._carrinho_de_compras
    
    def __str__(self) -> str:
        return f'Nome de Usuário:{self._nome_de_usuario} Contato:{self._senha} Contato:{self._contato} Carrinho de Compra:{self._carrinho_de_compras}'



    
    
    
