
var senha = document.querySelectorAll(".senha");
var mostra = document.querySelectorAll(".mostra");
var esconde = document.querySelectorAll(".esconde");


try {
    function mostrarSenha(){ 
        senha.forEach(elemet =>{
            elemet.type = "text";
        })
        
        mostra.forEach(elemet =>{
            elemet.style.display = "none";
        })
        
        esconde.forEach(elemet =>{
            elemet.style.display = "inline";
        })
    }
    
    function esconderSenha(){
        senha.forEach(elemet =>{
            elemet.type = "password";
        })
        
        mostra.forEach(elemet =>{
            elemet.style.display = "inline";
        })
        
        esconde.forEach(elemet =>{
            elemet.style.display =  "none";
        })

    }

    var mensagem_erro = document.querySelector(".mensagem_erro")

    console.log(senha[0], senha[1]);
    senha[1].addEventListener("input", function(){
        console.log(senha[1].value);
        if (senha[0].value != senha[1].value){
            mensagem_erro.textContent = "Senhas não correspondem!";
        }else{
            mensagem_erro.textContent= "";
        }
    })
    

} catch (error) {
    function mostrarSenha(){ 
        senha[0].type = "text";
        mostra[0].style.display = "none";
        esconde[0].style.display = "inline";
    }
    
    function esconderSenha(){
        senha[0].type = "password";
        mostra[0].style.display = "inline";
        esconde[0].style.display = "none";
    }
}
