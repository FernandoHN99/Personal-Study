export class SingletonLazy {
   private static sc: SingletonLazy;
   private constructor() {}
   public static getInstance(): SingletonLazy {
      if (!SingletonLazy.sc) {
         SingletonLazy.sc = new SingletonLazy();
      }
      return SingletonLazy.sc;
   }
}
