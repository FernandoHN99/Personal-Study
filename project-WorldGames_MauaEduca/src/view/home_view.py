import streamlit as st
from src.util import Util
from src.view.loja_view import Loja_View
from src.view.carrinho_view import Carrinho_View


class Home_View:

    def __init__(self, app_controller):
        self.app_controller = app_controller

        qtde_total_itens = self.app_controller.calcular_qtde_itens_carrinho()

        loja, carrinho = st.tabs(["Loja", f'Carrinho ({qtde_total_itens}) 🛒'])

        with loja:
            self.pagina_loja = Loja_View(self.app_controller)

        with carrinho:
            if qtde_total_itens != 0:
                self.pagina_carrinho = Carrinho_View(self.app_controller)
            else:
                self.pagina_carrinho = None
                st.header("Putz! Parece que seu carrinho está vazio! 😢")


        st.sidebar.radio("Navegação",["Home", "Minha Conta", "About Us"])
        st.sidebar.button(label="Sair",
                        on_click=Util.setar_ambiente_login
                        )

        



