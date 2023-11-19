import { XMLParser } from "./XMLParser";
export class TWOrderXMLParser implements XMLParser {
   public parse(): string {
      console.log("TW Parsing Order XML...");
      return "TW Order XML Message";
   }
}
