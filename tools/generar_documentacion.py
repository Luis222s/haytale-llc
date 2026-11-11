"""Construye el PDF técnico de Haytale LLC con ReportLab.

Uso: python3 tools/generar_documentacion.py
Se genera docs/documentacion.pdf sin depender de recursos externos.
"""

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table,
    TableStyle, PageBreak, KeepTogether, Flowable
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "documentacion.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

INK = colors.HexColor("#183B42")
MUTED = colors.HexColor("#55747A")
TEAL = colors.HexColor("#087F83")
PALE = colors.HexColor("#EAF5F3")
GOLD = colors.HexColor("#BF9454")
LIGHT = colors.HexColor("#F6FAF9")
LINE = colors.HexColor("#D7E7E6")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverSmallH", fontName="DejaVu-Bold", fontSize=10, leading=16, textColor=TEAL, alignment=TA_CENTER, spaceAfter=18))
styles.add(ParagraphStyle(name="CoverTitleH", fontName="DejaVu-Bold", fontSize=34, leading=42, textColor=INK, alignment=TA_CENTER, spaceAfter=12))
styles.add(ParagraphStyle(name="CoverSubH", fontName="DejaVu", fontSize=15, leading=23, textColor=MUTED, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="TitleH", fontName="DejaVu-Bold", fontSize=19, leading=26, textColor=INK, spaceAfter=14))
styles.add(ParagraphStyle(name="SubtitleH", fontName="DejaVu-Bold", fontSize=12, leading=18, textColor=TEAL, spaceBefore=13, spaceAfter=7))
styles.add(ParagraphStyle(name="BodyH", fontName="DejaVu", fontSize=9.1, leading=15, textColor=INK, spaceAfter=9))
styles.add(ParagraphStyle(name="MutedH", fontName="DejaVu", fontSize=8.2, leading=13, textColor=MUTED, spaceAfter=8))
styles.add(ParagraphStyle(name="CalloutH", fontName="DejaVu-Bold", fontSize=10.2, leading=17, textColor=TEAL, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="CellH", fontName="DejaVu", fontSize=7.5, leading=11.7, textColor=INK))
styles.add(ParagraphStyle(name="CellHeaderH", fontName="DejaVu-Bold", fontSize=7.5, leading=11.7, textColor=colors.white))
styles.add(ParagraphStyle(name="BulletH", fontName="DejaVu", fontSize=9.1, leading=15, textColor=INK, leftIndent=15, firstLineIndent=-9, spaceAfter=5))

P = lambda text, name="BodyH": Paragraph(text, styles[name])


class WaveArt(Flowable):
    def __init__(self, width=450, height=150):
        super().__init__()
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        c.setFillColor(PALE)
        c.roundRect(0, 0, self.width, self.height, 16, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#C0ECE7"))
        c.circle(self.width - 66, self.height - 43, 28, stroke=0, fill=1)
        c.setStrokeColor(colors.HexColor("#56B8B7"))
        c.setLineWidth(3)
        for y, offset in ((46, 0), (34, 22), (22, -3)):
            p = c.beginPath()
            p.moveTo(20, y)
            p.curveTo(110, y + 35, 170, y - 40, 240 + offset, y)
            p.curveTo(320, y + 30, 365, y - 18, self.width - 18, y + 4)
            c.drawPath(p)
        c.setFillColor(TEAL)
        c.setFont("DejaVu-Bold", 15)
        c.drawCentredString(self.width / 2, 102, "HAYTALE  LLC")
        c.setFont("DejaVu", 8.5)
        c.drawCentredString(self.width / 2, 83, "Caribe Premium  |  Punta Cana")


def tabla(headers, rows, widths, fontsize=7.5):
    data = [[P(str(value), "CellHeaderH") for value in headers]]
    data += [[P(str(value), "CellH") for value in row] for row in rows]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TEAL),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -1), .35, LINE),
    ]))
    return t


def bullet(text):
    return P("• " + text, "BulletH")


def page(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(TEAL)
    canvas.rect(0, h - 13, w, 13, fill=1, stroke=0)
    canvas.setStrokeColor(LINE)
    canvas.line(2.1 * cm, 1.65 * cm, w - 2.1 * cm, 1.65 * cm)
    canvas.setFont("DejaVu", 7.3)
    canvas.setFillColor(MUTED)
    canvas.drawString(2.1 * cm, 1.25 * cm, "HAYTALE LLC  |  DOCUMENTACIÓN TÉCNICA")
    canvas.drawRightString(w - 2.1 * cm, 1.25 * cm, f"Página {doc.page}")
    canvas.restoreState()


doc = BaseDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=2.1*cm, rightMargin=2.1*cm,
                      topMargin=2.25*cm, bottomMargin=2.0*cm, title="Haytale LLC - Documentación técnica",
                      author="Luis Aquino (2023-0685)")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, leftPadding=0, rightPadding=0,
              topPadding=0, bottomPadding=0)
doc.addPageTemplates(PageTemplate(id="normal", frames=[frame], onPage=page))
width = doc.width
story = []

# 1. Portada
story += [Spacer(1, 2.1*cm), P("PROYECTO INTEGRADOR · HTML5 + CSS3 + JAVASCRIPT", "CoverSmallH"),
          P("Haytale LLC", "CoverTitleH"),
          P("Diseño Caribe Premium y experiencia interactiva", "CoverSubH"),
          Spacer(1, 1.25*cm), WaveArt(width, 160), Spacer(1, 1.1*cm),
          P("DOCUMENTACIÓN TÉCNICA DEL SITIO WEB", "CalloutH"), Spacer(1, .6*cm),
          P("<b>Estudiante:</b> Luis Aquino"), P("<b>Matrícula:</b> 2023-0685"),
          P("<b>Proyecto:</b> Hotel conceptual en Punta Cana, República Dominicana"),
          P("<b>Fecha:</b> noviembre de 2026"),
          P("<b>Repositorio:</b> github.com/Luis222s/haytale-llc", "MutedH"),
          P("<b>Publicación:</b> luis222s.github.io/haytale-llc/", "MutedH"),
          PageBreak()]

# 2. Alcance
story += [P("1. Presentación del proyecto", "TitleH"),
          P("Haytale LLC es una propuesta de hotel turístico ubicada de forma conceptual en Punta Cana. La página permite conocer el alojamiento, comparar experiencias y completar una solicitud de ejemplo. No representa un negocio operativo: los precios son estimaciones académicas y el formulario no envía datos a un servidor."),
          P("Objetivo general", "SubtitleH"),
          P("Mejorar la práctica HTML5 anterior con una interfaz visual consistente, adaptable a diferentes dispositivos y funciones interactivas construidas con JavaScript puro."),
          P("Objetivos específicos", "SubtitleH"),
          bullet("Conservar y mejorar la estructura semántica de las tres páginas."),
          bullet("Diseñar una identidad Caribe Premium con variables CSS, Flexbox y Grid."),
          bullet("Implementar un catálogo de servicios con búsqueda y filtro por categoría."),
          bullet("Validar solicitudes con reglas propias del contexto dominicano y mensajes accesibles."),
          bullet("Documentar el código, realizar comprobaciones y publicar el resultado en GitHub Pages."),
          P("Público y contenido", "SubtitleH"),
          P("El contenido está redactado para una persona que busca información sobre una estancia turística. Las tres páginas tienen funciones claras: <b>Inicio</b> presenta la propuesta, <b>Servicios</b> compara seis opciones y <b>Contacto</b> recoge datos simulados."),
          P("2. Arquitectura y archivos", "TitleH"),
          tabla(["Capa", "Archivo", "Responsabilidad"], [
              ("Estructura", "index.html · servicios.html · contacto.html", "Contenido, semántica, accesibilidad y formularios."),
              ("Diseño", "css/estilos.css", "Variables, componentes, Grid, Flexbox, estados y media queries."),
              ("Interacción", "js/app.js", "Eventos, almacenamiento de tema, catálogo, filtros y validación."),
              ("Recursos", "img/ · assets/", "Ilustraciones SVG optimizadas y audio ambiental."),
              ("Entrega", "README.md · docs/", "Mapa de etiquetas, manual técnico y capturas."),
          ], [2.7*cm, 5.5*cm, width - 8.2*cm]), PageBreak()]

# 3. HTML
story += [P("3. Estructura HTML5 y semántica", "TitleH"),
          P("Cada archivo declara idioma español, codificación UTF-8, viewport y metadatos propios. Un único encabezado h1 identifica la página y un único main contiene su información central. El mismo menú enlaza las tres páginas y usa aria-current para indicar la activa."),
          P("Mapa de nueve familias de etiquetas", "SubtitleH"),
          tabla(["Familia", "Etiquetas representativas", "Aplicación y motivo"], [
              ("Documento", "html, head, meta, title, body", "Idioma, título y parámetros del documento."),
              ("Semántica", "header, nav, main, section, article, aside, footer, time, address, details", "Definen regiones, información adicional y contenido expandible."),
              ("Texto", "strong, em, mark, abbr, small, code, kbd, pre", "Destacan términos y ejemplos sin abusar de estilos visuales."),
              ("Citas", "blockquote, cite, q", "Distinguen testimonios extensos y frases cortas."),
              ("Listas", "ul, ol, li, dl, dt, dd", "Agrupan actividades, pasos y vocabulario hotelero."),
              ("Enlaces", "a, mailto:, tel:, #id, download", "Conectan páginas, información y archivo descargable."),
              ("Multimedia", "img, figure, figcaption, iframe, audio, source", "Ilustraciones, mapa y ambiente sonoro con contexto."),
              ("Tabla", "table, caption, thead, tbody, tfoot, th, td", "Tabla comparativa con rowspan y colspan."),
              ("Formulario", "form, fieldset, legend, label, input, select, optgroup, textarea", "Agrupa datos, preferencias y requisitos de entrada."),
          ], [2.5*cm, 5.25*cm, width - 7.75*cm]),
          Spacer(1, .25*cm),
          P("Decisiones de accesibilidad", "SubtitleH"),
          bullet("Todos los controles del formulario tienen etiqueta relacionada mediante for e id."),
          bullet("Los mensajes de error aparecen bajo los campos y se asocian por aria-describedby."),
          bullet("El menú móvil informa su estado mediante aria-expanded; los avisos usan aria-live."),
          PageBreak()]

# 4. CSS
story += [P("4. Diseño CSS: Caribe Premium", "TitleH"),
          P("Elegí una identidad de resort caribeño con turquesa, blanco suave, verde profundo y acentos arena/dorado. Los bordes redondeados y espacios amplios buscan transmitir calma sin afectar la legibilidad."),
          P("Variables y componentes", "SubtitleH"),
          tabla(["Variable", "Uso"], [
              ("--fondo, --superficie", "Fondos de página y tarjetas."),
              ("--texto, --texto-suave", "Jerarquía de lectura y textos secundarios."),
              ("--primario, --primario-hover", "Acciones, enlaces y acentos interactivos."),
              ("--linea, --sombra", "Separadores y elevación de paneles."),
              ("--fuente, --radio", "Tipografía con respaldo y redondeo de componentes."),
          ], [5.0*cm, width - 5.0*cm]),
          P("Distribución", "SubtitleH"),
          bullet("Flexbox alinea marca, enlaces, botones y pie de página."),
          bullet("Grid distribuye la portada y las tarjetas del catálogo, con columnas adaptables."),
          bullet("Dos puntos de ruptura (768 y 480 px) cambian la composición en tabletas y teléfonos."),
          bullet("Las imágenes y el mapa respetan el ancho disponible; la tabla tiene su propio desplazamiento horizontal."),
          P("Modo oscuro", "SubtitleH"),
          P("El selector body.oscuro cambia únicamente los valores de las variables. Así se reutilizan las mismas reglas para tarjetas, formularios, enlaces y tablas. La preferencia se guarda en localStorage si el navegador lo permite."),
          P("Interacción visual", "SubtitleH"),
          P("Se aplican transiciones cortas a botones, enlaces y tarjetas. Los campos tienen foco visible; el script agrega la clase invalido cuando encuentra errores. También se incluye una reducción de movimiento para las personas que solicitan esa preferencia al sistema."),
          PageBreak()]

# 5. JS
story += [P("5. JavaScript: comportamiento", "TitleH"),
          P("El archivo js/app.js está cargado con defer en las tres páginas. Usa const y let, eventos addEventListener y comprobaciones de existencia para que un control exclusivo de una página no genere errores en las demás."),
          tabla(["Función / bloque", "Evento", "Resultado"], [
              ("Menú móvil", "click", "Abre/cierra la navegación con classList.toggle y actualiza aria-expanded."),
              ("actualizarBotonTema()", "click", "Alterna modo oscuro y persiste la preferencia en localStorage."),
              ("Año automático", "carga", "Escribe el año de new Date().getFullYear() en el pie."),
              ("actualizarArriba()", "scroll / click", "Presenta el botón de retorno cuando la página se desplaza."),
              ("pintarTarjetas()", "carga / filtros", "Construye seis tarjetas HTML desde un arreglo de objetos."),
              ("filtrarServicios()", "input / change", "Combina búsqueda textual y categoría mediante filter()."),
              ("validarCampo()", "submit / input / blur", "Comprueba reglas y pinta errores al lado del campo."),
          ], [4.3*cm, 2.8*cm, width - 7.1*cm]),
          P("Datos del catálogo", "SubtitleH"),
          tabla(["Servicio", "Categoría", "Precio (DOP)"], [
              ("Habitación Clásica", "Alojamiento", "RD$ 4,500"),
              ("Habitación con Vista", "Alojamiento", "RD$ 6,800"),
              ("Suite Familiar", "Alojamiento", "RD$ 9,500"),
              ("Acceso a Piscina", "Actividades", "RD$ 1,200"),
              ("Restaurante Caribeño", "Actividades", "RD$ 1,800"),
              ("Excursión Punta Cana", "Actividades", "RD$ 3,200"),
          ], [6.4*cm, 4.3*cm, width - 10.7*cm]),
          P("Los precios son inventados para este ejercicio y se muestran con toLocaleString('es-DO', {style: 'currency', currency: 'DOP'}).", "MutedH"),
          PageBreak()]

# 6. Form and testing
story += [P("6. Validación del formulario", "TitleH"),
          P("El formulario de contacto sirve como ejemplo de solicitud, no como sistema de reservas. Por eso se utiliza preventDefault y se muestra una confirmación local sin enviar información a un servidor. Después de una solicitud válida se ejecuta reset()."),
          P("Reglas adicionales a la validación HTML", "SubtitleH"),
          tabla(["Regla", "Motivo", "Mensaje esperado"], [
              ("809 / 829 / 849 y diez dígitos", "Usar un formato coherente con teléfonos dominicanos.", "Escribe 10 dígitos con prefijo 809, 829 u 849."),
              ("Fecha igual o posterior a hoy", "Evitar solicitudes con fechas vencidas.", "La fecha de llegada no puede estar en el pasado."),
              ("Confirmar correo", "Reducir errores al escribir dirección de contacto.", "Los correos electrónicos no coinciden."),
              ("Clásica, máximo dos huéspedes", "Relacionar cantidad de viajeros con tipo de habitación.", "La habitación Clásica admite como máximo 2 huéspedes."),
          ], [3.8*cm, 5.3*cm, width - 9.1*cm]),
          P("Respuesta al usuario", "SubtitleH"),
          P("Cada campo obligatorio tiene un span.error vacío que se llena cuando corresponde. El script asigna la clase invalido, retira el error al corregir y lleva el foco al primer campo pendiente en caso de fallos. Cuando todos los datos son válidos, muestra nombre, cantidad de huéspedes, habitación, fecha y correo dentro de la página."),
          P("7. Calidad, pruebas y validación", "TitleH"),
          P("Se revisaron la sintaxis JavaScript, la estructura HTML, los recursos locales y las tres páginas publicadas. Los validadores oficiales W3C confirmaron cero errores en los tres HTML y en CSS3 el 11 de noviembre de 2026. Aún faltan las capturas finales y la comprobación específica de 360 px tras la reorganización de imágenes."),
          tabla(["Prueba", "Estado al preparar este documento"], [
              ("Sintaxis de js/app.js con node --check", "Comprobada sin errores de sintaxis."),
              ("Un único main y h1, nav activo y recursos locales", "Comprobación estructural inicial satisfactoria."),
              ("W3C HTML y CSS", "Tres HTML: 0 errores. CSS3: 0 errores y 7 advertencias informativas."),
              ("Tema y filtros en navegador", "Modo oscuro persistente, búsqueda y mensajes vacíos comprobados."),
              ("Vista a 360 px y capturas", "Pendiente de revisión en navegador real."),
          ], [7.1*cm, width - 7.1*cm]), PageBreak()]

# 7. Release and closing
story += [P("8. Publicación y mantenimiento", "TitleH"),
          P("El repositorio público contiene la fuente del proyecto. GitHub Pages permite publicar estas páginas estáticas sin servidor propio. Antes de entregar, debo comprobar que las rutas /, /servicios.html y /contacto.html cargan con los mismos estilos y funciones; después adjuntar capturas y documentación."),
          P("Procedimiento propuesto", "SubtitleH"),
          bullet("Revisar los cambios locales e incorporar commits separados con mensajes específicos."),
          bullet("Validar HTML5 y CSS, corregir errores y probar teclado, filtros y mensajes de formulario."),
          bullet("Capturar versiones de escritorio y móvil en docs/capturas/.") ,
          bullet("Subir los archivos actualizados y este PDF a la rama publicada en GitHub Pages."),
          bullet("Abrir la web pública, confirmar que funcionan las tres páginas y pegar los dos enlaces en Moodle."),
          P("9. Reflexión y decisiones personales", "TitleH"),
          P("En la primera práctica el énfasis estaba en utilizar correctamente las etiquetas HTML5. En esta evolución separé las responsabilidades: HTML describe, CSS presenta y JavaScript responde a las acciones. Esta separación hace más fácil corregir un problema sin tener que editar las tres páginas al mismo tiempo."),
          P("Elegí un diseño caribeño porque representa mejor el destino de Punta Cana. También mantuve la aclaración de que se trata de un hotel conceptual: no sería correcto hacer creer a una persona que su solicitud creó una reserva real. Para mejorar la experiencia, añadí respuestas junto a cada campo y filtros que no obligan a recargar la página."),
          P("La parte más importante del comportamiento es mantener los mismos datos en el catálogo y en la tabla, además de hacer que la validación tenga relación con el negocio. Por ejemplo, un teléfono dominicano y una cantidad de huéspedes que corresponda al tipo de habitación."),
          P("10. Fuentes y recursos", "TitleH"),
          bullet("MDN Web Docs: guías HTML, CSS, JavaScript y accesibilidad. https://developer.mozilla.org/es/"),
          bullet("W3C Nu HTML Checker: https://validator.w3.org/"),
          bullet("W3C CSS Validation Service: https://jigsaw.w3.org/css-validator/"),
          bullet("OpenStreetMap: mapa embebido de la zona general de Punta Cana."),
          bullet("Ilustraciones SVG y audio ambiental incluidos en el repositorio del proyecto."),
          Spacer(1, .4*cm),
          P("<b>Nota académica:</b> Las tarifas, instalaciones, contactos y solicitudes mostradas son ejemplos y no una oferta comercial.", "MutedH")]

doc.build(story)
print(OUTPUT)
