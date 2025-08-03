function atulizarLayoutHora() {
    var mensagem = window.document.getElementById("id_msg")
    var imagem   = window.document.getElementById("id_img")
    var bodyColor = document.body.style.background
    var horaAtual = new Date().getHours();
    mensagem.innerText = `Agora são ${horaAtual} horas.`
    
    if(horaAtual >= 6 && horaAtual < 12){
        imagem.src = "/images/foto_manha.png"
        bodyColor = "#6eefc0"
    }else if(horaAtual >= 12 && horaAtual < 18){
        imagem.src = "./images/foto_tarde.png"
        bodyColor= "#ff5800e3"
    }else{
        imagem.src = "./images/foto_noite.png"
        bodyColor = "#2a4858"
    }
}

