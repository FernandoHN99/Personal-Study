s = str(input("Escreva uma frase: "))


print("O número total de caracteres é: %s" % len(s))



x = 1
for c in s:
    if c == " ":
        x = x + 1

print("O número total de palavras é: %s" % x)
        
    