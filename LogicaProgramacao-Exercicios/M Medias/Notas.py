import numpy as np
Pesos_Semestre = [ 2,2,3,3]
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
            if Valor[-1] == "9" and Valor[-2] == "9":
                Valor = float(Valor)
                Valor = round(Valor, 2)
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
            Pesos_P = {"PesoSemestre1": 2, "PesoSemestre2": 3}
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
        
            Pesos_P = {"PesoSemestre1": 2, "PesoSemestre2": 3}
        
            Pesos_Totais = {"Prova" : 0.7 , "Trabalho": 0.3}

        if op == "QUIMICA" or op == "QUÍMICA":
            
            Tabela = {"Provas": {"P1": 9,   "P2": 9,
          
          "P3": 4.5,    "P4": -1}, 
          
          "Subs": {"Sub1": -1,  "Sub2": -1},
          
          "Trabalhos":{"T1": 8.5,     "T2": 9,
          
          "T3": 8,     "T4": -1}}
            
            Pesos_T = {"PT1": 1, "PT2": 1,
         "PT3": 1,  "PT4": 1}
        
            Pesos_P = {"PesoSemestre1": 2, "PesoSemestre2": 3}
        
            Pesos_Totais = {"Prova" : 2 , "Trabalho": 1}
            
        if op == "FÃÂSICA" or op == "FISICA":
            Tabela = {"Provas": {"P1": 9,   "P2": 7,
          
          "P3": 5.5 ,    "P4": -1}, 
          
          "Subs": {"Sub1": -1,  "Sub2": -1},
          
          "Trabalhos":{"T1": 9,     "T2": 8,
          
          "T3": 9.5,     "T4": -1}}
            
            Pesos_T = {"PT1": 1, "PT2": 1,
         "PT3": 1,  "PT4": 1}
        
            Pesos_P = {"PesoSemestre1": 2, "PesoSemestre2": 3}
        
            Pesos_Totais = {"Prova" : 2 , "Trabalho": 1}


        Media_P = "-"
        Media_T = "-"
        Media_FP = "-"
        Media_FT = "-"
        Media_Parcial_Final = "-"
        Media_Total_Final = "-"   
        Validacao = 0


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
                            try:
                                Valor = float(Valor)
                                if type(Valor) == float:
                                    if Valor >= 0 and Valor <= 10:
                                        Tabela["Provas"][Nota] = Valor    
                            except ValueError:
                                if type(Valor) == float:
                                    if Valor >= 0 and Valor <= 10:
                                        Tabela["Provas"][Nota] = Valor

            
                    elif (Nota in Tabela["Subs"]):
                        Valor = input("Digite o valor da nota %s: " % Nota ).upper() 
                        if Valor == "" or Valor == "-":
                            Tabela["Subs"][Nota] = -1
                        
                        elif Valor == "NF":
                            Tabela["Subs"][Nota] = 0
                        
                        else:
                            try:
                                Valor = float(Valor)
                                if type(Valor) == float:
                                    if Valor >= 0 and Valor <= 10:
                                        Tabela["Subs"][Nota] = Valor    
                            except ValueError:
                                    if type(Valor) == float:
                                        if Valor >= 0 and Valor <= 10:
                                            Tabela["Subs"][Nota] = Valor
               
                    elif  (Nota in Tabela["Trabalhos"]):
                        Valor = input("Digite o valor da nota %s: " % Nota ).upper() 
                        if Valor == "" or Valor == "-":
                            Tabela["Trabalhos"][Nota] = -1
                        elif Valor == "NF":
                            Tabela["Trabalhos"][Nota] = 0
                        else:
                            try:
                                Valor = float(Valor)
                                if type(Valor) == float:
                                    if Valor >= 0 and Valor <= 10:
                                        Tabela["Trabalhos"][Nota] = Valor                           
                            except ValueError:
                                if type(Valor) == float:
                                    if Valor >= 0 and Valor <= 10:
                                        Tabela["Trabalhos"][Nota] = Valor
            else:
                Nota = -1
                
         
#media de provas parcial
            C1 = 0  
            C2 = 0
            Soma_P = []
            Soma_V1 = 0
            Soma_V2 = 0

            for nota in Tabela["Provas"]:
                if Tabela["Provas"][nota] >= 0:
                    if nota == "P1" or nota == "P2":
                        C1 += 1
                    else:
                        C2 += 1
                    
                Soma_P.append(Tabela["Provas"][nota])
            
    #p1
            if Tabela["Subs"]["Sub1"] > Tabela["Provas"]["P1"] and Tabela["Provas"]["P1"] != -1:
                Soma_P[0] = Tabela["Subs"]["Sub1"]
#            elif Tabela["Subs"]["Sub1"] > Tabela["Provas"]["P1"] and Tabela["Provas"]["P1"] == -1:
#                Soma_P[0] = Tabela["Subs"]["Sub1"]
#                C1 += 1   # considerando -1 como prova feita (muda somente a parcial, deixando ela menor)
#    #p2
            if Tabela["Subs"]["Sub1"] > Tabela["Provas"]["P2"] and Tabela["Provas"]["P2"] != -1:
                Soma_P[1] = Tabela["Subs"]["Sub1"]
#            elif Tabela["Subs"]["Sub1"] > Tabela["Provas"]["P2"] and Tabela["Provas"]["P2"] == -1:
#                Soma_P[1] = Tabela["Subs"]["Sub1"]
#                C1 +=1

     #p3           
            if Tabela["Subs"]["Sub2"] > Tabela["Provas"]["P3"] and Tabela["Provas"]["P3"] != -1:
                Soma_P[2] = Tabela["Subs"]["Sub2"]
#            elif Tabela["Subs"]["Sub2"] > Tabela["Provas"]["P3"] and Tabela["Provas"]["P3"] == -1:
#                Soma_P[2] = Tabela["Subs"]["Sub2"]
#                C2 +=1
#    #p4
            if Tabela["Subs"]["Sub2"] > Tabela["Provas"]["P4"] and Tabela["Provas"]["P4"] != -1:
                Soma_P[3] = Tabela["Subs"]["Sub2"]
#            elif Tabela["Subs"]["Sub2"] > Tabela["Provas"]["P4"] and Tabela["Provas"]["P4"] == -1:
#                Soma_P[3] = Tabela["Subs"]["Sub2"]
#                C2 +=1
    #conta
            N = 4
            i = 0
            while i < N:
                if Soma_P[i] != -1 and (i == 0 or i==1):
                    Soma_V1 = Soma_V1 + Soma_P[i]

                elif Soma_P[i] != -1 and (i == 2 or i==3):
                    Soma_V2 = Soma_V2 + Soma_P[i]
                i +=1
                
                
            media1 = Soma_V1 * Pesos_P["PesoSemestre1"]
            media2 = Soma_V2 * Pesos_P["PesoSemestre2"]

            Numero_de_1 = Soma_P.count(-1)
            if Numero_de_1 != 4:
                Media_P = (media1 + media2)/(C1*Pesos_P["PesoSemestre1"]+C2*Pesos_P["PesoSemestre2"])
                x = Media_P
#            Media_P = round(Media_P,2)
#            Media_P = Arrumar_Valor(Media_P) #################################)
#            Media_P = round(Media_P,1)
                Media_P = Arrumar_Valor(Media_P)
             
             
            if Numero_de_1 == 4:
                Media_P = "-"
                Media_FP = "0.0"    
                
            else:
                Lista_FP = []
                for nota in Soma_P:
                    lugar = Soma_P.index(nota)
                    if nota == -1:
                        if lugar == 0 or lugar == 1:
                            if nota < Tabela["Subs"]["Sub1"]:
                                nota = Tabela["Subs"]["Sub1"]
                            else:
                                nota = 0
                        elif lugar == 2 or lugar == 3:
                            if nota < Tabela["Subs"]["Sub2"]:
                                nota = Tabela["Subs"]["Sub2"]
                            else:
                                nota = 0
                    Lista_FP.append(nota)
                        
                Media_FP = np.average( Lista_FP, weights = Pesos_Semestre ) 
                y = Media_FP
                Media_FP = Arrumar_Valor(Media_FP) ##########################

#            
#            
                      
#media de trbalhos 
            Soma_T = []
            C1 = 0  
            C2 = 0
            C3 = 0
            C4 = 0
            Soma_V1 = 0
            Soma_V2 = 0
            Soma_V3 = 0
            Soma_V4 = 0
        
            for nota in Tabela["Trabalhos"]:
                if Tabela["Trabalhos"][nota] >= 0:
                    if nota == "T1":
                        C1 += 1
                    if nota == "T2":
                        C2 += 1
                    if nota == "T3":
                        C3 += 1
                    if nota == "T4":
                        C4 +=1
                Soma_T.append(Tabela["Trabalhos"][nota])
        
            N = 4
            i = 0
            while i < N:
                if Soma_T[i] != -1 and i == 0:
                    Soma_V1 = Soma_T[i] * Pesos_T["PT1"]
                elif Soma_T[i] != -1 and (i == 1):
                    Soma_V2 = Soma_T[i] * Pesos_T["PT2"]
                elif Soma_T[i] != -1 and (i == 2):
                    Soma_V3 = Soma_T[i] * Pesos_T["PT3"]
                elif Soma_T[i] != -1 and (i == 3):
                    Soma_V4 = Soma_T[i] * Pesos_T["PT4"]
                i +=1
                                
            media1 = Soma_V1 + Soma_V2 + Soma_V3 +Soma_V4
        
            Numero_de_1 = Soma_T.count(-1)

            if Numero_de_1 != 4:
                Media_T = (media1)/(C1*Pesos_T["PT1"] +C2*Pesos_T["PT2"] + C3*Pesos_T["PT3"] + C4* Pesos_T["PT4"])
                z = Media_T
#            Media_T = round(Media_T,2)
#            Media_T = Arrumar_Valor(Media_T) ###############################
#            Media_T = round(Media_T,1)      
                Media_T = Arrumar_Valor(Media_T)
            
            if Numero_de_1 == 4:
                Media_T = "-"
                Media_FT = "0.0"     
            
            else:
                Media_FT = media1 / (Pesos_T["PT1"] + Pesos_T["PT2"] + Pesos_T["PT3"] + Pesos_T["PT4"])
                i = Media_FT
                Media_FT = Arrumar_Valor(Media_FT)


            
            
            
# media total
            if Media_FT != "0.0" and Media_FP != "0.0":  #trabalho sim/ prova sim
                Media_Parcial_Final = (Media_P * Pesos_Totais["Prova"] +  Media_T* Pesos_Totais["Trabalho"])/(Pesos_Totais["Prova"] + Pesos_Totais["Trabalho"])
                Media_Total_Final = (Media_FP * Pesos_Totais["Prova"] +  Media_FT* Pesos_Totais["Trabalho"])/(Pesos_Totais["Prova"] + Pesos_Totais["Trabalho"])
                j = Media_Parcial_Final
                k = Media_Total_Final
            
                Media_Parcial_Final = Arrumar_Valor(Media_Parcial_Final) #########################
                Media_Total_Final = Arrumar_Valor(Media_Total_Final)        ##########################
            

            elif Media_FT != "0.0"  and Media_FP == "0.0":                 #trab sim/ prova nao
                Media_Parcial_Final= Media_T 
                Media_Total_Final = Media_FT * Pesos_Totais["Trabalho"] / (Pesos_Totais["Prova"] + Pesos_Totais["Trabalho"])
                j = Media_Parcial_Final
                k = Media_Total_Final
                    
                Media_Total_Final = Arrumar_Valor(Media_Total_Final)
                Media_Parcial_Final = Arrumar_Valor(Media_Parcial_Final)

  
        

            elif Media_FT == "0.0"  and Media_FP != "0.0":     #trab nao/ prova sim
                Media_Parcial_Final= Media_P
                Media_Total_Final =  Media_FP * Pesos_Totais["Prova"]/ (Pesos_Totais["Prova"] + Pesos_Totais["Trabalho"])
                j = Media_Parcial_Final
                k = Media_Total_Final
                
                Media_Total_Final = Arrumar_Valor(Media_Total_Final)  ##########################
                Media_Parcial_Final = Arrumar_Valor(Media_Parcial_Final)


                        
            else:
                Media_Parcial_Final = "-"
                Media_Total_Final = "0.0"
            
                
                
                
                
                
                
            
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
                Qual = "oi"
                while type(Qual) != float:
                        Qual = input("Valor do esforço mínimo: ")
                        try:
                            Qual = float(Qual)
                        except:
                            print("Valor inválido!")
                                 
                
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
                
                for nota in Soma_P_ME:
                    lugar = Soma_P_ME.index(nota)
                    if lugar == 0 or lugar == 1:
                        if nota < Tabela["Subs"]["Sub1"]:
                            Soma_P_ME[lugar] = Tabela["Subs"]["Sub1"]
                    elif lugar == 2 or lugar == 3:
                        if nota < Tabela["Subs"]["Sub2"]:
                            Soma_P_ME[lugar] = Tabela["Subs"]["Sub2"]
                                
       
                            
                            
#                L_pos_P = []
#                for nota in Soma_P_ME:
#                    if nota == -1:
#                        L_pos_P.append(Soma_P_ME.index(nota))
#                        Soma_P_ME[Soma_P_ME.index(nota)] = 0
                        
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
                    if Contador >= 50 and Media_Total_Final_ME < Qual:
                        break
                    
                        
                    # para entrar sub1 e sub2
                if Contador >= 50 and Media_Total_Final_ME < Qual:
                    Media_Total_Final_ME = 0
                    Soma_T_ME =  Soma_T[:]
                    vezes = 0
                    L_pos_T = []
                    for nota in Soma_T_ME:
                        if nota == -1:
                            L_pos_T.append(Soma_T_ME.index(nota))
                            Soma_T_ME[Soma_T_ME.index(nota)] = 0
                            
                    if Tabela_ME["Subs"]["Sub1"] != -1 and Tabela_ME["Subs"]["Sub2"] != -1:   
                        Contador = 300
                        print("Não é possível atingir essa nota!")
                        print("O máximo é: %.1f" % Lista_Minimo[-1])
                        x = input()
#                        break
                        
                    elif Tabela_ME["Subs"]["Sub1"] == -1 and  Tabela_ME["Subs"]["Sub2"] == -1 and Contador != 1:
                        Soma_P_ME = [0,0,0,0]
                        while Media_Total_Final_ME < Qual:
                            if Soma_P_ME[0] + 0.5 <= 10:
                                Soma_P_ME[0] = Soma_P_ME[0] + 0.5
                            if Soma_P_ME[1] + 0.5 <= 10:
                                Soma_P_ME[1] = Soma_P_ME[1] + 0.5             
                                Lista_Minimo = list(Minimo_Esforco () )
                                Media_Total_Final_ME = Lista_Minimo[-1]
                                if Media_Total_Final_ME > Qual:
                                    break
                            
                            if Soma_P_ME[2] + 0.5 <= 10:
                                Soma_P_ME[2] = Soma_P_ME[2] + 0.5
                            if Soma_P_ME[3] + 0.5 <= 10:
                                Soma_P_ME[3] = Soma_P_ME[3] + 0.5
                                Lista_Minimo = list(Minimo_Esforco () )
                                Media_Total_Final_ME = Lista_Minimo[-1]
                                if Media_Total_Final_ME > Qual:
                                    break
                            while vezes < 2:
                                vezes += 1
                                for nota in L_pos_T:
                                    if Soma_T_ME[nota] + 0.5 <= 10:
                                        Soma_T_ME[nota] = Soma_T_ME[nota] + 0.5
                                        Lista_Minimo = list(Minimo_Esforco () )
                                        Media_Total_Final_ME = Lista_Minimo[-1]
                                        if Media_Total_Final_ME >= Qual:
                                            break
                                        
                        
                            vezes = 0
                            Contador += 1
                            if Contador >= 300:
                                print("Não é possível atingir essa nota!")
                                print("O máximo é: %.1f" % Lista_Minimo[-1])
                                x = input()
                                break
                            
                    elif Tabela_ME["Subs"]["Sub1"] == -1 and Contador != 300:
                        Soma_P_ME[0] = 0
                        Soma_P_ME[1] = 0 
                        while Media_Total_Final_ME < Qual and Contador != 300:
                            if Soma_P_ME[0] + 0.5 <= 10:
                                Soma_P_ME[0] = Soma_P_ME[0] + 0.5
                            if Soma_P_ME[1] + 0.5 <= 10:
                                Soma_P_ME[1] = Soma_P_ME[1] + 0.5             
                                Lista_Minimo = list(Minimo_Esforco () )
                                Media_Total_Final_ME = Lista_Minimo[-1]
                                if Media_Total_Final_ME > Qual:
                                    break
                                
                            while vezes < 2:
                                vezes += 1
                                for nota in L_pos_T:
                                    if Soma_T_ME[nota] + 0.5 <= 10:
                                        Soma_T_ME[nota] = Soma_T_ME[nota] + 0.5
                                        Lista_Minimo = list(Minimo_Esforco () )
                                        Media_Total_Final_ME = Lista_Minimo[-1]
                                        if Media_Total_Final_ME >= Qual:
                                            break
                                        
                        
                            vezes = 0
                            Contador += 1
                            if Contador >= 300:
                                print("Não é possível atingir essa nota!")
                                print("O máximo é: %.1f" % Lista_Minimo[-1])
                                x = input()
                                break
                            
                    elif Tabela_ME["Subs"]["Sub2"] == -1 and Contador != 300:
                        Soma_P_ME[2] = 0
                        Soma_P_ME[3] = 0 
                        while Media_Total_Final_ME < Qual:                            
                            if Soma_P_ME[2] + 0.5 <= 10:
                                Soma_P_ME[2] = Soma_P_ME[2] + 0.5
                            if Soma_P_ME[3] + 0.5 <= 10:
                                Soma_P_ME[3] = Soma_P_ME[3] + 0.5
                                Lista_Minimo = list(Minimo_Esforco () )
                                Media_Total_Final_ME = Lista_Minimo[-1]
                                if Media_Total_Final_ME > Qual:
                                    break
                            while vezes < 2:
                                vezes += 1
                                for nota in L_pos_T:
                                    if Soma_T_ME[nota] + 0.5 <= 10:
                                        Soma_T_ME[nota] = Soma_T_ME[nota] + 0.5
                                        Lista_Minimo = list(Minimo_Esforco () )
                                        Media_Total_Final_ME = Lista_Minimo[-1]
                                        if Media_Total_Final_ME >= Qual:
                                            break
                            
                            
                            vezes = 0
                            Contador += 1                        
                            if Contador >= 300:
                                print("Não é possível atingir essa nota!")
                                print("O máximo é: %.1f" % Lista_Minimo[-1])
                                x = input()
                                break
                    
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
                        
                        
                        
                if Contador < 50:
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
                    
                    Colocar_zeros = Tabela["Provas"]
                    Colocar_zeros = list( Colocar_zeros.values() )
                    Colocar_zeros.append(Tabela_ME["Subs"]["Sub1"])
                    Colocar_zeros.append(Tabela_ME["Subs"]["Sub2"])
                    
                    for nota in Colocar_zeros:
                        if nota == -1:
                            lugar = Colocar_zeros.index(nota)
                            if lugar != 4 and lugar != 5:
                                if lugar == 0 or lugar == 1:
                                    if nota != Soma_P_ME[lugar] and Soma_P_ME[lugar] != Tabela["Subs"]["Sub1"]:
                                        Colocar_zeros[lugar] = Soma_P_ME[lugar]
                                    else:
                                        Colocar_zeros[lugar] = 0 
                                if lugar == 2 or lugar == 3:
                                    if nota != Soma_P_ME[lugar] and Soma_P_ME[lugar] != Tabela["Subs"]["Sub2"]:
                                        Colocar_zeros[lugar] = Soma_P_ME[lugar]
                                    else:
                                        Colocar_zeros[lugar] = 0 
                            else:
                                Colocar_zeros[lugar] = 0

#                    
                                
                    Tabela_ME["Provas"]["P1"] = Colocar_zeros[0]
                    Tabela_ME["Provas"]["P2"] = Colocar_zeros[1]
                    Tabela_ME["Provas"]["P3"] = Colocar_zeros[2]
                    Tabela_ME["Provas"]["P4"] = Colocar_zeros[3]
                    Tabela_ME["Subs"]["Sub1"] = Colocar_zeros[4]
                    Tabela_ME["Subs"]["Sub2"] = Colocar_zeros[5]
                    
                    

                    
                    
                    
                    
                else:
                    if Tabela_ME["Subs"]["Sub1"] == -1 and Tabela_ME["Subs"]["Sub2"] == -1:
                        Tabela_ME["Subs"]["Sub1"] = Soma_P_ME[0]
                        Tabela_ME["Subs"]["Sub2"] = Soma_P_ME[2]
                        
                    elif Tabela_ME["Subs"]["Sub1"] == -1:
                        Tabela_ME["Subs"]["Sub1"] = Soma_P_ME[0]
                        
                    elif Tabela_ME["Subs"]["Sub2"] == -1:
                        Tabela_ME["Subs"]["Sub2"] = Soma_P_ME[2]
                    

                    Tabela_ME["Provas"] = Tabela["Provas"].copy()                   
                    Media_P_ME = Lista_Minimo[0]
                    Media_T_ME = Lista_Minimo[1]
                    Media_Parcial_Final_ME = Lista_Minimo[2]
                    Media_FP_ME = Lista_Minimo[3]
                    Media_FT_ME = Lista_Minimo[4]
                
                    Tabela_ME["Trabalhos"]["T1"] = Soma_T_ME[0]
                    Tabela_ME["Trabalhos"]["T2"] = Soma_T_ME[1]
                    Tabela_ME["Trabalhos"]["T3"] = Soma_T_ME[2]
                    Tabela_ME["Trabalhos"]["T4"] = Soma_T_ME[3]
                    
                    Colocar_zeros = Tabela["Provas"]
                    Colocar_zeros = list( Colocar_zeros.values() )
                    Colocar_zeros.append(Tabela_ME["Subs"]["Sub1"])
                    Colocar_zeros.append(Tabela_ME["Subs"]["Sub2"])
                    
                    for nota in Colocar_zeros:
                        if nota == -1:
                            lugar = Colocar_zeros.index(nota)
                            Colocar_zeros[lugar] = 0                           
                    Tabela_ME["Provas"]["P1"] = Colocar_zeros[0]
                    Tabela_ME["Provas"]["P2"] = Colocar_zeros[1]
                    Tabela_ME["Provas"]["P3"] = Colocar_zeros[2]
                    Tabela_ME["Provas"]["P4"] = Colocar_zeros[3]
                    Tabela_ME["Subs"]["Sub1"] = Colocar_zeros[4]
                    Tabela_ME["Subs"]["Sub2"] = Colocar_zeros[5]
                
                
                
                    
                if Contador < 300: 
                
                    print('\n' * 20)      
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
                
                    print("Aperte 'Enter' para voltar", end = "")
                    x = input()
                    
                            
                            

            Validacao = 2
            print('\n' * 40)  
            
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