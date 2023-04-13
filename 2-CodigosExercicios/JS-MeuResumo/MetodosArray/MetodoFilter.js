// Método Filter

// • A função filter () filtra os itens de um array com base em uma função.
// • Retona um array de tamanho <= ao tamanho do array original.
// • Sintaxe: objeto. filter (função)

// Objetivo: Desejamos obter apenas a lista de alunos que obtiveram nota superior a 6

const estudantes = [
    { nome: "José", nota: 5.7 },
    { nome: "Maria", nota: 4.8 },
    { nome: "Paula", nota: 7.5 },
    { nome: "Eustáquio", nota: 6.7 }
];

const estudantes_backup = JSON.parse(JSON.stringify(estudantes)); //se quiser copiar o array como Deep!

const aprovado = i => { if(i.nota > 6){return i}};

var maior_nota = Math.max(...estudantes.map(i=> i.nota)); // pega maior nota
let novas_notas = estudantes.map(i => i.nota).map(n => n*10/maior_nota.toFixed(2)); //cria array com novas notas
estudantes.map((i,indice) => i.nota= parseFloat(novas_notas[indice])); // atualiza o array de estudantes com a novas notas

//Opção mais simplificada:
// - já altero os estudantes original
// - já crio o array de novas_notas 
// let novas_notas = estudantes.map(n => n.nota = n.nota*10/maior_nota.toFixed(2)); 

//Filter -> Parametros:
    // 1-> item
    // 2-> indice
    // 3-> vetor inteiro

console.log(estudantes_backup.filter(aprovado))     //Sem a normalização das notas (somente 2)
console.log(estudantes.filter(aprovado))            //Com a normalização das notas (todos)
// console.log(estudantes.filter(i => i.nota > 6)) // Sem necessidade de fazer a função





