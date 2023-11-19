import { AbstractParserFactory } from "./AbstractParserFactory";
import { ParserFactoryProducer } from "./ParserFactoryProducer";
import { XMLParser } from "./XMLParser";

let parserFactory: AbstractParserFactory | null =
   ParserFactoryProducer.getFactory("NYFactory");
let parser: XMLParser | null = parserFactory
   ? parserFactory.getParserInstance("NYORDER")
   : null;
let msg: string = parser ? parser.parse() : "";
console.log(msg);
console.log("\n***************************************************\n");
parserFactory = ParserFactoryProducer.getFactory("TWFactory");
parser = parserFactory ? parserFactory.getParserInstance("TWFEEDBACK") : null;
msg = parser ? parser.parse() : "";
console.log(msg);
