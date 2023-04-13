#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int gFree, gHead, vetSize;

void showAllLists(int vetPrev[], int vetKey[], int vetNext []){
    printf("Next -->  ");
    showList(vetNext);
    printf("\n\nKey -->   ");
    showList(vetKey);
    printf("\n\nPrev -->  ");
    showList(vetPrev);
}
void flowAddElement(int vetPrev[], int vetKey[], int vetNext[]){
    int value;
    printf("\n\nValor a ser adicionado na Posicao %i: ", gFree);
    scanf("%i", &value);
    addElement(vetPrev, vetKey, vetNext, value);
}

int vetContains(int vetNext[], int value){
    int i;
    for(i=0; i<vetSize; i++){
        if(vetNext[i] == value){
            return 1;
            break;
        }
     }
     return 0;
}

void fillList(int vetKey[],int vetPrev[]){
    int i;
     for(i=0; i<vetSize; i++){
         vetKey[i] =-1;
         vetPrev[i] =-1;
     }
}

void readString(char s[]){
    setbuf(stdin,0);
    fgets(s,10,stdin);
    if(s[strlen(s)-1]=='\n'){
        s[strlen(s)-1] = '\0';
    }

}

void clrscr(){
    system("@cls||clear");
}

void inputUser(int vetNext[]){
    int i=1, valuePast, aux=-1;
    while((aux<=0 || aux>vetSize) && vetSize>0){
        printf("Posicao do %i Elemento a ser inserido na Lista: ", i);
        scanf("%i", &aux);
    }
    gFree = aux;
    valuePast = aux;
    for(i=1; i<vetSize; i++){
        clrscr();
        aux = -1;
        while(aux<=0 || aux>vetSize || gFree == aux || vetContains(vetNext, aux)){
            printf("Posicao do %i Elemento a ser inserido na Lista: ", (i+1));
            scanf("%i", &aux);
        }
        vetNext[valuePast-1] = aux;
        valuePast = aux;
    }
    vetNext[valuePast-1] = -1;
}

void callOptions(int option, int vetPrev[], int vetKey[], int vetNext[]){
    
    char aux[10];
    switch (option){
        case 1:
            clrscr();
            showAllLists(vetPrev, vetKey, vetNext);
            if(gFree != -1){
                flowAddElement(vetPrev, vetKey, vetNext);
                // printf("\n");
                // showList(vetNext);
                showAllLists(vetPrev, vetKey, vetNext);
            }else{
                printf("\n\nNao eh possivel adicionar elementos!");
            }
            printf("\n\nDigite 'Enter' para voltar ao menu ");
            readString(aux);
            break;
        case 2:
            clrscr();
            showAllLists(vetPrev, vetKey, vetNext);
            int result = flowRemoveElement(vetPrev, vetKey, vetNext);
            if(result){
                // printf("\n");
                // showAllLists(vetPrev, vetKey, vetNext);
            }else{
                printf("\nNao eh possivel remover o Elemento!");
            }
            printf("\n\nDigite 'Enter' para voltar ao menu ");
            readString(aux);
            break;
        case 3:
            clrscr();
            showAllLists(vetPrev, vetKey, vetNext);
            printf("\n\nDigite 'Enter' para voltar ao menu ");
            readString(aux);
            break;
    }
}



int flowRemoveElement(int vetPrev[], int vetKey[], int vetNext[]){
    int value;
    printf("\n\nPosicao a ser retirada: ");
    scanf("%i", &value);
    if(value <= vetSize && vetPrev[value-1] != -1){
        removeElement(vetPrev, vetKey, vetNext, value);
        return 1;
    }else{
        return 0;
    }
}

void showOptions(){
    char strMenu[] = "\n\t MENU DE OPCOES \n\n Opcao 1 - Adicionar elemento\n Opcao 2 - Remover elemento\n Opcao 3 - Visualizar todas Listas\n Opcao 4 - Sair\n\n";
    printf(strMenu);
}

void sizeArray(){
    printf("Tamanho da Lista: ");
    scanf("%i", &vetSize);
}

int allocateObject(int vetNext[]){
    if(gFree ==-1 ){
        return -1;
    }else{
        int x = gFree; 
        gFree = vetNext[x-1]; 
        return x; 
    }
}

void addElement(int vetPrev[], int vetKey[], int vetNext[], int value){
    int freePrev = allocateObject(vetNext); 
    if(freePrev != -1){
        vetPrev[gHead-1] = freePrev; 
        vetNext[freePrev-1] = gHead;
        vetPrev[freePrev-1] = 0;
        vetKey[freePrev-1] = value;
        gHead = freePrev;
    }
}

void freeObject(int vetNext[], int deletedPosition){
    vetNext[deletedPosition] = gFree;
    gFree = deletedPosition + 1;
}


void removeElement(int vetPrev[], int vetKey[], int vetNext[], int position){
    
    position = position - 1;                     
    int proxPosition = vetNext[position]-1;     
    int antPosition = vetPrev[position]-1;      

    vetNext[antPosition] = proxPosition +1;    
    vetPrev[proxPosition] = antPosition +1;

    vetKey[position] = -1;
    vetPrev[position] = -1;
    freeObject(vetNext, position);
}

void showList(int vet[]){
    int j;
    printf("[");
    for(j=0; j<vetSize; j++){
        if(j != (vetSize-1)){
            printf("%i, ", vet[j]);
        }else{
            printf("%i", vet[j]);
        }
    }
    printf("]");
}


int main(){

    //Limpando Tela
    clrscr();

    // Montando Listas
    sizeArray();
    int vetNext[vetSize], vetKey[vetSize], vetPrev[vetSize];
    fillList(vetKey, vetPrev);
    inputUser(vetNext);

    // Fluxo das operacoes basicas de Lista Ligadas
    int optionInt = 3;
    char optionChar[10];

    while(optionInt!=4){
        clrscr();
        showOptions();
        printf("Digite a Opcao Desejada: ");
        readString(optionChar);
        optionInt = atoi(optionChar);
        callOptions(optionInt, vetPrev, vetKey, vetNext);
    }

    return 0;
}


