import { XMLParser } from "./XMLParser";

export interface AbstractParserFactory {
   getParserInstance(parserType: string): XMLParser | null;
}
