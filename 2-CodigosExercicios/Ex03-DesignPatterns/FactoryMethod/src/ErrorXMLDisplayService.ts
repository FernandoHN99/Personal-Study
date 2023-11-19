import { DisplayService } from "./DisplayService";
import { ErrorXMLParser } from "./ErrorXMLParser";
import { XMLParser } from "./XMLParser";

export class ErrorXMLDisplayService extends DisplayService {
   public getParser(): XMLParser {
      return new ErrorXMLParser();
   }
}
