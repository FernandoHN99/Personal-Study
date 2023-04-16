//Método map

// • A função map () mapeia cada item de um array a uma determinada função.
// • Retona um array de mesmo tamanho com valores transformados pela função.
// • Sintaxe: objeto. map (função, índice)


// Objetivo do Exercício Ajustar as notas dos alunos com uma formula qualquer

const estudantes = [
    { nome: "José", nota: 5.7 },
    { nome: "Maria", nota: 4.8 },
    { nome: "Paula", nota: 7.5 },
    { nome: "Eustáquio", nota: 6.7 }
]

// ------------------- Forma 01: Mais Separada------------------------------
const normaliza = (n,i) => {
    console.log(n)
    console.log(i)
    return n*10/maior_nota.toFixed(2)
}

let notas = []
for(let i of estudantes){ notas.push(i.nota) } //cria lista de notas 

var maior_nota = Math.max(...notas)
console.log(maior_nota)

// Funcionamento do map:
// O map ja espepra receber uma funcao que utiliza pelo menos um parâmetro qualquer, no qual esse primeiro parâmetro  representa  cada item do array, em cada iteração (OBS: Forma bem automática, por trás dos panos)
// Quando uma função passa o segundo parâmetro o map já aloca esse parâmetro representando o indice do elemento daquela iteracao.
var notas_normalizadas = notas.map(normaliza) 
console.log(notas_normalizadas)


// ------------------- Forma 02: Mais Reduzida------------------------------

var maior_nota = Math.max(...estudantes.map(i=> i.nota))
console.log(maior_nota)

var notas_normalizadas = estudantes.map(
    (estudante) => (estudante.nota*10/maior_nota).toFixed(2) 
)
console.log(notas_normalizadas)
    
    