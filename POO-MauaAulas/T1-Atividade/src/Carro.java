public class Carro extends Transporte {

    public Carro(){
        this.idTransporte = gerarID();
        this.custoPorHora = 59.99;
        this.disponibilidade = true;
    }
}
