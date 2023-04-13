// Class containing left and right child
// of current node and key value
class Node {
    int key;
    Node left, right;
 
    public Node(int item)
    {
        key = item;
        left = right = null;
    }
}
 
// A Java program to introduce Binary Tree
class BinaryTree {

  public void traversePostOrder(Node node) {
    if (node != null) {
        traversePostOrder(node.left);
        traversePostOrder(node.right);
        System.out.print(" " + node.key);
    }
  }

  public void traversePreOrder(Node node) {
    if (node != null) {
        System.out.print(" " + node.key);
        traversePreOrder(node.left);
        traversePreOrder(node.right);
    }
  }

  public void traverseInOrder(Node node) {
    if (node != null) {
        traverseInOrder(node.left);
        System.out.print(" " + node.key);
        traverseInOrder(node.right);
    }
 }

 public boolean ifNodeExists( Node node, int key)
 {
     if (node == null)
         return false;
  
     if (node.key == key)
         return true;
  
     // then recur on left subtree /
     boolean res1 = ifNodeExists(node.left, key);
    
     // node found, no need to look further
     if(res1) return true;
  
     // node is not found in left,
     // so recur on right subtree /
     boolean res2 = ifNodeExists(node.right, key);
  
     return res2;
 }

 public int findMax(Node node)
 {
     if (node == null)
         return Integer.MIN_VALUE;

     int res = node.key;
     int lres = findMax(node.left);
     int rres = findMax(node.right);

     if (lres > res)
         res = lres;
     if (rres > res)
         res = rres;
     return res;
 }
 public int findMin(Node node)
{
    if (node == null)
        return Integer.MAX_VALUE;
 
    int res = node.key;
    int lres = findMin(node.left);
    int rres = findMin(node.right);
 
    if (lres < res)
        res = lres;
    if (rres < res)
        res = rres;
    return res;
}
     
    // Root of Binary Tree
    Node root;
 
    // Constructors
    BinaryTree(int key) { root = new Node(key); }
 
    BinaryTree() { root = null; }
 
    public static void main(String[] args)
    {
        BinaryTree tree = new BinaryTree();
 
        // create root
        tree.root = new Node(0);
 
        /* following is the tree after above statement
 
              0
            /   \
          null  null     */
 
        tree.root.left = new Node(1);
        tree.root.right = new Node(2);
 
        /* 1 and 2 become left and right children of 0
               0
            /     \
          1        2
        /   \     /  \
      null null null null  */
 
        tree.root.right.left = new Node(3);
        tree.root.right.right = new Node(4);
        /* 3 and 4 become left and right child of 2 respectively
                    0
                /       \
               1          2
             /   \       /  \
          null    null  3    4
         */
        tree.root.right.left.left = new Node(5);
        tree.root.right.left.right = new Node(6);
        /* 5 and 6 become left and rigth child of 2 respectively
                  0
              /       \
            1            2
          /    \      /     \
         null null   3        4
                   /   \      /  \ 
                5        6    null null
               / \      / \
            null null  null null 
       */

       // Traversing the tree
       // in order
       System.out.println("traversing in order: ");
       tree.traverseInOrder(tree.root);
       // pre order
       System.out.println("\ntraversing pre order: ");
       tree.traversePreOrder(tree.root);
       // post order
       System.out.println("\ntraversing post order: ");
       tree.traversePostOrder(tree.root);

       // searching for a integer on the tree
       System.out.println("\nsearching for K: ");
       int K = 15;
       if(tree.ifNodeExists(tree.root, K))
          System.out.println("it was found!!!");
        else
          System.out.println("not found :(");
       // finding the biggest value in the tree
       System.out.println("searching for biggest value: ");
       System.out.println("biggest value: " + tree.findMax(tree.root));
       // finding lowest value in the tree
       System.out.println("searching for lowest value: ");
       System.out.println("lowest value: " + tree.findMin(tree.root));
    }
}