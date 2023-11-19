import { XMLParser } from "./XMLParser";
export abstract class DisplayService {
   public display(): void {
      const parser: XMLParser = this.getParser();
      const msg: string = parser.parse();
      console.log(msg);
   }
   public abstract getParser(): XMLParser;
}
