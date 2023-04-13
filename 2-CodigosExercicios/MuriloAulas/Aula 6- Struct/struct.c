#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 255


// ************************
// Criar o tipo da estrutura de dados DS18B20 com 3 campos:
//   um string com MAX caracteres para o "id"
//   um string com MAX caracteres para o "local"
//   um número real para armazenar a "temperatura"
// ************************
typedef struct{
    char id[MAX];
    char local[MAX];
    float temperatura;

}DS18B20 ;

// ************************



void LerString(char s[]);
float getTemperature(char id[20]);
void CadastrarSensores(DS18B20[], int);
void OrdenarSensores(DS18B20[], int);


int main()
{
    // ************************
    // declarar uma variável chamada "sensores" que permita
    // armazenar até 127 sensores DS18B20
    DS18B20 sensores[127];

    // ************************
    int i, n;

    printf("Digite o numero de sensores: ");
    scanf("%i", &n);



    // ************************
    // cadastrar os n sensores
    CadastrarSensores(sensores, n);


    // ************************


    // ************************
    // ordenar os n sensores pelo nome do local
    // ************************
    OrdenarSensores(sensores, n);


    // ************************


    // ************************
    // faz a leitura dos sensores e exibe as temperaturas indefinidamente

    // ************************f
while (1){
    system("cls");
    printf("\tSensor\t\t\tTemp\t\tLocal\n");
    for (i=0; i<n; i++){
        // faz a leitura da temperatura e armazena na estrutura
        sensores[i].temperatura = getTemperature(sensores[i].id);
        // ********************
        // exiba o id, temperatura e o local de cada sensorfor



            // retirar os comentários do printf
            // ********************
            printf("\n\t%s\t\t      %7.2f     \t%s\t\n", sensores[i].id,sensores[i].temperatura,sensores[i].local);

            // ********************

        }
        printf("\n");
        system("pause");


    }
return 0;

}

// ************************
// pedir para o usuário digitar os ids e locais dos n sensores
// ************************
void CadastrarSensores(DS18B20 sensores[], int n)
{
    int i;
    for (i=0; i<n; i++){
        printf("\nDigite o id: ");
        fflush(stdin);
        fgets(sensores[i].id,MAX,stdin);
        LerString(sensores[i].id);
        printf("Digite o local: ");
        fflush(stdin);
        fgets(sensores[i].local, MAX, stdin);
        LerString(sensores[i].local);

    }
}


// ************************
// troca o elemento sensor da posição p para p+1
// ************************
void Troca(DS18B20 s[], int p){

    char aux[MAX];
    strcpy(aux, s[p].local);
    strcpy(s[p].local, s[p+1].local);
    strcpy(s[p+1].local , aux);
    }


// ************************
// ordena os n sensores pelo local onde foram instalados
// ************************
void OrdenarSensores(DS18B20 s[], int n){
    int i, j;
    for(i=(n-1); i>=1; i--){
        for(j=0; j<=(i-1); j++){
                if(strcmpi(s[j].local,s[j+1].local) == 1){
                        Troca(s, j);

                        }


                }

        }

    }


// ************************
// pode ser útil
// ************************
void LerString(char s[])
{
    //setbuf(stdin, 0);
    //fgets(s, MAX, stdin);
    if (s[strlen(s)-1] == '\n')
        s[strlen(s)-1] = '\0';
}


// ************************
// retorna a temperatura do sensor identificado pelo parâmetro id
// ************************
float getTemperature(char id[MAX])
{
#include <time.h>
    float temp, s=0;
    int i, mn=id[0], mx=id[0];
    time_t t = time(NULL);
    struct tm *local= localtime(&t);
    for (i=0; i<strlen(id); i++)
    {
        s += id[i]/(float)(strlen(id));
        mn = (id[i]<mn)?id[i]:mn;
        mx = (id[i]>mx)?id[i]:mx;
    }
    temp = 20*(s-mn)/((mx!=mn)?(mx-mn):1)+((local->tm_mon-3)<5?00:10)+local->tm_hour+(rand() % 100)/100.0;
    return ((int)(100*temp))/ 100.0;
}


