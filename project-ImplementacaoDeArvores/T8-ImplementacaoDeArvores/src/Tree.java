// *****************INTEGRANTES DO GRUPO**********************
// Fernando Henriques Neto RA: 18.00931-0
// Arthur Wypych de Almeida RA: 19.00565-2
// Lucas Romanato de Oliveira RA: 20.00313-7

public class Tree {
    Node_Tree root; 
    public static int size; 
    
    public Tree() {
        this.root = null; 
        this.size = 0;
    } 
    
    public void insert_root(Integer valor) {
        Node_Tree node = new Node_Tree(valor); 
        this.root = node; 
        this.size = 1;
    }

    public Node_Tree ret_Root() { 
        return (this.root);
    }

    public int size() { 
        return this.size;
    }

    public boolean isEmpty(){ 
        if (this.size == 0 ) 
            return true;
        else 
            return false;
    }
    

}