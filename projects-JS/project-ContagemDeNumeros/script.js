function contar(){
    let inicio = document.getElementById("inicio");
    let fim = document.getElementById("fim");
    let passo = document.getElementById("passo");
    let mensagem = document.getElementById("msg");

    if(inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0){
        mensagem.innerText = "Impossível contar!";
        // resultado.innerText = "";
    }else{
        mensagem.innerText = "Contando: \n"; //ou <br> se fosse em innerHTML
        let numberInicio = Number(inicio.value)
        let numberFim  = Number(fim.value);
        let numberPasso;
        
        if(Number(passo.value) <= 0){
            numberPasso = 1 
            window.alert("Passo Inválido! Considerando PASSO igual a 1");
        }else{
            numberPasso = Number(passo.value);
        }

        if(numberInicio <= numberFim){
            for(let i = numberInicio; i <= numberFim; i+=numberPasso){
                mensagem.innerText+= `${i} 👉🏼 `;
            }
        }else{
            console.log("ENTROU")
            for(let i = numberInicio; i >= numberFim; i-=numberPasso){
                mensagem.innerText+= `${i} 👉🏼 `;
            }
        }
        mensagem.innerText += " \u{1F3C1}"; //forma diferente colocar emoji

    }
}