D1 = {}
D2 = {}
op = "C"

while op == "C":
    op = input("(C)adastrar ou (S)air: ").upper()
    if op == "C":
        Placa = input("Digite a placa: ").upper()
        Vaga = input("Digite a vaga: ")
        
        if Placa in D1 or Vaga in D2:
            print("O veículo ou a vaga já estão ocupados!!!")
            op = "C"
            
        else:
            D1[Placa] = Vaga
            D2[Vaga] = Placa

Lista = list(D2.keys())
Lista.sort()
            
print("VAGA       PLACA")
for item in Lista:
    print("%2s %14s" % (item, D2[item]) )    