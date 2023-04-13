// ******INTEGRANTES DO GRUPO*******
// Fernando Henriques Neto RA: 18.00931-0
// Arthur Wypych de Almeida RA: 19.00565-2
// Lucas Romanato de Oliveira RA: 20.00313-7

public class Heapsort {
    private static int tamanho;
    private static int[] arrayMain;
    
    public static void heapsort(int[] array) {
        arrayMain = array;          
        tamanho = arrayMain.length - 1;     
        
        // Função para construir um Max-Heap
        constroiHeap();
        
        for (int i = tamanho; i > 0; i--) {
            troca(0, tamanho);     
            tamanho -= 1;         
            maxHeapifica(0);
        }
    }
    
    private static void constroiHeap() {

        int meio = (int) (tamanho/2);

        for (int i = meio - 1; i >= 0; i--) {
            maxHeapifica(i);
        }
    }
    
    // Função para auxiliar na troca de posição dos valores
    private static void troca(int i, int j) {
        int aux;

        aux = arrayMain[i];
        arrayMain[i] = arrayMain[j];
        arrayMain[j] = aux;
    }
    
    // Função para comparar  valores de um Heap e ao encontrar o maior
    private static void maxHeapifica(int pai) {
        int maior = pai,            
        esquerda = 2 * pai + 1,     
        direita = 2 * pai + 2;  
        
        if (esquerda <= tamanho && arrayMain[esquerda] > arrayMain[maior])
            maior = esquerda;
        
        if (direita <= tamanho && arrayMain[direita] > arrayMain[maior])
            maior = direita;
        
        if (maior != pai) {
            troca(pai, maior);
            maxHeapifica(maior);  
        }
    }

    //Função para exibição dos arrays
    private static String montarArray(int[] arr){
        String ouput = "";

        for(int valor : arr) {
            ouput += valor + " ";
        }
        return ouput;

    }

    // Função para limpar a tela
    public static void clearScreen() {  
        System.out.print("\033[H\033[2J");  
        System.out.flush();  
    }  
    
    // Função main
    public static void main(String[] args) {
        String strArray = "";
        clearScreen();

        //Array desordenado
        int[] arrayMainDesordenado = {3, 1, 4, 8, 2, 5, 9, 0};
        
        strArray = montarArray(arrayMainDesordenado);
        System.out.println("Array Desordenado = " + strArray);
        
        // Chamada da função para Ordenação
        heapsort(arrayMainDesordenado);
        
        strArray = montarArray(arrayMainDesordenado);
        System.out.println("Array Ordenado    = " + strArray);
        System.out.println();

        
    }
}