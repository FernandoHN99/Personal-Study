export class SingletonEager {
   private static sc: SingletonEager = new SingletonEager();
   private constructor() {}
   public static getInstance(): SingletonEager {
      return SingletonEager.sc;
   }
}
