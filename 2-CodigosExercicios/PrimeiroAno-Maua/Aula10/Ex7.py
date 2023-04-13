I = 1
S = 0
while 1/I > 0.0001:
    S = S + 1/(I+1)
    I = (I+1)
print(S+1)
