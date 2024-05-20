import string
import os
import numpy as np
import math

''' Util '''
def limpar_tela():
   #  os.system('clear')
   pass

def criar_matriz_quadrada(n_linhas):
    return np.full((n_linhas, n_linhas), ' ')

def criar_dicionario_letra_numero(n_colunas):
    dicionario = {}
    lista_letras = [chr(i) for i in range(ord('A'), ord('A') + n_colunas)]
    for i, letra in enumerate(string.ascii_uppercase[:len(lista_letras)]):
        dicionario[letra] = i
    return dicionario

def contar_jogadas_restantes(mat):
    return sum(1 for linha in mat for elem in linha if elem == " ")

def validar_coluna(coluna, dic_colunas):
    return coluna in dic_colunas.keys()

def validar_linha(linha, mat):
    return 0 <= linha < len(mat)

def validar_jogada(linha, coluna, dic_colunas):
    return validar_coluna(coluna, dic_colunas) and validar_linha(linha, mat) and mat[linha][dic_colunas[coluna]] == " "

def marcar_jogada_humano(linha, coluna):
    mat[linha][coluna] = "X"

def marcar_jogada_computador(linha, coluna):
    mat[linha][coluna] = "O"

def imprimir_jogo(mat, dic_colunas):
    limpar_tela()
    print("O = Computador     X = Humano\n")
    for i in range(1, len(mat)+1):
        print(f"{i:2}", end=" ")
        for j in range(1, len(mat[0])+1):
            jogada = mat[i-1][j-1]
            if(j != len(mat[0])):
                print(f"  {jogada}  |", end="")
            else:
                print(f"  {jogada}  ", end="")
        print(f"\n   {(' - - -' * len(mat[0]))[:-1]}")
    print("     ", end="")
    for letra in dic_colunas.keys():
        print(f"{letra:4}  ", end="")
    print("\n")

def perguntar_jogada(mat, dic_colunas):
    eh_jogada_valida = False
    while not eh_jogada_valida:
        imprimir_jogo(mat, dic_colunas)
        try:
            coluna = input(f"Digite a coluna: ").upper()
            linha = int(input(f"Digite a linha: ")) - 1
            eh_jogada_valida = validar_jogada(linha, coluna, dic_colunas)
            if not eh_jogada_valida:
                input("Jogada inválida! Enter para continuar.")
        except ValueError:
            input("Jogada inválida! Enter para continuar.")
            continue
    return linha, dic_colunas[coluna]

def verificar_vitoria(placar):
    return abs(placar) == 1000

def funcao_avaliacao(mat, n_consecutivos=3):
    pontuacaoComput = max(
        avaliar_linhas(mat, 'O'),
        avaliar_colunas(mat, 'O'),
        avaliar_diagonais_principais(mat, n_consecutivos, 'O'),
        avaliar_diagonais_secundarias(mat, n_consecutivos, 'O'),
    )
    pontuacaoHumano = max(
        avaliar_linhas(mat, 'X'),
        avaliar_colunas(mat, 'X'),
        avaliar_diagonais_principais(mat, n_consecutivos, 'X'),
        avaliar_diagonais_secundarias(mat, n_consecutivos, 'X'),
    )
    if pontuacaoHumano == 3:
        retorno = -1000
    elif pontuacaoComput == 3:
        retorno = 1000
    elif pontuacaoHumano == 2:
        retorno = -500
    elif pontuacaoComput == 2:
        retorno = 500
    else:
        retorno = 0
    print(f'Pontuação Humano={pontuacaoHumano}, Pontuação Computador={pontuacaoComput}, Retorno={retorno}')
    return retorno

def avaliar_linhas(mat, jogador):
    mat_linhas_str = ""
    for l in range(len(mat)):
        mat_linhas_str += ''.join(mat[l]) + "\n"
    return pontuar(mat_linhas_str, jogador)

def avaliar_colunas(mat, jogador):
    mat_transposta = np.transpose(mat)
    return avaliar_linhas(mat_transposta, jogador)

def avaliar_diagonais_principais(mat, n_consecutivos, jogador):
    mat_diagonais_str = ''.join(mat.diagonal()) + "\n"

    for i in range(1, len(mat)):
        diagonal_acima = mat.diagonal(offset=i)
        diagonal_abaixo = mat.diagonal(offset=-i)
        
        if len(diagonal_acima) >= n_consecutivos:
            mat_diagonais_str += ''.join(diagonal_acima) + "\n" + ''.join(diagonal_abaixo) + "\n"
    
    return pontuar(mat_diagonais_str, jogador)

def avaliar_diagonais_secundarias(mat, n_consecutivos, jogador):
    mat_invertida = np.fliplr(mat)
    return avaliar_diagonais_principais(mat_invertida, n_consecutivos, jogador)


def pontuar(mat_str, jogador):
    if (jogador * 3) in mat_str:
        return 3
    elif " " + (jogador * 2) in mat_str or (jogador * 2) + " " in mat_str:
        return 2
    else:
        return 0

''' Função Minimax '''
def minimax(mat, profundidade, is_maximizing):
    placar = funcao_avaliacao(mat)
    if verificar_vitoria(placar) or profundidade == 0 or contar_jogadas_restantes(mat) == 0:
        return placar

    if is_maximizing:
        max_avaliacao = -math.inf
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == ' ':
                    mat[i][j] = 'O'
                    avaliacao = minimax(mat, profundidade - 1, False)
                    mat[i][j] = ' '
                    max_avaliacao = max(max_avaliacao, avaliacao)
        return max_avaliacao
    else:
        min_avaliacao = math.inf
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == ' ':
                    mat[i][j] = 'X'
                    avaliacao = minimax(mat, profundidade - 1, True)
                    mat[i][j] = ' '
                    min_avaliacao = min(min_avaliacao, avaliacao)
        return min_avaliacao

def melhor_movimento():
    melhor_avaliacao = -math.inf
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == ' ':
                mat[i][j] = 'O'
                avaliacao = minimax(mat, 1, False)
                mat[i][j] = ' '
                if avaliacao > melhor_avaliacao:
                    melhor_avaliacao = avaliacao
                    linha, coluna = i, j
    return linha, coluna

''' main '''
n_colunas = 5
mat = criar_matriz_quadrada(n_colunas)
dic_colunas = criar_dicionario_letra_numero(n_colunas)

def main():
    while True:
        linha, coluna = perguntar_jogada(mat, dic_colunas)
        marcar_jogada_humano(linha, coluna)
        placar = funcao_avaliacao(mat)
        imprimir_jogo(mat, dic_colunas)
        if verificar_vitoria(placar):
            print("Você venceu!")
            break
        elif contar_jogadas_restantes(mat) == 0:
            print("Empate!")
            break
        linha, coluna = melhor_movimento()
        marcar_jogada_computador(linha, coluna)
        placar = funcao_avaliacao(mat)
        imprimir_jogo(mat, dic_colunas)
        if verificar_vitoria(placar):
            print("Computador venceu!")
            break
        elif contar_jogadas_restantes(mat) == 0:
            print("Empate!")
            break

main()
