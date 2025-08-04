from operator import itemgetter
inf = "Sarah Vaz\t8.5,4.5,7,6\nFulano de Tal\t4,5,6,7\nEma Thomaz\t6,8.5,7,7.5"
i = inf.count("\t")
cont = 0
inicial = 0
encontrar_t = 0
encontrar_n = -1
tabela = []
while cont < i:

    encontrar_t = inf.find("\t", encontrar_t + 1 ) 
    nome = inf[encontrar_n + 1  : encontrar_t ]  
    
    encontrar_n = inf.find("\n", encontrar_n + 1 )
    if cont == i - 1:
        nota = inf[encontrar_t + 1 :  ]
    else:
        nota = inf[encontrar_t + 1 : encontrar_n ]
    nota = nota.split(",")
    for elemento in range(len(nota)):
        nota[elemento] = float(nota[elemento])
    nota = [ sum(nota) / len(nota) ]
    nota.append(nome)
    nota.reverse()
    tabela.append(nota)
    cont = cont + 1
tabela.sort(key=itemgetter(1), reverse = True)


print()
print("%29s%15s " % ("Nome", "Média") )
print()
for linha in tabela:
    print(("%29s%15.1f"% tuple(linha)))
    
    