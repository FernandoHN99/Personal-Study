import streamlit as st
from models.contato.contato import Contato
from models.usuario.usuario import Usuario
from models.util import Util
import datetime as dt

class Cadastro_View:
    def __init__(self, controller) -> None:
        self.controller = controller

        data_min = dt.date(1900, 1, 1)
        data_max = dt.date.today() 
        
        st.title("Sua Jornada Começa Agora !🚀🔥")
        st.subheader("Meu Primeiro Acesso")

        col1, col2 = st.columns(2)
        with col1:
            self.nome_contato = st.text_input(label="Nome", placeholder ="Digite seu Nome Completo", value="")
            self.email_contato = st.text_input(label="E-mail", placeholder ="Digite seu endereço de E-mail", value="")
        with col2:
            self.telefone_contato = st.text_input(label="Telefone", placeholder ="Digite seu Telefone", value="")
            self.dt_nascimento_contato = st.date_input(label="Data de Nascimento", min_value=data_min, max_value=data_max)
        
        self.senha_usuario = st.text_input(label="Senha", placeholder ="Digite uma senha", value="",  type='password')
        self.senha_usuario_check = st.text_input(label="Confirmação de Senha", placeholder ="Digite novamente sua senha", value="", type='password')

        self.lista_campos_cadastro = [self.nome_contato, self.email_contato, self.telefone_contato, self.dt_nascimento_contato, self.senha_usuario,self.senha_usuario_check]

        col1, col2 = st.columns([8, 1])

        with col1:
            self.btt_confirmar_cadastro = st.button(
                label="Confirmar Cadastro", 
                    on_click=self.autenticar_cadastro
            )

            Util.escrever_mensagem_aviso()

        with col2:
            self.btt_voltar_login = st.button(
                    label='Voltar',
                    on_click=Util.setar_ambiente_pagina_login
                    )
    
    def autenticar_cadastro(self):
        if not self.checar_lista_cadastro():
                st.session_state["Caption"] = "Preencher todos os campos!"
        elif self.senha_usuario != self.senha_usuario_check:
                st.session_state["Caption"] = "As senhas não conferem!"
        elif len(self.controller.buscar_usuario_email(self.email_contato))!=0:
                st.session_state["Caption"] = "Usuário já Cadastrado!"
        else:
            contato_user = Contato(nome=self.nome_contato, email=self.email_contato, telefone=self.telefone_contato, data_nascimento=self.dt_nascimento_contato)
            usuario_novo = Usuario(contato_user, self.senha_usuario)
            self.controller.adicionar_usuario(usuario_novo)
            Util.setar_ambiente_pagina_login()

        
    def checar_lista_cadastro(self):
        for campo in self.lista_campos_cadastro:
            if not Util.validar_string(campo):
                return False
        return True
