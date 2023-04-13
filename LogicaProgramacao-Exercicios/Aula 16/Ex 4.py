Tabela = []
Cat = ""

while Cat != "Fim" :
    Cat = input("Digite a categoria (Fim para sair): ").title()
    if Cat == "Fim":
        Tabela.sort()
        print('\n' * 40)
        print(" " * 30 + "***LISTA DE COMPRAS***")
        print()
        for c in Tabela:
            print(c)
            print()

        
    else:
        produto = ""
        Lista_Prod = []
        while produto != "Fim":
            produto = input("Digite o produto (Fim para sair): ").title()
            if produto == "Fim":
                Lista_Prod.sort()
                Lista_Prod = ', '.join(Lista_Prod)
                Nova_Tabela = [Cat, Lista_Prod]
                Nova_Tabela = ': '.join(Nova_Tabela)
                Tabela.append(Nova_Tabela)
                print('\n' * 10)
            else:
                Lista_Prod.append(produto)