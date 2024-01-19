var menu = document.querySelector(".menu-dropdown");
var botao_menu = document.querySelector(".btn-dropdown");

botao_menu.addEventListener("click", function(){
    menu.classList.toggle("menu-dropdown--ativo");
})



var texto = document.querySelector(".message__texto");
var mensagem = document.querySelector(".message")
var btn_message = document.querySelector('.message__spam');

if (texto == null){
    mensagem.classList.add("message-off");
}else{
    mensagem.classList.remove("message-off");
    btn_message.addEventListener("click", function(){
        mensagem.classList.add("message-off");
    })
}






var itens = document.querySelectorAll(".cabecalho__item");

if(window.location.href == 'http://192.168.0.103:5000/'){
    itens[0].classList.add('active');
}else{
    if(window.location.href == 'http://192.168.0.103:5000/tarefas'){
    itens[1].classList.add('active');
    }
}

var usuario = document.querySelector(".usuario_logado");
var cabecalho_btns = document.querySelector(".cabecalho__btns");
var avatar = document.querySelector(".avatar-ico");
var divisor = document.querySelectorAll(".divisor--usuario-logado");

if (usuario.textContent != "None"){
    cabecalho_btns.classList.remove("cabecalho__btns");
    cabecalho_btns.classList.add("cabecalho__btns--usuario-logado");
    menu.classList.add('menu-dropdown--usuario-logado')
    
    divisor.forEach(element => {
        element.classList.remove('divisor--usuario-logado');
    });
}else{

    avatar.classList.add("avatar-ico--usuario-deslogado");

    itens[2].style.display = "none";
    itens[3].style.display = "none";
}

