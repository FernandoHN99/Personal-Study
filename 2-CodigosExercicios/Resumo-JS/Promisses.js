/*
"Promise" (promessa) é um recurso do JavaScript que permite que o código assíncrono seja executado de forma mais organizada e legível.

Uma "Promise" é um objeto que representa a eventual conclusão (ou falha) de uma operação assíncrona e pode ter um dos seguintes estados:

"pending" (pendente): estado inicial, antes da promessa ser concluída ou rejeitada.
"fulfilled" (concluída): a operação assíncrona foi concluída com sucesso e a promessa é resolvida com um valor.
"rejected" (rejeitada): a operação assíncrona falhou e a promessa é rejeitada com um motivo (um objeto de erro).
Para criar uma "Promise", você pode usar o construtor "Promise". O construtor "Promise" recebe uma função que, por sua vez, recebe duas funções de retorno de chamada: "resolve" e "reject". A função "resolve" é chamada quando a operação assíncrona é concluída com sucesso e a função "reject" é chamada quando ocorre um erro.

Por exemplo, aqui está uma função que retorna uma "Promise" que é resolvida após um atraso de 1 segundo:
*/

function delay(ms) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();
    }, ms);
  });
}

/*A função "delay" recebe um argumento "ms" (milissegundos) e retorna uma "Promise". Dentro do construtor da "Promise", há uma chamada para a função "setTimeout" que é executada após o número especificado de milissegundos. Quando a função "setTimeout" é concluída, a função "resolve" é chamada, o que significa que a promessa foi concluída com sucesso.

A função "resolve" é uma função de retorno de chamada que é passada para o construtor da "Promise". Quando a função "resolve" é chamada, a "Promise" é resolvida com o valor passado como argumento. Por exemplo, se você quiser retornar um valor da "Promise", você pode passá-lo para a função "resolve":
*/

function getUser() {
    return new Promise((resolve, reject) => { //Aqui a promisse é criada com status pending
      // console.log("DEU CERTO"); //Síncrono
      const user = { name: "John", age: 30 };
      resolve(user);
    });
  }

getUser().then(res => console.log(res))

/*
Neste exemplo, a função "getUser" retorna uma "Promise" que é resolvida com um objeto de usuário contendo um nome e idade.

Em resumo, a função "resolve" é uma função de retorno de chamada que é chamada quando uma "Promise" é resolvida com sucesso. Ela pode ser usada para retornar valores de uma "Promise".
*/

//********************** Promisses setadas com estados fulfilled e rejected **********************

// function calculoRapidinho(numero) {
//   return numero >= 0
//     ? Promise.resolve((numero * (numero + 1)) / 2)
//     : Promise.reject("Somente valores positivos, por favor");
// }

function calculoRapidinho(numero) {
  if(numero >= 0){
    // console.log("DEU CERTO"); // Síncrono
    return Promise.resolve((numero * (numero + 1)) / 2); //Aqui a promisse é criada com status fulfilled
  }else{
    // console.log("DEU ERRADO"); // Síncrono
    return Promise.reject("Somente valores positivos, por favor"); //Aqui a promisse é criada com status rejected
  }
}

calculoRapidinho(10)
  .then((resultado) => {
    console.log(resultado);
  })
  .catch((err) => {
    console.log(err);
  });

calculoRapidinho(-1)
  .then((resultado) => {
    console.log(resultado);
  })
  .catch((err) => {
    console.log(err);
  });

console.log("esperando...");
