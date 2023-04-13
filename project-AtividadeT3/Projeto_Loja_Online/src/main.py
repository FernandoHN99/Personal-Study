# Fernando Henriques Neto
# RA:18.00931-0

import streamlit as st
from controllers.usuario_controller import Usuario_Controller
from controllers.produto_controller import Produto_Controller
from view.login_view import Login_View
from view.cadastro_view import Cadastro_View
from view.home_view import Home_View
from models.util import Util
from models.paginas import Paginas

# --------------------- COMEÇO ---------------------
if __name__ == "__main__":

# --------------------- SETANDO/COLETANDO INFORMAÇÕES ---------------------
    if not(Util.validar_dicionario(st.session_state)):
        usuario_controller = Usuario_Controller()
        produto_controller = Produto_Controller()
        Util.setar_ambiente_pagina_login()
    else:
        usuario_controller = st.session_state["Usuario_Controller"]
        produto_controller = st.session_state["Produto_Controller"]

# --------------------- LOGIN---------------------
    if st.session_state["Pagina"] == Paginas.LOGIN.name:
        pagina_atual = Login_View(usuario_controller)

# --------------------- CADASTRO---------------------
    elif st.session_state["Pagina"] == Paginas.CADASTRO.name:
        pagina_atual = Cadastro_View(usuario_controller)

# --------------------- HOME--------------------
    elif st.session_state["Pagina"] == Paginas.HOME.name:
        pagina_atual = Home_View(usuario_controller, produto_controller)
        
# --------------------- SALVAR CONTROLLER ---------------------
    st.session_state["Usuario_Controller"] = usuario_controller
    st.session_state["Produto_Controller"] = produto_controller

# --------------------- FIM ---------------------


