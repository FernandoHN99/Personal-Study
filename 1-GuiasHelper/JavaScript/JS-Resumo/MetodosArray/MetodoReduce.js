//Método Reduce

// • A função reduce() reduz os itens de um array com base em uma função.
// • Retona um único valor.
// • Sintaxe: objeto. reduce (função)

// Objetivo do Exercício calcular a média das notas dos alunos

const estudantes = [
    { nome: "José", nota: 5.7 },
    { nome: "Maria", nota: 4.8 },
    { nome: "Paula", nota: 7.5 },
    { nome: "Eustáquio", nota: 6.7 }
]

var x = 1;
const somatorio = (acumulador, valor_atual) => {
    console.log(`${x}: acumulador: ${acumulador}`);
    console.log(`${x}: valor_atual_01:  ${valor_atual}`);
    x++;
    return acumulador+valor_atual};

    // O Reduce já espera RECEBER uma FUNÇÃO que necessita de DOIS parâmetros!!
    // O primeiro e o segundo parâmetro tem comportamentos diferentes dependendo da iteração:
        //Na primeira Iteração:
            // O primeiro parâmetro assume necessariamente o valor do primeiro elemento do array
            // O segundo parâmetro assume necessariamente o valor do segundo elemento array.
        //Na segundo iteração:
            // O primeiro parâmetro assume necessariamente o valor do retorno da função considerando os parâmetros da primeira chamada. 
            // O segundo parâmetro assume necessariamente o valor do terceiro elemento array.
        //Na terceira iteração:
            // O primeiro parâmetro assume necessariamente o valor do retorno da função considerando os parâmetros da segunda chamada. 
            // O segundo parâmetro assume necessariamente o valor do quarto elemento array.
        // Nás próximas interações o comportamento se repete da mesma forma até o reduce chegar o último elemento do array.
    
        //OBS:// Quando uma função passa um terceiro parâmetro o reduce já aloca esse parâmetro representando o indice do elemento daquela iteracao, LEMBRAR: indice começa como 1, pois o valor atual já está no segundo elmento do array.

        //OBS:// Quando uma função passa um 4 parâmetro o reduce já aloca esse parâmetro representando o vetor inteiro

    
let media = estudantes.map(i=>i.nota).reduce(somatorio)/estudantes.length
