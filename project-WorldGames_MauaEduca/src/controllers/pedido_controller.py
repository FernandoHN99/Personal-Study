from src.models.pedido import Pedido

class Pedido_Controller:

    def __init__(self):
        self._pedidos_cadastrados = []

    def adicionar_pedido(self, pedido):
        self._pedidos_cadastrados.append(pedido)
        # self.exibir_pedidos_cadastrados()
    
    def remover_pedido(self, id_pedido):
        for pedido in self._pedidos_cadastrados:
            if id_pedido == pedido.get_id():
                self._pedidos_cadastrados.remove(pedido)
                return True
        return False
    
    def atualizar_pedido(self, id_pedido, pedido):
        if self.remover_pedido(id_pedido):
            self.adicionar_pedido(pedido)
            return True
        return False
    
    def buscar_pedido_user_status(self, usuario_email, status):
        lista_pedidos = []
        for pedido in self._pedidos_cadastrados:
            if(pedido.get_email_user() == usuario_email and status == pedido.get_status()):
                lista_pedidos.append(pedido)
        return lista_pedidos

    
    def get_pedidos_cadastrados(self):
        return self._pedidos_cadastrados
    
    def exibir_pedidos_cadastrados(self):
        for i, pedido in enumerate(self._pedidos_cadastrados):
            print(f"Pedido {i}:", pedido)
