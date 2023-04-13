Lista = []
print( "%40s" % "* * * MONTAGEM DE ESTOQUE * * *")
N = int(input("Deseja cadastrar quantos produtos no estoque? "))
I = 1
while I <= N:
    Nome = input("Nome do %s° produto: " % I).title()
    Origem = input("Origem %s° produto: " % I).title()
    Quant= int(input("Quantidade %s° produto: " % I))
    Preco = float(input("Preço %s° produto: " % I))
    Lista.append([ 
                  {"Nome": Nome} ,
                  {"Origem": Origem} ,
                  {"Quant": Quant},
                  {"Preço": Preco} 
                                      ] )
    I = I + 1
print('\n' * 10)


N = int(input("Deseja cadastrar quantos produtos no menu? "))
I = 1    
Produtos = []
while I <= N:
    Item = input("Digite o nome do produto: ").title()
    Produtos.append(Item)
    I = I + 1
    
def ValorEstoque (Produtos):
    Total = 0
    for Item in Produtos:
        for elemento in Lista:
            if Item == elemento[0]["Nome"]:
                Total = Total + ( 
                            (elemento[2]["Quant"]) * (elemento[3]["Preço"]) 
                                                                         )
    return Total

X = ValorEstoque(Produtos)
print("O valor total em estoque desses produtos é de: R$%.2f" % X)