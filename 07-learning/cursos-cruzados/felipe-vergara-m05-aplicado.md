# Felipe Vergara · Módulo 5 · Lanzando Campañas Desde Cero — Aplicado al Affiliate

> **Curso:** Cómo Vender por Meta Ads (Felipe Vergara)
> **Módulo 5:** "Lanzando Campañas Desde Cero" (56 clases · ~25% transcrito al momento de esta síntesis)
> **Fecha síntesis:** 2026-04-28
> **Audiencia:** Cris (setup principal), Romi (estrategia campaña)
>
> Este documento extrae los frameworks accionables de M05 y los aplica al stack affiliate ClickBank + Meta Ads + hispano-US. Se actualizará cuando se completen las transcripciones restantes.

---

## Las 3 Partes Fundamentales de una Campaña Meta (clase 02)

### Estructura jerárquica

```
CAMPAÑA          → ¿QUÉ quieres? (objetivo)
   ↓
CONJUNTO DE ANUNCIOS → ¿QUIÉN, DÓNDE, CUÁNTO, CUÁNDO?
   ↓
ANUNCIOS         → ¿CÓMO se ve? (creativo, copy, link, CTA)
```

### Aplicación al affiliate

**Nivel Campaña (objetivo):**
Para affiliate ClickBank con landing intermedia → **Sales (Ventas)** con conversion event = Purchase (vía CAPI postback) o como fallback Initiate Checkout.

**Nivel Conjunto de Anuncios:**
- **Quién:** Advantage+ Audience por defecto
- **Dónde:** Advantage Placements (Meta decide)
- **Cuánto:** $50/día por conjunto al iniciar (ver SOP 04)
- **Cuándo:** Continuo (no programar fechas iniciales)

**Nivel Anuncio:**
- **FB Page + IG Account:** los del proyecto affiliate (jamás reusar de otros proyectos)
- **Texto:** copy según nivel de consciencia (ver M04 doc)
- **Arte:** uno de los 10 tipos de creativos
- **Link:** landing intermedia (NO HopLink directo)
- **CTA:** "Más información" o "Ver más" (NO "Comprar ahora" para frío)

---

## Las 4 Situaciones de Campaña (clase 03)

Felipe define 4 escenarios típicos. Para affiliate aplica el #2 (eCommerce) con landing intermedia.

| Situación | Tipo de campaña | Aplica a affiliate? |
|---|---|---|
| 1. WhatsApp / DMs | Interaction | No (affiliate no responde DMs) |
| 2. eCommerce | **Sales (Ventas)** | **SÍ — nuestro caso default** |
| 3. Lead Gen | Lead Generation | A veces (si pre-vendemos via webinar/quiz) |
| 4. Tienda física | Reach + Map | No |

**Nota:** Felipe menciona que más adelante hace clases específicas para affiliate marketing — esas son las que más nos interesan (módulos posteriores).

### Variantes de affiliate adicionales

Felipe menciona 4 industrias específicas:
- Cursos online
- **Marketing de afiliados (la nuestra)**
- Dropshipping
- Print on demand

Cuando se transcriban esas clases específicas, agregar aquí lo aplicable.

---

## Las 4 IAs de Meta · Andromeda + 3 más (clase 05)

Felipe destaca que **Andromeda** es la IA principal — la que decide a quién mostrar cada ad. Las otras 3 trabajan para optimizar otros aspectos (placement, conversion prediction, audience).

### Implicancia para affiliate
Lo importante es que **toda la estructura post-2024 de Meta favorece dejar al algoritmo decidir.**
- Advantage+ Audience > Detailed
- Advantage Placements > Manual
- Lowest Cost > Bidcap (al inicio · ver M07 cuando aplica Bidcap)

---

## Clave 1: Diversificación Creativa (clase 06) — la más importante

> "Diferentes personas responden a diferentes anuncios. Si quieres que tus campañas den buenos resultados, diseña anuncios diferentes entre sí."

### Principio clave
Andromeda categoriza tus anuncios y los muestra a diferentes "grupos de usuarios". Si todos tus anuncios son iguales, **te mantienes en un grupo pequeño**. Si son diversos, desbloqueas más grupos.

### El concepto "Entity ID" (huella digital)

**Crítico que entendamos esto:**
- En el Ads Manager cada ad tiene su propio ID
- Pero en el back-end (Andromeda), si 2 ads son **muy similares**, los consolida en la misma "huella digital"
- Anuncios con la misma huella → mismo grupo de audiencia → no escalas

### Cambios pequeños vs significativos

**Cambios pequeños (NO funcionan — misma huella):**
- Cambiar solo el texto del CTA en el ad
- Cambiar solo el headline manteniendo imagen
- Mismo creator de UGC con misma toma cambiando solo el opening

**Cambios significativos (SÍ funcionan — nueva huella):**
- Cambiar el formato (foto vs video vs reel)
- Cambiar el creator de contenido
- Cambiar el ángulo estratégico
- Mostrar producto vs lifestyle vs testimonio

### Aplicación al affiliate (CRÍTICO para Dali)

**Regla operativa para SOP 07 producción de creativos:**

Cuando Dali produce 10 variantes para un brief, NO deben ser:
- ❌ Misma persona HeyGen con 10 voice-overs distintos
- ❌ Mismo creativo con 10 textos overlay distintos
- ❌ Misma escena con 10 cortes ligeramente distintos

DEBEN ser:
- ✅ 3 personas diferentes en HeyGen (avatares distintos)
- ✅ 3 escenas distintas (cocina / sala / parque)
- ✅ Mix de formatos: 3 reels 9:16 + 3 feed 1:1 + 3 stories
- ✅ Mix de tipos de arte: 2 demostración + 2 testimonio + 2 aspiracional

**Test sencillo de diversificación:** si pongo dos creativos lado a lado y "se sienten iguales", no son diversos.

### Cómo lograr verdadera diversificación creativa

Felipe identifica 4 fuentes:
1. **Entender al cliente** (M03 del curso) → diferentes razones de compra
2. **Usar niveles de consciencia** (M04) → 5 ads por mismo producto
3. **Usar los 10 tipos de artes** (M04) → variedad estructural
4. **Usar IA para acelerar producción** (M09)

**Para affiliate:** combinar las 4 estrategias en cada brief de Dali.

---

## Clave 2: Datos de Calidad (clase 07)

> "Los datos son la sangre que alimenta tus campañas. Sin buenos datos, Meta no entiende quiénes son tus clientes."

### 3 métodos para enviar datos de calidad

#### Método 1: Pixel + CAPI (página web)

**Eventos críticos que debe disparar nuestra landing affiliate:**

| Evento | Cuándo | Quién dispara |
|---|---|---|
| **PageView** | Carga de página | Pixel automático |
| **ViewContent** | Scroll 50% | JS custom |
| **InitiateCheckout** | Click en CTA al VSL | JS custom |
| **AddPaymentInfo** | (no aplica · es del vendor) | — |
| **Purchase** | Cuando ClickBank confirma venta | **CAPI postback (servidor)** |

**Crítico:** sin el Purchase event vía CAPI, Meta no sabe quién convirtió, Andromeda no aprende, ROAS calculado es ficticio.

**Solución técnica:**
- ClickBank manda webhook/postback a nuestro servidor
- Servidor (Vercel / Cloudflare Workers) hashea email del comprador
- POST a Meta CAPI con event="Purchase" + value + currency

Esto debe ser **prioridad absoluta para Cris** en SOP 04 paso 10.

#### Método 2: CRM Sync

Felipe recomienda 3 CRMs según contexto:
- **Klaviyo** — ecommerce (pero NO aplica directo a affiliate sin email capture)
- **ActiveCampaign** — servicios B2B
- **Kommo** — WhatsApp (LATAM)

**Aplicación affiliate:** Si en Fase 3+ decidimos capturar emails (quiz pre-VSL, lead magnet), Klaviyo sería el indicado, sincronizado con Meta para crear públicos similares y excluir compradores.

#### Método 3: WhatsApp Business Tags (no aplica para nosotros)

Nuestro modelo no usa WhatsApp como canal de venta.

### Implicancia operativa

Sin Purchase event a Meta vía CAPI, **toda la diversificación creativa del mundo no nos sirve.** Andromeda optimiza ciegamente.

**Acción:** SOP 04 paso 10 (CAPI postback) NO es opcional — es bloqueante para escalar.

---

## Clave 3: Estructura Correcta (clase 08) — la más larga y rica

> "No hay una estructura que aplique al 100% de los casos. La respuesta más honesta es: depende."

### Lo que NUNCA hacer: estructura 1-1-1

**1 campaña + 1 conjunto + 1 anuncio = lineación perdedora.**

> "Tristemente veo que la mayoría de empresas que me escriben usan esta estructura. No le dan al algoritmo nada con qué optimizar."

### Las 2 posturas extremas (ambas erróneas)

**Postura A — "ser super específico":** crear muchas campañas, conjuntos micro-segmentados, intereses muy estrechos. **Ya no funciona** con las IAs actuales.

**Postura B — "darle libertad total al algoritmo":** una sola campaña con un conjunto y todo abierto. **Tampoco funciona** consistentemente para empresas reales (solo para gurús que enseñan cursos sobre cursos).

**La verdad está en el medio**, y depende de si la cuenta es nueva o tiene historial.

### Pregunta diagnóstica clave

> "¿Tu cuenta es nueva o tiene historial?"

Esto define la estructura.

### Estructura para CUENTA NUEVA (ideal para nosotros en Fase 1)

**2 campañas siempre:**

#### Campaña 1: Presentación / Tráfico Frío
- **3 conjuntos de anuncios** probando los 3 tipos de público:
  - Conjunto A: **Segmentación Detallada** (intereses)
  - Conjunto B: **Públicos Similares (Lookalike)** (después de ~50 conversiones)
  - Conjunto C: **Segmentación Abierta** (sin intereses)
- En cada conjunto: **3-5 anuncios diferentes** (diversificación creativa)

#### Campaña 2: Evaluación / Retargeting
- **1 conjunto** con públicos personalizados:
  - Visitantes web últimos 30 días
  - Engagers FB/IG últimos 30 días
  - Video viewers 50%+ últimos 30 días
- 5-6 anuncios variados (diversificación creativa)

### Estructura para CUENTA CON HISTORIAL (Fase 2-3 cuando ya tengamos data)

> "Cuando ya hay 50+ conversiones, la segmentación abierta tiende a funcionar mejor."

#### Campaña 1: Presentación
- 1-2 conjuntos con **segmentación abierta**
- Diferentes ideas de anuncios por conjunto (para escalar pruebas)
- Mantener algún conjunto con intereses si funcionó bien

#### Campaña 2: Evaluación
- Públicos personalizados (igual que cuenta nueva)

#### Campaña 3 (si tráfico alto): Conversión
- Carrito abandonado / Initiate Checkout sin Purchase
- Anuncios de urgencia + recordatorio

### Aplicación al affiliate por fase del roadmap

#### Fase 1 (mes 1) — cuenta nueva
**Estructura para primera oferta TEST:**

```
Campaña Presentación · Sales · Budget $50/día
├── Conjunto A: Detailed (intereses nutra hispano-US)
│   ├── Ad 1: Demostración (HeyGen avatar producto)
│   ├── Ad 2: Testimonio (foto cliente + frase)
│   └── Ad 3: Aspiracional (lifestyle)
├── Conjunto B: Lookalike (post-50 conversiones)
│   └── (mismos anuncios)
└── Conjunto C: Open (sin segmentación)
    └── (mismos anuncios)

Campaña Evaluación · Sales · Budget $20/día
└── Conjunto: Visitantes web 30d + engagers FB/IG
    ├── Ad 1: Recordatorio + garantía
    ├── Ad 2: Testimonio fuerte
    └── Ad 3: Beneficio diferencial
```

#### Fase 2-3 (cuando primer winner valida ROAS > 1.5x)
**Migrar a:**

```
Campaña Presentación · Budget $200-500/día
├── Conjunto A: Open (segmentación abierta, ya validada)
│   └── 5-7 anuncios variados
├── Conjunto B: Open con otra paleta de creativos
│   └── 5-7 anuncios DIFERENTES
└── Conjunto C: Detailed con intereses validados
    └── 3-5 anuncios

Campaña Evaluación · Budget $50-100/día
└── (igual a Fase 1, escalado)

Campaña Conversión · Budget $30-50/día
└── Carrito abandonado / IC sin Purchase
    └── Ads de urgencia + garantía
```

### Las exclusiones (cuándo sí, cuándo no)

> "Las exclusiones son depende. A nivel general, empezar con exclusiones y luego quitarlas si las campañas no funcionan."

**Aplicación affiliate:**
- **SÍ excluir:** compradores pasados (sincronizar via Klaviyo en Fase 3+)
- **SÍ excluir:** quienes hicieron Purchase en últimos 14 días
- **NO excluir** demasiado en cuenta nueva — limita el aprendizaje

---

## Cómo Calcular el Presupuesto (clase 10) — framework crítico

### El framework de Felipe

```
Paso 1: Meta de Ventas
   ¿Cuánto quieres vender este mes? → $X USD

Paso 2: Ticket Promedio
   ¿Cuánto te compra el cliente promedio? → $Y USD

Paso 3: Número de Ventas Necesarias
   X / Y = Z ventas

Paso 4: % del Margen para Adquisición
   ¿Qué % de tu margen estás dispuesto a invertir en adquirir cliente? → 10-30%

Paso 5: Inversión en Publicidad
   X × % = Inversión en ads
```

### Ejemplo aplicado al affiliate

**Supuesto inicial — primera oferta TEST:**
- Oferta ClickBank: AOV $147 USD, comisión 75% = **$110 USD/venta neta para nosotros**
- Conv rate landing → VSL → checkout estimada: 1.5%
- Meta de ventas mes 2 (primer winner): $3,000 USD revenue (= ~27 ventas)
- % del margen para reinversión: ClickBank afiliados típicamente reinvierten 60-70% del primer dólar (sin retener tanto margen al inicio)

**Cálculo:**
- 27 ventas × $110 = $2,970 revenue
- Si reinvertimos 60% → $1,782 USD ad spend
- $1,782 / 30 días = **$60/día budget total**

**Comparación con los $50/día sugeridos en SOP 04:** alineado.

### Tabla aplicada a 3 escenarios

| Escenario | Revenue mes | Reinversión | Daily budget | Ventas necesarias |
|---|---|---|---|---|
| Conservador (Fase 1) | $1,500 | 60% = $900 | $30/día | 14 |
| Validación (Fase 2) | $3,000 | 65% = $1,950 | $65/día | 27 |
| Escalado inicial (Fase 3) | $10,000 | 70% = $7,000 | $230/día | 91 |
| Operación madura (Fase 4) | $30,000+ | 60% = $18,000 | $600/día | 273+ |

### Reglas operativas derivadas

1. **Nunca lanzar campaña sin esta math hecha** (parte de SOP 01)
2. **Documentar en `02-offers/[oferta-XX]/economics.md`** los 5 pasos del framework
3. **Si la math no cierra** (ej: necesitas $10/click pero CPC industria es $3), **NO lanzar**

---

## Tres preguntas que la cuenta debe responder antes de cualquier decisión

Felipe es enfático sobre el "depende" — para resolverlo, sus 3 preguntas filtro:

### 1. ¿Cuánto presupuesto tengo?
- < $30/día → cuenta nueva, estructura conservadora
- $30-100/día → estructura validación
- $100-500/día → escalar lo que funciona
- $500+/día → multi-campaña, segmentación abierta dominante

### 2. ¿Qué historial tiene la cuenta?
- 0 conversiones → estructura cuenta nueva (3 conjuntos + retargeting)
- 50-100 conversiones → empezar a usar segmentación abierta
- 100+ conversiones → segmentación abierta dominante

### 3. ¿Qué objetivo persigo?
- Validar oferta nueva → pequeño budget, múltiples conjuntos
- Escalar winner → grande budget, pocos conjuntos optimizados
- Recuperar carritos → budget pequeño, retargeting agresivo

### Aplicación equipo

**Romi/Cris en SOP 06 (decisión semanal):** antes de cualquier scale/kill, responder estas 3 preguntas explícitamente en el weekly report. Esto previene decisiones por feeling.

---

## Cambios concretos a nuestras SOPs derivados de M05

### Cambios a SOP 01 (Selección oferta)
**Agregar en paso 7 (math de economics):** usar el framework de 5 pasos de Felipe (clase 10). Documentar en `02-offers/[oferta-XX]/economics.md` con esa estructura.

### Cambios a SOP 04 (Setup funnel)
**Reescribir paso 8 (Cuenta publicitaria Meta):** estructura inicial debe ser:
- Campaña Presentación con **3 conjuntos** (no 1)
- Cada conjunto con **3-5 anuncios** diversificados (no 1)
- Campaña Evaluación con 1 conjunto retargeting

**Elevar prioridad paso 10 (CAPI postback):** **bloqueante** para considerar setup completo.

### Cambios a SOP 06 (Análisis semanal)
**Agregar checklist pre-decisión:**
- [ ] ¿Qué presupuesto disponible para próxima semana?
- [ ] ¿Cuántas conversiones acumulé en cuenta?
- [ ] ¿Qué objetivo es prioritario (validar / escalar / convertir)?

**Agregar regla:** si ROAS de un conjunto está bien pero el aprendizaje aún no está completo (< 50 conversiones), **NO killear** aunque el ROAS individual fluctúe.

### Cambios a SOP 07 (Producción creativos)
**Agregar regla de diversificación:** cada batch de 10 creativos debe pasar el "test entity ID":
- Mínimo 3 personas/avatares distintos
- Mínimo 3 tipos de artes (de los 10 de M04)
- Mínimo 2 formatos (9:16 + 1:1 mínimo)

Si todos se "sienten iguales", regenerar antes de entregar a Cris.

### Cambios al skill `affiliate-funnel-structure.md`
**Agregar sección "Pixel + CAPI":** el postback es bloqueante, no opcional.
**Agregar referencia:** este documento + framework de presupuesto de Felipe.

---

## Pendientes cuando completen las 44 transcripciones restantes de M05

Clases que aún esperan ser transcritas y que probablemente añadirán valor:

- **Cómo configurar campañas paso a paso** (las 4 situaciones)
- **Investigación de mercado y sesgos psicológicos** (parcial, hay 1 clase)
- **Rastreador de actividad de campañas**
- **Cómo nombrar campañas / conjuntos / anuncios** (en proceso)
- **Actualizar públicos** (en proceso)
- **Optimizar retargeting**
- **Probar nuevos tipos de anuncios** (rendimiento de creativos)
- **Diferentes objetivos detallados** (ASC, Sales, Lead Gen)

**Cuando estén listas, actualizar este documento.**

---

## Insight maestro de M05

Toda esta estructura se reduce a:

> "Tu trabajo no es controlar al algoritmo. Tu trabajo es **alimentarlo bien** (data + creatividades diversas) y **darle el espacio correcto** (estructura adecuada según historial). Andromeda hace el resto."

**Aplicado al affiliate:** nuestro éxito o fracaso lo define más:
- La oferta elegida (Romi en SOP 01)
- La diversificación creativa (Dali en SOP 07)
- El postback CAPI funcionando (Cris en SOP 04)

**Que NO lo define:**
- Micro-segmentaciones de intereses
- "Trucos" de configuración
- Bidcap vs Lowest Cost (al inicio)

---

*Este documento se actualizará después de transcribir las 44 clases pendientes de M05 + comparar con realidad operativa después de aplicar 30 días.*
