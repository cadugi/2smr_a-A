    // Función para validar números
    function validarNumero(input) {
        input.value = input.value.replace(/[^0-9.]/g, '');
        var puntos = input.value.split('.').length - 1;
        if (puntos > 1) {
            input.value = input.value.slice(0, -1);
        }
    }

    // Función para guardar datos
    function guardarDatos() {
        var tabla = document.querySelector('table');
        var datos = [];

        // Recorre las filas y celdas y guarda los datos en un array
        for (var i = 1; i < tabla.rows.length; i++) {
            var fila = tabla.rows[i];
            var filaDatos = [];

            for (var j = 1; j < fila.cells.length; j++) {
                var celda = fila.cells[j];
                filaDatos.push(celda.querySelector('input').value);
            }

            datos.push(filaDatos);
        }

        // Convierte el array a JSON y guarda en localStorage
        localStorage.setItem('datosGuardados', JSON.stringify(datos));
        alert('Datos guardados con éxito.');
    }

    // Función para cargar datos al cargar la página
    window.onload = function () {
        var datosGuardados = localStorage.getItem('datosGuardados');

        if (datosGuardados) {
            datosGuardados = JSON.parse(datosGuardados);

            var tabla = document.querySelector('table');

            for (var i = 0; i < datosGuardados.length; i++) {
                var filaDatos = datosGuardados[i];
                var fila = tabla.rows[i + 1];

                for (var j = 0; j < filaDatos.length; j++) {
                    var celda = fila.cells[j + 1];
                    celda.querySelector('input').value = filaDatos[j];
                }
            }
        }
    };


    function guardarComoPDF() {
        var element = document.querySelector('table');
    
        var options = {
            margin: 10,
            filename: 'tabla_notas.pdf',
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { scale: 2 },
            jsPDF: { unit: 'mm', format: 'a4', orientation: 'landscape' }
        };
    
        html2pdf(element, options);
    }

