import { XMLParser } from "./XMLParser";
export class TWResponseXMLParser implements XMLParser {
   public parse(): string {
      console.log("TW Parsing Response XML...");
      return "TW Response XML Message";
   }
}
