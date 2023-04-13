D = {}
while True:
    Nome = input("Digite o nome do filme: ").upper()
    print()
    print("Comédia")
    print()
    print("Drama")
    print()
    print("Suspense")
    print()
    print("Terror")
    print()
    print("Documentário")
    print()
    Cat = input("Digite a categoria: ").title()
    if Cat == "Comédia"or Cat =="Drama" or Cat == "Suspense" or Cat == "Terror" or Cat == "Documentário":
        D[Nome] = Cat
        print()
    op = input("Deseja digitar outro filme: ").upper()
    if op == "N":
        break

D2 = {}
for filme in D:
    if D[filme] not in D2:
        D2[D[filme]] = 1
    else:
        D2[D[filme]] = D2[D[filme]] + 1

print("%12s %30s" % ("Categoria", "Quantidade de filmes")        )
print()
for cat in D2:
    print("%12s %20i" % (cat, D2[cat] ) )
    
print()
print()
print()
print()
print()

print("%12s %30s" % ("Categoria", "Quantidade de filmes")        )
print()
D3 = {}
L = ["Comédia", "Terror", "Suspense", "Documentário", "Drama"]
for cat in L:
    for filme in D:
        if D[filme] == cat and D[filme] not in D3:
            D3[cat] = 1
        elif (filme == cat) and (filme in D3):
            D3[cat] += 1
            
    if cat in D3:
        print("%12s %20i" % (cat, D3[cat]))
            
    
    
        
    
    
    
    
    
    
    
    
    