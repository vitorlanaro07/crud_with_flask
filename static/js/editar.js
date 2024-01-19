

function editarTask(id) {
    var tarefa = document.querySelector(".input-edit");
    var desc = document.querySelector(".span-edit");
    var botao_salvar = document.querySelector(".botao-salvar button");

    tarefa.disabled = false;
    desc.disabled = false;
    botao_salvar.disabled = false;
}

var itens = document.querySelectorAll(".cabecalho__item");
itens[1].classList.add('active');
