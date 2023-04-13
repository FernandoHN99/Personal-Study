import numpy as np
def Minimo_Esforco ():
    C1 = 2
    C2 = 2

    
    N = 4
    i = 0
    Soma_V1 = 0
    Soma_V2 = 0
    while i < N:
        if Soma_P_ME[i] != -1 and (i == 0 or i==1):
            Soma_V1 = Soma_V1 + Soma_P_ME[i]

        elif Soma_P_ME[i] != -1 and (i == 2 or i==3):
            Soma_V2 = Soma_V2 + Soma_P_ME[i]
            
        i +=1
                
                
    media1 = Soma_V1 * Pesos_P["PesoSemestre1"]
    media2 = Soma_V2 * Pesos_P["PesoSemestre2"]

    Numero_de_1 = Soma_P_ME.count(-1)
    if Numero_de_1 != 4:
        Media_P_ME = (media1 + media2)/(C1*Pesos_P["PesoSemestre1"]+C2*Pesos_P["PesoSemestre2"])
#            Media_P = round(Media_P,2)
#            Media_P = Arrumar_Valor(Media_P) #################################)
#            Media_P = round(Media_P,1)
    Media_P_ME = Arrumar_Valor(Media_P_ME)
             
             
#    if Numero_de_1 == 4:
#        Media_P = "-"
#        Media_FP = "-"    
#                
#    else:
    Media_FP_ME = (media1 + media2) / ((Pesos_P["PesoSemestre1"]   + Pesos_P["PesoSemestre2"]) *2)
    Media_FP_ME = Arrumar_Valor(Media_FP_ME) ##########################

       
                      
                
                
                
                
                
                
##media de trbalhos 
    C1 = 1
    C2 = 1
    C3 = 1
    C4 = 1
    N = 4
    i = 0
    while i < N:
        if Soma_T_ME[i] != -1 and i == 0:
            Soma_V1 = Soma_T_ME[i] * Pesos_T["PT1"]
        elif Soma_T_ME[i] != -1 and (i == 1):
            Soma_V2 = Soma_T_ME[i] * Pesos_T["PT2"]
        elif Soma_T_ME[i] != -1 and (i == 2):
            Soma_V3 = Soma_T_ME[i] * Pesos_T["PT3"]
        elif Soma_T_ME[i] != -1 and (i == 3):
            Soma_V4 = Soma_T_ME[i] * Pesos_T["PT4"]
        i +=1
                                
    media1 = Soma_V1 + Soma_V2 + Soma_V3 +Soma_V4
        
    Numero_de_1 = Soma_T_ME.count(-1)

    if Numero_de_1 != 4:
        Media_T_ME = (media1)/(C1*Pesos_T["PT1"] +C2*Pesos_T["PT2"] + C3*Pesos_T["PT3"] + C4* Pesos_T["PT4"])
#            Media_T = round(Media_T,2)
#            Media_T = Arrumar_Valor(Media_T) ###############################
#            Media_T = round(Media_T,1)      
        Media_T_ME = Arrumar_Valor(Media_T_ME)
            
    if Numero_de_1 == 4:
        Media_T_ME = "-"
        Media_FT_ME = "-"     
            
    else:
        Media_FT_ME = media1 / (Pesos_T["PT1"] + Pesos_T["PT2"] + Pesos_T["PT3"] + Pesos_T["PT4"])
        i = Media_FT_ME
        Media_FT_ME = Arrumar_Valor(Media_FT_ME)


            
            
            
# media total
    if Media_FT_ME != "-" and Media_FP_ME != "-":  #trabalho sim/ prova sim
        Media_Parcial_Final_ME = (Media_P_ME * Pesos_Totais["Prova"] +  Media_T_ME* Pesos_Totais["Trabalho"])/(Pesos_Totais["Prova"] + Pesos_Totais["Trabalho"])
        Media_Total_Final_ME = (Media_FP_ME * Pesos_Totais["Prova"] +  Media_FT_ME* Pesos_Totais["Trabalho"])/(Pesos_Totais["Prova"] + Pesos_Totais["Trabalho"])
        
        Media_Parcial_Final_ME = Arrumar_Valor(Media_Parcial_Final_ME) #########################
        Media_Total_Final_ME = Arrumar_Valor(Media_Total_Final_ME)        ##########################
            

    
    elif Media_FT_ME != "-"  and Media_FP_ME == "-":                 #trab sim/ prova nao
        Media_Parcial_Final_ME= Media_T_ME 
        Media_Total_Final_ME = Media_FT_ME * Pesos_Totais["Trabalho"] / (Pesos_Totais["Prova"] + Pesos_Totais["Trabalho"])

        Media_Total_Final_ME = Arrumar_Valor(Media_Total_Final_ME)
        Media_Parcial_Final_ME = Arrumar_Valor(Media_Parcial_Final_ME)

  
        
    elif Media_FT_ME == "-"  and Media_FP_ME != "-":     #trab nao/ prova sim
        Media_Parcial_Final_ME= Media_P_ME
        Media_Total_Final_ME =  Media_FP_ME * Pesos_Totais["Prova"]/ (Pesos_Totais["Prova"] + Pesos_Totais["Trabalho"])
                
        Media_Total_Final_ME = Arrumar_Valor(Media_Total_Final_ME)  ##########################
        Media_Parcial_Final_ME = Arrumar_Valor(Media_Parcial_Final_ME)

                        
    else:
        Media_Parcial_Final_ME = "-"
        Media_Total_Final_ME = "-"
            
    return  Media_P_ME, Media_T_ME, Media_Parcial_Final_ME, Media_FP_ME, Media_FT_ME, Media_Total_Final_ME


        
        
        
def Arrumar_Valor(Valor):
    if Valor != "-":
        Valor = str(Valor)
        tamanho = len(Valor)
        if tamanho == 4:
            if Valor[3] == "5":
                Valor = float(Valor)
                Valor = Valor + 0.05
                Valor = round(Valor, 1)
            else:
                Valor = float(Valor)
                Valor = round(Valor, 1)
        else:
            if Valor[-2] == "9" and Valor[-3] == "9" and Valor[-4] == "9":
                Valor = float(Valor)
                Valor = round(Valor, 2)
                Valor = Valor + 0.01
                Valor = round(Valor, 1) 
            else:
                Valor = float(Valor)
                Valor = round(Valor, 1)  
            

    return Valor


while True:
    op = input("Digite a matéria ('Enter' para sair): " ).upper()
    while not (op == "" or op=="GA" or op=="CALCULO" or op =="CÁlCULO" or op=="FÍSICA" or op =="FISICA" or op == "QUIMICA" or op =="QUÍMICA" or op =="COMP" or op =="COMPUTAÇÃO" or op == "DESENHO" ):
        op = input("Digite a matéria: " ).upper()
    if op =="":
        break

    elif op=="GA" or op=="CALCULO" or op =="CÁlCULO" or op=="FÍSICA" or op =="FISICA" or op =="QUÍMICA" or op=="QUIMICA":
        print('\n' * 15)
        if op == "CÃÂLCULO" or op == "CALCULO":
            Tabela = {"Provas": {"P1": 6.5,   "P2": 6,
          
          "P3": 6 ,    "P4": -1}, 
          
          "Subs": {"Sub1": -1,  "Sub2": -1},
          
          "Trabalhos":{"T1": 8.5,     "T2": 8.5,
          
          "T3": 7.5,     "T4": -1}}
            Pesos_T = {"PT1": 2.5, "PT2": 2.5,
            "PT3": 2.5,  "PT4": 2.5}
            
            Pesos_P = {"P1": 2,"P2": 2,"P3": 3,"P4": 3 }
            Pesos_Totais = {"Prova" : 0.7 , "Trabalho": 0.3}

        if op == "GA":
            Tabela = {"Provas": {"P1": 8.5,   "P2": 5,
          
          "P3": 6.5 ,    "P4": -1}, 
          
          "Subs": {"Sub1": -1,  "Sub2": -1},
          
          "Trabalhos":{"T1": 7.5,     "T2": 5,
          
          "T3": 7,     "T4": -1}}
            
            Tabela_ME = {"Provas": {"P1": 8.5,   "P2": 5,
          
          "P3": 6.5 ,    "P4": -1}, 
          
          "Subs": {"Sub1": -1,  "Sub2": -1},
          
          "Trabalhos":{"T1": 7.5,     "T2": 5,
          
          "T3": 7,     "T4": -1}}
        
            Pesos_T = {"PT1": 0.2 , "PT2": 0.3,
         "PT3": 0.3 ,  "PT4": 0.2 }
        
            Pesos_P = {"P1": 2,"P2": 2,"P3": 3,"P4": 3 }
        
            Pesos_Totais = {"Prova" : 0.7 , "Trabalho": 0.3}

        if op == "QUIMICA" or op == "QUÍMICA":
            
            Tabela = {"Provas": {"P1": 9,   "P2": 9,
          
          "P3": 4.5,    "P4": -1}, 
          
          "Subs": {"Sub1": -1,  "Sub2": -1},
          
          "Trabalhos":{"T1": 8.5,     "T2": 9,
          
          "T3": 8,     "T4": -1}}
            
            Pesos_T = {"PT1": 1, "PT2": 1,
         "PT3": 1,  "PT4": 1}
        
            Pesos_P = {"P1": 2,"P2": 2,"P3": 3,"P4": 3 }
        
            Pesos_Totais = {"Prova" : 2 , "Trabalho": 1}
            
        if op == "FÃÂSICA" or op == "FISICA":
            Tabela = {"Provas": {"P1": 9,   "P2": 7,
          
          "P3": 5.5 ,    "P4": -1}, 
          
          "Subs": {"Sub1": -1,  "Sub2": -1},
          
          "Trabalhos":{"T1": 9,     "T2": 8,
          
          "T3": 9.5,     "T4": -1}}
            
            Pesos_T = {"PT1": 1, "PT2": 1,
         "PT3": 1,  "PT4": 1}
        
            Pesos_P = {"P1": 2,"P2": 2,"P3": 3,"P4": 3 }
        
            Pesos_Totais = {"Prova" : 2 , "Trabalho": 1}


        Media_P = "-"
        Media_T = "-"
        Media_FP = "-"
        Media_FT = "-"
        Media_Parcial_Final = "-"
        Media_Total_Final = "-"   
        Validacao = 0
#        media_arit = "-"
#        media_arit_final = "-"


        #                         #EXIBIÃÃO
        while True:  
    
            print("%35s - %s" % ( "* * * BOLETIM * * *", op) )
            print("---------------------------------------------------------------")
            for elemento in Tabela:
                for nota in Tabela[elemento]:
                    if nota == "Sub1" and Tabela[elemento][nota] == -1:
                        print("%s: " % nota, "      ", end = "    ")
                    elif nota == "Sub1":
                        print("%s: %.1f" % (nota, Tabela[elemento][nota]), "        ", end = "")
                    elif nota != "Sub1"and Tabela[elemento][nota] == -1:
                        print("%s: " % nota, "        ", end = "    ")
                    else:
                        print("%s: %.1f" % (nota, Tabela[elemento][nota]), "        ", end = "")
                print()
                print("---------------------------------------------------------------")
            print("MÉDIAS PARCIAIS"+"                 " + "MÉDIAS TOTAIS")
            if Media_P == "-":
                print("Média de Prova: %s              Média de prova: %s"  % (Media_P,Media_FP)) 
            else:
                print("Média de Prova: %.1f            Média de prova: %.1f " % (Media_P,Media_FP)) 
            if Media_T == "-":
                print("Média de Trabalho: %s            Média de Trabalho: %s " % (Media_T,Media_FT))
                print("_________________________________________________________________ ")
                print("Média Parcial: %s                Média Final: %s " % (Media_Parcial_Final, Media_Total_Final))
            else:
                print("Média de Trabalho: %.1f         Média de Trabalho: %.1f " % (Media_T,Media_FT))
                print("___________________________________________________________________")
                print("Média Parcial: %.1f             Média Final: %.1f " % (Media_Parcial_Final, Media_Total_Final))
         
            print('\n' * 1)
#            print(media_arit)
#            print(media_arit_final)
            if Validacao != 0:
                Nota = input("Digite a nota que vc quer alterar ('Enter' para trocar de matéria): ").title()
                if Nota =="":
                    break
                else:
                    if (Nota in Tabela["Provas"]):
                        Valor = input("Digite o valor da nota %s: " % Nota ).upper() 
                        if Valor == "" or Valor == "-":
                            Tabela["Provas"][Nota] = -1
             
                        elif Valor == "NF":
                            Tabela["Provas"][Nota] = 0
                        
                        else:
                            Valor = float(Valor)
                            if Valor >= 0 and Valor <= 10:
                                Tabela["Provas"][Nota] = Valor

            
                    elif (Nota in Tabela["Subs"]):
                        Valor = input("Digite o valor da nota %s: " % Nota ).upper() 
                        if Valor == "" or Valor == "-":
                            Tabela["Subs"][Nota] = -1
                        
                        elif Valor == "NF":
                            Tabela["Subs"][Nota] = 0
                        
                        else:
                            Valor = float(Valor)
                            if Valor >= 0 and Valor <= 10:
                                Tabela["Subs"][Nota] = Valor
               
                    elif  (Nota in Tabela["Trabalhos"]):
                        Valor = input("Digite o valor da nota %s: " % Nota ).upper() 
                        if Valor == "" or Valor == "-":
                            Tabela["Trabalhos"][Nota] = -1
                        elif Valor == "NF":
                            Tabela["Trabalhos"][Nota] = 0
                        else:
                            Valor = float(Valor)
                            if Valor >= 0 and Valor <= 10:
                                Tabela["Trabalhos"][Nota] = Valor
            else:
                Nota = -1
                
         
            Lista_De_Provas_Inicial = list(Tabela["Provas"].values() )
            Lista_De_Provas_Inicial.append(Tabela["Subs"]["Sub1"])
            Lista_De_Provas_Inicial.append(Tabela["Subs"]["Sub2"])
            Lista_Calculo_Media_Prova_Parcial = []
            Lista_Calculo_Media_Prova_Parcial_Final = []
            i = 0
            
            Lista_De_Valores_Inicial_Prova = list(Pesos_P.values() )
            Lista_De_Valores_Final_Prova = [ ]

#media de provas parcial   
            
            while i < 4:
                if Lista_De_Provas_Inicial[i] != -1:
                    if i == 0:
                        if Lista_De_Provas_Inicial[4]>Lista_De_Provas_Inicial[0]:
                            Lista_Calculo_Media_Prova_Parcial.append(Lista_De_Provas_Inicial[4])
                        else:
                            Lista_Calculo_Media_Prova_Parcial.append(Lista_De_Provas_Inicial[0])
################################################################################################ 
                    if i == 1:
                        if Lista_De_Provas_Inicial[4]>Lista_De_Provas_Inicial[1]:
                            Lista_Calculo_Media_Prova_Parcial.append(Lista_De_Provas_Inicial[4])
                        else:
                            Lista_Calculo_Media_Prova_Parcial.append(Lista_De_Provas_Inicial[1])
################################################################################################      
                    if i == 2:
                        if Lista_De_Provas_Inicial[5]>Lista_De_Provas_Inicial[2]:
                            Lista_Calculo_Media_Prova_Parcial.append(Lista_De_Provas_Inicial[5])
                        else:
                            Lista_Calculo_Media_Prova_Parcial.append(Lista_De_Provas_Inicial[2])
################################################################################################ 
                    if i == 3:
                        if Lista_De_Provas_Inicial[5]>Lista_De_Provas_Inicial[3]:
                            Lista_Calculo_Media_Prova_Parcial.append(Lista_De_Provas_Inicial[5])
                        else:
                            Lista_Calculo_Media_Prova_Parcial.append(Lista_De_Provas_Inicial[3])
                            
                    Lista_De_Valores_Final_Prova.append(Lista_De_Valores_Inicial_Prova[i])
                            
#media final so de provas                       
                if i == 0:
                    if Lista_De_Provas_Inicial[4]>Lista_De_Provas_Inicial[0]:
                        Lista_Calculo_Media_Prova_Parcial_Final.append(Lista_De_Provas_Inicial[4])
                    else:
                        Lista_Calculo_Media_Prova_Parcial_Final.append(Lista_De_Provas_Inicial[0])
################################################################################################ 
                if i == 1:
                    if Lista_De_Provas_Inicial[4]>Lista_De_Provas_Inicial[1]:
                        Lista_Calculo_Media_Prova_Parcial_Final.append(Lista_De_Provas_Inicial[4])
                    else:
                        Lista_Calculo_Media_Prova_Parcial_Final.append(Lista_De_Provas_Inicial[1])
################################################################################################      
                if i == 2:
                    if Lista_De_Provas_Inicial[5]>Lista_De_Provas_Inicial[2]:
                        Lista_Calculo_Media_Prova_Parcial_Final.append(Lista_De_Provas_Inicial[5])
                    else:
                        Lista_Calculo_Media_Prova_Parcial_Final.append(Lista_De_Provas_Inicial[2])
################################################################################################ 
                if i == 3:
                    if Lista_De_Provas_Inicial[5]>Lista_De_Provas_Inicial[3]:
                        Lista_Calculo_Media_Prova_Parcial_Final.append(Lista_De_Provas_Inicial[5])
                    else:
                        Lista_Calculo_Media_Prova_Parcial_Final.append(Lista_De_Provas_Inicial[3])
                    
                i = i + 1

                
            if len(Lista_Calculo_Media_Prova_Parcial) != 0:
                Media_P = np.average( Lista_Calculo_Media_Prova_Parcial, weights = Lista_De_Valores_Final_Prova)
                Media_P = Arrumar_Valor(Media_P)
                
            else:
                Media_P= "-"
                
#media de prova final 
            for nota in Lista_Calculo_Media_Prova_Parcial_Final:
                if nota == -1:
                    lugar = Lista_Calculo_Media_Prova_Parcial_Final.index(nota)
                    Lista_Calculo_Media_Prova_Parcial_Final[lugar] = 0
                    
            Media_FP = np.average( Lista_Calculo_Media_Prova_Parcial_Final, weights = Lista_De_Valores_Inicial_Prova)
            Media_FP = Arrumar_Valor(Media_FP)
                

                      
#media de trbalhos parcial
             
            ListaDeTrabalho_inicial = list(Tabela["Trabalhos"].values() )
            listaDevalores_inicial = list(Pesos_T.values() )
            ListaDeTrabalho = []
            listaDevalores = []
            
            if Tabela["Trabalhos"]["T1"] != -1:
                ListaDeTrabalho.append(Tabela["Trabalhos"]["T1"])
                listaDevalores.append(listaDevalores_inicial[0])
            if Tabela["Trabalhos"]["T2"] != -1:
                ListaDeTrabalho.append(Tabela["Trabalhos"]["T2"])
                listaDevalores.append(listaDevalores_inicial[1])
            if Tabela["Trabalhos"]["T3"] != -1:
                ListaDeTrabalho.append(Tabela["Trabalhos"]["T3"])
                listaDevalores.append(listaDevalores_inicial[2])
            if Tabela["Trabalhos"]["T4"] != -1:
                ListaDeTrabalho.append(Tabela["Trabalhos"]["T4"])
                listaDevalores.append(listaDevalores_inicial[3])
                
                
            if len(ListaDeTrabalho) != 0:
                Media_T = np.average(ListaDeTrabalho, weights = listaDevalores)
                Media_T = Arrumar_Valor(Media_T)
                
            else:
                Media_T= "-"
                
#media final de trbalhos 
            for nota in ListaDeTrabalho_inicial:
                if nota == -1:
                    lugar = ListaDeTrabalho_inicial.index(nota)
                    ListaDeTrabalho_inicial[lugar] = 0
                
            
                Media_FT = np.average(ListaDeTrabalho_inicial, weights = listaDevalores_inicial)
                Media_FT = Arrumar_Valor(Media_FT)
                
                     
                
                
                
# medias totais
            ListaDePesos = list(Pesos_Totais.values() )           
            
            if Media_T != "-" and Media_P != "-":                 #trabalho sim/ prova sim
                Media_Parcial_Final = Arrumar_Valor(np.average([Media_P,Media_T], weights = ListaDePesos  )    )
                Media_Total_Final =  Arrumar_Valor(np.average([Media_FP,Media_FT], weights = ListaDePesos       ) )

            elif Media_T != "-"  and Media_P == "-":              #trab sim/ prova nao
                 Media_Parcial_Final = Arrumar_Valor(np.average([0,Media_T], weights = [0, ListaDePesos[1] ]    ) )
                 Media_Total_Final =  Arrumar_Valor(np.average([0,Media_FT], weights = ListaDePesos             ) )

            elif Media_T == "-"  and Media_P != "-":     #trab nao/ prova sim
                Media_Parcial_Final = Arrumar_Valor(np.average([Media_P,0], weights = [ListaDePesos[0],0   ]    ) )
                Media_Total_Final =  Arrumar_Valor(np.average([Media_FP,0], weights = ListaDePesos              ) )
                        
            else:
                Media_Parcial_Final = "-"
                Media_Total_Final = "-"
            
                
                
                
                
                
                
            
            if Nota == "Me":
                Media_Total_Final_ME = Media_Total_Final
                Tabela_ME = Tabela.copy()
                Tabela_ME["Provas"] = Tabela["Provas"].copy()
                Tabela_ME["Subs"] = Tabela["Subs"].copy()
                Tabela_ME["Trabalhos"] = Tabela["Trabalhos"].copy()
                Contador = 0
                
                
                vezes = 0
                Soma_T_ME =  Soma_T[:]
                Soma_P_ME = Soma_P[:]
                Qual = float(input("Valor do esforço mínimo: "))
                
                
                L_pos_T = []
                for nota in Soma_T_ME:
                    if nota == -1:
                        L_pos_T.append(Soma_T_ME.index(nota))
                        Soma_T_ME[Soma_T_ME.index(nota)] = 0
                        
                L_pos_P = []
                for nota in Soma_P_ME:
                    if nota == -1:
                        L_pos_P.append(Soma_P_ME.index(nota))
                        Soma_P_ME[Soma_P_ME.index(nota)] = 0
                        
                if Media_Total_Final_ME == "-":
                    Media_Total_Final_ME = 0
                    
                while Media_Total_Final_ME < Qual:
                    
                    for nota in L_pos_P:
                        if Soma_P_ME[nota] + 0.5 <= 10:
                            Soma_P_ME[nota] = Soma_P_ME[nota] + 0.5
                            Lista_Minimo = list(Minimo_Esforco () )
                            Media_Total_Final_ME = Lista_Minimo[-1]
                            if Media_Total_Final_ME > Qual:
                                break
                            
                    if Media_Total_Final_ME >= Qual:
                        break

                    
                    while vezes < 2:
                        for nota in L_pos_T:
                            if Soma_T_ME[nota] + 0.5 <= 10:
                                Soma_T_ME[nota] = Soma_T_ME[nota] + 0.5
                                Lista_Minimo = list(Minimo_Esforco () )
                                Media_Total_Final_ME = Lista_Minimo[-1]
                            if Media_Total_Final_ME >= Qual:
                                break
                        vezes += 1
                        
                    vezes = 0
                    Contador += 1
                    

                    if Contador >= 300:
                        print("Não é possível atingir essa nota!")
                        x = input()
                        break
#                    else:
#                        
                if Media_Total_Final_ME >= Qual:
                    for nota in L_pos_T:
                        Soma_T_ME[nota] = 0
                        Lista_Minimo = list(Minimo_Esforco () )
                        Media_Total_Final_ME = Lista_Minimo[-1]
                    
                while Media_Total_Final_ME < Qual and Contador != 300:
                    for nota in L_pos_T:
                        Soma_T_ME[nota] = Soma_T_ME[nota] + 0.5
                        Lista_Minimo = list(Minimo_Esforco () )
                        Media_Total_Final_ME = Lista_Minimo[-1]
                        if Media_Total_Final_ME == Qual:
                            break
                    
                if Contador < 300:
                    Media_P_ME = Lista_Minimo[0]
                    Media_T_ME = Lista_Minimo[1]
                    Media_Parcial_Final_ME = Lista_Minimo[2]
                    Media_FP_ME = Lista_Minimo[3]
                    Media_FT_ME = Lista_Minimo[4]
                
                    Tabela_ME["Provas"]["P1"] = Soma_P_ME[0]
                    Tabela_ME["Provas"]["P2"] = Soma_P_ME[1]
                    Tabela_ME["Provas"]["P3"] = Soma_P_ME[2]
                    Tabela_ME["Provas"]["P4"] = Soma_P_ME[3]
                
                    Tabela_ME["Trabalhos"]["T1"] = Soma_T_ME[0]
                    Tabela_ME["Trabalhos"]["T2"] = Soma_T_ME[1]
                    Tabela_ME["Trabalhos"]["T3"] = Soma_T_ME[2]
                    Tabela_ME["Trabalhos"]["T4"] = Soma_T_ME[3]
                
                    print('\n' * 12)      
                    print("%50s - %s" % ( "* * * BOLETIM - MÍNIMO ESFORÇO * * *", op) )
                    print("---------------------------------------------------------------")
                    for elemento in Tabela_ME:
                        for nota in Tabela_ME[elemento]:
                            if nota == "Sub1" and Tabela_ME[elemento][nota] == -1:
                                print("%s: " % nota, "      ", end = "    ")
                            elif nota == "Sub1":
                                print("%s: %.1f" % (nota, Tabela_ME[elemento][nota]), "        ", end = "")
                            elif nota != "Sub1"and Tabela_ME[elemento][nota] == -1:
                                print("%s: " % nota, "        ", end = "    ")
                            else:
                                    print("%s: %.1f" % (nota, Tabela_ME[elemento][nota]), "        ", end = "")
                        print()
                        print("---------------------------------------------------------------")
                    print("MÉDIAS PARCIAIS"+"                 " + "MÉDIAS TOTAIS")
                    if Media_P_ME == "-":
                        print("Média de Prova: %s              Média de prova: %s"  % (Media_P_ME,Media_FP_ME)) 
                    else:
                        print("Médiade Prova: %.1f            Média de prova: %.1f " % (Media_P_ME,Media_FP_ME))                     
                    if Media_T_ME == "-":
                        print("Média de Trabalho: %s            Média de Trabalho: %s " % (Media_T_ME,Media_FT_ME))
                        print("_________________________________________________________________ ")
                        print("Média Parcial: %s                Média Final: %s " % (Media_Parcial_Final_ME, Media_Total_Final_ME))
                    else:
                        print("Média de Trabalho: %.1f         Média de Trabalho: %.1f " % (Media_T_ME,Media_FT_ME))
                        print("___________________________________________________________________")
                        print("Média Parcial: %.1f             Média Final: %.1f " % (Media_Parcial_Final_ME, Media_Total_Final_ME))
         
                    print('\n' * 1)
                
                    print("Aperte 'Enter' para voltar")
                    x = input()
                    
                            
                            

            Validacao = 2
            print('\n' * 12)  
            
    elif op == "COMP" or op == "COMPUTAÇÃO" or op == "DESENHO":
        print('\n' * 15)
        Tabela = {
         "T1": 8,     "T2": 7,
                
          "T3": 7.5, 
          
          "Sub1": -1,  "Sub2": -1,
          
            "T4": 10, "T5": -1 , "T6" : -1 ,  "T7": 9.5 }
        
        Pesos_T = {"PT": 1.5, "PT7": 1}
    
        Media_P = -1
        Media_F = -1
        
        while True:
            if op == "COMP" or op== "COMPUTAÇÃO" or op == "DESENHO":
                print("%35s -%s" % ("* * * BOLETIM * * *" , op ) )
                print("---------------------------------------------------------------")
                for chave in Tabela:
                    if chave == "Sub1" and Tabela[chave] == -1:
                        print()
                        print("---------------------------------------------------------------")
                        print("%s:            " % (chave) , end = "")
                    elif chave == "Sub1":
                        print()
                        print("---------------------------------------------------------------")
                        print("%s: %.1f        " % (chave,Tabela[chave] ) , end = "" )
                    elif chave == "T4" and Tabela[chave] == -1:
                        print()
                        print("---------------------------------------------------------------")
                        print(chave + ":" , "             ", end = "")
                    elif chave == "T4":
                        print()
                        print("---------------------------------------------------------------")
                        print("%s: %.1f          " % (chave,Tabela[chave] ), end = "" )
                    elif  chave != "Sub1" and chave != "T4" and Tabela[chave] == -1 :
                            print(chave + ":" ,"             ", end = "")
                    else:
                        print("%s: %.1f        " % (chave,Tabela[chave] ), end = "" )
                print()
                print("---------------------------------------------------------------")

                print("MÉDIA PARCIAL:"+"                 " + "MÉDIA FINAL:")
                if Media_P == -1:
                    print("     ---                           ---   ")
                else:           
                    print("%8.1f                          %.1f" %(Media_P, Media_F))
                print("___________________________________________________________________")
        
                Nota = input("Digite a nota que vc quer alterar ('Enter' para trocar de matéria): ").title()
                if Nota =="":
                    break
                else:
                    if Nota in Tabela:
                        Valor = input("Digite o valor da nota %s: " % Nota).upper()
                        if Valor == "" or Valor == "-":
                            Valor = -1
                            Tabela[Nota] = Valor
                        elif Valor == "NF":
                            Tabela[Nota] = 0
                        else:
                            Valor = float(Valor)
                            if Valor >=0 and Valor <= 10:
                                Tabela[Nota] = Valor

                    
    #media de trabalhos parcial
                Media_P = -1
                L1 = []
                L2 = []
    
    #sub1##################################################
                L = [Tabela["T1"], Tabela["T2"], Tabela["T3"]]
                menor1 = min(L)
                onde1 = L.index(menor1)   
                if Tabela["Sub1"] > menor1:
                    L.insert(onde1, Tabela["Sub1"])
                for nota in L:
                    if nota != -1:
                        L1.append(nota)
          
    #sub2#######################################
                L = [Tabela["T4"], Tabela["T5"], Tabela["T6"]]
                menor2 = min(L)
                onde2 = L.index(menor2)
                if Tabela["Sub2"] > menor2:
                    L.insert( onde2, Tabela["Sub2"])           
                for nota in L:
                    if nota != -1:
                        L2.append(nota)
    
    
    #contas final
                soma1 = sum(L1)
                N1 = len(L1)
                soma2 = sum(L2)  
                N2 = len(L2)
        
  
                if  (N1 + N2 != 0) and Tabela["T7"] == -1:
                    Media_P = ((soma1 + soma2) * Pesos_T["PT"] ) / ( (N1+N2) * Pesos_T["PT"] )
                elif  (N1 + N2 != 0) and Tabela["T7"] != -1:
                    Media_P = ((soma1 + soma2) * Pesos_T["PT"] +Tabela["T7"]) / (( (N1+N2) * Pesos_T["PT"] ) +  Pesos_T["PT7"])
                elif  N1 + N2 == 0 and Tabela["T7"] != -1:
                    Media_P = ( Tabela["T7"] /  Pesos_T["PT7"] )  
        
#        if Tabela["T7"] != -1:
#            soma3 = Tabela["T7"]/ Pesos_T["PT7"]
#            if soma != -1 :
#                Media_P = soma + soma3
#            else:
#                Media_P = soma3
#        else:          
                Media_P = Arrumar_Valor(Media_P)
        
                                                                #media final
                if Media_P != -1:
                    if Tabela["T7"] != -1:
                        Media_F = ( (sum(L1) + sum(L2))*Pesos_T["PT"] + Tabela["T7"]*Pesos_T["PT7"] ) / (6*Pesos_T["PT"] + Pesos_T["PT7"])
                    elif Tabela["T7"] == -1:
                        Media_F= ( (sum(L1) + sum(L2))*Pesos_T["PT"] )/ (6*Pesos_T["PT"] + Pesos_T["PT7"])  
                
                Media_F = Arrumar_Valor(Media_F)
            
                print('\n' * 12)

            Validacao = 1