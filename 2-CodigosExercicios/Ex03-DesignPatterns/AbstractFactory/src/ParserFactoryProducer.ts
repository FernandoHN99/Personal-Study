import { AbstractParserFactory } from "./AbstractParserFactory";
import { NYParserFactory } from "./NYParserFactory";
import { TWParserFactory } from "./TWParserFactory";

export class ParserFactoryProducer {
   private constructor() {
      throw new Error("A classe não pode ser instanciada");
   }
   public static getFactory(factoryType: string): AbstractParserFactory | null {
      switch (factoryType) {
         case "NYFactory":
            return new NYParserFactory();
         case "TWFactory":
            return new TWParserFactory();
      }
      return null;
   }
}
