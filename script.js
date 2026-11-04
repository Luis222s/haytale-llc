"use strict";

const formulario = document.querySelector("#formulario-contacto");
const controlTranquilidad = document.querySelector("#tranquilidad");
const valorTranquilidad = document.querySelector("#valor-tranquilidad");

if (controlTranquilidad && valorTranquilidad) {
  controlTranquilidad.addEventListener("input", () => {
    valorTranquilidad.value = controlTranquilidad.value;
    valorTranquilidad.textContent = controlTranquilidad.value;
  });
}

if (formulario) {
  formulario.addEventListener("submit", (evento) => {
    evento.preventDefault();
    if (!formulario.reportValidity()) return;

    const estado = document.querySelector("#estado-formulario");
    const nombre = formulario.elements.namedItem("nombre").value.trim();
    estado.textContent = `Gracias, ${nombre}. Tu solicitud de prueba se validó correctamente. No se enviaron ni guardaron datos.`;
    estado.hidden = false;
    estado.scrollIntoView({ behavior: "smooth", block: "nearest" });
    formulario.reset();
    if (valorTranquilidad) {
      valorTranquilidad.value = "3";
      valorTranquilidad.textContent = "3";
    }
  });
}
