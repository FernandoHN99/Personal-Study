// ********* Caso 01 ********* 
// O operador spread em JavaScript é representado por três pontos consecutivos ... e serve para expandir elementos de um array ou propriedades de um objeto em outro contexto

//Array
const array1 = [1, 2, 3];
const array2 = [...array1, 4, 5, 6];
console.log(array2); // [1, 2, 3, 4, 5, 6]

//Objeto
const objeto1 = {a: 1, b: 2, c: 3};
const objeto2 = {...objeto1, d: 4, e: 5};
console.log(objeto2); // {a: 1, b: 2, c: 3, d: 4, e: 5}


// ********* Caso 02 ********* 
// O operador spread também pode ser utilizado em outras situações, como em parâmetros de funções para passar múltiplos argumentos.

// Exemplo 01:
// Nesse exemplo, a função soma recebe três argumentos a, b e c. Em vez de passá-los separadamente, criamos um array numeros com os valores [1, 2, 3] e utilizamos o operador spread ... para expandir o array na chamada da função soma. O resultado é a soma dos números 1 + 2 + 3, que é igual a 6.

function soma(a, b, c) {
    return a + b + c;
  }
  
  const numeros = [1, 2, 3];
  const resultado = soma(...numeros);
  console.log(resultado); // 6


// Exemplo 02:

function logNumeros2(...nums){
    for(let n of nums) {
        console.log(n)
    }
}
logNumeros2(1,2,3,4,5,6,7);
  
  
