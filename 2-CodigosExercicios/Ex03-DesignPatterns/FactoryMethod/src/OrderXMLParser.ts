import { XMLParser } from './XMLParser'
export class OrderXMLParser implements XMLParser { parse():string {
        console.log("Parsing order XML...");
        return "Order XML Message";
    }
}