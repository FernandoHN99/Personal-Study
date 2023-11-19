import { XMLParser } from './XMLParser'
export class FeedbackXMLParser implements XMLParser { parse():string {
        console.log("Parsing feedback XML...");
        return "Feedback XML Message";
    }
}