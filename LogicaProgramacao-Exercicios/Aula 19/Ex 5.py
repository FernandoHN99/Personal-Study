Lista = []
while True:
    Nome = input("Digite o nome de um vinho ('Enter' para sair): ").capitalize()
    if Nome == "":
        break
    Vinicola = input("Digite a vinícola: ").capitalize()
    Safra = input("Digite o ano da safra: ").capitalize()
    Pais = input("Digite o país: ").capitalize()
    Uva = input("Digite o tipo de uva: ").capitalize()
    Quant = int(input("Digite a quantidade: "))
    Lista.append(  {      "Nome": Nome , 
                         "Vinicola": Vinicola , 
                         "Safra": Safra , 
                         "Pais": Pais ,
                         "Uva": Uva ,
                         "Quant": Quant } )       


dic = {}
for vinho in Lista:
    if vinho["Quant"] > 0:
        
        if vinho["Uva"] not in dic:
            dic[vinho["Uva"] ] = 1
        else:
            dic[vinho["Uva"] ] = dic[ vinho["Uva"] ] + 1
            

Lista_Uvas = list(dic.keys() )         
Lista_Uvas.sort()
for uva in Lista_Uvas:
    print(uva + ":" , dic[uva])
    
            
            

            