from math import sqrt
N = int(input("Quantidade de disparos: " ))
i = 1
D = {}
Melhor = 0
while i <= N:
    X = float(input("Coordenada x do %i° disparo: " % i ))
    Y = float(input("Coordenada y do %i° disparo: " % i ))
    Distancia = sqrt(X**2 + Y**2)
    if Distancia >= 10 :
        Pontos = 10 - Distancia // 10 
    else:
        Pontos = 10 - Distancia // 10 
    
    if Pontos >= Melhor:
        Melhor = Pontos
        
    D[i] = {(X,Y): Pontos}
    i = i + 1
    
print()
print( "%40s" % "*** MELHORES DISPAROS ***")
print()
print(" %10s %18s %15s" % ("Disparo", "Coordenadas", "Pontos") )

for disparo in D:
    for chave in D[disparo]:
        if D[disparo][chave] >= Melhor:
            print("%7i°" % disparo, end = "")
            print( " "*10 , chave, end = "")
            print("%16.2f" % D[disparo][chave])
