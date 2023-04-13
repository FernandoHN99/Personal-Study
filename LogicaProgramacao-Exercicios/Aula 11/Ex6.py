Frase = input("Escreve uma frase: ").lower().replace(" ", "")
 
def teste (x):
    resp = ''
    for c in Frase:
        resp = c + resp
    return resp

if Frase == teste(Frase):
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
    