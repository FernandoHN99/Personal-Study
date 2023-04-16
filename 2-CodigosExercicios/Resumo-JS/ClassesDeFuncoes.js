// ********* Funções de Primeira Classe (First-class function) *********

// São tratadas como uma variável (Já vimos)
const mensagem = ()=> "Olá, "
const saudacao_01 = (nome) => {console.log(mensagem() + nome) }
saudacao_01("Fernando") //Invocar

// Ser passada como argumento para uma função (Exemplo01 e Exemplo02) 
function f(funcao) {
    funcao()
}

// ----- Exemplo 01 -----
f(function(){
    console.log('Estou sendo passada para f') //Funcao ja invocada
})

// ----- Exemplo 02 -----
const saudacao_04 = () => console.log("Olá Mundo!")
f(saudacao_04) //Invocar


// ********* Funções de Classes Mais Altas (Higher-order function) *********

// Ser devolvida por uma função.
function saudacao_03(){
    return function() {
        console. log ("olá mundo!"); 
    }
}

saudacao_03()() //Invocar: método 1
const saudacao_03_Result = saudacao_03() //Invocar: método 2
saudacao_03_Result()

