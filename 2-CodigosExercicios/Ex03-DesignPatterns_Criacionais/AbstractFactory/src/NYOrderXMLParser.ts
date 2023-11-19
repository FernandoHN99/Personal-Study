import { XMLParser } from "./XMLParser";
export class NYOrderXMLParser implements XMLParser {
   public parse(): string {
      console.log("NY Parsing Order XML...");
      return "NY Order XML Message";
   }
}
