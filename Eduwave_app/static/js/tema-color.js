const toggleButton = document.getElementById("toggleMode");
const root = document.documentElement;
const logos = document.querySelectorAll(".logoo"); 
const fondo = document.getElementById("contenedor");
const modeIcon = document.getElementById("modeIcon");
const esInicio = document.body.classList.contains("inicio");

let darkMode = localStorage.getItem("modoOscuro") === "true";

function aplicarModoOscuro(activar) {
  if (activar) {
    root.style.setProperty('--color-fondo', '#04324D');
    root.style.setProperty('--color-verde-oscuro', '#00E5FE');
    root.style.setProperty('--color-verde-claro', '#1D93A0');
    root.style.setProperty('--color-titulo-inicio', '#fefefe');
    root.style.setProperty('--color-linea1', '#35BCCA');
    root.style.setProperty('--color-linea2', '#35BCCA');
    root.style.setProperty('--color-texto', '#eee');
    root.style.setProperty('--color-formularios', '#1d93a0de');
    root.style.setProperty('--color-encabezado', '#ffffff33');
    root.style.setProperty('--color-cuadro', '#04324D');
    root.style.setProperty('--color-letra', '#fefefe');
    root.style.setProperty('--color-th-tabla', '#1D93A0');
    root.style.setProperty('--color-fondo-tabla', '#eeeeee24');

    if (esInicio) {
      fondo.style.background = "linear-gradient(#04324d8e,#04324d8e), url('/static/img/fondo_oscuro.png') no-repeat center center/cover";
    } else {
      fondo.style.background = "var(--color-fondo)";
    }

    logos.forEach(logo => {
      logo.src = "/static/img/logo_sena_blanco.png";
    });

    toggleButton.classList.add("dark");
    modeIcon.src = "/static/img/luna.png";
  } else {
    root.style.setProperty('--color-fondo', '#f7f7f7');
    root.style.setProperty('--color-verde-oscuro', '#385C57');
    root.style.setProperty('--color-verde-claro', '#38a900ce');
    root.style.setProperty('--color-titulo-inicio', '#000000c9');
    root.style.setProperty('--color-linea1', '#385C57');
    root.style.setProperty('--color-linea2', '#385c57ad');
    root.style.setProperty('--color-texto', '#353535');
    root.style.setProperty('--color-formularios', '#75b42cd3');
    root.style.setProperty('--color-encabezado', '#ffffff9a');
    root.style.setProperty('--color-cuadro', '#385c57a2');
    root.style.setProperty('--color-letra', '#385C57');
    root.style.setProperty('--color-th-tabla', '#385C57');
    root.style.setProperty('--color-fondo-tabla', '#eee');

    if (esInicio) {
      fondo.style.background = "linear-gradient(#ffffff80, #ffffff80), url('/static/img/fondo_home.jpeg') no-repeat center center/cover";
    } else {
      fondo.style.background = "var(--color-fondo)";
    }

    logos.forEach(logo => {
      logo.src = "/static/img/logo_sena.svg";
    });

    toggleButton.classList.remove("dark");
    modeIcon.src = "/static/img/soleado.png";
  }

  localStorage.setItem("modoOscuro", activar);
}

aplicarModoOscuro(darkMode);

toggleButton.addEventListener("click", () => {
  darkMode = !darkMode;
  aplicarModoOscuro(darkMode);
});
