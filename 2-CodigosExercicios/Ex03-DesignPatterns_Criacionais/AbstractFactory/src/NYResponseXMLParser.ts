import { XMLParser } from "./XMLParser";
export class NYResponseXMLParser implements XMLParser {
   public parse(): string {
      console.log("NY Parsing Response XML...");
      return "NY Response XML Message";
   }
}
