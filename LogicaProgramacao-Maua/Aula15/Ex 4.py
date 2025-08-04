comando = input("Deseja utilizar qual comando? (Soma, seno, trapezio)" ).lower().replace(" ", "" )

funcao = comando[0 : comando.find("(")]

parametros = comando[ comando.find( "(" ) + 1  : comando.find( ")" ) ]

sla = parametros.split( "," )

for c in range(len(sla)):
    sla[c] = float(sla[c])
    


if funcao == "soma":
    resp = sum(sla)
    
    print(resp)
#print(parametros)



#
#if op == "SOMA":
#    soma = input("Digite o comando soma: ").lower().replace(" ", "" )
#    
#    for c in soma: 
#        if c == ")":
#            posicao = soma.index(c)
#            
#    numeros = soma[5 : posicao] 
#    
#    soma = numeros.split(",")
#    
#    for c in range(len(soma)):
#        soma[c] = float(soma[c])
#        
#    soma = sum(soma)
#    print(soma)
#
#
#    