#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 255
void Trocar(int V[], int p){
    int aux;
    aux = V[p];
    V[p] = V[p+1];
    V[p+1]= aux;

    }
void Ordenar(int V[], int n){
    int i, j;
    for(i=(n-1); i>=1; i--){
        for(j=0; j<=(i-1); j++){
                if(V[j]>V[j+1]){

                    Trocar(V, j);
                    }


                }

        }

    }
void Adicionar_Valores(int V[],int n){

    int j;
   for(j=0; j<n; j++){
        printf("%i Valor: ", (j+1));
        scanf("%i", &V[j]);
        }
    printf("\n");
    }
void Mostrar_Valores(int V[], int n){

    int j;
    for(j=0; j<n; j++){
        printf("Valor %i: %i\n",(j+1), V[j]);
        }
    }


int main(){
    int n;
    printf("Tamanho do vetor: ");
    scanf("%i", &n);
    int Vetor[n];

    Adicionar_Valores(Vetor, n);
    Ordenar(Vetor, n);
    Mostrar_Valores(Vetor, n);

    return 0;
    }
