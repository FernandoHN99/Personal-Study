
abstract class Pizza {
   preparar(): void {
      console.log("Preparando a pizza...");
   }

   assar(): void {
      console.log("Assando a pizza...");
   }

   cortar(): void {
      console.log("Cortando a pizza...");
   }

   empacotar(): void {
      console.log("Empacotando a pizza...");
   }

   // @override
   toString(): string {
      return "Pizza";
   }
}

abstract class PizzaDeQueijo extends Pizza {
   preparar(): void {
      console.log("Preparando pizza de queijo...");
   }

   assar(): void {
      console.log("Assando pizza de queijo...");
   }

   cortar(): void {
      console.log("Cortando pizza de queijo...");
   }

   empacotar(): void {
      console.log("Empacotando pizza de queijo...");
   }
}

abstract class PizzaGrega extends Pizza {
   preparar(): void {
      console.log("Preparando pizza grega...");
   }

   assar(): void {
      console.log("Assando pizza grega...");
   }

   cortar(): void {
      console.log("Cortando pizza grega...");
   }

   empacotar(): void {
      console.log("Empacotando pizza grega...");
   }
}

abstract class PizzaDePepperoni extends Pizza {
   preparar(): void {
      console.log("Preparando pizza de pepperoni...");
   }

   assar(): void {
      console.log("Assando pizza de pepperoni...");
   }

   cortar(): void {
      console.log("Cortando pizza de pepperoni...");
   }

   empacotar(): void {
      console.log("Empacotando pizza de pepperoni...");
   }
}

abstract class PizzaDeMolusco extends Pizza {
   preparar(): void {
      console.log("Preparando pizza de molusco...");
   }

   assar(): void {
      console.log("Assando pizza de molusco...");
   }

   cortar(): void {
      console.log("Cortando pizza de molusco...");
   }

   empacotar(): void {
      console.log("Empacotando pizza de molusco...");
   }
}

abstract class PizzaVegetariana extends Pizza {
   preparar(): void {
      console.log("Preparando pizza vegetariana...");
   }

   assar(): void {
      console.log("Assando pizza vegetariana...");
   }

   cortar(): void {
      console.log("Cortando pizza vegetariana...");
   }

   empacotar(): void {
      console.log("Empacotando pizza vegetariana...");
   }
}

class PizzaDeQueijoDeNY extends PizzaDeQueijo {
   preparar(): void {
      console.log("Preparando pizza de queijo de NY...");
   }

   assar(): void {
      console.log("Assando pizza de queijo de NY...");
   }
   cortar(): void {
      console.log("Cortando pizza de queijo de NY...");
   }

   empacotar(): void {
      console.log("Empacotando pizza de queijo de NY...");
   }
}

class PizzaDePepperoniDeNY extends PizzaDePepperoni {
   preparar(): void {
      console.log("Preparando pizza de pepperoni de NY...");
   }

   assar(): void {
      console.log("Assando pizza de pepperoni de NY...");
   }

   cortar(): void {
      console.log("Cortando pizza de pepperoni de NY...");
   }

   empacotar(): void {
      console.log("Empacotando pizza de pepperoni de NY...");
   }
}

class PizzaDeQueijoDeChicago extends PizzaDeQueijo {
   preparar(): void {
      console.log("Preparando pizza de queijo de Chicago...");
   }

   assar(): void {
      console.log("Assando pizza de queijo de Chicago...");
   }

   cortar(): void {
      console.log("Cortando pizza de queijo de Chicago...");
   }

   empacotar(): void {
      console.log("Empacotando pizza de queijo de Chicago...");
   }
}

class PizzaDePepperoniDeChicago extends PizzaDePepperoni {
   preparar(): void {
      console.log("Preparando pizza de pepperoni de Chicago...");
   }

   assar(): void {
      console.log("Assando pizza de pepperoni de Chicago...");
   }

   cortar(): void {
      console.log("Cortando pizza de pepperoni de Chicago...");
   }

   empacotar(): void {
      console.log("Empacotando pizza de pepperoni de Chicago...");
   }
}

abstract class SimplePizzaFactory {
   abstract criarPizza(tipo: string): Pizza | null;

}

//simplefactory ny
class SimplePizzaFactoryNY extends SimplePizzaFactory {
   criarPizza(tipo: string): Pizza | null {
      let pizza: Pizza | null = null;
      if (tipo === "Queijo") {
         pizza = new PizzaDeQueijoDeNY();
      } else if (tipo === "Pepperoni") {
         pizza = new PizzaDePepperoniDeNY();
      }
      return pizza;
   }
}

class SimplePizzaFactoryChicago extends SimplePizzaFactory {
   criarPizza(tipo: string): Pizza | null {
      let pizza: Pizza | null = null;
      if (tipo === "Queijo") {
         pizza = new PizzaDeQueijoDeChicago();
      } else if (tipo === "Pepperoni") {
         pizza = new PizzaDePepperoniDeChicago();
      }
      return pizza;
   }
}

class PizzaStore {
   constructor(private simplePizzaFactory: SimplePizzaFactory) {}

   pedirPizza = (tipo: string): Pizza | null => {
      let pizza = this.simplePizzaFactory.criarPizza(tipo);
      pizza?.preparar();
      pizza?.assar();
      pizza?.cortar();
      pizza?.empacotar();
      return pizza;
   };
}

let franquias = [
   new PizzaStore(new SimplePizzaFactoryNY()),
   new PizzaStore(new SimplePizzaFactoryChicago()),
];

console.log(franquias[0].pedirPizza("Queijo"));
