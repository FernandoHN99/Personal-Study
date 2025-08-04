s = str(input("Escreva uma frase: "))


x = 0
y = 0


for c in s:
    print( s[x : ] + s[0 : y]) 
    y = y + 1
    x = x + 1

print(s)

