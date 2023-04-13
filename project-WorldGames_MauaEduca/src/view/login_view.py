import streamlit as st
from src.util import Util
from src.models.usuario import Usuario


class Login_View:

    def __init__(self, app_controller):
        self.app_controller = app_controller
        st.title("Bem vindo ao W🌎rld Games! 🚀")
        st.header("Login")

        self.login_email = st.text_input(label="E-mail", placeholder="Digite seu E-mail", value="")
        self.login_senha = st.text_input(label="Senha", placeholder="Digite sua Senha", value="")
    
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 3.35, 1.5])

        with col1:
            self.btt_fazer_login = st.button(label="Entrar",
                                             on_click=self.autenticar_login
                                            )

        with col4:
            self.msg_cadastro = st.write("Novo por aqui? Faça agora seu Cadastro👉")

        with col5:
            self.btt_fazer_cadastro = st.button(label="Cadastra-se",
                                                on_click=Util.setar_ambiente_cadastro
                                                )
        
        Util.escrever_mensagem_aviso()

    def autenticar_login(self):
        if (Util.validar_string(self.login_email) and Util.validar_string(self.login_senha)):
            usuario = self.app_controller.usuario_controller.buscar_usuario_email(self.login_email)
            if (usuario == None or usuario.get_senha() != self.login_senha):
                st.session_state["Mensagem Aviso"] = "Usuário não Encontrado!"
            else:
                st.session_state["Email Logado"]   = usuario.get_email()
                st.session_state["Mensagem Aviso"] = None
                st.session_state["Pagina"]         = "Pagina Loja"

        else:
            st.session_state["Mensagem Aviso"] = "Preencher todos os campos!"
        


            

