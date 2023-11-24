let pizarra = document.getElementById('pizarra');
let ctx = pizarra.getContext('2d');
let pintando = false;
let borrando = false;
let grosor = document.getElementById('grosor');
let trazos = [];

function empezarPintar(e) {
    pintando = true;
    trazos.push([{ x: e.clientX - pizarra.getBoundingClientRect().left, y: e.clientY - pizarra.getBoundingClientRect().top }]);
    dibujar(e);
}

function pararPintar() {
    pintando = false;
    ctx.beginPath();
}

function dibujar(e) {
    if (!pintando) return;
    let rect = pizarra.getBoundingClientRect();
    let x = e.clientX - rect.left;
    let y = e.clientY - rect.top;

    ctx.lineWidth = grosor.value;
    ctx.lineCap = 'round';
    ctx.strokeStyle = borrando ? '#FFFFFF' : '#000000';

    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);

    
    trazos[trazos.length - 1].push({ x: x, y: y });
}

function borrarTodo() {
    ctx.clearRect(0, 0, pizarra.width, pizarra.height);
    
    trazos = [];
}

function descargarSVG() {
    
    let svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('width', pizarra.width);
    svg.setAttribute('height', pizarra.height);

    
    for (let i = 0; i < trazos.length; i++) {
        if (trazos[i].length > 1) {
            let path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            let d = trazos[i].map(point => `L${point.x} ${point.y}`).join(' ');
            path.setAttribute('d', `M${trazos[i][0].x} ${trazos[i][0].y} ${d}`);
            path.setAttribute('stroke', borrando ? '#FFFFFF' : '#000000');
            path.setAttribute('stroke-width', grosor.value);
            path.setAttribute('fill', 'none');
            svg.appendChild(path);
        }
    }

    
    let svgString = new XMLSerializer().serializeToString(svg);

    // Crear un enlace de descarga
    let enlaceDescarga = document.createElement('a');
    enlaceDescarga.href = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgString);
    enlaceDescarga.download = 'dibujo.svg';

    
    document.body.appendChild(enlaceDescarga);
    enlaceDescarga.click();
    document.body.removeChild(enlaceDescarga);
}

pizarra.addEventListener('mousedown', empezarPintar);
pizarra.addEventListener('mouseup', pararPintar);
pizarra.addEventListener('mousemove', dibujar);

document.getElementById('pincel').addEventListener('click', function () {
    borrando = false;
});

document.getElementById('goma').addEventListener('click', function () {
    borrando = true;
});

document.getElementById('borrarTodo').addEventListener('click', borrarTodo);
document.getElementById('descargarSVG').addEventListener('click', descargarSVG);


function volverAlIndex() {
    window.location.href = "../startmenu/index.html";
}