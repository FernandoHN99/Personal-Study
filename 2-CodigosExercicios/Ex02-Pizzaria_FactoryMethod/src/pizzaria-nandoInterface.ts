// interface  Pizza {

//    preparar(): void
//    assar(): void 
//    cortar(): void 
//    empacotar(): void 

// }


// class PizzaDeQueijoDeNY implements Pizza {
//    preparar(): void {
//       console.log("Preparando pizza de queijo de NY...");
//    }

//    assar(): void {
//       console.log("Assando pizza de queijo de NY...");
//    }
//    cortar(): void {
//       console.log("Cortando pizza de queijo de NY...");
//    }

//    empacotar(): void {
//       console.log("Empacotando pizza de queijo de NY...");
//    }
// }

// class PizzaDePepperoniDeNY implements Pizza {
//    preparar(): void {
//       console.log("Preparando pizza de pepperoni de NY...");
//    }

//    assar(): void {
//       console.log("Assando pizza de pepperoni de NY...");
//    }

//    cortar(): void {
//       console.log("Cortando pizza de pepperoni de NY...");
//    }

//    empacotar(): void {
//       console.log("Empacotando pizza de pepperoni de NY...");
//    }
// }

// class PizzaDeQueijoDeChicago implements Pizza {
//    preparar(): void {
//       console.log("Preparando pizza de queijo de Chicago...");
//    }

//    assar(): void {
//       console.log("Assando pizza de queijo de Chicago...");
//    }

//    cortar(): void {
//       console.log("Cortando pizza de queijo de Chicago...");
//    }

//    empacotar(): void {
//       console.log("Empacotando pizza de queijo de Chicago...");
//    }
// }

// class PizzaDePepperoniDeChicago implements Pizza {
//    preparar(): void {
//       console.log("Preparando pizza de pepperoni de Chicago...");
//    }

//    assar(): void {
//       console.log("Assando pizza de pepperoni de Chicago...");
//    }

//    cortar(): void {
//       console.log("Cortando pizza de pepperoni de Chicago...");
//    }

//    empacotar(): void {
//       console.log("Empacotando pizza de pepperoni de Chicago...");
//    }
// }

// interface SimplePizzaFactory {
//    criarPizza(tipo: string): Pizza | null
// }

// //simplefactory ny
// class SimplePizzaFactoryNY implements SimplePizzaFactory {
//    criarPizza(tipo: string): Pizza | null {
//       let pizza: Pizza | null = null;
//       if (tipo === "Queijo") {
//          pizza = new PizzaDeQueijoDeNY();
//       } else if (tipo === "Pepperoni") {
//          pizza = new PizzaDePepperoniDeNY();
//       }
//       return pizza;
//    }
// }

// class SimplePizzaFactoryChicago implements SimplePizzaFactory {
//    criarPizza(tipo: string): Pizza | null {
//       let pizza: Pizza | null = null;
//       if (tipo === "Queijo") {
//          pizza = new PizzaDeQueijoDeChicago();
//       } else if (tipo === "Pepperoni") {
//          pizza = new PizzaDePepperoniDeChicago();
//       }
//       return pizza;
//    }
// }

// class PizzaStore {
//    constructor(private simplePizzaFactory: SimplePizzaFactory) {}

//    pedirPizza = (tipo: string): Pizza | null => {
//       let pizza = this.simplePizzaFactory.criarPizza(tipo);
//       pizza?.preparar();
//       pizza?.assar();
//       pizza?.cortar();
//       pizza?.empacotar();
//       return pizza;
//    };
// }

// let franquias = [
//    new PizzaStore(new SimplePizzaFactoryNY()),
//    new PizzaStore(new SimplePizzaFactoryChicago()),
// ];

// console.log(franquias[0].pedirPizza("Queijo"));
