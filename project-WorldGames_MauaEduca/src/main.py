import streamlit as st
from src.util import Util
from src.controllers.app_controller import App_Controller
from src.view.login_view import Login_View
from src.view.cadastro_view import Cadastro_View
from src.view.home_view import Home_View

if __name__ == "__main__":

    if (not Util.validar_dicionario(st.session_state)):
        st.session_state["App Controller"] = None
        Util.setar_ambiente_login()
    
    app_controller = App_Controller()
    
    if st.session_state["Pagina"] == "Pagina Login":
        pagina_atual = Login_View(app_controller)

    elif st.session_state["Pagina"] == "Pagina Cadastro":
        pagina_atual = Cadastro_View(app_controller)

    elif st.session_state["Pagina"] == "Pagina Loja":
        pagina_atual = Home_View(app_controller)

    st.session_state["App Controller"] = app_controller