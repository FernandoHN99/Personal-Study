first()
avisarUsuaurio()

function first(){
    if(sessionStorage.getItem("paginaAtual") == null){
        sessionStorage.setItem("paginaAtual", "page00");
        sessionStorage.setItem("conclusaoCurso", "false");
        var dictPages = {
            "page01": false,
            "page02": false,
            "page03": false,
            "page04": false,
        };
        sessionStorage.setItem("dictPages", JSON.stringify(dictPages));
    }
}

function ativarPagina(){
    let paginaAtual = getPaginaAtual()
    let dictPages = getDictPages()
    dictPages[paginaAtual] = true
    sessionStorage.setItem("dictPages", JSON.stringify(dictPages));
    avisarUsuaurio()
}

function avisarUsuaurio() {
    let paginaAtual = getPaginaAtual()
    let dictPages = getDictPages()
    if(paginaAtual != 'page00'){
        let objectMsensagem = document.querySelector(".msg")
        if(dictPages[paginaAtual]){
            objectMsensagem.innerHTML = "Você já viu esse vídeo!!"
        }else{
            objectMsensagem.innerHTML = "Você ainda não viu esse vídeo!!"
        }
    }else if(getConclusaoCurso()){
        let objectMsensagem = document.getElementsByTagName("p")[0]
        objectMsensagem.innerHTML = "<strong>Parabéns!!</strong> Você concluiu todo nosso Curso!"
        objectMsensagem.style.fontSize = "25px"
    }else{
        let objectMsensagem = document.getElementsByTagName("p")[0]
        objectMsensagem.innerHTML = ""
    }
}

function resetar(){
    sessionStorage.clear()
    first()
    avisarUsuaurio()
    console.clear()
}

function concluirCruso(){
    setarPaginaAtual('page00')
    let counter = 0
    let dictPages = getDictPages()
    for (let pagina in dictPages) {
        if(dictPages[pagina]){
            counter++
        }
    }
    if(counter === 4){
        sessionStorage.setItem("conclusaoCurso", "true");
    }
}

function setarPaginaAtual(paginaAtual) {
    sessionStorage.setItem("paginaAtual", paginaAtual);
}

function getPaginaAtual(){
    return sessionStorage.getItem("paginaAtual")
}

function getConclusaoCurso(){
    return sessionStorage.getItem("conclusaoCurso") === "true"
}

function getDictPages(){
    return JSON.parse(sessionStorage.getItem("dictPages"))
}

