fetch("productos.json")
.then(function(response){
    return response.json();
})
.then(function(productos){
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let producto of productos){
        out += `
       
        <tr>
        <td>${producto.nombre}</td>
        <td>${producto.descripcion}</td>
        <td>${producto.precio}</td>
        <td>${producto.disponibilidad}</td>
        </tr>
        `;
    }

    placeholder.innerHTML = out;
})