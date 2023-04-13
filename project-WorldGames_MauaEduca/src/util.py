import streamlit as st
from PIL import Image as img
from src.controllers.app_controller import App_Controller

class Util:

    @staticmethod
    def validar_dicionario(dicionario):
        return len(dicionario.keys()) != 0
    
    @staticmethod
    def validar_string(var_string):
        return var_string != None and var_string != ""
    
    @staticmethod
    def escrever_mensagem_aviso():
        if Util.validar_string(st.session_state["Mensagem Aviso"]):
            st.error(st.session_state["Mensagem Aviso"], icon="⚠️")

    @staticmethod
    def setar_ambiente_login():
        st.session_state["Email Logado"]   = None
        st.session_state["Mensagem Aviso"] = None
        st.session_state["Pagina"]         = "Pagina Login"


    @staticmethod
    def setar_ambiente_cadastro():
        st.session_state["Email Logado"]   = None
        st.session_state["Mensagem Aviso"] = None
        st.session_state["Pagina"]         = "Pagina Cadastro"
    
    @staticmethod
    def ajustar_imagem(caminho_img, x, y):
        imagem = img.open(caminho_img)
        return imagem.resize((x, y))
    
    @staticmethod
    def converter_float_str(valor):
        result = str("{:.2f}".format(valor))
        return result.replace(".",",")



