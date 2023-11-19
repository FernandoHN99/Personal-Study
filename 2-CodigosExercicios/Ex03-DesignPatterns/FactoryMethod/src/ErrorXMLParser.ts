import { XMLParser } from './XMLParser'
export class ErrorXMLParser implements XMLParser { parse():string {
        console.log("Parsing error XML...");
        return "Error XML Message";
    }
}