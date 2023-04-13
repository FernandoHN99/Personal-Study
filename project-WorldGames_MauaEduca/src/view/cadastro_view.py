import streamlit as st
from src.util import Util
from src.models.usuario import Usuario
from src.models.contato import Contato
import datetime as dt

class Cadastro_View:

    def __init__(self, app_controller):
        self.app_controller = app_controller

        data_min = dt.date(1900,1,1)
        data_max = dt.date.today()


        st.title("Sua Jornada Começa Agora !🚀🔥")
        st.subheader("Meu Primeiro Acesso")
    
        self.nome_contato = st.text_input(label="Nome", placeholder ="Digite seu Nome Completo", value="")
        col1, col2 = st.columns([1,1])

        with col1:
            self.email_usuario = st.text_input(label="E-mail", placeholder ="Digite seu endereço de E-mail", value="")
            self.telefone_contato = st.text_input(label="Telefone", placeholder ="Digite seu Telefone", value="")

        with col2:
            self.genero_contato = st.selectbox('Gênero', ('Masculino', 'Feminino', 'Nenhum'), index=0)
            self.dt_nascimento_contato = st.date_input(label="Data de Nascimento", min_value=data_min, max_value=data_max)

        self.senha_usuario = st.text_input(label="Senha", placeholder ="Digite uma senha", value="",  type='password')
        self.senha_usuario_check = st.text_input(label="Confirmação de Senha", placeholder ="Digite novamente sua senha", value="", type='password')

        col1, col2 = st.columns([8, 1])

        with col1:
            self.btt_confirmar_cadastro = st.button(label="Confirmar Cadastro",
                                                    on_click=self.autenticar_cadastro
                                                    )          
        with col2:
            self.btt_voltar_login = st.button(label='Voltar',
                                            on_click=Util.setar_ambiente_login
                                            )
        
        Util.escrever_mensagem_aviso()

    
    def autenticar_cadastro(self):
        st.session_state["Mensagem Aviso"] = "Preencher todos os campos!"
        if(Util.validar_string(self.nome_contato) and Util.validar_string(self.email_usuario) and Util.validar_string(self.telefone_contato) and Util.validar_string(self.senha_usuario) and Util.validar_string(self.senha_usuario_check)):
            st.session_state["Mensagem Aviso"] = "Senhas não conferem!"
            if(self.senha_usuario == self.senha_usuario_check):
                usuario_check = self.app_controller.usuario_controller.buscar_usuario_email(self.email_usuario)
                st.session_state["Mensagem Aviso"] = "Usuário já cadastrado!"
                if usuario_check == None:
                    novo_contato = Contato(nome=self.nome_contato, dt_nascimento=self.dt_nascimento_contato, sexo=self.genero_contato, telefone=self.telefone_contato)
                    novo_usuario = Usuario(email=self.email_usuario, senha=self.senha_usuario, contato=novo_contato)
                    self.app_controller.usuario_controller.adicionar_usuario(novo_usuario)
                    Util.setar_ambiente_login()






          
        

