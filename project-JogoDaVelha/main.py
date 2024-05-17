def criar_matriz_quadrada(n_linhas):
	return [[' ' for _ in range(n_linhas)] for _ in range(n_linhas)]

def gerar_lista_letras(n):
    return [chr(i) for i in range(ord('A'), ord('A') + n)]

def imprimir_matriz(mat):
    print("😡 = Computador     😎 = Humano\n")
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
    lista_letras = gerar_lista_letras(len(mat[0]))
    for letra in lista_letras:
        print(f"{letra:4}  ", end="")
    print()


mat = criar_matriz_quadrada(7)
mat[0][0] = 'X'
mat[0][2] = 'X'
mat[1][1] = 'O'
mat[0][6] = 'X'
print(imprimir_matriz(mat))
