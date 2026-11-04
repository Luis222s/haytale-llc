# Haytale LLC — Proyecto integrador HTML5

Sitio académico de **tres páginas** que presenta el concepto de un hotel en **Punta Cana, República Dominicana**.

**Estudiante:** Luis Aquino  
**Matrícula:** 2023-0685  
**Tecnologías:** HTML5, CSS3 y JavaScript básico, sin frameworks.

## Páginas del sitio

| Página | Función |
| --- | --- |
| [`index.html`](index.html) | Presentación del hotel, filosofía, lista anidada, imágenes, audio y mapa. |
| [`servicios.html`](servicios.html) | Habitaciones, experiencias, glosario, lista ordenada y tabla de seis servicios. |
| [`contacto.html`](contacto.html) | Datos de contacto de ejemplo, formulario completo y preguntas frecuentes. |

> **Nota:** Haytale LLC se presenta como un concepto de proyecto académico. Los servicios, ilustraciones, correo y teléfono son demostrativos. El formulario valida en el navegador, pero no envía datos a un servidor ni confirma reservas.

## Mapa de etiquetas: nueve familias HTML

| Familia | Etiquetas utilizadas | ¿En qué página? | ¿Por qué se eligieron? |
| --- | --- | --- | --- |
| **1. Documento y metadatos** | `<!DOCTYPE html>`, `html lang="es"`, `head`, `meta charset`, `meta viewport`, `title`, `meta description`, `body` | En las **tres páginas**. | Definen un documento HTML5 válido, el idioma español, la codificación, la adaptación a móviles y metadatos únicos para cada página. |
| **2. Estructura semántica** | `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, `h1`–`h3`, `time datetime`, `address`, `details`, `summary` | Estructura general en las **tres**; `article` en **inicio** y **servicios**; `aside` en **inicio**, **servicios** y **contacto**; `address` en **contacto**. | Organizan las regiones y jerarquías del sitio de forma comprensible para usuarios y tecnologías de asistencia. `time` identifica fechas, `address` muestra contacto y `details` presenta información ampliable. |
| **3. Texto y énfasis** | `p`, `strong`, `em`, `mark`, `abbr`, `small`, `code`, `kbd`, `pre` | **Inicio:** descripción, énfasis y abreviatura; **servicios:** ejemplo preformateado; **contacto:** ayudas del formulario y teclado. | Diferencian importancia, énfasis, contenido resaltado, abreviaturas, notas secundarias, código y entradas de teclado sin depender solo del estilo visual. |
| **4. Citas** | `blockquote`, `cite`, `q` | **Inicio:** cita larga de la filosofía de Haytale y autoría del concepto; **servicios:** cita breve en el texto de exploración. | Distinguen una cita extensa de una frase breve citada y atribuyen la primera a su origen conceptual. |
| **5. Listas** | `ul`, `li`, `ol start`, `ol type`, `dl`, `dt`, `dd` | **Inicio:** itinerario `ol` con una `ul` anidada dentro de su segundo `li`; **servicios:** lista ordenada que empieza en 2 y glosario de tres términos; **tres páginas:** navegación `ul`. | Presentan pasos secuenciales, elementos sin orden y definiciones con la estructura apropiada. |
| **6. Enlaces** | `a href`, `target="_blank"`, `rel="noopener noreferrer"`, `mailto:`, `tel:`, `href="#id"`, `download` | Navegación común en las **tres**; enlace externo y salto interno en **inicio** y **servicios**; contacto `mailto:` y `tel:` en **contacto**; descarga de este README en los **tres pies**. | Facilitan navegación entre páginas, acceso a una sección, sitio externo seguro, correo, llamada y descarga de archivo. |
| **7. Multimedia** | `img alt`, `figure`, `figcaption`, `iframe title`, `audio controls`, `source` | **Inicio:** tarjetas con imágenes dentro de figuras, mapa interactivo y audio local; **servicios:** imágenes descriptivas. | Las imágenes ilustran las experiencias, `alt` explica su contenido, `figcaption` añade contexto, el mapa sitúa la zona y el audio permite escuchar un ambiente simulado con controles. |
| **8. Tablas de datos** | `table`, `caption`, `thead`, `tbody`, `tfoot`, `tr`, `th scope="col"`, `th scope="row"`, `th scope="rowgroup"`, `td`, `rowspan`, `colspan` | **Servicios:** sección “Todo lo que puedes imaginar”. | Compara **seis servicios** en cuatro columnas; `rowspan` agrupa tres filas de alojamiento y tres de experiencias, y `colspan` une las cuatro celdas del resumen final. No se usa para maquetar el sitio. |
| **9. Formularios** | `form`, `fieldset`, `legend`, `label for`, `input`, `select`, `optgroup`, `option`, `textarea`, `button type="submit"`, `output` | **Contacto:** sección “Tu viaje empieza con un mensaje”. | Dos grupos lógicos reúnen datos y preferencias; se emplean nueve tipos de entrada (`text`, `email`, `tel`, `date`, `time`, `number`, `range`, `radio`, `checkbox`), un selector agrupado, comentarios y confirmación local. |

## Verificación de la rúbrica

- [x] Tres archivos con `DOCTYPE`, `lang="es"`, `head`, `body`, `UTF-8`, viewport, títulos y descripciones diferentes.
- [x] Menú con las mismas tres opciones y enlaces entre todas las páginas.
- [x] Un `main` y un `h1` por página, más secciones con encabezados jerárquicos.
- [x] Etiquetas semánticas, `time`, `address`, `details` y `summary`.
- [x] Al menos ocho etiquetas de texto/citas, tres tipos de lista y sublista anidada.
- [x] Cinco tipos de enlace, `alt` descriptivos, `figure`, `figcaption`, `iframe` con `title` y `audio` con `controls` y `source`.
- [x] Tabla de seis filas con `caption`, secciones, cabeceras y combinaciones de celdas.
- [x] Formulario con dos `fieldset`, nueve tipos de entrada, etiquetas asociadas, `select`/`optgroup`, `textarea`, radio, checkbox y botón.
- [x] Validación nativa: `required`, `min`, `max`, `minlength` y `pattern`.
- [ ] Confirmar la validación definitiva en el [validador HTML del W3C](https://validator.w3.org/nu/) después de publicar.
- [ ] Confirmar la publicación y enlazar este repositorio desde GitHub Pages.

## Cómo abrir el proyecto

1. Descarga o clona el repositorio.
2. Abre `index.html` en tu navegador.
3. Navega a las otras páginas desde el menú. Las ilustraciones y el audio son archivos locales; el mapa requiere conexión a internet.

Para validar, visita el [validador Nu HTML del W3C](https://validator.w3.org/nu/), usa la URL pública de cada página y corrige cualquier error que informe. Después de crear el repositorio público en GitHub, activa **Settings → Pages → Deploy from a branch → main / (root)**.

## Créditos

Proyecto integrador de **Luis Aquino**, matrícula **2023-0685**. Ilustraciones SVG y audio ambiental elaborados para este proyecto.
