I = 1
x = 1
s = 0

while abs( ((1/(x+2)) - (1/x)) ) >= 0.0000000000000000000005:
    if I % 2 != 0:
        s = s + (1/(x))
        x = x + 2
        I = I + 1
    elif I % 2 == 0:
        s = s - (1/(x))
        x = x + 2
        I = I + 1
        
print("O valor de pi é: %.18f" % (s*4))

