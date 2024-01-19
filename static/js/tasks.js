var forms= document.querySelector(".tasks__forms");
var task_list = document.querySelector(".tasks__apresentar");


function getTexto(elemento) {
    var texto = elemento.querySelector(".tasks__cards__tarefa").textContent.split(":"); 
    return texto;
}

var campo_de_busca = document.querySelector(".tasks__filtros input");
campo_de_busca.addEventListener("input", function(event){
    var lista_de_tarefas = task_list.querySelectorAll(".tasks__cards");
    lista_de_tarefas.forEach(function(elemento){
        var texto = getTexto(elemento)

        var resultado = texto[1].toUpperCase().match(campo_de_busca.value.toUpperCase());
       
        try {
            for (let index = 0; index < resultado.length; index++) {
                elemento.classList.remove("tasks__cards--remove");
            }
        } catch (error) {
            elemento.classList.add("tasks__cards--remove");
        }       
    })    
})



var select = document.querySelector(".tasks__filtros select");



select.addEventListener("change", function(event){
    var toSort = task_list.getElementsByClassName("tasks__cards");
    toSort = Array.from(toSort);

    //Ordem alfabética (A-Z)
    if(select.value == 0){
        toSort.sort((a, b) => {
            if (a.querySelector(".tasks__cards__tarefa").textContent.split(":")[1].toUpperCase() > b.querySelector(".tasks__cards__tarefa").textContent.split(":")[1].toUpperCase()) return 1;
            if (a.querySelector(".tasks__cards__tarefa").textContent.split(":")[1].toUpperCase() < b.querySelector(".tasks__cards__tarefa").textContent.split(":")[1].toUpperCase()) return -1;
            return 0;
        });
    
        toSort.forEach(function (element) {
            document.querySelector(".tasks__apresentar").appendChild(element);
        })
    }

    //Ordem alfabética (Z-A)
    if(select.value == 1){
        toSort.sort((a, b) => {
            if (a.querySelector(".tasks__cards__tarefa").textContent.split(":")[1].toUpperCase() < b.querySelector(".tasks__cards__tarefa").textContent.split(":")[1].toUpperCase()) return 1;
            if (a.querySelector(".tasks__cards__tarefa").textContent.split(":")[1].toUpperCase() > b.querySelector(".tasks__cards__tarefa").textContent.split(":")[1].toUpperCase()) return -1;
            return 0;
        });
    
        toSort.forEach(function (element) {
            document.querySelector(".tasks__apresentar").appendChild(element);
        })
    }

    //Adicionado mais recentemente
    if(select.value == 2){
        toSort.sort((a, b) => {
            var dataA = a.querySelector(".tasks__cards__dia").textContent.split(":")[1].split("/");
            var HoraA = a.querySelector(".tasks__cards__hora").textContent.replace("Hora: ","").split(":");

            var dataB = b.querySelector(".tasks__cards__dia").textContent.split(":")[1].split("/");
            var HoraB = b.querySelector(".tasks__cards__hora").textContent.replace("Hora: ","").split(":");

            var diaA = new Date(dataA[2], parseInt(dataA[1])-1, dataA[0], HoraA[0], HoraA[1], HoraA[2]);
            var diaB = new Date(dataB[2], parseInt(dataA[1])-1, dataB[0], HoraB[0], HoraB[1], HoraB[2]);

            if (diaA < diaB) return 1;
            if (diaA > diaB) return -1;
            return 0;
        });
    
        toSort.forEach(function (element) {
            document.querySelector(".tasks__apresentar").appendChild(element);
        })
    }

    //Adicionado menos recentemente
    if(select.value == 3){
        toSort.sort((a, b) => {
            var dataA = a.querySelector(".tasks__cards__dia").textContent.split(":")[1].split("/");
            var HoraA = a.querySelector(".tasks__cards__hora").textContent.replace("Hora: ","").split(":");

            var dataB = b.querySelector(".tasks__cards__dia").textContent.split(":")[1].split("/");
            var HoraB = b.querySelector(".tasks__cards__hora").textContent.replace("Hora: ","").split(":");

            var diaA = new Date(dataA[2], parseInt(dataA[1])-1, dataA[0], HoraA[0], HoraA[1], HoraA[2]);
            var diaB = new Date(dataB[2], parseInt(dataA[1])-1, dataB[0], HoraB[0], HoraB[1], HoraB[2]);

            if (diaA > diaB) return 1;
            if (diaA < diaB) return -1;
            return 0;
        });
    
        toSort.forEach(function (element) {
            document.querySelector(".tasks__apresentar").appendChild(element);
        })
    }

})




