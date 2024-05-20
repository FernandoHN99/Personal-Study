from jogoVelha3x3 import JogoVelha3x3
from jogoVelhaNxN import JogoVelhaNxN
from util import Util

def obter_opcao_usuario(prompt, opcoes_validas):
    while True:
        opcao = input(prompt).strip()
        if opcao in opcoes_validas:
            return opcao
        print(f"\nOpção inválida! Por favor, escolha uma das seguintes opções: {', '.join(opcoes_validas)}")

def main():
    Util.limpar_tela()
    dic_dificuldade = {
        '1': { '3x3': 0, 'NxN': 0},
        '2': { '3x3': 2, 'NxN': 1},
        '3': { '3x3': 5, 'NxN': 2}
    }
    print("\nBem-vindo ao Jogo da Velha!")
    
    tamanho = obter_opcao_usuario(f'\nEscolha o tamanho do tabuleiro 3 ou 5 ou 7: ', ['3', '5', '7'])
    dificuldade = obter_opcao_usuario("\nEscolha a dificuldade (1 para fácil, 2 para médio, 3 para difícil): ", ['1', '2', '3'])

    if tamanho == '3':
        jogo = JogoVelha3x3(dic_dificuldade[dificuldade]['3x3'])
    elif tamanho == '5':
        jogo = JogoVelhaNxN(5, dic_dificuldade[dificuldade]['NxN'])
    else:
        jogo = JogoVelhaNxN(7, dic_dificuldade[dificuldade]['NxN'])
    
    jogo.iniciar()

if __name__ == "__main__":
    main()
