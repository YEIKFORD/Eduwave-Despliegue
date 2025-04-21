
function toggleSeleccion(source) {
    const checkboxes = document.getElementsByName('seleccionados');
    for (let i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = source.checked;
    }
}

function alternarMenuFiltros() {
    const menu = document.getElementById("menuFiltros");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

window.addEventListener("click", function(e) {
    const contenedor = document.querySelector(".contenedor-filtros");
    if (!contenedor.contains(e.target)) {
    document.getElementById("menuFiltros").style.display = "none";
    }
});