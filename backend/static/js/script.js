function getData(){
    // let input = document.getElementById('input').value;

        
    request({
        method: 'GET',
        url: `http://127.0.0.1:5000/get-data`
    }).then(data => {
        let a = JSON.parse(data);
        printTemplate(a);
    }).catch(error => {
        console.log(error);
    })


}

//Funcion para imprimir los datos en la pagina web

function getCount(parent, getChildrensChildren){
    var relevantChildren = 0;
    var children = parent.childNodes.length;
    for(var i=0; i < children; i++){
        if(parent.childNodes[i].nodeType != 3){
            if(getChildrensChildren)
                relevantChildren += getCount(parent.childNodes[i],true);
            relevantChildren++;
        }
    }
    return relevantChildren;
}

function deleteRow(id, data){
    console.log("delete");
    element = document.getElementById(id);
    request({
        method: 'GET',
        url: `http://127.0.0.1:5000/delete-data/${data}`
    }).then(data => {
        let a = JSON.parse(data);
        console.log(a);
    }).catch(error => {
        console.log(error);
    })
    element.parentNode.removeChild(element);
    
}

function printTemplate(data){
    let element = document.getElementById("bodyTable");
    let rows = element.childElementCount;
    console.log(rows);
    console.log(data);
    for(let i = 0; i<data.length; i++){
        element.innerHTML +=    `<tr id='row${i+rows}'>
                                    <th scope='row'>${data[i][0]}</th>
                                    <td>${data[i][1]}</td>
                                    <td>${data[i][2]}</td>
                                    <td>$${data[i][3]}</td>
                                    <td>
                                    <button class="btn btn-primary" >Editar</button>
                                    <button class="btn btn-danger" onclick='deleteRow("row${i+rows}", ${data[i][0]})'>Eliminar</button>
                                    </td>
                                </tr>`
    }
}

window.onload = getData();