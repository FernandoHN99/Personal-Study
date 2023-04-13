import streamlit as st
from models.util import Util

class Home_View:
    def __init__(self, usuario_controller, produto_controller) -> None:

        self.carrinho_de_compras = (usuario_controller.buscar_usuario_email(st.session_state["Logado"])[0]).get_carrinho_de_compras()
        qtde_total_itens = self.carrinho_de_compras.qtde_total_itens()

        loja, carrinho, pagamento = st.tabs(["Loja", f'Carrinho ({qtde_total_itens}) 🛒' ,"Pagamento"])

        with loja:
            self.pagina_loja = Loja_View(usuario_controller, produto_controller)
        with carrinho:
            if (qtde_total_itens != 0):
                self.pagina_carrinho = Carrinho_View(usuario_controller, self.carrinho_de_compras)
            else:
                self.pagina_carrinho = None
                self.exibr_carrinho_vazio()

        st.sidebar.radio("Navegação",["Home", "Minha Conta", "About Us"])
        st.sidebar.button(label="Sair", on_click=Util.setar_ambiente_pagina_login)
    
    def exibr_carrinho_vazio(self):
            st.header("Putz! Parece que seu carrinho está vazio! 😢")

# -------------------------------- PAGINA LOJA PRODUTOS ----------------------------------------------

class Loja_View:
    def __init__(self, usuario_controller, produto_controller) -> None:
        self.usuario_controller = usuario_controller
        self.produto_controller = produto_controller

        st.title("A sua Loja favorita de Ga🎮es!")
        lista_nomes_produtos = self.produto_controller.gerar_lista_nomes_produtos()
        lista_nomes_produtos.insert(0, "Visualizar Todos")
        opcao_busca = st.selectbox(
                    label="Pesquise aqui seu jogo!", 
                    options=lista_nomes_produtos, 
                    index=(0)
                    )

        item_especifico = self.exibir_item_especifico(opcao_busca)
        if(item_especifico != None):
            self.exibir_produto_busca(item_especifico)
        else:
            self.exibir_produtos_3_colunas(self.produto_controller.get_lista_itens_cadastrados(), 200, 250)

    def exibir_item_especifico(self, caixa_seletora):
        if caixa_seletora != "Visualizar Todoss":
            try:
                item = self.produto_controller.get_item_pelo_nome(caixa_seletora)
                return item
            except:
                return None
        else:
            return None

    def exibir_produto_busca(self, item_especifico):
        col1, col2, col3 = st.columns(3)
        with col2:
            self.exibir_produto(item_especifico, 400, 500)

        
    def exibir_produtos_3_colunas(self, lista_itens, largura_imagem, altura_imagem):
        col1, col2, col3 = st.columns(3)
        list_coluna1=range(1,len(lista_itens)-1,3)
        list_coluna2=range(2,len(lista_itens),3)

        for i, item in enumerate(lista_itens):
            if(i in list_coluna1):
                with col1:
                    self.exibir_produto(item, largura_imagem, altura_imagem)
            elif(i in list_coluna2):
                with col2:
                    self.exibir_produto(item, largura_imagem, altura_imagem)
            else:
                with col3:
                    self.exibir_produto(item, largura_imagem, altura_imagem)
        
    def exibir_produto(self, produto, x, y):
        nome_item = st.subheader(produto.get_nome())
        st.image(Util.ajustar_imagem(produto.get_imagem(), x, y))
        st.info("R$ " + Util.converter_float_str_decimal_BR(produto.get_valor()),icon="💵")

        btt_add_car = st.button(
                label="Adicionar ao carrinho", 
                key=("btt"+str(nome_item)),
                on_click= self.usuario_controller.update_usuario_compra,
                kwargs={"produto": produto}
                )

        if(btt_add_car):
            st.balloons()
            st.caption("Adicionado com Sucesso!")

        # -------------------------------- PAGINA CARRINHO ----------------------------------------------

class Carrinho_View:
    def __init__(self, usuario_controller, carrinho_de_compras) -> None:
        self.usuario_controller = usuario_controller

        st.header("Confira tudo pra ver se não faltou nada! 😉")
        col1, col2, col3 = st.columns([1.8,1.5,0.8])
        with col1:
            st.header("Produto")
        with col2:
            st.header("Quantidade")
        with col3:
            st.header("Total")
        col1, col2, col3, col4, col5 = st.columns([1.75,0.05,0.8,0.4,0.8])

        for item in (carrinho_de_compras.get_itens()):
            with col1:
                st.subheader(item["Produto"].get_nome())
            with col3:
                st.write("")
                qtde_carrinho = carrinho_de_compras.retornar_qtd_item(item["Produto"])
                qtde_input = st.number_input(label="teste",
                                key=("btt"+str(item)),
                                min_value=0, 
                                value=qtde_carrinho,
                                label_visibility="collapsed"
                                )
            with col3:
                self.alterar_carrinho_input_number(qtde_input, qtde_carrinho, item["Produto"])

            with col5:
                valor_total_produto = Util.converter_float_str_decimal_BR((item["Produto"].get_valor())*item["Quantidade"])
                st.subheader("R$ " + valor_total_produto)

        col1, col2 = st.columns([1,0.4])
        with col2:
            st.write("")
            str_valor_total = Util.converter_float_str_decimal_BR(carrinho_de_compras.calcular_valor_total())
            st.header("Valor Total: R$ " + str_valor_total)
        # with col2:
        #     st.write("")
        #     st.header("R$ " + str_valor_total)


    def alterar_carrinho_input_number(self, qtde_desejada, qtd_carrinho, item, ):
        if(qtde_desejada > qtd_carrinho):
            Util.exibir_spinner(0.5,"Adicionando","")
            self.usuario_controller.update_usuario_compra(item)
            st.experimental_rerun() 

        elif(qtde_desejada < qtd_carrinho):
            Util.exibir_spinner(0.5,"Removendo","")
            self.usuario_controller.update_usuario_venda(item)
            st.experimental_rerun() 
                
