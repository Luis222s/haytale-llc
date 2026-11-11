"use strict";

// 1. Datos compartidos: los nombres y precios coinciden con la tabla HTML.
const servicios = [
  { nombre: "Habitación Clásica", categoria: "Alojamiento", precio: 4500, descripcion: "Para una o dos personas; tarifa estimada por noche.", imagen: "img/haytale-suite.svg", alt: "Habitación ilustrada con cama doble y balcón" },
  { nombre: "Habitación con Vista", categoria: "Alojamiento", precio: 6800, descripcion: "Descanso con vista al mar; tarifa estimada por noche.", imagen: "img/haytale-resort.svg", alt: "Resort frente al mar con palmeras y piscina" },
  { nombre: "Suite Familiar", categoria: "Alojamiento", precio: 9500, descripcion: "Espacio diseñado para familias; tarifa estimada por noche.", imagen: "img/haytale-suite.svg", alt: "Suite ilustrada con mobiliario y vista exterior" },
  { nombre: "Acceso a Piscina", categoria: "Actividades", precio: 1200, descripcion: "Recreación en la piscina; tarifa estimada por persona.", imagen: "img/haytale-pool.svg", alt: "Piscina de agua azul rodeada de jardines tropicales" },
  { nombre: "Restaurante Caribeño", categoria: "Actividades", precio: 1800, descripcion: "Menú inspirado en la cocina local; tarifa estimada por persona.", imagen: "img/haytale-resort.svg", alt: "Vista del entorno tropical del complejo hotelero" },
  { nombre: "Excursión Punta Cana", categoria: "Actividades", precio: 3200, descripcion: "Recorrido guiado por la zona; tarifa estimada por persona.", imagen: "img/haytale-pool.svg", alt: "Paisaje tropical del área recreativa del hotel" }
];

// 2. Funciones comunes: navegación, tema, año y vuelta arriba.
const botonMenu = document.querySelector(".menu-boton");
const menu = document.querySelector(".navegacion");
if (botonMenu && menu) {
  botonMenu.addEventListener("click", () => {
    const abierto = menu.classList.toggle("abierta");
    botonMenu.setAttribute("aria-expanded", String(abierto));
    botonMenu.setAttribute("aria-label", abierto ? "Cerrar menú" : "Abrir menú");
  });
  menu.querySelectorAll("a").forEach(enlace => enlace.addEventListener("click", () => {
    menu.classList.remove("abierta");
    botonMenu.setAttribute("aria-expanded", "false");
    botonMenu.setAttribute("aria-label", "Abrir menú");
  }));
}

const botonTema = document.querySelector(".tema-boton");
function actualizarBotonTema() {
  if (!botonTema) return;
  const oscuro = document.body.classList.contains("oscuro");
  botonTema.setAttribute("aria-pressed", String(oscuro));
  botonTema.setAttribute("aria-label", oscuro ? "Activar modo claro" : "Activar modo oscuro");
  botonTema.firstChild.textContent = oscuro ? "☀ " : "☾ ";
}
try {
  if (localStorage.getItem("haytale-tema") === "oscuro") document.body.classList.add("oscuro");
} catch { /* El sitio sigue funcionando si el navegador bloquea el almacenamiento. */ }
actualizarBotonTema();
if (botonTema) botonTema.addEventListener("click", () => {
  document.body.classList.toggle("oscuro");
  try { localStorage.setItem("haytale-tema", document.body.classList.contains("oscuro") ? "oscuro" : "claro"); } catch { /* Sin persistencia en modo privado. */ }
  actualizarBotonTema();
});

document.querySelectorAll(".anio").forEach(nodo => { nodo.textContent = String(new Date().getFullYear()); });
const botonArriba = document.querySelector(".volver-arriba");
if (botonArriba) {
  const actualizarArriba = () => botonArriba.classList.toggle("visible", window.scrollY > 330);
  window.addEventListener("scroll", actualizarArriba, { passive: true });
  botonArriba.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  actualizarArriba();
}

// 3. Catálogo dinámico: pintar tarjetas y filtrar el arreglo.
const gridServicios = document.querySelector("#tarjetas-servicios");
const buscarServicio = document.querySelector("#buscar-servicio");
const filtrarCategoria = document.querySelector("#filtrar-categoria");
const contadorServicios = document.querySelector("#contador-servicios");
const sinResultados = document.querySelector("#sin-resultados");
const moneda = valor => valor.toLocaleString("es-DO", { style: "currency", currency: "DOP", maximumFractionDigits: 0 });

function pintarTarjetas(lista) {
  if (!gridServicios) return;
  gridServicios.replaceChildren();
  lista.forEach(servicio => {
    const tarjeta = document.createElement("article");
    tarjeta.className = "tarjeta";
    const imagen = document.createElement("img");
    imagen.src = servicio.imagen;
    imagen.alt = servicio.alt;
    imagen.loading = "lazy";
    imagen.width = 480;
    imagen.height = 300;
    const contenido = document.createElement("div");
    contenido.className = "tarjeta-cuerpo";
    const categoria = document.createElement("span");
    categoria.className = "categoria";
    categoria.textContent = servicio.categoria;
    const titulo = document.createElement("h3");
    titulo.textContent = servicio.nombre;
    const descripcion = document.createElement("p");
    descripcion.textContent = servicio.descripcion;
    const precio = document.createElement("span");
    precio.className = "precio";
    precio.textContent = moneda(servicio.precio);
    contenido.append(categoria, titulo, descripcion, precio);
    tarjeta.append(imagen, contenido);
    gridServicios.append(tarjeta);
  });
  if (contadorServicios) contadorServicios.textContent = `Mostrando ${lista.length} de ${servicios.length} servicios`;
  if (sinResultados) sinResultados.hidden = lista.length !== 0;
}

function filtrarServicios() {
  const texto = (buscarServicio?.value || "").trim().toLocaleLowerCase("es-DO");
  const categoria = filtrarCategoria?.value || "todas";
  const filtrados = servicios.filter(servicio =>
    (categoria === "todas" || servicio.categoria === categoria) &&
    `${servicio.nombre} ${servicio.descripcion} ${servicio.categoria}`.toLocaleLowerCase("es-DO").includes(texto)
  );
  pintarTarjetas(filtrados);
}
if (gridServicios) {
  pintarTarjetas(servicios);
  buscarServicio?.addEventListener("input", filtrarServicios);
  filtrarCategoria?.addEventListener("change", filtrarServicios);
}

// 4. Formulario: validaciones HTML5 y reglas adicionales de negocio.
const formulario = document.querySelector("#solicitud");
if (formulario) {
  const campos = ["nombre", "correo", "confirmar-correo", "telefono", "fecha", "hora", "personas", "habitacion", "motivo", "acepto"];
  const obtener = id => document.getElementById(id);
  const hoyLocal = () => {
    const fecha = new Date();
    const año = fecha.getFullYear();
    const mes = String(fecha.getMonth() + 1).padStart(2, "0");
    const dia = String(fecha.getDate()).padStart(2, "0");
    return `${año}-${mes}-${dia}`;
  };
  const campoFecha = obtener("fecha");
  if (campoFecha) campoFecha.min = hoyLocal();

  function mostrarError(id, mensaje) {
    const campo = obtener(id) || (id === "motivo" ? obtener("descanso") : null);
    const error = obtener(`error-${id}`);
    if (error) error.textContent = mensaje;
    campo?.classList.toggle("invalido", Boolean(mensaje));
    campo?.setAttribute("aria-invalid", String(Boolean(mensaje)));
  }

  function validarCampo(id) {
    const campo = obtener(id);
    let mensaje = "";
    if (id === "motivo") {
      if (!formulario.querySelector('input[name="motivo"]:checked')) mensaje = "Selecciona el motivo del viaje.";
    } else if (id === "acepto") {
      if (!campo.checked) mensaje = "Debes aceptar que es una demostración.";
    } else if (!campo.value.trim()) {
      mensaje = "Este campo es obligatorio.";
    } else if (!campo.checkValidity()) {
      const mensajes = {
        nombre: "Escribe al menos 3 caracteres.", correo: "Introduce un correo válido.",
        "confirmar-correo": "Introduce un correo válido.", telefono: "Introduce un teléfono válido.",
        personas: "Selecciona entre 1 y 12 huéspedes.", habitacion: "Selecciona una habitación."
      };
      mensaje = mensajes[id] || "Revisa el valor de este campo.";
    }
    // Tres reglas propias: prefijos dominicanos, fecha futura y coincidencia de correos.
    if (!mensaje && id === "telefono") {
      const digitos = campo.value.replace(/\D/g, "");
      const numero = digitos.length === 11 && digitos.startsWith("1") ? digitos.slice(1) : digitos;
      if (!/^(809|829|849)\d{7}$/.test(numero)) mensaje = "Escribe 10 dígitos con prefijo 809, 829 u 849.";
    }
    if (!mensaje && id === "fecha" && campo.value < hoyLocal()) mensaje = "La fecha de llegada no puede estar en el pasado.";
    if (!mensaje && id === "confirmar-correo" && campo.value.trim().toLowerCase() !== obtener("correo").value.trim().toLowerCase()) mensaje = "Los correos electrónicos no coinciden.";
    // Cuarta regla propia: máximo dos huéspedes en una habitación Clásica.
    if (!mensaje && id === "personas" && obtener("habitacion").value === "clasica" && Number(campo.value) > 2) mensaje = "La habitación Clásica admite como máximo 2 huéspedes.";
    if (!mensaje && id === "habitacion" && campo.value === "clasica" && Number(obtener("personas").value) > 2) mensaje = "Para más de 2 huéspedes, elige otra habitación.";
    mostrarError(id, mensaje);
    return !mensaje;
  }

  campos.forEach(id => {
    const campo = obtener(id);
    if (!campo) return;
    ["input", "change", "blur"].forEach(tipo => campo.addEventListener(tipo, () => {
      validarCampo(id);
      if (id === "correo" && obtener("confirmar-correo").value) validarCampo("confirmar-correo");
      if (id === "personas" || id === "habitacion") {
        if (obtener("personas").value && obtener("habitacion").value) {
          validarCampo(id === "personas" ? "habitacion" : "personas");
        }
      }
    }));
  });
  obtener("familia")?.addEventListener("change", () => validarCampo("motivo"));

  formulario.addEventListener("submit", evento => {
    evento.preventDefault();
    const correcto = campos.map(validarCampo).every(Boolean);
    const resultado = obtener("resultado");
    resultado.replaceChildren();
    if (!correcto) {
      const primerError = campos.find(id => obtener(`error-${id}`)?.textContent);
      (obtener(primerError) || obtener("descanso"))?.focus();
      return;
    }
    const titulo = document.createElement("strong");
    titulo.textContent = "¡Solicitud de demostración completada!";
    const resumen = document.createElement("p");
    const eleccion = obtener("habitacion");
    resumen.textContent = `${obtener("nombre").value.trim()}, registramos tu consulta de prueba para ${obtener("personas").value} huésped(es) en ${eleccion.options[eleccion.selectedIndex].text}, con llegada el ${obtener("fecha").value} a las ${obtener("hora").value}. Responderíamos a ${obtener("correo").value.trim()}. No se envió información a ningún servidor ni se creó una reserva.`;
    resultado.append(titulo, resumen);
    formulario.reset();
    campos.forEach(id => mostrarError(id, ""));
  });
}
