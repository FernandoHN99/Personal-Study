                         #Função
def exibirTabela(Tabela):
    s = 0
    print('\n' * 40)
    print(" " * 35 + "* * * LISTA DE COMPRAS * * *")
    print()
    print("    Produto\t Quantidade\t   Preço")
    Tabela.sort()
    for linha in Tabela:
        print("%8s\t%6.1f\t%15.2f" % tuple(linha))
        s = s + linha[1]*linha[2]
    print()
    print("Total: $%.2f " % s)
    


                       #principal
print(" " * 25 + "* * * CADASTRO DE PRODUTOS * * *")
N = int(input("Digite a quantidade de itens: " ))
Tabela = []
for produtos in range(N):
    nome =  input("Digite o nome do produto: ").title()
    quant = float(input("Quantidade do produto: "))
    preco = 0
    lista = [nome, quant, preco]
    Tabela.append(lista)
   
exibirTabela(Tabela)

                            #alterar valores
for produtos in range(N):
    alterar =  input("Digite o nome do produto para alterar seu preço: ").title()
    preco = float(input("%s - Preço: "% alterar))
    for linha in Tabela:   
        if linha[0] == alterar:
            linha[2] = preco
            
    exibirTabela(Tabela)
        
        
    