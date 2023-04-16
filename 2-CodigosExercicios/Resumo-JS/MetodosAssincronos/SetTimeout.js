//Funcionamenot do timeout, a contagem eh iniciada ao compilador passar pela função que o invoca. ENTRETANTO se o tempo setado nele for menor do que o tempo de execução do escopo global, ele será enfileirado por último, sim é uma proproedade estranha!!
setTimeout(function(){
    console.log('dentro da timeout')
    },20) //Demora 20 Milisegundos, porem escopo do timeout. Virá Depois do escopo global e depois do Timeout de baixo 

setTimeout(function(){
        console.log('dentro da timeout2')
        },10) //Demora 10 Milisegundos, porem escopo do timeout. Virá Depois do escopo global porem antes do Timeout de cima 

const a = new Date().getTime() + 3000 //Demora 3 segundos, porem escopo global. Irá vir antes de qualquer Timeout
while (new Date().getTime() <= a);
console.log('fora da timeout')