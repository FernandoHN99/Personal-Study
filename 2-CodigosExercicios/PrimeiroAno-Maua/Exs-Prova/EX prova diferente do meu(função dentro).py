#função
def dentro(x, y, f):
    fig_1 = x**2 + y**2 
    fig_2 = (x + 1)*(x - 1) 
    fig_3 = x**2 - y**2 
    
    if f == 1:
       if fig_1 <= 1:
           Resposta = "Pertence"
       else:
           Resposta = "Não pertence"
           
    if f == 2:
       if fig_2 <= Y**2:
           Resposta = "Pertence"
       else:
           Resposta = "Não pertence"
           
    if f == 3:
       if fig_3 >= 1:
           Resposta = "Pertence"
       else:
           Resposta = "Não pertence" 
     
    return Resposta


#principal
X = float(input("De um valor para X: "))
Y = float(input("De um valor para Y: "))
F = int(input("De um valor para f: "))

if F == 1 or F == 2 or F == 3:
    dentro(X,Y,F)
    print(dentro(X,Y,F))
    
else:
    print("Valor Inválido")