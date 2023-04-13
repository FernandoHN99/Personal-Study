public class App {
    public static void main(String[] args) {

        System.clearProperty("clear");
        Caneta c1 = new Caneta();
        Caneta c2 = new Caneta();

        c1.iniciarCaneta("BIC", "AZUL", 1.0);
        c2.iniciarCaneta("BIC", "AZUL", 1.0);

        System.out.println("\n Minha caneta C1: \n" + c1.pegarDados());
        c1.escrever("\n" + "Teste Caneta 1" + "\n");
        System.out.println("\n Minha caneta C1: \n" + c1.pegarDados());

        System.out.println("\n Minha caneta C2: \n" + c2.pegarDados());
        c2.escrever("\n" + "Teste Caneta 2 - bla bla bla" + "\n");
        System.out.println("\n Minha caneta C2: \n" + c2.pegarDados());

    }
}
