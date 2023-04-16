var btn_add_task = document.querySelector("#btt-add-task");
var new_task_text = document.querySelector("#id-task").value;

btn_add_task.addEventListener('click', function(e){
    console.log(btn_add_task)
    e.preventDefault();
    if(new_task_text){
        add_task();
    }
    // console.log(new_task_text)
    document.querySelector("#id-task").value = '';
});

function add_task(){
    let task_list = document.querySelector("#task-list");

    new_task = cloneTemplate(new_task_text);
    task_list.appendChild(new_task);
    btn_remover = new_task.querySelector(".remove-btn");

    const function_remover = btn_remover.addEventListener("click", function(){
        remove_task(this)
    });


    // Para entender qual objeto o this representa é necessário enxergar qual é o escopo parent que está sendo responsável por invocá-lo.
    // No caso, se eu utilizasse o this dentro da function add_task diretamente, o pai é o escopo onde a funcao está sendo invocada, neste caso seria o próprio escopo global que é o window (maior parent possivel), e portanto o this seria o window.
    // No caso acima pelo fato de o this estar dentro de uma funcao anônima e essa funcao anônima estar sendo invocada pelo botao remover (btn_remover), o this se torna o próprio botao remover.
    // Se eu colocar o remove_task sem estar dentro de uma funcao anonima, é importante observar dois pontos:
    // Primeiro Ponto: se analisarmos somente o ponto do this ele se referiria ao escopo global (window), entao já não é o parent que estamos desejando, entretanto se seguirmos mesmo assim por motivos didáticos, chegamos no segundo ponto que é IMPORTANTE!!
    //Segundo Ponto: Pelo fato da funcao remove_task ter um parametro (neste caso o this, que seria o window mesmo), a funcao não seria invocada ao apertar o botao de remover. Ela seria invocada ao momento que o complidor ler a linha do addEventListener, pois quando se usa event listener nao se pode passar uma funcao com parametro, pois o compilador acha que funcao está sendo invocada naquele instante, então somente se pode passar uma funcao sem parametro quando se tratar do event listener. Ou ainda se quisermos realmente passar uma funcao com parametro no event listener é necessario passsar dentro de uma funcao anonima, que é como tesmos feito até então -> function(){ funcaoQualquer(parametro1, parametro2)});
    // A solucao abaixo exemplifica o paragrafo acima, que repetindo NAO FUNCIONARIA como desejado:

    // ***** FORMA ERRADA ******
    // btn_remover.addEventListener("click", remove_task(this));

    // Uma solição alternativa estaria abaixo, juntamente com FUNCTION OUTRA SOLUÇÃO

    // btn_remover.addEventListener("click", remove_task);

    const function_switch_status = new_task.querySelector(".done-btn").addEventListener("click", function(){
        switch_status(this);
    });

};

function remove_task(task){
    task.parentNode.remove(true);
    // console.log(task)    
}

function switch_status(task){
    // parent_classes = task.parentNode.classList;
    // console.log(parent_classes.length)
    // if(parent_classes.length === 1){
    //     parent_classes.add("done")
    // }else{
    //     parent_classes.remove("done")
    // }
    task.parentNode.classList.toggle("done")
}

// ***** FUNCTION OUTRA SOLUÇÃO ******
// function remove_task(){
//     this.parentNode.remove(true);
//     console.log(this)
// }

function cloneTemplate(){
    let template = document.querySelector(".template");
    new_element = template.cloneNode(true);
    // new_element.className = "task-item";   //outro método de se fazer
    new_element.classList.remove("template");
    new_element.classList.remove("hide");
    new_element.querySelector(".task-title").textContent = new_task_text;
    return new_element;
}


// function create_full_li(new_task_text){
//     let new_li = document.createElement('li')
//     let new_span = document.createElement('span')
//     let new_done_btt = document.createElement('ion-icon')
//     let new_close_btt = document.createElement('ion-icon')

//     new_li.className = "task-item"

//     new_span.className = "task-title"
//     new_span.textContent = `${new_task_text}`

//     new_done_btt.className="done-btn"
//     new_done_btt.name="checkmark-outline"

//     new_close_btt.className="remove-btn"
//     new_close_btt.name="close-outline"

//     new_li.appendChild(new_span)
//     new_li.appendChild(new_done_btt)
//     new_li.appendChild(new_close_btt)
//     return new_li
// }

