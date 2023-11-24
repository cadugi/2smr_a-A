
window.onload = function () {
    mostrarArchivosGuardados();
};



function mostrarArchivosGuardados() {
    var listaArchivos = document.getElementById('listaArchivos');

    // Recupera los nombres de los archivos desde el localStorage
    var archivos = Object.keys(localStorage);

    archivos.forEach(function (fileName) {
        var listItem = document.createElement('li');
        var link = document.createElement('a');
        link.href = '#';
        link.textContent = fileName;
        link.onclick = function () {
            descargarArchivo(fileName);
        };

        listItem.appendChild(link);
        listaArchivos.appendChild(listItem);
    });
}

function subirArchivo() {
    var input = document.getElementById('fileInput');
    var file = input.files[0];

    if (file) {
        var fileName = file.name;
        var listaArchivos = document.getElementById('listaArchivos');

        var listItem = document.createElement('li');

        // En lugar de crear el enlace aquí, crearemos el contenedor del texto y el enlace
        var textContainer = document.createElement('span');
        textContainer.textContent = fileName;

        var link = document.createElement('a');
        link.href = '#';
        link.textContent = '❌';
        link.style.cursor = 'pointer';
        link.onclick = function () {
            borrarArchivo(fileName);
        };

        listItem.appendChild(textContainer);
        listItem.appendChild(link);

        listaArchivos.appendChild(listItem);

        // Guardar el archivo en el almacenamiento local
        var reader = new FileReader();
        reader.onload = function (e) {
            localStorage.setItem(fileName, e.target.result);
        };
        reader.readAsDataURL(file);
    } else {
        alert('Selecciona un archivo para subir.');
    }
}

function descargarArchivo(fileName) {
    var fileData = localStorage.getItem(fileName);

    if (fileData) {
        var byteCharacters = atob(fileData.split(',')[1]);
        var byteNumbers = new Array(byteCharacters.length);

        for (var i = 0; i < byteCharacters.length; i++) {
            byteNumbers[i] = byteCharacters.charCodeAt(i);
        }

        var byteArray = new Uint8Array(byteNumbers);
        var blob = new Blob([byteArray], { type: 'application/octet-stream' });

        var link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = fileName;
        link.click();
    } else {
        alert('No se pudo encontrar el archivo.');
    }
}

window.onload = function () {
    mostrarArchivosGuardados();
};

function mostrarArchivosGuardados() {
    var listaArchivos = document.getElementById('listaArchivos');

    // Recupera los nombres de los archivos desde el localStorage
    var archivos = Object.keys(localStorage);

    archivos.forEach(function (fileName) {
        var listItem = document.createElement('li');
        var link = document.createElement('a');
        link.href = '#';
        link.textContent = fileName;
        link.onclick = function () {
            descargarArchivo(fileName);
        };

        var deleteButton = document.createElement('span');
        deleteButton.textContent = ' ❌';
        deleteButton.style.cursor = 'pointer';
        deleteButton.onclick = function () {
            borrarArchivo(fileName);
        };

        listItem.appendChild(link);
        listItem.appendChild(deleteButton);
        listaArchivos.appendChild(listItem);
    });
}

document.body.insertAdjacentHTML(
    'beforeend',
    '<button onclick="ordenarAlfabeticamente()">Ordenar Alfabéticamente</button>' +
    '<button onclick="ordenarAscendente()">Ordenar Ascendente</button>' +
    '<button onclick="ordenarDescendente()">Ordenar Descendente</button>'
);

function mostrarArchivosGuardados() {
    var listaArchivos = document.getElementById('listaArchivos');
    listaArchivos.innerHTML = ''; // Limpia la lista antes de mostrarla nuevamente

    // Recupera los nombres de los archivos desde el localStorage
    var archivos = Object.keys(localStorage);

    archivos.forEach(function (fileName) {
        var listItem = document.createElement('li');
        var link = document.createElement('a');
        link.href = '#';
        link.textContent = fileName;
        link.onclick = function () {
            descargarArchivo(fileName);
        };

        var deleteButton = document.createElement('span');
        deleteButton.textContent = ' ❌';
        deleteButton.style.cursor = 'pointer';
        deleteButton.onclick = function () {
            borrarArchivo(fileName);
        };

        listItem.appendChild(link);
        listItem.appendChild(deleteButton);
        listaArchivos.appendChild(listItem);
    });
}

function ordenarAlfabeticamente() {
    mostrarArchivosGuardados();
    var listaArchivos = document.getElementById('listaArchivos');
    Array.from(listaArchivos.children)
        .sort((a, b) => a.firstChild.textContent.localeCompare(b.firstChild.textContent))
        .forEach(item => listaArchivos.appendChild(item));
}

function ordenarAscendente() {
    mostrarArchivosGuardados();
    var listaArchivos = document.getElementById('listaArchivos');
    Array.from(listaArchivos.children)
        .sort((a, b) => a.firstChild.textContent.localeCompare(b.firstChild.textContent))
        .reverse()
        .forEach(item => listaArchivos.appendChild(item));
}

function ordenarDescendente() {
    mostrarArchivosGuardados();
    var listaArchivos = document.getElementById('listaArchivos');
    Array.from(listaArchivos.children)
        .sort((a, b) => a.firstChild.textContent.localeCompare(b.firstChild.textContent))
        .forEach(item => listaArchivos.appendChild(item));
}

function borrarArchivo(fileName) {
    // Eliminar el archivo de la lista y del localStorage
    var listaArchivos = document.getElementById('listaArchivos');
    var listItem = Array.from(listaArchivos.children).find(function (item) {
        return item.firstChild.textContent === fileName;
    });

    if (listItem) {
        listaArchivos.removeChild(listItem);
        localStorage.removeItem(fileName);
    }
}

