import { XMLParser } from "./XMLParser";
export class NYErrorXMLParser implements XMLParser {
   public parse(): string {
      console.log("NY Parsing error XML...");
      return "NT Error XML Message";
   }
}
