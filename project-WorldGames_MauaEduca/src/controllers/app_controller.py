from src.controllers.usuario_controller import Usuario_Controller
from src.controllers.item_controller import Item_Controller
from src.controllers.pedido_controller import Pedido_Controller
from src.models.pedido import Pedido
from src.models.item import Item
from src.models.usuario import Usuario
import streamlit as st
import uuid

class App_Controller:

    def __init__(self):
        self.usuario_controller = Usuario_Controller() if st.session_state["App Controller"] == None else st.session_state["App Controller"].usuario_controller
        self.item_controller    = Item_Controller() if st.session_state["App Controller"] == None else st.session_state["App Controller"].item_controller 
        self.pedido_controller  = Pedido_Controller() if st.session_state["App Controller"] == None else st.session_state["App Controller"].pedido_controller
        self.usuario_logado     = self.usuario_controller.buscar_usuario_email(st.session_state["Email Logado"])
        self.carrinho_usuario   = [] if self.usuario_logado == None else self.montar_carrinho()
        self.numero_pedido      = [] if self.usuario_logado == None else self.pegar_numero_pedido()

    def montar_carrinho(self):
        carrinho = []
        lista_pedidos = self.pedido_controller.buscar_pedido_user_status(self.usuario_logado.get_email(), "Carrinho")
        self.pedido_controller.exibir_pedidos_cadastrados()
        for pedido in lista_pedidos:
            carrinho.append({"Id":pedido.get_id() ,"Item": self.item_controller.buscar_item_id(pedido.get_item_id()), "Qtde": pedido.get_qtde()})
        return carrinho
    
    def pegar_numero_pedido(self):
        lista_pedidos = self.pedido_controller.buscar_pedido_user_status(self.usuario_logado.get_email(), "Carrinho")
        if len(lista_pedidos) > 0:
            return lista_pedidos[0].get_numero_pdd()
        else:
            return self.usuario_logado.get_email() + str(uuid.uuid4())
        
    def pegar_qtde_itens_carrinho(self, item_id):
        for item_carrinho in self.carrinho_usuario:
            if item_carrinho["Item"].get_id() == item_id:
                return item_carrinho["Qtde"]
        return 0

    def adicionar_compra(self, item_id_):
        qtde_item = self.pegar_qtde_itens_carrinho(item_id_) 
        if qtde_item != 0:
            for item_carrinho in self.carrinho_usuario:
                if item_carrinho["Item"].get_id() == item_id_:
                    id_pedido = item_carrinho["Id"]
                    pdd = Pedido(email_user=self.usuario_logado.get_email(), status="Carrinho", qtde=(qtde_item+1), item_id=item_id_, numero_pdd=self.numero_pedido)
                    self.pedido_controller.atualizar_pedido(id_pedido, pdd)
                    break
        else:
            pdd = Pedido(email_user=self.usuario_logado.get_email(), status="Carrinho", qtde=1, item_id=item_id_, numero_pdd=self.numero_pedido)
            self.pedido_controller.adicionar_pedido(pdd)

    def remover_compra(self, item_id_):
        qtde_item = self.pegar_qtde_itens_carrinho(item_id_)
        for item_carrinho in self.carrinho_usuario:
                if item_carrinho["Item"].get_id() == item_id_:
                    id_pedido = item_carrinho["Id"]
                    break
        if qtde_item != 1:
            pdd = Pedido(email_user=self.usuario_logado.get_email(), status="Carrinho", qtde=(qtde_item-1), item_id=item_id_, numero_pdd=self.numero_pedido)
            self.pedido_controller.atualizar_pedido(id_pedido, pdd)
        else:
            self.pedido_controller.remover_pedido(id_pedido)
    
    def calcular_total_carrinho(self):
        qtd_total = 0
        for item_carrinho in self.carrinho_usuario:
            qtd_total += item_carrinho["Item"].get_valor() * item_carrinho["Qtde"]
            
        return qtd_total

    def calcular_qtde_itens_carrinho(self):
        qtd_total = 0
        for item_carrinho in self.carrinho_usuario:
            qtd_total += item_carrinho["Qtde"]
        return qtd_total













