X = int(input("Dê um valor para X: "))     #entrada de valores

#variaveis do resultado
Soma_do_resultado = 2 + 1 + X/(3*2)         #soma inicial do resultado
Expoente = 2                                #expoente para while do resultado      
Validacao_do_resultado = 1                   #condição para o resultado

#variaveis do fatorial
Expoente1 = Expoente                         #expoente para while do fatorial
Validacao_do_fatorial = 1                             #condição para o fatorial
Soma_do_fatorial = 1                         #Guardar os valores  do fatorial em cada repetição
Valor_Inicial_Expoente1 = Expoente1          #Guarda o valor inicial do expoente do fatorial

Resposta = "sim"


while Resposta == Resposta == "sim" or Resposta == "s" or Resposta == "S":
    Validacao_do_resultado = 1
    
#FATORIALLL (PRIMEIRO PASSO)
    while Validacao_do_fatorial < Expoente1:
        Soma_do_fatorial = Soma_do_fatorial * (Expoente1 - 1)         #fatorial
        Expoente1 = Expoente1 - 1
    Fatorial = Valor_Inicial_Expoente1 * Soma_do_fatorial
        
#RESULTADO FINAL (SEGUNDOO PASSO): PRECISO DO FATORIAL
    while X**Expoente/Fatorial > 10**-8 and Validacao_do_resultado == 1 :  # SÓ valores maiores que 10 elevado a -8
        Soma_do_resultado = Soma_do_resultado + (X**Expoente/Fatorial)   #expressão dada
        Expoente  = Expoente  + 2                                      #acréscimo de 2 no Y
        Expoente1 = Expoente
        Valor_Inicial_Expoente1 = Expoente1
        Validacao_do_resultado = 2
        Validacao_da_Validacao = 2
        
        
    while not ((X**Expoente/Fatorial > 10**-8 or Validacao_da_Validacao == 1)):
        Resposta = "Não"
        Validacao_da_Validacao  = 1
        print("O resultado é: %.18f" % Soma_do_resultado)
        Resposta = str(input("Deseja digitar um outro valor: "))
        if Resposta == "sim" or Resposta == "s" or Resposta == "S":
            X = int(input("Dê um valor para X: "))    
            Soma_do_resultado = 2 + 1 + X/(3*2)         
            Expoente = 2                                 
            Validacao_do_resultado = 1                  
            Expoente1 = Expoente                         
            Validacao_do_fatorial = 1                          
            Soma_do_fatorial = 1                         
            Valor_Inicial_Expoente1 = Expoente1
        else:
            print("OK, até a próxima!!")