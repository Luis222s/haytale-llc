# Haytale LLC — Punta Cana

Sitio académico de un hotel conceptual en Punta Cana, República Dominicana. Esta segunda etapa incorpora un diseño **Caribe Premium** con CSS3 adaptable y comportamiento con JavaScript puro. Los servicios, precios, contactos y solicitudes son simulaciones educativas: el hotel no recibe reservas reales.

**Sitio publicado:** https://luis222s.github.io/haytale-llc/

**Repositorio:** https://github.com/Luis222s/haytale-llc

**Autor:** Luis Aquino · Matrícula 2023-0685

## Capturas

Las capturas de escritorio y móvil se incorporarán a `docs/capturas/` cuando se complete la revisión visual.

**Documentación técnica:** [Descargar PDF](docs/documentacion.pdf) (7 páginas, elaborado a partir de la rúbrica de la práctica).

## Mapa de etiquetas: nueve familias

| Familia | Página y sección | Etiquetas usadas | ¿Por qué esa etiqueta? |
| --- | --- | --- | --- |
| Cimientos | Las tres, documento | `DOCTYPE`, `html`, `head`, `meta`, `title`, `body` | Identifican documento, idioma y adaptación a cada pantalla. |
| Semántica | Todas, estructura; contacto, datos | `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, `time`, `address`, `details`, `summary` | Dan significado a cada región sin depender de su aspecto. |
| Texto | Inicio, servicios, contacto | `strong`, `em`, `mark`, `abbr`, `small`, `code`, `kbd`, `pre` | Diferencian énfasis, abreviaturas y ejemplos. |
| Citas | Inicio y servicios | `blockquote`, `cite`, `q` | Distinguen frases citadas y citas completas. |
| Listas | Inicio y servicios | `ul`, `ol`, `li`, `dl`, `dt`, `dd` | Organizan experiencias, pasos y definiciones hoteleras. |
| Enlaces | Todas, navegación y datos | `a`, `mailto:`, `tel:`, `#id`, `download`, `target`, `rel` | Permiten navegar, contactar, consultar fuentes y descargar. |
| Multimedia | Inicio y servicios | `img`, `figure`, `figcaption`, `iframe`, `audio`, `source` | Presentan imágenes, mapa y sonido ambiental. |
| Tabla | Servicios, tarifas | `table`, `caption`, `thead`, `tbody`, `tfoot`, `th`, `td`, `rowspan`, `colspan` | Comparan seis servicios y sus tarifas estimadas. |
| Formulario | Contacto, solicitud | `form`, `fieldset`, `legend`, `label`, `input`, `select`, `optgroup`, `textarea`, `button` | Recogen datos de ejemplo con campos asociados y validaciones. |

## Funcionalidades de JavaScript

| Funcionalidad | Página | Evento | Función principal |
| --- | --- | --- | --- |
| Menú hamburguesa accesible | Las tres | `click` | `classList.toggle()` y actualización de `aria-expanded` |
| Modo oscuro persistente | Las tres | `click` | `actualizarBotonTema()`, `localStorage` |
| Año automático | Las tres | Carga | `new Date().getFullYear()` |
| Volver arriba | Las tres | `scroll`, `click` | `actualizarArriba()` |
| Seis tarjetas | Servicios | Carga | `pintarTarjetas()` |
| Búsqueda y categorías | Servicios | `input`, `change` | `filtrarServicios()` con `filter()` |
| Precios en DOP | Servicios | Renderizado | `toLocaleString("es-DO", …)` |
| Validación bajo los campos | Contacto | `submit`, `input`, `blur` | `validarCampo()`, `mostrarError()` |
| Confirmación local y limpieza | Contacto | `submit` | Listener de `#solicitud`, `reset()` |

### Reglas propias del formulario

- Teléfono de diez dígitos con prefijo 809, 829 u 849 (se admite `+1` opcional).
- Fecha de llegada no anterior a hoy.
- Confirmación de correo idéntica al correo principal.
- Máximo dos huéspedes en habitación Clásica.

## Estructura

```text
index.html
servicios.html
contacto.html
css/estilos.css
js/app.js
assets/                imágenes y audio
docs/                  PDF y capturas finales
README.md
```

## Cómo ejecutarlo

Abrir `index.html` con Live Server o visitar el sitio publicado. El formulario no envía ni almacena datos en un servidor.

## Pendiente para la entrega

- Comprobar los tres HTML en https://validator.w3.org/ y CSS en https://jigsaw.w3.org/css-validator/.
- Generar capturas de escritorio y móvil verificadas dentro de `docs/capturas/`.
- Crear `docs/documentacion.pdf` conforme a la guía del docente, aún no facilitada.
- Publicar y comprobar las tres rutas de GitHub Pages.
- Conservar un historial de diez commits auténticos, claros y descriptivos.
