#função
def dentro(x, y, f):
    fig_1 = x**2 + y**2 
    fig_2 = (x + 1)*(x - 1) 
    fig_3 = x**2 - y**2 
    
    if f == 1:
       f = fig_1
       if f <= 1:
           Resposta = print("Pertence")
       else:
           Resposta = print("Não pertence")
           
    elif f == 2:
       f = fig_2
       if f <= Y**2:
           Resposta = print("Pertence")
       else:
           Resposta = print("Não pertence")
           
    elif f == 3:
       f = fig_3
       if f >= 1:
           Resposta = print("Pertence")
       else:
           Resposta = print("Não pertence") 
     
    return Resposta


#principal
X = float(input("De um valor para X: "))
Y = float(input("De um valor para Y: "))
F = int(input("De um valor para f: "))

dentro(X,Y,F)

