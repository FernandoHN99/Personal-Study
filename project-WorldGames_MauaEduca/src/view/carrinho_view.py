import streamlit as st
from src.util import Util

class Carrinho_View:

    def __init__(self, app_controller):
        self.app_controller = app_controller

        st.header("Confira tudo pra ver se não faltou nada! 😉")
        col1, col2, col3 = st.columns([1.8,1.5,0.8])
        
        with col1:
            st.header("Produto")
        with col2:
            st.header("Quantidade")
        with col3:
            st.header("Total")

        col1, col2, col3, col4, col5 = st.columns([1.75,0.05,0.8,0.4,0.8])

        for item_pedido in self.app_controller.carrinho_usuario:
            with col1:
                st.subheader(item_pedido["Item"].get_nome())
            
            with col3:
                st.write("")
                qtde_input = st.number_input(label="btt_input",
                                            key=("btt_input" + item_pedido["Item"].get_id()),
                                            min_value=0,
                                            value = item_pedido["Qtde"],
                                            label_visibility="collapsed"
                                            )

                self.alterar_carrinho_input(qtde_input, item_pedido["Qtde"], item_pedido["Item"].get_id())

            with col5:
                sub_total_item = item_pedido["Item"].get_valor() * item_pedido["Qtde"]
                st.subheader("R$ " + Util.converter_float_str(sub_total_item))

        col1, col2 = st.columns([1,0.4])

        with col1:
            st.header("Valor Total a Pagar: ")

        with col2:
            valor_total_compra = Util.converter_float_str(self.app_controller.calcular_total_carrinho())
            st.header("R$" + valor_total_compra)



        


        
    def alterar_carrinho_input(self, qtde_desejada, qtde_atual, item_id):
        if qtde_desejada > qtde_atual:
            self.app_controller.adicionar_compra(item_id)
            st.experimental_rerun()


        elif qtde_desejada < qtde_atual:
            self.app_controller.remover_compra(item_id)
            st.experimental_rerun()








                
        




