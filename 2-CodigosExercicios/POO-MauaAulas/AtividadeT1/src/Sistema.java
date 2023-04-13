public class Sistema {
    
    public static void run(){
        Util.clearScreen();
        Usuario usuario1 = new Usuario("Fernando", "132456", "fernando@gmail.com");
        Usuario usuario2 = new Usuario("Sandra", "78910", "Sandra@gmail.com");
        System.out.println("Usuario1: " + usuario1);

        Carro car = new Carro();
        Moto motorcycle = new Moto();
        Bicicleta bike = new Bicicleta();
        Patinete scooter = new Patinete();

        car.testar();
        motorcycle.testar();
        bike.testar();
        scooter.testar();

        System.out.println(usuario1.Alugar(car)); 
        System.out.println(usuario1.Trocar(car, motorcycle)); 
        System.out.println(usuario2.Alugar(motorcycle));
        System.out.println(usuario2.Alugar(scooter));
        System.out.println(usuario2.Devolver(scooter));
    }
}
