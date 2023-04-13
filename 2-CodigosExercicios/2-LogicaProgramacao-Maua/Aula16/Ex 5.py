Sub = ["s2", "p6", "d10", "f14"]

Quant = ["1", "2", "3", "4", "5", "6", "7"]

for nivel in Quant:
    for subnivel in Sub:
        if nivel == "1":
            print(nivel + subnivel)
        break
            