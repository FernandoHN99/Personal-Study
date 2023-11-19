import { DisplayService } from "./DisplayService";
import { FeedbackXMLParser } from "./FeedbackXMLParser";
import { XMLParser } from "./XMLParser";

export class FeedbackXMLDisplayService extends DisplayService {
   public getParser(): XMLParser {
      return new FeedbackXMLParser();
   }
}
