c = "s"
lista1 = []
i = 1
while c == "s":
    elemento = float(input("Digite o %sº valor da lista 1: "% i))
    lista1.append(elemento)
    c = input("Quer digitar outro valor? ").lower()
    i = i +1
    
c = "s"
lista2 = []
i = 1
while c == "s":
    elemento = float(input("Digite o %sº valor da lista 2: "% i))
    lista2.append(elemento)
    c = input("Quer digitar outro valor? ").lower()
    i = i + 1
 
Lista3 = lista1 + lista2

for elemento in Lista3:
    x = Lista3.count(elemento)
    if x > 1:
        Lista3.pop(Lista3.index(elemento))
    
Lista3.sort()
print(Lista3)
