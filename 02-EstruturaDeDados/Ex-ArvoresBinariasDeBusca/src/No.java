// ******INTEGRANTES DO GRUPO*******
// Fernando Henriques Neto RA: 18.00931-0
// Arthur Wypych de Almeida RA: 19.00565-2
// Lucas Romanato de Oliveira RA: 20.00313-7

import java.util.ArrayList;
import java.util.List;

public class No {
    private Integer valor = null;
    private No esquerda = null;
    private No direita = null;

    public No() {
    }

    public No(Integer valor) {
        this.valor = valor;
    }

    public void adicionar(Integer valor) {
        if (isNull(this.valor)) {
            this.valor = valor;
            return;
        }

        if (this.valor == valor) {
            return;
        }

        if (valor < this.valor) {
            if (!isNull(this.esquerda)) {
                this.esquerda.adicionar(valor);
                return;
            }
            this.esquerda = new No(valor);
            return;
        }

        if (!isNull(this.direita)) {
            this.direita.adicionar(valor);
            return;
        }
        this.direita = new No(valor);
        return;
    }

    public List<Integer> preOrder(List<Integer> list) {
        if (!isNull(this.valor)) {
            list.add(this.valor);
        }
        if (!isNull(this.esquerda)) {
            this.esquerda.preOrder(list);
        }
        if (!isNull(this.direita)) {
            this.direita.preOrder(list);
        }
        return list;
    }

    public List<Integer> postOrder(List<Integer> list) {
        if (!isNull(this.esquerda)) {
            this.esquerda.postOrder(list);
        }
        if (!isNull(this.direita)) {
            this.direita.postOrder(list);
        }
        if (!isNull(this.valor)) {
            list.add(this.valor);
        }
        return list;
    }

    public List<Integer> inOrder(List<Integer> list) {
        if (!isNull(this.esquerda)) {
            this.esquerda.inOrder(list);
        }
        if (!isNull(this.valor)) {
            list.add(this.valor);
        }
        if (!isNull(this.direita)) {
            this.direita.inOrder(list);
        }
        return list;
    }

    public boolean condicaoDeExistencia(Integer valor) {
        if (this.valor == valor) {
            return true;

        } else if (this.valor > valor) {
            if (isNull(this.esquerda)) {
                return false;
            } else {
                return (this.esquerda.condicaoDeExistencia(valor));
            }
        } else if (isNull(this.direita)) {
            return false;
        }
        return this.direita.condicaoDeExistencia(valor);
    }

    public Integer minValue() {
        No noAux = (No) getObjeto();
        while (!isNull(noAux.esquerda)) {
            noAux = this.esquerda;
        }
        return noAux.valor;
    }

    public Integer quantidadeNos() {
        Integer counter = 1;
        if (isNull(getObjeto()))
            return 0;
        if (!isNull(getObjeto()))
            if (!isNull(this.esquerda))
                counter += this.esquerda.quantidadeNos();
        if (!isNull(this.direita))
            counter = this.direita.quantidadeNos();

        return counter;
    }

    public Integer altura(No base) {
        if (isNull(base))
            return 0;
        else {
            return (1 + Math.max(altura(base.esquerda), altura(base.direita)));
        }
    }

    public double media() {
        List<Integer> listValues = new ArrayList<Integer>();
        listValues = postOrder(listValues);
        double media = sum(listValues) / listValues.size();
        return media;
    }

    public Integer quantidadeNull() {
        Integer nulos = 0;
        if (!isNull(this.esquerda))
            this.esquerda.quantidadeNos();
        if (!isNull(this.direita))
            this.direita.quantidadeNos();
        if (isNull(this.esquerda))
            nulos += 1;
        if (isNull(this.direita))
            nulos += 1;
        return nulos;
    }

    public void multiplosDois() {
        if (!isNull(this.esquerda))
            this.esquerda.multiplosDois();
        if (!isNull(this.direita))
            this.direita.multiplosDois();
        if ((double) this.valor % 2 == 0)
            System.out.print(this.valor + "\t");
    }

    public double somatorio() {
        List<Integer> list = new ArrayList<Integer>();
        List<Integer> aux = this.postOrder(list);
        return sum(aux);
    }

    public double sum(List<Integer> list) {
        double soma = 0;
        for (Integer integer : list) {
            soma += integer;
        }
        return soma;
    }

    public Object getObjeto() {
        return this;
    }

    public boolean isNull(Object obj) {
        return obj == null;
    }
}
