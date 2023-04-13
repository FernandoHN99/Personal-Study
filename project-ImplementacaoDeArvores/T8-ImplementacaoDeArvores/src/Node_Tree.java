// *****************INTEGRANTES DO GRUPO**********************
// Fernando Henriques Neto RA: 18.00931-0
// Arthur Wypych de Almeida RA: 19.00565-2
// Lucas Romanato de Oliveira RA: 20.00313-7

import java.security.SecureRandomParameters;
import javax.swing.plaf.synth.SynthScrollBarUI;

public class Node_Tree {
    Integer item; 
    Node_Tree parent; 
    Node_Tree firstChild; 
    Node_Tree next;

    public Node_Tree(Integer item) { 
        this.item = item; 
        this.parent = null; 
        this.firstChild = null; 
        this.next = null;
        Tree.size+=1;
    }
    
    //item 1-a) 
    public void imprimeFilhos() { 
        if (this.firstChild == null) 
            System.out.println("Nó nao tem filhos....");
        else {
            Node_Tree trab = this.firstChild; 
            while (trab != null) {
                System.out.println(trab.item); 
                trab = trab.next;
            }  
        }
    }

    //item 1-b) 
    public Node_Tree Pai() { 
        return this.parent;
    }

    //item 1-c) 
    public void imprime_Pai(){ 
        if (this.parent != null) 
            System.out.println("Pai: " + this.parent.item );
        else 
            System.out.println("Este nó é root, não tem pai...");
    }

    //item 1-d) 
    public boolean EhInterno() { 
        if (this.firstChild != null) 
            return true;
        else 
            return false;
    }
        
    //item 1-e) 
    public void imprimeFilhosFolhas(){ 
        Boolean aux = false;
        Node_Tree trab = this.firstChild; 
        while(trab != null){
            if(!trab.EhInterno()){
                aux = true;
                System.out.println(trab.item); 
            }
            trab = trab.next;
        }
        if(!aux)
            System.out.println("Nó nao tem filhos folhas....");
    }

    //item 1-f) 
    public void preorder(){ 
        System.out.println(this.item);
        
        Node_Tree noFilho = this.firstChild;
        while(noFilho != null){ 
            noFilho.preorder(); 
            noFilho = null;
        }
        if(this.next != null){
            this.next.preorder();
        }
    }
    
    //item 1-g) 
    public void posorder(){ 
        Node_Tree noFilho = this.firstChild;
        while(noFilho != null){ 
            noFilho.posorder(); 
            noFilho = noFilho.next;
        }
        System.out.println(this.item);
    }

    public int dept() { 
        if (this.parent == null) 
            return 0;
        else 
            return (1 + this.parent.dept());
        }
    
    public int height() { 
        if (this.firstChild == null ) 
            return 0;

        int h=0; 
        Node_Tree trab = this.firstChild;
        while(trab.next != null ){ 
            h = Math.max(h , trab.next.height()); 
            trab = trab.next;
        } 
        return 1 + h;
    }


    public void DobraPai(){
        this.parent.item = this.parent.item * 2; 
    }
    
    public void DobraFilhos(){
        if(this.firstChild != null){
            this.firstChild.item = this.firstChild.item *2;
            Node_Tree noAux = this.firstChild;
            while(noAux.next != null){
                noAux.next.item = noAux.next.item * 2;
                noAux = noAux.next;
            }
        }
    }

    public void imprimiValor(){
        System.out.println(this.item);
    }
    

    public Node_Tree getParent() {
        return parent;
    }

}