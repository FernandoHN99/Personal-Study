

#Tabela = [ materia, pt1, pt2, pt3, pt4, peso de trab final, peso de prova final]
Tabela = [ ["GA", 0.2, 0.3, 0.3, 0.2, 0.3, 0.7], ["CALCULO", 2.5, 2.5, 2.5, 2.5, 0.3, 0.7], ["FISICA", 1, 1, 1, 1, 1, 2], ["QUIMICA", 1, 1, 1, 1, 1, 2] ]
Peso_p = [2,2,3,3]
Mat = input("Digite a matéria: ").upper()
N = int(input("Está cursando qual bimestre; 2, 3, 4 ou 5(concluiu ): "))

i = 1
Provas = []
Trabs = []


lista = []


for linha in Tabela:
    if Mat == linha[0]:
        while i <= N-1:
            Prova = float(input("Digite a nota da P%i: " % i ))
            while 0<= Prova <=10:
                Trab = float(input("Digite a nota do T%i: " % i ))
                while 0<= Trab <=10:
                    lista.append([Prova, Trab])
                    Prova = (Prova*Peso_p[i-1])  
                    Trab = (Trab * linha[i])              
                    Provas.append(Prova)
                    Trabs.append(Trab)
                    i = i + 1
                    Trab = -1
                    Prova = -1
    if i == N:
        break


print('\n' * 6)
Nota_p = round(sum(Provas)/sum(Peso_p[0:i-1]) , 1)#*linha[-1]
print("Média de prova: %.1f " % Nota_p)
Nota_t = round(sum(Trabs)/sum(linha[1:i]) , 1)#* linha[-2]
print("Média de trabalho: %.1f " % Nota_t)

Nota_pp = Nota_p*linha[-1]
Nota_tt = Nota_t*linha[-2]
Media = (Nota_pp + Nota_tt)/( linha[-1] + linha[-2] )
print("Média parcial: %.1f " % Media)

#lista.append([Nota_p])
#lista.append([Nota_t])
#while True: