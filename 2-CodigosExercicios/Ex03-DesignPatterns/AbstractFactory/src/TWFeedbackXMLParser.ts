import { XMLParser } from "./XMLParser";
export class TWFeedbackXMLParser implements XMLParser {
   public parse(): string {
      console.log("TW Parsing Feedback XML...");
      return "TW Feedback XML Message";
   }
}
