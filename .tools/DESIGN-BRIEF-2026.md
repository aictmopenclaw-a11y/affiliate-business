# Design Brief 2026 — Rediseño del ecosistema de documentos HTML

> **TL;DR.** El sistema actual es un tema oscuro editorial denso, sin gráficos, pensado para "verse premium" pero costoso de leer en sesiones largas. La recomendación: **pasar a un tema claro cálido (paper) como default con toggle a oscuro**, fijar el ancho de medida en **65-70 caracteres**, montar un **sistema de espaciado de 8px** con ritmo vertical generoso, elegir el pairing **Newsreader (display) + un sans legible para body**, y dar al renderer Python un set de **componentes de data viz sin dependencias** (stat cards, barras CSS, donut con `conic-gradient`, sparklines SVG) más **example boxes / callouts** y un sticky TOC con scroll-spy ya existente mejorado. Prioridad #1: legibilidad (tema + medida + ritmo). Lo demás amplifica.

---

## 1. Contexto y diagnóstico

### Qué tenemos hoy (auditado en `.tools/render.py`)

- Renderer Python custom, **sin build, sin dependencias** (parser markdown propio → HTML autocontenido con CSS y JS inline). Esto es una fortaleza: hay que conservarla.
- Tema **oscuro** (`--bg: #0e0e0c`, texto `--paper: #f5f0e6`) con textura de ruido, gradientes radiales y `h1` con gradiente de relleno de texto.
- Tipografía: **Fraunces** (headings serif) + **Inter Tight** (body) + **JetBrains Mono** (UI/labels). Inter es exactamente lo que el brief pide evitar por genérica.
- Componentes existentes: barra de progreso de lectura, topbar sticky, sidebar TOC con scroll-spy y smooth scroll, tablas con hover, blockquotes que auto-detectan box types (TL;DR, veredicto, crítico, recomendado, warning, info), badges que reemplazan emojis. **Buena base de "callouts" ya implementada.**
- **Cero data viz.** Contenido denso (research, SOPs, casos con números, síntesis de videos) presentado solo como párrafos + tablas.

### Los 5 problemas que lo hacen "frío y pesado"

1. **Dark mode por defecto para lectura larga densa.** La evidencia 2025 es consistente: para proofreading y lectura de texto denso por períodos largos, **light mode rinde mejor** en agudeza visual y comprensión; dark mode no muestra ventaja de fatiga estadísticamente significativa y puede perder definición de borde en tipos finos (NN/g; estudio MDPI 2025). El dark default va en contra del caso de uso real de este ecosistema.
2. **No hay control de medida de línea.** El `.content` permite hasta `max-width: 800px`; con body de 16px eso supera fácilmente los 80-90 caracteres por línea. La medida óptima es **50-75 cpl, sweet spot ~66** (Bringhurst, Baymard, UXPin). Líneas largas = fatiga de tracking = exactamente la sensación de "pesado".
3. **Todo pesa lo mismo.** Sin números grandes, sin jerarquía visual fuerte, sin gráficos: el ojo no tiene anclas para escanear. Los casos "con números" se diluyen en prosa y tablas.
4. **Decoración que no ayuda a leer.** Ruido fractal + gradientes + `-webkit-text-fill-color: transparent` en `h1` reducen contraste y nitidez sin aportar a la comprensión. Es "premium look" a costa de legibilidad.
5. **Inter Tight = look IA genérico.** Cumple, pero no da carácter ni señala "documento serio para leer".

---

## 2. Principios de legibilidad que guían el rediseño (con evidencia)

| Principio | Regla concreta | Fuente |
|---|---|---|
| **Medida de línea** | Body a **65-70 cpl** (`max-width: 68ch`). Nunca pasar de 75. | Baymard, UXPin, Bringhurst |
| **Tema** | **Light cálido default + toggle a dark.** Apps de lectura larga deben ofrecer ambos; default claro por rendimiento de lectura. | NN/g |
| **Ritmo vertical** | Sistema **8px** (4/8/12/16/24/32/48/64). Line-height múltiplo de 4. Body line-height ~1.6-1.7. | 8-point grid, Better Web Type |
| **Jerarquía / escala** | Escala modular (~1.25 minor third). Primary KPI ~30% más grande que secundarios. | Typography Scales, Baymard dashboards |
| **Scannability** | Subtítulos frecuentes, bullets, **negritas estratégicas** (no decorativas), 5-7 ítems por bloque antes de agrupar. | Progressive disclosure (LogRocket), Baymard |
| **Callouts / admonitions** | Cajas tipadas: Note / Tip / Important / Warning + TL;DR + Veredicto. Mejoran jerarquía y atención. | MarkdownTools, Diátaxis-style |
| **Progressive disclosure** | TL;DR arriba; detalle colapsable (`<details>`) para lo secundario; no volcar todo de golpe. | LogRocket, UI-Patterns |
| **Contraste** | Texto principal con contraste alto sobre fondo (apuntar AA+; bordes nítidos para tipos finos). | NN/g, MontanaB accesibilidad |
| **Motion** | Sutil, siempre detrás de `prefers-reduced-motion`. | MDN, Comeau |

---

## 3. Dirección de diseño recomendada

**Concepto:** "Editorial claro de research" — una revista digital de inteligencia de negocio. Cálido pero nítido, con números que saltan a la vista. Conserva el alma editorial actual (serif con carácter, mono para metadata) pero invierte la base a luz y mete datos visuales.

### 3.1 Tema y paleta (light default + dark token-mirror)

Mantener el sistema de variables CSS (`:root`) y añadir un `[data-theme="dark"]` que reescribe los mismos tokens. El toggle solo cambia el atributo en `<html>` (persistir en `localStorage`, respetar `prefers-color-scheme` en primera carga).

**Light (default) — "warm paper", no blanco puro (reduce glare, mantiene calidez actual):**

```
--bg:        #faf7f0   /* paper cálido de fondo */
--bg-elev:   #ffffff   /* cards, superficies elevadas */
--bg-sunk:   #f1ece0   /* code blocks, zonas hundidas */
--ink:       #1c1a17   /* texto principal (no negro puro) */
--ink-dim:   #4a463f   /* texto secundario */
--ink-mute:  #87806f   /* metadata, captions */
--line:      #e4ddcd   /* bordes suaves */
--line-strong:#cabfa6  /* bordes de énfasis */

--accent:    #b5651d   /* ámbar tostado — hereda el espíritu Romi/accent actual */
--green:     #4f7a4a   /* positivo / recomendado */
--red:       #b23a1f   /* crítico / negativo */
--amber:     #c08a1e   /* warning */
--blue:      #2f6f8f   /* info */
/* identidades de equipo conservadas, oscurecidas para contraste sobre paper */
--romi:      #b5651d
--cris:      #4f7a4a
--dali:      #9c3f86
```

**Dark (toggle) — partiendo del tema actual pero subiendo contraste de texto y matando el ruido fractal:**

```
--bg:#14130f  --bg-elev:#1d1c18  --bg-sunk:#0c0b09
--ink:#f3eee2  --ink-dim:#c9c2b2  --ink-mute:#8d8676
--line:#2c2a25  --line-strong:#433f37
--accent:#e0a050  --green:#7fb377  --red:#e07a55  --amber:#e8b647  --blue:#6fb6d6
```

> **Quitar en ambos temas:** la textura de ruido (`body::after`), los 3 gradientes radiales pesados (`body::before`) y el `-webkit-text-fill-color: transparent` del `h1`. Reemplazar por un h1 sólido de alto contraste. Esto solo ya sube nitidez y baja "frialdad".

### 3.2 Tipografía — pairing elegido

**Candidatos evaluados (los 3 disponibles en Google Fonts):**

1. **Newsreader (display + headings) + Public Sans (body)** — Newsreader está diseñado específicamente para lectura larga en pantalla y noticias; tiene carácter editorial sin ser decorativo. Public Sans (US Web Design System) es neutra, muy legible, con autoridad "institucional/USA" que encaja con el mercado USA, y no es Inter/Roboto/Arial.
2. **Fraunces (display) + Newsreader (body)** — conserva el display actual (Fraunces tiene mucha personalidad en tamaños grandes) y pone Newsreader como serif de lectura. Pairing "revista premium". Riesgo: dos serifs pueden sentirse uniformes; requiere buen contraste de tamaño/peso.
3. **Source Serif 4 (body) + Space Grotesk (display)** — serif robusto de Adobe muy cómodo en párrafo + display geométrico con carácter. Contraste serif/sans fuerte y moderno.

**ELEGIDO: Opción 1 — Newsreader + Public Sans** (con **JetBrains Mono** retenida para labels/metadata/código).

**Por qué:**
- **Newsreader** carga el carácter editorial que el cliente valora (reemplaza a Fraunces para H1-H3 con igual o más personalidad y mejor legibilidad a tamaño medio), y fue diseñada para lectura en pantalla.
- **Public Sans** como body resuelve dos cosas: lectura densa cómoda y un tono "serio/USA" alineado al mercado, evitando explícitamente Inter. Un sans para body (no serif) maximiza legibilidad en bloques de SOPs/tablas/números.
- El **contraste serif-display + sans-body** es la guía clásica de pairing (contraste suficiente, sin competir).
- Las 3 son Google Fonts → cero fricción para el renderer (un solo `<link>`).

```
Display/Headings: 'Newsreader', Georgia, serif
Body:             'Public Sans', system-ui, sans-serif
Mono/UI/labels:   'JetBrains Mono', monospace
```

Escala tipográfica (modular ~1.25, redondeada a la grilla):
`h1 2.8rem · h2 1.95rem · h3 1.45rem · h4 1.15rem · body 1.0625rem (17px) · small 0.85rem`. Body 17px da mejor lectura que 16px en sans para texto largo. Line-height body 1.65.

### 3.3 Sistema de espaciado (8px)

Una sola escala, usada en todo margin/padding/gap:
`--s1:4px · --s2:8px · --s3:12px · --s4:16px · --s5:24px · --s6:32px · --s7:48px · --s8:64px · --s9:96px`.

- Párrafos: `margin-block: var(--s4)`.
- Entre secciones (h2): `margin-top: var(--s8)`.
- Cards/boxes padding: `var(--s5)`.
- Medida del contenido: `max-width: 68ch` (≈660-720px según fuente). El `.layout` puede seguir en grid 280px + 1fr, pero el `.content` interno limita a 68ch y centra.

### 3.4 Set de componentes a crear/mejorar

Componentes nuevos que el renderer debe poder emitir desde sintaxis markdown:

1. **Stat card** — número grande (display), label (mono uppercase pequeño), delta con flecha verde/roja y, opcional, sparkline SVG. Agrupables en grid de 2-4. (Patrón estándar: big number + label + trend + mini-graph.)
2. **Stat strip / KPI row** — fila de 3-5 stat cards al inicio de un caso o reporte. El KPI principal 30% mayor.
3. **Bar chart (CSS)** — barras horizontales con `width: %` y label + valor; o verticales con grid. Sin JS.
4. **Donut / progress** — `conic-gradient` para % (una sola `div`, sin SVG ni JS).
5. **Sparkline (SVG inline)** — micro-línea de tendencia generada por Python (polyline en viewBox). Va al lado de un número.
6. **Before / After** — dos columnas comparativas (o una barra dividida) para "antes del cambio vs después".
7. **Example box / "En la práctica"** — caja diferenciada (borde + etiqueta + fondo sutil) para ejemplos realistas concretos: muestra el caso, no la teoría. Variante "anotada" con número/flecha.
8. **Callouts tipados** (extender los actuales): `note · tip · important · warning · info · tldr · veredicto · recomendado · critico`. Ya existe la mitad; estandarizar a iconografía SVG mono (no emoji) y consistencia de color.
9. **Collapsible `<details>`** — para progressive disclosure de detalle secundario (apéndices, data cruda, pasos largos de SOP).
10. **Theme toggle** — botón en topbar (sol/luna SVG), persiste en `localStorage`.

Componentes existentes a conservar y pulir: barra de progreso, sticky TOC con scroll-spy (subir contraste del estado activo), tablas (zebra suave + hover, header mono), badges (pasar de emoji a label/SVG ya está bien encaminado), index con cards.

---

## 4. Recomendación técnica de data viz para el renderer Python (sin deps)

**Principio rector: el renderer ya genera HTML/CSS string en Python. La mejor relación impacto/simplicidad es generar el markup del gráfico en Python y dejar que CSS/SVG lo dibujen. Cero runtime JS, cero CDN, cero build.**

### Enfoque recomendado por tipo

| Gráfico | Técnica | Por qué |
|---|---|---|
| **Stat card / KPI** | HTML + CSS puro | Trivial de emitir, máximo impacto visual, escala perfecto. |
| **Barras** | CSS puro (`width: N%` inline) | El más simple; Python calcula el % y lo inyecta. Render más rápido que canvas/SVG. |
| **Donut / progress / gauge** | `conic-gradient(var(--accent) 0 N%, var(--line) 0)` | Una `div`, una propiedad. Python solo pasa el %. Sin matemática de paths. |
| **Sparkline / línea** | **SVG inline** generado por Python | Python mapea datos → `points` de un `<polyline>` en un `viewBox`. Ligero, nítido, escalable. |
| **Comparativa before/after** | CSS (dos barras o barra dividida) | Igual que barras. |

**Por qué NO Chart.js (vía CDN):** rompe el principio "autocontenido sin dependencias" (requiere red al abrir el HTML), añade ~200KB de JS, y es overkill para barras/donuts/sparklines estáticos. **Reservarlo solo** si en el futuro se necesita interactividad real (tooltips, zoom, series grandes). Para este ecosistema, **CSS + SVG inline gana** en simplicidad, peso, offline y velocidad de render.

### Sintaxis markdown sugerida para el renderer (fenced blocks)

Que el parser reconozca bloques con info-string y los convierta a componentes. Ejemplos:

````
```stat
value: $48,200
label: Revenue mes 1
delta: +12%
spark: 3,5,4,7,6,9,11
```

```bars
Niche A | 82
Niche B | 64
Niche C | 41
```

```donut
value: 73
label: Margen objetivo
```

```example
title: Así se ve en la práctica
Página de comparación "best X for Y" con tabla de afiliados arriba + 3 reviews...
```
````

`stat`, `bars`, `donut`, `example`, `before-after` → cada uno mapea a una función `render_stat()`, `render_bars()`, etc. en `render.py`, devolviendo el HTML del componente. Los callouts ya se infieren de blockquotes; se puede añadir `> [!WARNING]` (sintaxis GitHub/Obsidian) para tipado explícito.

### Micro-interacciones (todas detrás de `prefers-reduced-motion: no-preference`)

- **Staggered reveal** al entrar en viewport (CSS scroll-driven animations o `IntersectionObserver` mínimo) — sutil fade+rise de secciones/cards.
- **Scroll-spy del TOC** — ya existe; mejorar contraste del activo.
- **Sticky TOC** — ya existe.
- **Hover** en cards/filas/stat cards (lift sutil, no translateX exagerado).
- **Theme toggle** con transición de color suave.
- Mantener barra de progreso de lectura.

---

## 5. Lista priorizada de cambios (lo que más mueve la aguja primero)

**P0 — Legibilidad base (80% del beneficio, bajo esfuerzo):**
1. Invertir a **tema claro cálido por defecto** + añadir tokens dark espejo y **toggle** (localStorage + `prefers-color-scheme`).
2. Fijar **medida de línea a `max-width: 68ch`** en `.content`.
3. **Eliminar** ruido fractal, gradientes radiales pesados y el `text-fill transparent` del h1 (subir contraste).
4. Subir body a **17px**, line-height 1.65, y aplicar **escala de espaciado 8px** consistente.

**P1 — Carácter y jerarquía:**
5. Swap tipográfico a **Newsreader + Public Sans** (JetBrains Mono se queda).
6. Estandarizar **callouts tipados** (note/tip/important/warning + tldr/veredicto/recomendado) con iconos SVG mono y colores consistentes en ambos temas.
7. Mejorar tablas (zebra suave, header mono, números tabulares con `font-variant-numeric: tabular-nums`).

**P2 — Data viz (lo que rompe la "frialdad" y vende los casos con números):**
8. **Stat cards + KPI strip** (mayor impacto visual por esfuerzo).
9. **Barras CSS** y **donut `conic-gradient`**.
10. **Sparklines SVG** generadas en Python.
11. **Example boxes "en la práctica"** y **before/after**.

**P3 — Pulido / motion / disclosure:**
12. **Staggered reveal** + hover refinados (con `prefers-reduced-motion`).
13. **`<details>` colapsables** para progressive disclosure.
14. Rediseño del **index** con stat strip global (nº docs, palabras, min lectura ya están) + cards en tema claro.

**Regla de implementación:** P0 se puede hacer solo tocando el bloque `CSS` y el `<head>` de `render.py` (sin tocar el parser). P1 igual. P2 requiere añadir funciones de parsing de fenced blocks. Hacer P0+P1 primero, regenerar, validar lectura, luego P2.

---

## 6. Fuentes

- NN/g — Dark Mode vs. Light Mode: https://www.nngroup.com/articles/dark-mode/
- MDPI 2025 — Light/Dark Mode y fatiga visual en tablets: https://www.mdpi.com/1660-4601/22/4/609
- Eye Tracking Study 2025 (ACM ETRA) — dark/light themes y carga de trabajo: https://dl.acm.org/doi/10.1145/3715669.3725879
- Baymard — Readability: The Optimal Line Length: https://baymard.com/blog/line-length-readability
- UXPin — Optimal Line Length 50-75 (2026): https://www.uxpin.com/studio/blog/optimal-line-length-for-readability/
- Mintlify — How Stripe creates the best documentation: https://www.mintlify.com/blog/stripe-docs
- Mintlify — Recommendations for creating API documentation: https://www.mintlify.com/library/our-recommendations-for-creating-api-documentation-with-examples
- MarkdownTools — Admonitions and Callouts guide: https://blog.markdowntools.com/posts/markdown-admonitions-callouts-complete-guide
- LogRocket — Progressive disclosure in UX: https://blog.logrocket.com/ux-design/progressive-disclosure-ux-types-use-cases/
- CSS-Tricks — Making Charts with CSS: https://css-tricks.com/making-charts-with-css/
- Rainforest QA — Pie charts without JavaScript (conic-gradient): https://www.rainforestqa.com/blog/drawing-pie-charts-without-javascript
- DEV — Stacked bar chart with only CSS: https://dev.to/vyckes/creating-a-stacked-bar-chart-using-only-css-3jc1
- UX Planet — 8-point grid system: https://uxplanet.org/everything-you-should-know-about-8-point-grid-system-in-ux-design-b69cb945b18d
- freeCodeCamp — 8-Point Grid: Typography on the Web: https://www.freecodecamp.org/news/8-point-grid-typography-on-the-web-be5dc97db6bc/
- Typewolf — 40 Best Google Fonts: https://www.typewolf.com/google-fonts
- Webflow — Best Google fonts for high-performance sites: https://webflow.com/blog/google-fonts
- Baymard — Dashboard cards consistency: https://baymard.com/blog/cards-dashboard-layout
- Pencil & Paper — Dashboard UX patterns: https://www.pencilandpaper.io/articles/ux-pattern-analysis-data-dashboards
- Josh W. Comeau — Scroll-Driven Animations: https://www.joshwcomeau.com/animation/scroll-driven-animations/
- MDN — Scroll-driven animation timelines: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines
- Maggie Appleton — Garden (referencia de digital garden legible): https://maggieappleton.com/

---

*Brief de diseño. No es implementación. Generado 2026-06-17 para el rediseño del renderer `.tools/render.py` del proyecto affiliate-business.*
