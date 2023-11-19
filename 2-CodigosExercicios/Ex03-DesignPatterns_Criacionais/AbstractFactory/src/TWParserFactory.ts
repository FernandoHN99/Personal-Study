import { AbstractParserFactory } from "./AbstractParserFactory";
import { TWErrorXMLParser } from "./TWErrorXMLParser";
import { TWFeedbackXMLParser } from "./TWFeedbackXMLParser";
import { TWOrderXMLParser } from "./TWOrderXMLParser";
import { TWResponseXMLParser } from "./TWResponseXMLParser";
import { XMLParser } from "./XMLParser";

export class TWParserFactory implements AbstractParserFactory {
   public getParserInstance(parserType: string): XMLParser | null {
      switch (parserType) {
         case "TWERROR":
            return new TWErrorXMLParser();
         case "TWFEEDBACK":
            return new TWFeedbackXMLParser();
         case "TWORDER":
            return new TWOrderXMLParser();
         case "TWRESPONSE":
            return new TWResponseXMLParser();
      }
      return null;
   }
}
