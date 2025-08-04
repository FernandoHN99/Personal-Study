import math
from util import Util


class Tela_Cientifica:
    def __init__(self):
        self.menu = {
            "1": "Adição",
            "2": "Subtração",
            "3": "Multiplicação",
            "4": "Divisão",
            "5": "Seno",
            "6": "Cosseno",
            "7": "Tangente",
            "8": "Potência"
        }
        self._resultado = 0

    def exibir(self):
        while True:
            Util.limpar_tela()
            self.exibir_menu()
            opcao = input("\nEscolha uma operação (S)air: ")

            if opcao in self.menu.keys():
                Util.limpar_tela()
                self.realizar_operacao(opcao)
                input("\nEnter para continuar")

            elif opcao.upper() == "S":
                Util.limpar_tela()
                break

    def exibir_menu(self):
        for opcao, descricao in self.menu.items():
            print(f"{opcao}. {descricao}")

    def get_value(self, msg):
        num = input(msg).upper()
        if num == 'R':
            return self._resultado

        try:
            return float(num)
            
        except ValueError:
            return None

    def realizar_operacao(self, operacao):
        try:
            match operacao:
                case "1":
                    num1 =  self.get_value("Digite o primeiro número: ")
                    num2 =  self.get_value("Digite o segundo número: ")
                    self._resultado = self.adicao(num1, num2)

                case "2":
                    num1 =  self.get_value("Digite o primeiro número: ")
                    num2 =  self.get_value("Digite o segundo número: ")
                    self._resultado = self.subtracao(num1, num2)

                case "3":
                    num1 =  self.get_value("Digite o primeiro número: ")
                    num2 =  self.get_value("Digite o segundo número: ")
                    self._resultado = self.multiplicacao(num1, num2)

                case "4":
                    num1 =  self.get_value("Digite o primeiro número: ")
                    num2 =  self.get_value("Digite o segundo número: ")
                    self._resultado = self.divisao(num1, num2)

                case "5":
                    num = math.radians( self.get_value("Digite o número em graus: "))
                    self._resultado = (self.seno(num))

                case "6":
                    num = math.radians( self.get_value("Digite o número em graus: "))
                    self._resultado = self.cosseno(num)

                case "7":
                    num = math.radians( self.get_value("Digite o número em graus: "))
                    self._resultado = self.tangente(num)

                case "8":
                    num1 =  self.get_value("Digite o número base: ")
                    num2 =  self.get_value("Digite o expoente: ")
                    self._resultado = self.potencia(num1, num2)

            if self._resultado != round(self._resultado):
                print(f"Resultado: {self._resultado:.6f}")
            else:
                print(f"Resultado: {self._resultado}")

        except ValueError:
            print("Entrada inválida. Certifique-se de digitar um número válido.")

    def adicao(self, num1, num2):
        return num1 + num2

    def subtracao(self, num1, num2):
        return num1 - num2

    def multiplicacao(self, num1, num2):
        return num1 * num2

    def divisao(self, num1, num2):
        return num1 / num2

    def seno(self, num):
        return math.sin(num)

    def cosseno(self, num):
        return math.cos(num)

    def tangente(self, num):
        return math.tan(num)

    def potencia(self, num1, num2):
        return math.pow(num1, num2)
