from util import Util
from jogoVelha3x3 import JogoVelha3x3
from jogoVelha5x5 import JogoVelha5x5
from jogoVelha7x7 import JogoVelha7x7
from jogoVelhaNxN import JogoVelhaNxN

class Sistema:
    def __init__(self):
        self.dic_dificuldade = {
            '1': { '3': 0, '5': 0, '7': 0},
            '2': { '3': 2, '5': 2, '7': 1},
            '3': { '3': 5, '5': 3, '7': 2}
        }

    def obter_opcao_usuario(self, entrada_usuario, opcoes_validas):
        while True:
            opcao = input(entrada_usuario).strip()
            if opcao in opcoes_validas:
                return opcao
            print(f"\nOpção inválida! Por favor, escolha uma das seguintes opções: {', '.join(opcoes_validas)}")

    def iniciar(self):
        Util.limpar_tela()
        print("Bem-vindo ao Jogo da Velha!")
        
        tamanho = self.obter_opcao_usuario(f'\nEscolha o tamanho do tabuleiro 3 ou 5 ou 7: ', ['3', '5', '7'])
        dificuldade = self.obter_opcao_usuario("\nEscolha a dificuldade (1 para fácil, 2 para médio, 3 para difícil): ", ['1', '2', '3'])

        if tamanho == '3':
            jogo = JogoVelha3x3(nivel_dificuldade=self.dic_dificuldade[dificuldade][tamanho])
        elif tamanho == '5':
            jogo = JogoVelha5x5(self.dic_dificuldade[dificuldade][tamanho])
        else:
            jogo = JogoVelha7x7(self.dic_dificuldade[dificuldade][tamanho])
        
        jogo.jogar()

if __name__ == "__main__":
    Sistema().iniciar()