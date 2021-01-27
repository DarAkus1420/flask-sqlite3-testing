let data;

function getData(){
    // let input = document.getElementById('input').value;

        
    request({
        method: 'GET',
        url: `http://127.0.0.1:5000/get-data`
    }).then(data => {
        let dbData = JSON.parse(data);
        printTemplate(dbData);
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

    

    element = document.getElementById(id);
    request({
        method: 'GET',
        url: `http://127.0.0.1:5000/delete-data/${data}`
    }).then(data => {
        let a = JSON.parse(data);
        console.log(a + "a");
    }).catch(error => {
        console.log(error);
    })
    element.parentNode.removeChild(element);
    
}

function hideButton(button){

    if(button == "submit"){
        element = document.getElementById('submitButton');
        element.style.display = "block";
        element = document.getElementById('updateButton');
        element.style.display = 'none'
        element = document.getElementById('codigoForm');
        element.style.display = "block";
    } else if (button == 'update'){
        element = document.getElementById('updateButton');
        element.style.display = "block"
        element = document.getElementById('submitButton');
        element.style.display = "none";
        element = document.getElementById('codigoForm');
        element.style.display = "none";
    }

    
}

function datoActual(id){
    data = id;
    console.log(data);
}


function updateRow(){

    let code = document.getElementById('code').value;
    let name = document.getElementById('name').value;
    let city = document.getElementById('city').value;
    let debt = document.getElementById('debt').value;



    request({
        method: 'POST',
        url: `http://127.0.0.1:5000/update-data`,
        body: JSON.stringify({
            'code':code,
            'name':name,
            'city':city,
            'debt':debt,
            'actualCode': data
        }),
        
    }).then(data => {
        console.log(data);
        hideButton("Submit");
        getData();
    }).catch(error => {
        console.log(error);
    })

    
}

function submitData(){

    let code = document.getElementById('code').value;
    let name = document.getElementById('name').value;
    let city = document.getElementById('city').value;
    let debt = document.getElementById('debt').value;



    request({
        method: 'POST',
        url: `http://127.0.0.1:5000/create-data`,
        body: JSON.stringify({
            'code':code,
            'name':name,
            'city':city,
            'debt':debt
        }),
        
    }).then(data => {
        console.log(data);
        getData();
    }).catch(error => {
        console.log(error);
    })
}

function printTemplate(data){
    let element = document.getElementById("bodyTable");
    element.innerHTML = '';
    let rows = element.childElementCount;
    for(let i = 0; i<data.length; i++){
        element.innerHTML +=    `<tr id='row${i+rows}'>
                                    <th scope='row'>${data[i][0]}</th>
                                    <td>${data[i][1]}</td>
                                    <td>${data[i][2]}</td>
                                    <td>$${data[i][3]}</td>
                                    <td>
                                    <a href="#ventana1" class="btn btn-primary" data-toggle='modal' onclick="hideButton('update');datoActual(${data[i][0]})">Editar</a>
                                    <button class="btn btn-danger" onclick='deleteRow("row${i+rows}", ${data[i][0]})'>Eliminar</button>
                                    </td>
                                </tr>`
    }
}

window.onload = getData();