// ********* Função Padrão *********
function soma_01(a, b=5){ // Forma normal de declaracão | neste caso com parametro b já definido sem não for passado
    return a + b;
}
let retorno = soma_01(1, 2); // Invocar (3)
retorno     = soma_01(1);   // Invocar (5)

// ********* Função Anônima *********
(function(a,b){return a + b}); // Não possuí nome | Necessita de parênteses | Não foi invocada 

// ********* Função Anônima IIFE *********
(function(a,b){return a + b})(1,2);  // Não possuí nome | Necessita de parênteses | Foi invocada 

// ********* Função de Expressão (Function Expression) *********
const soma_02 = function(a,b){return a + b}; // Atribui a funcao a uma variável
retorno = soma_02(1,2); // Invocar

const soma_03 = soma_02; // Cópia da funcao
retorno = soma_03(1,2);  // Invocar a cópia

// ********* Arrow functions *********
// Caso 1:
const soma_04 = (a,b) => {return a+b}; // Atribui a funcao a uma variável | Não possúi a notacao function | Possuí a notacao "=>"| Retorno qdo for simples sem necessidade de chaves (optei por deixar)
retorno = soma_04(1,2);  // Invocar 

// Caso 2:
const incrementa_01 = n => n + 1;  // Único parâmetro, sem necessidade de parenteses | Retorno qdo for simples sem necessidade de chaves
retorno = incrementa_01(1); // Invocar

// Caso 3:
const imprime_01 = () => console.log("Funcao sem parâmetro");  // Sem parâmetro, necessidade de parenteses vazio | Retorno qdo for simples sem necessidade de chaves
imprime_01() // Invocar

// ********* Juntando Arrow functions com Função Anônima IIFE *********

(() => console. log ('Invocando uma função') ) ();

