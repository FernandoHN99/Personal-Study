import { XMLParser } from "./XMLParser";
export class TWErrorXMLParser implements XMLParser {
   public parse(): string {
      console.log("TW Parsing error XML...");
      return "TW Error XML Message";
   }
}
