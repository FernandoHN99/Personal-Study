import { DisplayService } from "./DisplayService";
import { OrderXMLParser } from "./OrderXMLParser";
import { XMLParser } from "./XMLParser";
export class OrderXMLDisplayService extends DisplayService {
   public getParser(): XMLParser {
      return new OrderXMLParser();
   }
}
