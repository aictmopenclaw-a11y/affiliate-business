# Playbook de bridge pages bulletproof (anti-ban + conversion)

> *"Estás a un anuncio de cambiar tu vida."*
>
> La bridge page es donde se gana o se pierde la plata. El cuello de botella del negocio no es generar leads baratos: es monetizarlos. Meta puede mandarte clicks a $0.40, pero si la página intermedia no pre-vende, no filtra y no trackea, ese tráfico se evapora antes del HopLink. La bridge es nuestra única ventaja competitiva: el VSL y el checkout son del vendor y los usan todos los afiliados iguales `[FUENTE REPO: affiliate-funnel-structure.md, "El funnel completo"]`.

---

## Cómo leer este documento

Convención de marcas:

- `[FUENTE REPO]` material extraído de un archivo del repo (research, cursos, skills). Se cita el archivo y la sección.
- `[BEST-PRACTICE]` práctica estándar de la industria de affiliate/CRO, no atada a una fuente puntual del repo.
- `[CRITERIO]` decisión u opinión del director de copy/CRO para este negocio.

Regla de oro de seguridad antes de empezar: **nunca se manda el ad directo al HopLink.** Es ban casi garantizado y, si cae una cuenta, pueden caer las asociadas `[FUENTE REPO: SINTESIS-VIDEOS-FOROS-2026.md §0 TL;DR]`.

---

## 1. Qué es y por qué existe

### El rol de la bridge en el funnel

La bridge page (o pre-lander, o landing intermedia) es la página propia que se interpone entre el anuncio de Meta y el HopLink de ClickBank. El flujo completo es:

```
Ad (Meta) -> Bridge page / pre-lander PROPIA -> HopLink ClickBank -> VSL del vendor -> checkout
```

`[FUENTE REPO: SINTESIS-VIDEOS-FOROS-2026.md §3 "El funnel ClickBank to Meta"]`

Visto como embudo con números de referencia (ilustrativos del consenso de foros + video, no datos de nuestra cuenta):

```
Anuncio Meta              100
Bridge page propia         60
HopLink (VSL del vendor)   20
Checkout                    8
Venta confirmada            3
```

`[FUENTE REPO: SINTESIS-VIDEOS-FOROS-2026.md §3, funnel de conversión]`

La bridge cumple cuatro funciones que ninguna otra pieza del funnel puede cumplir `[FUENTE REPO: affiliate-funnel-structure.md, "El funnel completo"]`:

1. **Pre-vende** al usuario (sube la percepción de valor antes del VSL).
2. **Filtra tráfico** (los que no califican rebotan antes de llegar al VSL del vendor).
3. **Captura data nuestra** (pixel, GA4, eventos de scroll y click).
4. **Construye brand percibido** (el usuario cree que somos la marca).

Param lo demuestra en vivo: "no pongas el affiliate link, el affiliate link va aquí [en la landing], lo que va [en el ad] es la URL del website" `[FUENTE REPO: SINTESIS-VIDEOS-FOROS-2026.md §3, video Param N3-SH71IXrbp-A 16:18-16:26]`.

### Por qué NUNCA direct link

Direct linking (mandar el ad directo al HopLink) es el error #1 y el más repetido en todos los foros. No importa si la oferta es "Facebook-friendly": tarde o temprano cae la cuenta. Citas del repo `[FUENTE REPO: 09-errores-foros-clickbank-meta.md §2.2 "EL error letal: direct linking"]`:

- "Don't direct link it, my housemate and I lost several accounts" (Social God, BlackHatWorld).
- "NO! You will get banned eventually" (T J Tutor, admin AffiliateFix).
- "I wouldn't do any direct linking without a lander, you're just asking for trouble. If 1 account gets banned using the URL, i heard you all get banned from FB ads" (wayne12, AffiliateFix).

Razones técnicas y de negocio para la bridge propia, no solo de policy:

- **Control del pixel y la data.** El HopLink es dominio del vendor: no se puede instalar tu pixel ahí. Sin bridge propia, Meta nunca ve el comportamiento del usuario `[FUENTE REPO: affiliate-funnel-structure.md, "Tracking"]`.
- **Customización obligatoria.** Param insiste varias veces: customizar, no copiar; copy-paste de la landing del vendor hace que Facebook suspenda `[FUENTE REPO: SINTESIS-VIDEOS-FOROS-2026.md §3, video Param 05:32-05:53 y 24:42-25:14]`.
- **Page-match con el ad.** Las primeras 2 líneas del primary text deben enganchar con el problema que la landing resuelve. Eso solo se controla en página propia `[FUENTE REPO: SINTESIS-VIDEOS-FOROS-2026.md §3, video Param 15:14-15:30]`.

La bridge corre en dominio propio y verificado en el Business Portfolio (ejemplo de este negocio: la oferta 1 vive en `truhealthdaily.com` con bridge informativa) `[FUENTE REPO: meta-ads-estructura-bulletproof.md §7 "Qué montar HOY"]`.

---

## 2. Las 4 reglas anti-ban de la landing (críticas)

Estas cuatro reglas son la diferencia entre una cuenta que escala y una cuenta muerta. No son negociables.

### Regla 1: Tono informativo / editorial, NO de venta

La regla más citada de los foros, atribuida a Chris Newman en BlackHatWorld `[FUENTE REPO: 09-errores-foros-clickbank-meta.md §2.4]`:

> "The landing page must have an informative tone and NOT a sales / marketing tone, otherwise the algorithms of FB Ads will detect it as pure affiliate marketing."

Traducción operativa: si la bridge grita "COMPRA AHORA 50% OFF", el algoritmo de Meta la clasifica como puro marketing de afiliado y flagea la cuenta. La página tiene que leerse como un artículo, una nota, una historia o un quiz, no como una carta de ventas. Lenguaje sensacionalista en mayúsculas ("INCREÍBLE", "ESTO TE SHOCKEARÁ") está entre las razones de disapproval comunes en nutra `[FUENTE REPO: affiliate-compliance-nutra.md "Sensational language"]`.

### Regla 2: Disclaimer de salud visible

Para todo lo que sea nutra/supplement el disclaimer FDA es obligatorio y debe estar visible en el footer `[FUENTE REPO: affiliate-compliance-nutra.md "Lo que SIEMPRE debe estar"]`:

> "These statements have not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease."

Meta además exige (regla 2026) que el disclaimer "This product is not intended to diagnose, treat, cure, or prevent any disease" aparezca también en el copy del ad, no solo en la landing; sin eso = rechazo automático `[FUENTE REPO: meta-ads-estructura-bulletproof.md §5; 09-errores-foros §2.4, AuditSocials Meta policy 2026]`. Cerca de cualquier testimonio: "Results not typical" o "Individual results may vary" `[FUENTE REPO: affiliate-compliance-nutra.md, testimonios]`.

### Regla 3: Contenido que aporta valor por sí mismo (advertorial real, no cloaking)

La bridge tiene que aportar valor real: contenido, quiz, artículo informativo. No puede ser un puente transparente a la oferta `[FUENTE REPO: 09-errores-foros §2.4, lección Chris Newman]`. Meta exige una landing "que poseas, con valor por sí misma".

Esto NO es cloaking. Cloaking es mostrar a Meta una página y al usuario otra `[FUENTE REPO: 09-errores-foros §2.4]`, y viola explícitamente las políticas de Meta: ban permanente del ad account y posible acción legal `[FUENTE REPO: 09-errores-foros §2.4, Meta Transparency Center]`. **Recomendación del repo y de este playbook: NO cloaking, nunca.** Es incompatible con un negocio sostenible. El advertorial real le muestra a Meta y al usuario exactamente la misma página de valor.

### Regla 4: El HopLink va en un CTA suave, no como link crudo

El CTA primario nunca es "Comprar ahora". El flujo es: el usuario hace click en un botón suave que lo lleva al VSL del vendor, y la compra ocurre allá `[FUENTE REPO: affiliate-funnel-structure.md, anatomía advertorial + anti-patterns]`.

- CTA correcto: "Watch the full video", "See how it works", "Read her story" `[CRITERIO]`.
- CTA prohibido en la bridge: "Buy now", botón de compra directa (rompe el tono informativo y el flow) `[FUENTE REPO: affiliate-funnel-structure.md, anti-patterns #4]`.

El HopLink se ata al botón con el `tid=` único por variante; el usuario nunca ve la URL cruda de `hop.clickbank.net` `[FUENTE REPO: affiliate-clickbank.md "HopLink"]` `[BEST-PRACTICE]`.

---

## 3. Anatomía de una bridge page que convierte

Orden de las secciones, de arriba hacia abajo. Base: la anatomía advertorial del repo `[FUENTE REPO: affiliate-funnel-structure.md, "Anatomía detallada de una landing advertorial"]`, enriquecida con los frameworks de copy (sección 6).

| # | Sección | Qué va | Por qué |
|---|---|---|---|
| 1 | **Hook / titular (H1)** | 6-12 palabras, hook directo al problema o a la curiosidad. No el nombre de la marca. | Es el filtro de atención. Debe hacer page-match con las 2 primeras líneas del ad `[FUENTE REPO: SINTESIS §3]`. Bueno: "The morning trick women in Miami are using". Malo: "Product X will change your life" `[FUENTE REPO: affiliate-funnel-structure.md]`. |
| 2 | **Sub-hook** | Validación social o el problema en una línea ("Thousands of women over 45 are discovering..."). | Confirma al lector "esto es para mí" y baja el bounce inmediato. Activa el aha moment `[FUENTE REPO: cruce-cursos-aplicado.md, Aha Moment]`. |
| 3 | **Apertura (problema)** | 2-3 párrafos donde un personaje arquetipo del target vive el problema. Identificación pura. | Tráfico frío está en consciencia de problema, no de producto. Hay que nombrar el dolor antes de ofrecer nada `[FUENTE REPO: felipe-vergara-m04, niveles de consciencia]`. |
| 4 | **Agitación** | Profundizar el costo de no resolver: cómo afecta el día a día, qué se pierde. 1 momento de "¿y si hubiera otra forma?". | Es la "A" de PAS. Sube la urgencia (maleta 6) sin prometer nada todavía `[FUENTE REPO: cruce-cursos-aplicado.md, 7 maletas]`. |
| 5 | **Historia / mecanismo (reveal)** | El personaje descubre el método/producto. Pseudo-mecánica: ciencia simplificada, sin claims dudosos. | El "aha" del producto. Construye percepción de valor (regla del 5x de Ogilvy) amplificando lo que el vendor ya promete, sin inventar `[FUENTE REPO: felipe-vergara-m04, mejorar la oferta]`. |
| 6 | **Prueba social** | "Thousands already using it", testimonio simple tipo plantilla. Cerca de cada testimonio: "Results not typical". | Activa autoridad y prueba social (Cialdini) `[FUENTE REPO: cruce-cursos-aplicado.md, 6 trucos]`. Reduce fricción para tráfico desconfiado. |
| 7 | **Transición a la oferta** | Puente del relato al CTA: "Here's where you can see the full method she used". Mención de beneficios concretos (3-5 bullets específicos). | Conecta la historia con la acción. 3-5 beneficios específicos convierten más que 15 genéricos `[FUENTE REPO: affiliate-funnel-structure.md, anti-patterns #6]`. |
| 8 | **CTA** | Un solo CTA, suave, botón grande (mínimo 48px, ancho completo): "Watch the full video". Mención de garantía 60 días del vendor cerca. | Un CTA, claro `[FUENTE REPO: affiliate-funnel-structure.md, anti-patterns #3]`. La garantía baja la fricción (maleta confianza). |
| 9 | **Disclaimer / footer** | FDA disclaimer, "individual results may vary", "consult your doctor", affiliate disclosure, privacy policy, terms. "Advertorial" visible si simula formato editorial. | Obligatorio por FTC/FDA y Meta `[FUENTE REPO: affiliate-compliance-nutra.md + affiliate-funnel-structure.md]`. Sin esto = disapproval o riesgo legal. |

Anti-patterns que matan la página (no hacer nunca) `[FUENTE REPO: affiliate-funnel-structure.md, "Anti-patterns que matan funnels"]`:

1. Logo de marca real arriba (destruye la sensación de descubrimiento).
2. Pop-up "antes de irte" (Meta lo penaliza con disapproval).
3. CTAs múltiples (uno solo).
4. Botón "comprar ahora" en la bridge (el flow es comprar en el VSL del vendor).
5. Botón "saltar al video" muy arriba (perdés la pre-venta).
6. Demasiados beneficios genéricos.
7. Texto dentro de imágenes (no escaneable).
8. Auto-play de video con audio (Meta lo flagea).
9. Pretender ser news site sin el disclaimer "Advertorial".

---

## 4. Los 4 tipos de bridge page y cuándo usar cada uno

Base: `[FUENTE REPO: affiliate-funnel-structure.md, "4 tipos de landing intermedia"]`. Columna "flagea menos" es `[CRITERIO]` del director CRO según el riesgo de tono de venta.

### (a) Advertorial / artículo

- **Cuándo usar:** ofertas nutra/health donde la historia del producto es clave. Convierte bien en audiencias 45+.
- **Estructura:** hook headline (problema doloroso) -> sub-hook -> story de personaje arquetipo -> reveal del producto/método -> beneficios -> CTA al VSL ("Watch the full video").
- **Pros:** alta conversión en frío; permite testear muchos hooks sobre la misma estructura; fácil de iterar; formato dominante en el nicho según el repo.
- **Contras:** caro de producir; difícil de escalar a múltiples variantes.
- **Flagea menos:** SÍ, es el que menos flagea cuando el tono es genuinamente editorial. Es la recomendación inicial del repo para empezar `[FUENTE REPO: affiliate-funnel-structure.md, "Recomendación inicial"]`.

### (b) Quiz / encuesta

- **Cuándo usar:** ofertas que aplican a sub-segmentos distintos (ej. "tu tipo de piel"). Convierte en 25-45. Thomas Owen lo menciona como palanca de conversión `[FUENTE REPO: SINTESIS §3, video N2-26x8v-Lmzq0]`.
- **Estructura:** pregunta inicial enganchadora -> 4-7 preguntas de calificación -> "Processing your result..." -> resultado personalizado + reveal -> CTA al VSL.
- **Pros:** alta engagement; captura email opcional; los que terminan están altamente calificados; el compromiso/consistencia (Cialdini) sube la conversión `[FUENTE REPO: cruce-cursos-aplicado.md, 6 trucos]`.
- **Contras:** complejo de armar bien; puede sentirse manipulador si está mal hecho.
- **Flagea menos:** medio. El engagement es buena señal para Meta, pero un quiz que asume condiciones médicas puede chocar con "personal attributes" (ver nota abajo).

### (c) Listicle / comparación "best X for Y"

- **Cuándo usar:** nichos saturados donde "comparación" es un keyword de búsqueda potente.
- **Estructura:** headline "The 3 best [product] of 2026" -> pseudo-revisión objetiva (escala arbitraria) -> producto del vendor en #1 (siempre) -> CTA al VSL.
- **Pros:** funciona muy bien con Google Ads search.
- **Contras:** menos efectivo en Meta Ads (tráfico frío); más riesgo legal (puede parecer engañoso si está mal hecho).
- **Flagea menos:** en Meta, el que más riesgo tiene si la "comparación" es claramente un pretexto de venta. Mejor reservarlo para search `[CRITERIO]`.

### (d) Pre-lander de historia hacia VSL (pre-VSL)

- **Cuándo usar:** cuando el VSL del vendor es muy largo (15+ min) y se necesita pre-calificar.
- **Estructura:** video corto 60-90 seg con host propio (avatar HeyGen funciona) -> setup del problema + "what you're about to see will surprise you" -> botón al VSL.
- **Pros:** filtra a quienes no quieren video largo.
- **Contras:** menor variabilidad creativa; tu host puede convertir menos que el del vendor.
- **Flagea menos:** medio-alto si es solo texto de venta + botón. El video propio que aporta contexto ayuda a que se lea como contenido.

> Nota "personal attributes" `[FUENTE REPO: affiliate-compliance-nutra.md]`: Meta no permite ads ni páginas que asuman algo del usuario. Evitar "Do you suffer from joint pain?" (asume condición). Usar "People with joint pain are discovering..." (no asume). Aplica especialmente al quiz y al ad que lleva a él.

---

## 5. Niveles de consciencia (Schwartz) aplicados a la bridge

El error más caro del affiliate principiante: hablarle al tráfico como si ya conociera el producto. Los 5 niveles `[FUENTE REPO: felipe-vergara-m04-aplicado.md, "Niveles de Consciencia"]`:

1. **Unaware (inconsciente):** no sabe que tiene el problema.
2. **Problem aware (problema):** sabe que tiene el problema, no conoce soluciones.
3. **Solution aware (solución):** conoce soluciones, no nuestra marca.
4. **Product aware (producto):** conoce la marca, no ha comprado.
5. **Most aware (decisión):** ya compró.

Regla central para nuestro negocio `[FUENTE REPO: felipe-vergara-m04, "Aplicación al affiliate (CRÍTICO)"]`:

> El cold traffic de Meta para affiliate generalmente está en niveles 1-2 (inconsciente o problema). Las ofertas ClickBank suelen ser productos que el target NO sabe que existen como solución. Casi nadie está buscando "Prosta-X" o "Glucosamina Plus": están buscando alivio para la próstata o las articulaciones.

Error fatal: si la persona está en nivel inconsciente y le mostramos un mensaje de nivel decisión ("buy now 25% off"), el mensaje no funciona. El target ni sabe qué es el producto `[FUENTE REPO: felipe-vergara-m04, "Error fatal"]`. Por eso la bridge para tráfico frío abre con problema, no con producto.

### Tabla nivel -> hook -> tipo de bridge

| Nivel | Estado mental | Ángulo del hook | Verbo que delata el nivel `[FUENTE REPO: m04]` | Tipo de bridge recomendado |
|---|---|---|---|---|
| **Unaware** | No sabe que tiene el problema | Dato/hecho sorpresa ("Did you know...?") | "Did you know...", hecho sorpresa | Advertorial (necesita educar, copy largo) |
| **Problem aware** | Siente el dolor, no conoce solución | Empatía con el problema ("People who can't sleep through the night...") | "Are you tired of...", "People who struggle with..." | Advertorial o Quiz |
| **Solution aware** | Conoce categorías de solución | Beneficio directo + diferencial del método | Beneficios directos sin pregunta | Pre-VSL o Listicle (comparación de soluciones) |
| **Product aware** | Conoce la marca (retargeting) | Autoridad + prueba social fuerte | Nombre de la marca primero | Pre-VSL corto o ad directo a oferta (retargeting) |
| **Most aware** | Ya compró | Recordatorio + cross-sell/promo | "Remember...", "You already know..." | Retargeting, no bridge fría |

Longitud del copy por nivel `[FUENTE REPO: m04, "Longitud del copy"]`: inconsciente/problema = copy más largo (hay que educar); solución = medio; producto/decisión = corto. "Ni una palabra más, ni una palabra menos" (Felipe Vergara).

Mapa de tráfico -> estrategia `[FUENTE REPO: m04]`:

- Cold ad de Meta -> nivel inconsciente/problema -> ad presenta problema, landing educa, VSL del vendor cierra.
- Retargeting (visitó la bridge, no compró) -> solución/producto -> ad de beneficios + diferenciales.
- Retargeting (carrito abandonado) -> decisión -> recordatorio + urgencia suave (limitada por compliance).

---

## 6. Frameworks de copy aplicados a la bridge

### PAS (Problema - Agitación - Solución)

El esqueleto natural del advertorial. Mapea directo a la anatomía de la sección 3:

- **Problema** = apertura (sección 3.3): el personaje vive el dolor.
- **Agitación** = sección 3.4: el costo de no resolverlo.
- **Solución** = historia/mecanismo + transición (3.5 y 3.7): el reveal del método y el puente al VSL.

`[FUENTE REPO: cruce-cursos-aplicado.md + felipe-vergara-m04]` `[BEST-PRACTICE]`

### AIDA (Atención - Interés - Deseo - Acción)

Vista del flujo completo de la página: **Atención** = hook H1; **Interés** = sub-hook + apertura; **Deseo** = historia + beneficios + prueba social; **Acción** = CTA suave al VSL. Útil para auditar que la página no se quede sin uno de los cuatro pasos `[BEST-PRACTICE]`.

### Las 7 maletas / el aha moment

Las 7 maletas que el cliente carga al decidir comprar `[FUENTE REPO: cruce-cursos-aplicado.md, "7 maletas" (Felipe Vergara M03)]`: necesidad, conciencia del problema, conocimiento de soluciones, confianza en el vendedor, capacidad económica, urgencia, permiso para comprar. Cada bloque de la bridge debe activar 2-3:

- Hook + apertura -> necesidad + conciencia del problema.
- Historia + prueba social -> conocimiento de soluciones + confianza.
- CTA + garantía -> urgencia + permiso ("you give yourself this permission").

El aha moment es el test creativo del hook `[FUENTE REPO: cruce-cursos-aplicado.md, "Aha Moment"]`: ¿el lector diría "that's me"? Si sí, el ángulo es correcto. Si es "interesting but doesn't apply to me", el ángulo está equivocado. Se prueba leyéndole el hook a alguien sin contexto: si no reacciona con "eso le pasa a [arquetipo]", el hook no está listo.

### Característica -> beneficio (regla del 5x de Ogilvy)

No vender la característica, vender lo que el cliente obtiene `[FUENTE REPO: felipe-vergara-m04, "Los 10 artes" #5 Beneficio + "Cómo mejorar la Oferta"]`. "Un producto excelente se podrá vender con una campaña mediocre. La mejor campaña no salvará a un producto mediocre" (Ogilvy, citado por Vergara). La regla del 5x: el lector debe sentir que recibió 5 veces más valor del que pagó. Nuestro rol es **amplificar la percepción de valor del vendor**, sin inventar:

- Profundizar los beneficios reales que el vendor menciona pero no desarrolla.
- Educar sobre el problema (mercado inconsciente/problema).
- Pre-construir autoridad (referencias, validación social).

Boosters de oferta que conviene destacar en la bridge antes del VSL `[FUENTE REPO: m04, "GRATIS + Garantía + Pago fácil"]`: la palabra "FREE" (envío gratis, bono gratis si el vendor lo incluye), la garantía de 60 días de ClickBank, y los métodos de pago fáciles (PayPal baja fricción). Nunca prometer una garantía que el vendor no honre (chargebacks + compliance).

---

## 7. Ejemplos de copy concretos por nicho

> El copy de ejemplo va en inglés (mercado USA, público real). Debajo de cada bloque, una nota corta en español de por qué funciona. Prueba social siempre como plantilla: "[Name], [city]". No son testimonios reales.

### Nicho 1: DENTAL (oral / gum health)

**3 titulares (hooks) por ángulo distinto:**

1. Ángulo curiosidad/unaware: *"The 10-second nighttime habit dentists rarely talk about"*
   Nota: hook de dato sorpresa para tráfico inconsciente; promete un secreto sin nombrar el producto.
2. Ángulo problema/problem aware: *"People with bleeding gums are quietly trying this at home"*
   Nota: nombra el problema sin asumir que el lector lo tiene (evita "personal attributes" de Meta) `[FUENTE REPO: affiliate-compliance-nutra.md]`.
3. Ángulo mecanismo/solution aware: *"Why brushing alone may not be enough for your gums"*
   Nota: introduce la idea de que la solución conocida (cepillarse) es incompleta, abre espacio al método nuevo.

**Apertura de advertorial (2-3 párrafos):**

> For years, [Name] from [City] did everything her dentist told her. She brushed twice a day, flossed when she remembered, and still dreaded every checkup. The verdict was always the same: a little more bleeding, a little more recession, another deep cleaning scheduled.
>
> What bothered her most was the feeling that she was losing a battle she didn't fully understand. The gums kept pulling back. The sensitivity kept creeping in. And no one ever explained why her routine wasn't enough.
>
> Then a hygienist mentioned something almost in passing, a detail about what actually happens below the gum line at night, that made her rethink everything she thought she knew about oral care.

Nota: PAS puro. Problema (rutina que no alcanza) + agitación (sensación de perder una batalla) + apertura al reveal. Tono editorial, cero venta `[FUENTE REPO: 09-errores-foros, Chris Newman]`.

**Bloque de transición a la oferta:**

> What the hygienist described isn't a new toothpaste or a stronger mouthwash. It's a different way of supporting the environment your gums live in every single night, and it's explained in full in a short presentation that [Name] says finally connected the dots for her.

Nota: puente del relato al CTA. No dice "compra", reposiciona el producto como "a different way" y deriva a la presentación (VSL) `[FUENTE REPO: affiliate-funnel-structure.md, transición + CTA suave]`.

**CTA:**

> Watch the short presentation here

Nota: CTA suave, un solo botón, lleva al HopLink/VSL, nunca a un checkout `[FUENTE REPO: affiliate-funnel-structure.md, anti-patterns #4]`.

**Disclaimer (footer):**

> Individual results may vary. These statements have not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease. Consult your dentist or physician before starting any new supplement. This page may contain affiliate links; if you purchase, we may earn a commission at no extra cost to you. [Privacy Policy] | [Terms]

Nota: cubre FDA + resultados individuales + consulta profesional + affiliate disclosure `[FUENTE REPO: affiliate-compliance-nutra.md, disclaimers obligatorios]`.

### Nicho 2: IDIOMAS (learn English / a language)

> Nicho no salud: no aplica disclaimer FDA. Sí aplican affiliate disclosure y "results may vary".

**3 titulares (hooks) por ángulo distinto:**

1. Ángulo curiosidad/unaware: *"The reason most adults never become fluent (it's not talent)"*
   Nota: reencuadra la creencia limitante; tráfico que no sabe que el método es el problema, no su capacidad.
2. Ángulo problema/problem aware: *"Stuck at the same level for years? You're not the problem"*
   Nota: empatía con el estancamiento, quita la culpa al lector. Alta tasa de "that's me" (aha moment).
3. Ángulo mecanismo/solution aware: *"Why classroom grammar fails and what fluent speakers do instead"*
   Nota: contrasta la solución conocida (clases/gramática) con un mecanismo distinto.

**Apertura de advertorial (2-3 párrafos):**

> [Name] from [City] had tried it all. Three different apps, two night courses, a shelf of grammar books. He could pass a written test, but the moment a real conversation started, his mind went blank and the words wouldn't come.
>
> It's a frustration millions of adult learners know well: years of effort, and still that wall between understanding a language and actually speaking it. Most people quietly conclude they're just "not good at languages" and give up.
>
> What [Name] discovered was that the wall had nothing to do with talent. It had to do with the order in which he was learning, and once he flipped that order, speaking started to feel less like translating and more like reacting.

Nota: PAS para idiomas. Agitación = la conclusión de "no soy bueno para esto". Reveal = el orden de aprendizaje, mecanismo simple y creíble `[FUENTE REPO: felipe-vergara-m04, mecanismo simplificado]`.

**Bloque de transición a la oferta:**

> The method [Name] used isn't another app or another textbook. It's a short approach built around how the brain actually wires a second language, and the full walkthrough is laid out in a free video that shows exactly how it works.

Nota: reposiciona frente a apps/libros (la solución que el lector ya probó y le falló). "Free video" usa el booster "FREE" `[FUENTE REPO: m04, GRATIS]`.

**CTA:**

> Watch the free walkthrough

Nota: CTA suave + palabra "free", deriva al VSL del vendor.

**Disclaimer (footer):**

> Individual results may vary and depend on effort and consistency. This page may contain affiliate links; if you purchase, we may earn a commission at no extra cost to you. [Privacy Policy] | [Terms]

Nota: sin FDA (no es salud), pero con results-may-vary + affiliate disclosure obligatorios por FTC `[FUENTE REPO: affiliate-compliance-nutra.md, affiliate disclosure]`.

### Nicho 3: WEIGHT LOSS

> Nicho de máximo riesgo de compliance. Cero claims de cantidad/tiempo ("lose X kg in Y days") `[FUENTE REPO: affiliate-compliance-nutra.md, claims prohibidos]`. Lenguaje de wellness suave, before/after prohibido `[FUENTE REPO: affiliate-compliance-nutra.md, "Antes/después: no los uses"]`.

**3 titulares (hooks) por ángulo distinto:**

1. Ángulo curiosidad/unaware: *"The morning ritual women over 40 are talking about"*
   Nota: curiosidad + segmento, sin prometer resultado. "Talking about" es prueba social blanda, no claim.
2. Ángulo problema/problem aware: *"When eating less and moving more stops working"*
   Nota: valida la frustración del plateau sin asumir nada del lector ni prometer pérdida de peso.
3. Ángulo mecanismo/solution aware: *"The metabolism myth that keeps healthy women stuck"*
   Nota: ataca una creencia (la solución conocida), abre al mecanismo del producto.

**Apertura de advertorial (2-3 párrafos):**

> By 43, [Name] from [City] had done everything the magazines told her. She counted calories, walked every morning, cut out the foods she loved. The scale would budge for a week, then settle right back where it started, as if her body had a setpoint it refused to leave.
>
> If you've ever felt like you're doing everything "right" and still spinning your wheels, you already know how discouraging that loop becomes. It's easy to blame willpower. [Name] did, for years.
>
> What changed things for her wasn't another diet. It was learning about a factor most plans ignore entirely, one that helped her body feel supported instead of fought, and the difference in how she felt day to day surprised her more than anything on the scale.

Nota: agitación = el loop de "doing everything right". Reveal cuidado: "feel supported", "how she felt day to day", evita prometer pérdida de peso (compliance) `[FUENTE REPO: affiliate-compliance-nutra.md, lenguaje "apoya" en vez de "cura"]`.

**Bloque de transición a la oferta:**

> The factor [Name] learned about is explained, in plain language, in a short video presentation. It walks through what may be quietly working against women over 40 and what a growing number of them are doing to support their bodies instead.

Nota: transición sin claim, sin número, sin timeframe. Deriva al VSL donde el vendor (responsable de su propio compliance) hace su pitch `[FUENTE REPO: affiliate-compliance-nutra.md, testimonios del VSL del vendor]`.

**CTA:**

> Watch the free presentation

Nota: CTA suave, deriva al HopLink/VSL.

**Disclaimer (footer):**

> Individual results are not typical and may vary. These statements have not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease. Consult your physician before starting any supplement, especially if pregnant, nursing, or taking medication. Any testimonials reflect individual experiences and are not a guarantee of results. This page may contain affiliate links; if you purchase, we may earn a commission at no extra cost to you. [Privacy Policy] | [Terms]

Nota: el footer más estricto de los tres, por ser nutra + weight loss. Incluye "results not typical", FDA, consulta médica con casos especiales, descargo de testimonios y affiliate disclosure `[FUENTE REPO: affiliate-compliance-nutra.md, disclaimers obligatorios + testimonios]`.

---

## 8. Checklist de bridge page bulletproof

Marcar cada item antes de mandar tráfico. Si uno falla, no se lanza.

### Bloque A: Anti-ban (crítico)

- [ ] El ad apunta a la bridge en dominio propio, NUNCA al HopLink directo `[FUENTE REPO: SINTESIS §0]`.
- [ ] Dominio verificado en el Business Portfolio de Meta `[FUENTE REPO: meta-ads-estructura-bulletproof.md §5]`.
- [ ] Tono informativo/editorial, no de venta. Sin mayúsculas sensacionalistas `[FUENTE REPO: 09-errores-foros §2.4]`.
- [ ] La página aporta valor por sí misma (advertorial/quiz/artículo real), no es puente transparente `[FUENTE REPO: 09-errores-foros §2.4]`.
- [ ] Cero cloaking: misma página para Meta y para el usuario `[FUENTE REPO: 09-errores-foros §2.4]`.
- [ ] CTA suave al VSL ("Watch the video"), nunca "Buy now" ni checkout en la bridge `[FUENTE REPO: affiliate-funnel-structure.md, anti-patterns #4]`.
- [ ] Copy NO copiado-pegado de la landing del vendor (customizado) `[FUENTE REPO: SINTESIS §3, Param]`.
- [ ] Page-match: las 2 primeras líneas del ad enganchan con el problema que resuelve la bridge `[FUENTE REPO: SINTESIS §3]`.
- [ ] Sin "personal attributes" (no "Do you suffer from X?"; sí "People with X are discovering...") `[FUENTE REPO: affiliate-compliance-nutra.md]`.
- [ ] Sin antes/después; sin claims de cura/tratamiento/garantía de resultado `[FUENTE REPO: affiliate-compliance-nutra.md]`.
- [ ] Disclaimer FDA presente en footer (nutra) y también en el copy del ad `[FUENTE REPO: meta-ads-estructura-bulletproof.md §5]`.
- [ ] Affiliate disclosure visible `[FUENTE REPO: affiliate-compliance-nutra.md]`.

### Bloque B: Técnico

- [ ] Mobile-first: CTAs grandes (mín. 48px alto, ancho completo), headline legible sin zoom (mín. 18px) `[FUENTE REPO: affiliate-funnel-structure.md, mobile first]`.
- [ ] Carga < 3s. Targets: LCP < 2.5s, CLS < 0.1, page weight < 500 KB `[FUENTE REPO: affiliate-funnel-structure.md, tiempos de carga]`.
- [ ] Imágenes WebP, lazy load below the fold, CSS crítico inline, JS mínimo, CDN (Cloudflare) `[FUENTE REPO: affiliate-funnel-structure.md]`.
- [ ] Sin pop-ups, sin redirects, sin auto-play con audio `[FUENTE REPO: affiliate-funnel-structure.md + affiliate-compliance-nutra.md]`.
- [ ] Pixel Meta: PageView + ViewContent (50% scroll) + InitiateCheckout (click CTA) `[FUENTE REPO: affiliate-funnel-structure.md, tracking]`.
- [ ] GA4: page_view + scroll_50/75/100 + cta_click `[FUENTE REPO: affiliate-funnel-structure.md]`.
- [ ] HopLink con `tid=` único por variante (convención fb_a1_h3, etc.) `[FUENTE REPO: affiliate-clickbank.md, HopLink]`.
- [ ] Postback ClickBank -> Meta CAPI configurado (Purchase con email hasheado); fbclid anexado al HopLink `[FUENTE REPO: meta-ads-estructura-bulletproof.md §3 paso 7 + SINTESIS §3]`.
- [ ] Tracking validado con compra real de $1 ANTES de gastar; evento Purchase visible en Events Manager en ~30 min con buen EMQ. No avanzar si no trackea `[FUENTE REPO: meta-ads-estructura-bulletproof.md §3 paso 8]`.
- [ ] QA en iPhone + Android gama media + 3G simulado + con bloqueador de ads `[FUENTE REPO: affiliate-funnel-structure.md, QA antes de live]`.
- [ ] Tools page del vendor leída completa (restricciones de tráfico/compliance respetadas) `[FUENTE REPO: affiliate-funnel-structure.md, tools page]`.

### Bloque C: Conversión

- [ ] Hook H1 de 6-12 palabras, al problema/curiosidad, no a la marca `[FUENTE REPO: affiliate-funnel-structure.md]`.
- [ ] El nivel de consciencia del tráfico (frío = problema/unaware) matchea el ángulo del hook `[FUENTE REPO: felipe-vergara-m04]`.
- [ ] Estructura PAS completa: problema -> agitación -> historia/mecanismo -> transición `[BEST-PRACTICE]`.
- [ ] Aha moment validado: alguien sin contexto dice "that's me" al leer el hook `[FUENTE REPO: cruce-cursos-aplicado.md]`.
- [ ] 3-5 beneficios concretos y específicos (no 15 genéricos) en lenguaje característica->beneficio `[FUENTE REPO: affiliate-funnel-structure.md + felipe-vergara-m04]`.
- [ ] Prueba social como plantilla ("[Name], [city]") con "results not typical" cerca `[FUENTE REPO: affiliate-compliance-nutra.md]`.
- [ ] Garantía de 60 días del vendor mencionada cerca del CTA `[FUENTE REPO: felipe-vergara-m04]`.
- [ ] Un solo CTA, repetido en los puntos lógicos del scroll, siempre el mismo destino `[FUENTE REPO: affiliate-funnel-structure.md, anti-patterns #3]`.
- [ ] 3+ variantes de hook listas para A/B sobre la misma estructura `[CRITERIO; alineado con regla de 3 variantes del equipo]`.

---

### Fuentes del repo citadas

- `01-ejecucion-2026/clickbank-2026-research/SINTESIS-VIDEOS-FOROS-2026.md` (funnel CB-Meta, bridge page, tracking)
- `01-ejecucion-2026/meta-ads-estructura-bulletproof.md` (funnel ad->bridge->HopLink, reglas anti-ban, setup CAPI)
- `00-viabilidad/research-fuentes/09-errores-foros-clickbank-meta.md` (anti-ban: tono editorial Chris Newman, direct linking, cloaking, disclaimers Meta)
- `07-learning/cursos-cruzados/felipe-vergara-m04-aplicado.md` (niveles de consciencia, triángulo dorado, feature->beneficio, copy por nivel)
- `07-learning/cursos-cruzados/cruce-cursos-aplicado.md` (7 maletas, aha moment, 6 trucos psicológicos)
- `07-learning/cursos-cruzados/felipe-vergara-m05-aplicado.md` (diversificación creativa, datos/CAPI)
- `knowledge/skills/affiliate-funnel-structure.md` (4 tipos de bridge, anatomía advertorial, tracking, mobile, tiempos de carga, anti-patterns)
- `knowledge/skills/affiliate-compliance-nutra.md` (claims prohibidos, disclaimers obligatorios, FTC, personal attributes, before/after)
- `knowledge/skills/affiliate-clickbank.md` (HopLink, gravity, refund rates, workflow)
