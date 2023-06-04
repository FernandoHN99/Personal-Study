from tela_menu import Tela_Menu
from tela_normal import Tela_Normal
from tela_cientifica import Tela_Cientifica
from util import Util


class Sistema:
    def __init__(self):
        self._menu = Tela_Menu()
        self._tela_normal = Tela_Normal()
        self._tela_cientifica = Tela_Cientifica()

    def executar(self):
        Util.limpar_tela()
        while True:
            Util.limpar_tela()
            self._menu.exibir()
            opcao = input("\nDigite a opção desejada (S)air: ")

            if opcao == "1":
                self._tela_normal.exibir()

            elif opcao == "2":
                self._tela_cientifica.exibir()
            
            elif opcao.upper() == "S":
                break

            else:
                print("Opção inválida. Tente novamente.")



sistema = Sistema()
sistema.executar()