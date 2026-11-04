document.querySelector("#solicitud")?.addEventListener("submit", function (evento) {
  evento.preventDefault();
  document.querySelector("#resultado").textContent = "Formulario validado. No se enviaron datos ni se creó una reserva.";
  this.reset();
});
