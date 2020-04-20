function getData(search){
    let input = document.getElementById('input').value;
    if(input === ''){
        return false;
    }
    if(search === 1){
        
        fetch(`http://127.0.0.1:5000/get-code/${input}`)
        .then(res => res.json())
        .then(data =>{
            printTemplate(data);
        });
    }else if(search === 2){
        fetch(`http://127.0.0.1:5000/get-city/${input}`)
        .then(res => res.json())
        .then(data => {
            printTemplate(data)
        });
    }
}

//Funcion para imprimir los datos en la pagina web
function printTemplate(data){
    let element = document.getElementById("data");
    element.innerHTML = ''
    for(let i = 0; i<data.length; i++){
        element.innerHTML += `<p> ${data[i]} <p>`
    }
}