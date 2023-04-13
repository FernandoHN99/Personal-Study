// ******INTEGRANTES DO GRUPO*******
// Fernando Henriques Neto RA: 18.00931-0
// Arthur Wypych de Almeida RA: 19.00565-2
// Lucas Romanato de Oliveira RA: 20.00313-7

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {

        // Item 1-)
        List<Integer> listValues = new ArrayList<>(Arrays.asList(3, 7, 8, 9, 10, 5));
        No Arvore = new No();
        for (Integer integer : listValues) {
            Arvore.adicionar(integer);
        }

        // Item 2-)
        Integer k = 2;
        Arvore.adicionar(k);

        // Item 3-)
        System.out.println("\nPreOrder:");
        System.out.println(Arvore.preOrder(new ArrayList<Integer>()));

        // Item 4-)
        System.out.println("\nPostOrder");
        System.out.println(Arvore.postOrder(new ArrayList<Integer>()));

        // Item 5-)
        System.out.println("\nInOrder");
        System.out.println(Arvore.inOrder(new ArrayList<Integer>()));

        // Item 6-)
        System.out.println("\nExistencia do Nó com valor de 2:");
        System.out.println(Arvore.condicaoDeExistencia(2));

        // Item 7-)
        System.out.println("\nValor Minino na Arvore");
        System.out.println(Arvore.minValue());

        // Item 8-)
        System.out.println("\nQuantidade de Nós");
        System.out.println(Arvore.quantidadeNos());

        // Item 9-)
        System.out.println("\nMedia");
        System.out.printf("%.2f", Arvore.media());
        System.out.println();

        // Ex. 10-)
        System.out.println("\nAltura:");
        System.out.println(Arvore.altura(Arvore));

        // Item 11-)
        System.out.println("\nQuantidade de Nulls");
        System.out.println(Arvore.quantidadeNull());

        // Item 12-)
        System.out.println("\nMultiplos de 2");
        Arvore.multiplosDois();
        System.out.println();

        // Item 13-)
        System.out.println("\nSomatorio");
        System.out.println(Arvore.somatorio());
    }
}
