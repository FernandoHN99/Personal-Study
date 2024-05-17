import string 
import os

''' Util '''

def limpar_tela():
   os.system('clear')

def criar_matriz_quadrada(n_linhas):
	return [[' ' for _ in range(n_linhas)] for _ in range(n_linhas)]

def criar_dicionario_letra_numero(n_colunas):
    dicionario = {}
    lista_letras = [chr(i) for i in range(ord('A'), ord('A') + n_colunas)]
    for i, letra in enumerate(string.ascii_uppercase[:len(lista_letras)]):
        dicionario[letra] = i
    return dicionario

def contar_jogadas_restantes():
    return sum(1 for linha in mat for elem in linha if elem == " ")
   
def validar_coluna(coluna):
      return coluna in dic_colunas.keys()

def validar_linha(linha):
      return 0 <= linha < len(mat)

def validar_jogada(linha, coluna):
   return validar_coluna(coluna) and validar_linha(linha) and mat[linha][dic_colunas[coluna]] == " "
      

def imprimir_jogo():
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


def perguntar_jogada():
   eh_jogada_valida = False
   while not eh_jogada_valida:
      limpar_tela()
      imprimir_jogo()
      try:
         coluna = input(f"Digite a coluna: ").upper()
         linha = int(input(f"Digite a linha: ")) - 1 
         eh_jogada_valida = validar_jogada(linha, coluna)
         if not eh_jogada_valida:
            input("Jogada inválida! Enter para continuar.")
      except ValueError:
         input("Jogada inválida! Enter para continuar.")
         continue
   return linha, dic_colunas[coluna]
''' main '''
n_colunas = 5
mat = criar_matriz_quadrada(n_colunas)
dic_colunas = criar_dicionario_letra_numero(n_colunas)
def main():
   while True:
      linha, coluna = perguntar_jogada()
      mat[linha][coluna] = "X"
      limpar_tela()
      imprimir_jogo()
      break

main()