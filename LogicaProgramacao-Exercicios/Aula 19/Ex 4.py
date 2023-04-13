D = {}
while True:     
        
    Nome = input("Digite o nome do morador ('Enter' para sair): ").title()
    if Nome == "":
        break
    Tarefa = input("%s irá realizar qual tarefa? "% Nome).capitalize()
    Dia = input("%s irá trabalhar em qual dia da semana? "% Nome).title()

    while not( Dia == "Domingo" or Dia == "Segunda" or Dia == "Terça" or Dia == "Quarta" or Dia == "Quinta" or Dia == "Sexta" or Dia == "Sabado"):
        print('\n' * 3)
        print("Dia da semana invalido!" )
        Dia = input("%s irá trabalhar em qual dia da semana? "% Nome).title()
        
    if Nome not in D:
        D[Nome] = {"Tarefa": [Tarefa], "Dia": [Dia]}
        print('\n' * 3)
    else:
        for item in D[Nome]["Dia"]:
            if item == Dia:
                print('\n' * 5)
                print("O morador já está ocupado neste dia !")
                print("Refaça esse usuário!" )
                break
                    
            if item != Dia:
                D[Nome]["Tarefa"].append(Tarefa)
                D[Nome]["Dia"].append(Dia)
                print('\n' * 3)

L = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado"]
for dia in L:
    print()
    print(dia)
    for nome in D:
        I = -1
        for item in D[nome]["Dia"]:
            I = I + 1
            if item == dia:
                print("%s deve %s" % (nome, D[nome]["Tarefa"][I]))