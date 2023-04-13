class No:
    def __init__(self, valor = None):
     
        self.valor = valor
        self.left = self.right = None
        

    def Adicionar(self, valor):
    
        if not self.valor:
            self.valor = valor
            return

        if self.valor == valor:
            return

        if valor < self.valor:
            if self.left:
                self.left.Adicionar(valor)
                return
            self.left = No(valor)
            return
        
        if self.right:
            self.right.Adicionar(valor)
            return
        self.right = No(valor)

    def preOrder(self, var):
        
        if self.left is not None:
            self.left.preOrder(var)
        
        if self.right is not None:
            self.right.preOrder(var)
                
        if self.valor is not None:
            var.append(self.valor)

        return var

    def postOrder(self, var):
        if self.left is not None:
            self.left.postOrder(var)
            
        if self.right is not None:
            self.right.postOrder(var)
            
        if self.valor is not None:
            var.append(self.valor)
            
        return var

    def inOrder(self, var):
      
        if self.left is not None:
            self.left.inOrder(var)
        

        if self.right is not None:
            self.right.inOrder(var)

        if self.valor is not None:
            var.append(self.valor)
        
        return var

    def CondicaodeExistencia(self, valor):

        if valor == self.valor:
            return True

        if valor < self.valor:
            if self.left == None:
                return False
            return self.left.CondicaodeExistencia(valor)
        
        if self.right == None:
            return False
        return self.right.CondicaodeExistencia(valor)

    def ValorMin(self):

        set = self
        while set.left is not None:
            set = set.left
        return set.valor

    
    def QuantidadeDNos(self):
      count = 1
      if self is None:
        return 0
      if self is not None:
        if self.left is not None:
            count += self.left.QuantidadeDNos()
        if self.right is not None:
            count += self.right.QuantidadeDNos()
      return count

    def Altura(self, base):
      if base is None:
        return 0
      else:
        return 1 + max(self.Altura(base.left), self.Altura(base.right))

    def media(self):
        values = self.postOrder([])
        mean = sum(values)/len(values)
        return mean


    def QuantidadeDNulls(self): 
        nulls = 0
        if (self.left is not None):
          self.left.QuantidadeDNos()
        if (self.right is not None):
          self.right.QuantidadeDNos()
        if (self.left is None):
          nulls += 1
        if (self.right is None):
          nulls += 1
        return nulls

      
    def DoisX(self):
        if (self.left is not None):
            self.left.DoisX()
        
        if (self.right is not None):
            self.right.DoisX()
        
        if ((self.valor % 2) == 0):
            print(self.valor, end='\t')

    
    def somatorio(self):
        X = self.postOrder([])
        return sum(X)


def main():
    array = [3, 7, 8, 9, 10, 5]
    Arvore = No()
    for X in array:
        Arvore.Adicionar(X)

    # Item 2)
    k = 2
    Arvore.Adicionar(k)

    # Item 3)
    print("\nPreOrder:")
    print(Arvore.preOrder([]))
    
    # Item 4)
    print("\nPostOrder")
    print(Arvore.postOrder([]))

    # Item 5)
    print("\nInOrder")
    print(Arvore.inOrder([]))

    # Item 6)
    print("\nExistencia do Nó com valor de 2:")
    print(Arvore.CondicaodeExistencia(2))


    # Item 7
    print("\nValor Minino na Arvore")
    print(Arvore.ValorMin())

    # Item 8
    print("\nQuantidade de Nós")
    print(Arvore.QuantidadeDNos())

    # Item 9
    print("\nMedia")
    print(round(Arvore.media(), 2))
    
    # Ex. 10
    print("\nAltura:")
    print(Arvore.Altura(Arvore))

    # Item 11
    print("\nQuantidade de Nulls")
    print(Arvore.QuantidadeDNulls())

    # Item 12
    print("\nMultiplos de 2")
    Arvore.DoisX()

    # Item 13
    print("\nSomatorio")
    print(Arvore.somatorio())
   
if __name__ == "__main__":
    main()