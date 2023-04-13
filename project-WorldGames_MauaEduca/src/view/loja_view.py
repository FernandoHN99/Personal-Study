import streamlit as st
from src.util import Util


class Loja_View:

    def __init__(self, app_controller):
        self.app_controller = app_controller

        self.lista_nomes_itens = list(self.app_controller.item_controller.gerar_dict_item_nomes().values())
        self.lista_id_itens = list(self.app_controller.item_controller.gerar_dict_item_nomes().keys())

        self.lista_nomes_itens.insert(0,"Visualizar Todos")

        self.opcao_busca = st.selectbox("Pesquise aqui seu jogo!",
                                    options=self.lista_nomes_itens,
                                    index=0)
        
        self.exibir_itens_busca()
        
    
    def exibir_itens_busca(self):

        if self.opcao_busca != "Visualizar Todos":
            index_item = self.lista_nomes_itens.index(self.opcao_busca)
            item = self.app_controller.item_controller.buscar_item_id(self.lista_id_itens[index_item-1])
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                self.exibir_item(item, 250, 300)
        else:
            self.exibir_todos_itens()
    
    def exibir_item(self, item, x, y):
        st.subheader(item.get_nome())
        st.image(Util.ajustar_imagem(item.get_imagem(),x, y))
        st.info("R$ " + Util.converter_float_str(item.get_valor()),icon="💵")
        btt_add_car = st.button(label="Adicionar ao carrinho",
                                key=("btt"+str(item.get_id())),
                                on_click=self.app_controller.adicionar_compra,
                                kwargs={"item_id_":item.get_id()}
                                )
        
        if btt_add_car:
            st.balloons()


    def exibir_todos_itens(self):
        col1, col2, col3 = st.columns([1, 1, 1])
        var_control1 = True
        var_control2 = False
        var_control3 = False

        for item_id in self.lista_id_itens:
            item = self.app_controller.item_controller.buscar_item_id(item_id)
            if var_control1:
                with col1:
                    self.exibir_item(item, 200, 250)
                    var_control1 = False
                    var_control2 = True

            elif var_control2:
                with col2:
                    self.exibir_item(item, 200, 250)
                    var_control2 = False
                    var_control3 = True
            
            elif var_control3:
                with col3:
                    self.exibir_item(item, 200, 250)
                    var_control3 = False
                    var_control1 = True



        

            
    







