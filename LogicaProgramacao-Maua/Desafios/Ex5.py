Frase = input("Digite uma frase: ").lower()


def CONTAR_VOGAIS(Frase):
    ra=0
    re=0
    ri=0
    ro=0
    ru =0
    for c in Frase:
    
        if c == "a":       
            ra = Frase.count("a")

            
        elif c == "e":
            re = Frase.count("e")

        elif c == "i":
            ri = Frase.count("i")

        elif c == "o":
            ro = Frase.count("o")

        elif c == "u":
            ru = Frase.count("u")
            
    o = ra + re + ri + ro + ru
    return o
    
print(CONTAR_VOGAIS(Frase))
