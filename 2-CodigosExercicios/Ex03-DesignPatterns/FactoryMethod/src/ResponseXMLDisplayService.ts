import { DisplayService } from "./DisplayService";
import { ResponseXMLParser } from "./ResponseXMLParser";
import { XMLParser } from "./XMLParser";
export class ResponseXMLDisplayService extends DisplayService {
   public getParser(): XMLParser {
      return new ResponseXMLParser();
   }
}
