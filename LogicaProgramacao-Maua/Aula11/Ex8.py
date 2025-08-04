Frase = input("Digite uma frase: ")

for c in Frase:
    if c == Frase[0]:
        Numero_maior_de_letras = Frase.count(c)
        c1 = c
    else:
        if Frase.count(c) > Numero_maior_de_letras:
            Numero_maior_de_letras = Frase.count(c)
            c1 = c
        
print("A letra que mais se repete é: %s" % c1)
if Numero_maior_de_letras == 1:
    print("Se repete %s vez" % Numero_maior_de_letras)
else:
    print("Se repete %s vezes" % Numero_maior_de_letras)


            
    