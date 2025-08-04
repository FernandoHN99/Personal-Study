import math
from util import Util


class Tela_Normal:
    def __init__(self):
        self.menu = {
            "1": "Adição",
            "2": "Subtração",
            "3": "Multiplicação",
            "4": "Divisão",
            "5": "Porcentagem",
            "6": "Raiz Quadrada"
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
        print("Utilize 'R' para obter o resultado anterior")
        try:
            match operacao:
                case "1":
                    num1 = self.get_value("Digite o primeiro número: ")
                    num2 = self.get_value("Digite o segundo número: ")
                    self._resultado = self.adicao(num1, num2)

                case "2":
                    num1 = self.get_value("Digite o primeiro número: ")
                    num2 = self.get_value("Digite o segundo número: ")
                    self._resultado = self.subtracao(num1, num2)

                case "3":
                    num1 = self.get_value("Digite o primeiro número: ")
                    num2 = self.get_value("Digite o segundo número: ")
                    self._resultado = self.multiplicacao(num1, num2)

                case "4":
                    num1 = self.get_value("Digite o primeiro número: ")
                    num2 = self.get_value("Digite o segundo número: ")
                    self._resultado = self.divisao(num1, num2)

                case "5":
                    num = self.get_value("Digite o número: ")
                    self._resultado = self.porcentagem(num)

                case "6":
                    num = self.get_value("Digite o número: ")
                    self._resultado = self.raiz_quadrada(num)
            
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

    def porcentagem(self, num):
        return num / 100

    def raiz_quadrada(self, num):
        return math.sqrt(num)

