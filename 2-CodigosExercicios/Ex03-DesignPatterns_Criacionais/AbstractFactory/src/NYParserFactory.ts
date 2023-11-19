import { AbstractParserFactory } from "./AbstractParserFactory";
import { NYErrorXMLParser } from "./NYErrorXMLParser";
import { NYFeedbackXMLParser } from "./NYFeedbackXMLParser";
import { NYOrderXMLParser } from "./NYOrderXMLParser";
import { NYResponseXMLParser } from "./NYResponseXMLParser";
import { XMLParser } from "./XMLParser";

export class NYParserFactory implements AbstractParserFactory {
   
   public getParserInstance(parserType: string): XMLParser | null {
      switch (parserType) {
         case "NYERROR":
            return new NYErrorXMLParser();
         case "NYFEEDBACK":
            return new NYFeedbackXMLParser();
         case "NYORDER":
            return new NYOrderXMLParser();
         case "NYRESPONSE":
            return new NYResponseXMLParser();
      }
      return null;
   }
}
