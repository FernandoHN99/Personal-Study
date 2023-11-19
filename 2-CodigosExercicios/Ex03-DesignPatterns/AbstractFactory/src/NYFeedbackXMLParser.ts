import { XMLParser } from "./XMLParser";
export class NYFeedbackXMLParser implements XMLParser {
   public parse(): string {
      console.log("NY Parsing Feedback XML...");
      return "NY Feedback XML Message";
   }
}
