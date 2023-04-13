from random import choice
import os

def imprime(ponto, certas, erradas, palavra):
    os.system('clear')
    print("*************** Forca ***************")
    print("\n\nPalavra secreta: " + palavra + "\n\n")
    if(ponto == 0):
        print("=======[_] \n||      |  \n||         \n||         \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 1):
        print("=======[_] \n||      |  \n||      o  \n||         \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 2):
        print("=======[_] \n||      |  \n||      o  \n||      |  \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 3):
        print("=======[_] \n||      |  \n||      o  \n||     /|  \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 4):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 5):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||     /   \n||         \nHHHHHHHHHHHH")
    elif(ponto == 6):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||     / \ \n||         \nHHHHHHHHHHHH")

    print("\nLetras erradas:",erradas)
    print("Letras corretas:",certas)

def iniciaPalavra(tamanho):
    return '_'*tamanho

def sorteia():
    return choice(['cachorro', 'gato', 'galinha', 'cavalo', 'camelo', 'girafa', 'elefante', 'pirata', 'rato', 
        'arara', 'arame', 'familia', 'camisa', 'fazenda', 'cama', 'mesa', 'garfo', 'sapato', 'formiga', 'martelo',
         'lagarto', 'lanche', 'copo', 'corpo', 'humano', 'laranja', 'pera', 'melancia', 'manteiga', 'sofa'])

def atualizaPalavra(letra, palavra_sorteada, palavra):
    for i in range(len(palavra_sorteada)):
        if(palavra_sorteada[i] == letra):
            palavra = palavra[:i] + letra + palavra[i+1:]
    return palavra

if __name__ == '__main__':
    ponto=0
    certas = []
    erradas = []
    palavra_sorteada = sorteia()
    tamanho = len(palavra_sorteada)
    palavra = iniciaPalavra(tamanho)
    while(ponto < 7):
        imprime(ponto, certas, erradas, palavra)
        letra = input("Digite uma letra: ")
        if(letra in certas or letra in erradas):
            print("Letra já digitada!")
            input("Pressione enter para continuar...")
        else:
            if(letra in palavra_sorteada):
                certas.append(letra)
                palavra = atualizaPalavra(letra, palavra_sorteada, palavra)
                if(palavra == palavra_sorteada):
                    imprime(ponto, certas, erradas, palavra)
                    print("Você ganhou!")
                    break
            else:
                erradas.append(letra)
                ponto+=1
                if(ponto == 7):
                    print("Você perdeu!")