import { XMLParser } from './XMLParser'
export class ResponseXMLParser implements XMLParser { parse():string {
        console.log("Parsing response XML...");
        return "Response XML Message";
    }
}