Frase = input("Escreve uma frase: ")     #entrada da frase


#função para inveter 
def Inverter (x):
    resp = ''
    for c in x:
        resp = c + resp
    return resp

Numero_De_Palavras = Frase.count(" ") + 1

Invertida = ""
p = ""
for c in Frase:   #separar em palavras para depois inveter
    if c != " ":
        p = p + c
    else:
        Invertida = Invertida + " " + (Inverter(p))
        p = ""

Invertida = Invertida + " " + (Inverter(p))   #ultima palavra

print(Invertida)