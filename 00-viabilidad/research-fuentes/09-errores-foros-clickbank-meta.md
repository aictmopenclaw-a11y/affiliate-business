# 09 · Errores reales de foros: ClickBank + Meta Ads (afiliados)

> **Objetivo:** aprender de los errores ajenos ANTES de gastar dinero. Investigación de foros y comunidades (BlackHatWorld, Warrior Forum, affLIFT, AffiliateFix, Quora) para extraer casos reales de fracaso, bans, problemas de tracking, compliance y cash flow en el modelo afiliado ClickBank + Meta Ads, nutra/health, mercado USA.
>
> **Contexto del equipo:** arranque affiliate ClickBank + Meta Ads, mercado USA inglés, nicho nutra/health, capital $2-5K USD.
>
> **Fecha de investigación:** 2026-06-15
> **Metodología:** firecrawl (scraping de foros) + WebSearch (snippets institucionales). Citas verbatim con link a la fuente. Cada hallazgo marcado: `[VERIFICADO]` (números/políticas confirmadas en fuente primaria) · `[ANECDÓTICO]` (testimonio individual de un usuario) · `[CONSENSO COMUNIDAD]` (repetido por múltiples usuarios independientes).
>
> **Nota de acceso:** Reddit bloqueó todos los métodos de acceso automatizado (WebFetch, WebSearch con dominio reddit.com, firecrawl: los tres devolvieron "no soportado/bloqueado"). El contenido de Reddit aparece solo vía snippets de búsqueda general, no como cita directa. Las citas verbatim de este documento provienen de foros que SÍ permiten scraping: BlackHatWorld, Warrior Forum, affLIFT, AffiliateFix y Quora. Esto se documenta abajo en cada caso.

---

## 1. Resumen ejecutivo: los 5 errores más letales

1. **Direct linking a la oferta ClickBank desde Meta = ban casi garantizado.** Es el error #1 y el más repetido en todos los foros. No importa si la landing es "Facebook-friendly": tarde o temprano cae la cuenta, y cuando cae una, pueden caer todas las asociadas. `[CONSENSO COMUNIDAD]`

2. **Subestimar el muro de tiempo y dinero.** El dato institucional de ClickBank es demoledor: **promedio de 570 días desde que creas la cuenta hasta tu primer cheque** como afiliado. El que entra esperando ROAS en la primera semana con $500 quema el capital antes de aprender. `[VERIFICADO]`

3. **Tracking roto = optimizas a ciegas.** Caso documentado: integración OptinMonster↔Drip no trackeaba, el Pixel reportaba números distintos a los reales, y el media buyer terminó tomando decisiones con data inexacta de Facebook. Sin atribución confiable no sabes qué apagar ni qué escalar. `[ANECDÓTICO]` reforzado por `[CONSENSO COMUNIDAD]`.

4. **El cuello de botella no es generar leads baratos, es monetizarlos.** Múltiples casos: leads a $0.92-$2 conseguidos sin problema, pero 1600 leads/mes terminaron en break-even, o 1 sola venta tras $180 de spend. El email/autoresponder mal armado mata el negocio. `[CONSENSO COMUNIDAD]`

5. **Cash flow de ClickBank te puede sangrar antes de cobrar.** Customer Distribution Requirement (5 ventas con 2+ métodos de pago antes del primer pago), dormant fees que escalan a $50/periodo, y chargebacks con penalidad no reversible incluso después de los 60 días. Puedes "ganar" y terminar en $0. `[VERIFICADO]`

---

## 2. Errores por categoría

### 2.1 Errores de selección de oferta

**Promover producto demasiado competido o sin demanda real.** El error de selección más citado. Quora consolida la lista de fallos:

> "Product Selection: Choose wisely. Promoting the wrong products or services can lead to failure. Align your choices with the needs and preferences of your target audience."
> Atribución: Nwaukwa Charles, [Quora: "Why do people fail on ClickBank?"](https://www.quora.com/Why-do-people-fail-on-ClickBank) `[CONSENSO COMUNIDAD]`

> "many people make the mistake of promoting a product that is too competitive or has no demand."
> Atribución: síntesis de respuestas en [Quora / ClickBank blog](https://www.clickbank.com/blog/affiliate-marketing-mistakes-to-avoid/) `[CONSENSO COMUNIDAD]`

**Traducción / lección:** elegir la oferta es un acto de equilibrio. Gravity demasiado alto = saturado; demasiado bajo = no convierte. El sweet spot mencionado por afiliados está entre **15-70 de gravity para principiantes** (menos competencia) y **50-200 para validados** (ventas probadas).

> "When I started ClickBank, I got my first sale in about 3 weeks, but it was also a refund that happened…"
> Atribución: Vivian Murga, [Quora: "Why did I fail to sell ClickBank's product?"](https://www.quora.com/Why-did-I-fail-to-sell-ClickBanks-product) `[ANECDÓTICO]`

> **Traducción:** "Cuando empecé en ClickBank, hice mi primera venta en unas 3 semanas, pero fue una venta que terminó en reembolso."
> **Lección:** la primera venta no es el hito real. La primera venta *que sobrevive a los 60 días de garantía* lo es. Ofertas nutra exclusivamente digitales tienen tasas de reembolso más altas.

**El producto deja de convertir y no sabes por qué (riesgo de oferta "quemada").** Caso del afiliado que vio caer su producto:

> "Some guy wrote a while back here that his clickbank sales went from $2000 per week to $100 on clickbank. Digistore24 offered the same product, so switched out the links and sales went back to $2000 per week."
> Atribución: Allark, [BlackHatWorld: "Clickbank affiliate here, feeling a little lost"](https://www.blackhatworld.com/seo/clickbank-affiliate-here-feeling-a-little-lost.1601068/) `[ANECDÓTICO]`

> **Traducción:** "Alguien escribió aquí hace tiempo que sus ventas en ClickBank cayeron de $2000/semana a $100. Digistore24 ofrecía el mismo producto, cambió los links y las ventas volvieron a $2000/semana."
> **Lección:** la misma oferta puede rendir distinto según la red/plataforma. No casarse con ClickBank: tener Digistore24 como alternativa para A/B de plataforma.

---

### 2.2 Errores de Meta Ads (bans, estructura, audiencias, presupuesto)

**EL error letal: direct linking → ban.** Es el consenso más fuerte de toda la investigación.

> "Don't direct link it — my housemate and I lost several accounts years ago and they're still pretty strict."
> Atribución: Social God (Supreme Member), [BlackHatWorld: "Can I send Facebook ads to clickbank offer?"](https://www.blackhatworld.com/seo/can-i-send-facebook-ads-to-clickbank-offer.1504449/) `[ANECDÓTICO]`

> **Traducción:** "No hagas direct link: mi compañero de piso y yo perdimos varias cuentas hace años y siguen siendo bastante estrictos."

> "you will probably get banned at some point. facebook usually catches people running clickbank in the long run.. whether you use landing page or not. in fact, facebook will ban you even if you promote white hat offer, it happens."
> Atribución: peux pas (Senior Member), [BlackHatWorld](https://www.blackhatworld.com/seo/can-i-send-facebook-ads-to-clickbank-offer.1504449/) `[CONSENSO COMUNIDAD]`

> **Traducción:** "Probablemente te baneen en algún momento. Facebook usualmente caza a la gente que corre ClickBank a la larga... uses landing page o no. De hecho, Facebook te banea incluso si promueves una oferta white hat, pasa."

> "NO! You will get banned eventually."
> Atribución: T J Tutor (Administrador del foro), respondiendo si se puede linkear directo a la landing "Facebook-friendly" de Custom Keto Diet. [AffiliateFix: "Is it possible to direct link to a Clickbank offer using Facebook Ads?"](https://www.affiliatefix.com/threads/is-it-possible-to-direct-link-to-a-clickbank-offer-using-facebook-ads.175915/) `[CONSENSO COMUNIDAD]`

> "I wouldn't do any direct linking without a lander you're just asking for trouble. If 1 account gets banned using the URL, i heard you all get banned from FB ads."
> Atribución: wayne12, [AffiliateFix](https://www.affiliatefix.com/threads/is-it-possible-to-direct-link-to-a-clickbank-offer-using-facebook-ads.175915/) `[ANECDÓTICO]`

> **Traducción:** "No haría direct linking sin un lander, estás buscando problemas. Si una cuenta cae usando esa URL, escuché que las baneas todas en FB ads."

**Ban incluso teniendo cuenta vieja "durable".**

> "I was banned for promoting an affiliate product. 5 year old FB account disabled."
> Atribución: tc888, [Warrior Forum: "Can I get banned for clickbank products on facebook?"](https://www.warriorforum.com/pay-per-click-search-engine-marketing-ppc-sem/1161023-can-i-get-banned-clickbank-products-facebook.html) `[ANECDÓTICO]`

> **Traducción:** "Me banearon por promover un producto afiliado. Cuenta de FB de 5 años, deshabilitada." (En su apelación subió ID y recibió cierre permanente sin opción de crear cuentas nuevas.)

**Estructura de campaña: error de cortar mal los ad sets perdedores.**

> "The only part of the last post that didn't make sense is that you cut the budget of the poor performers in half. Why do that at all? If they are performing poorly why wouldn't you cut them out and move on."
> Atribución: Notion, criticando la decisión de Drought de bajar presupuesto a ad sets malos en vez de matarlos. [BlackHatWorld: "Facebook Ads + Clickbank Journey to $10,000/month"](https://www.blackhatworld.com/seo/facebook-ads-clickbank-journey-to-10-000-month.1040654/) `[ANECDÓTICO]`

> **Lección:** consenso de media buying: ad set que no rinde se mata, no se "rescata" bajándole budget. Bajar budget reduce data y alarga el learning phase sin arreglar el problema de fondo.

**Error de targeting/setup inicial documentado por el propio media buyer (caso Drought):**
- Targeting solo a **desktop** "porque me dio flojera hacer la landing mobile-friendly" (lol): perdió el grueso del tráfico hasta que cambió a mobile y los CPA bajaron de inmediato.
- Cita textual: *"All the ad sets are only targeting desktop because I was too lazy to make my landing page mobile friendly (lol)."* `[ANECDÓTICO]`

**Presupuesto: dos errores opuestos, ambos fatales.** Consenso institucional + foros:
- Spending demasiado poco → la campaña muere antes de salir del learning phase (Meta necesita ~50 conversiones/semana para salir del learning). `[VERIFICADO]`
- Para una oferta con CPA $5: mínimo $50/día. Para oferta de payout alto con CPA $70-100: $150-200/día. `[VERIFICADO]` ([ROIAds](https://roiads.co/blog/affiliate-test-budget-for-ad-campaigns/), [ROASPIG](https://roaspig.com/blog/minimum-viable-budget-testing-facebook-ads))
- Recomendación de presupuesto realista para 1-2 ad sets bien financiados: **$1,500-$3,000/mes**, más 20-30% de "desperdicio de learning phase". `[VERIFICADO]`

> "I would start with one traffic source and learn the numbers first because throwing money at sites and ads without testing usually ends bad."
> Atribución: CashPhantom (Jr. VIP), [BlackHatWorld: "Do you make money with Clickbank?"](https://www.blackhatworld.com/seo/do-you-make-money-with-clickbank-want-your-honest-opinion.1812856/) `[CONSENSO COMUNIDAD]`

> **Traducción:** "Empezaría con una sola fuente de tráfico y aprendería los números primero, porque tirar dinero a sitios y ads sin testear usualmente termina mal."

**Riesgo de comprar cuentas "aged" / agency accounts para evadir bans.** Práctica común en el espacio, pero con su propio riesgo:
> "A previously clean ad account can get flagged within hours if Facebook detects it's being accessed from the same fingerprint as a banned account."
> Atribución: [Multilogin / Octo Browser, guías de cuentas aged 2026](https://multilogin.com/blog/buy-facebook-aged-accounts/) `[CONSENSO COMUNIDAD]`
> **Lección:** las "farmed accounts" son baratas y buenas para volumen, pero tienen **alto riesgo de ban**. Si accedes desde el mismo fingerprint (huella de navegador/IP) que una cuenta baneada, contaminas la nueva en horas. Si el equipo va por esta ruta, necesita antidetect browser + proxies dedicados, lo que añade costo y complejidad.

---

### 2.3 Errores de tracking / atribución (CAPI)

**Caso completo documentado: la integración rota (Drought):**

> "there is a discrepancy between the number of leads that were actually generated and the number Facebook reports… I'm using OptinMonster for my optin form and Drip for my email marketing/autoresponder, and unfortunately the 2 do not integrate nicely… none of the Source Tags tracked correctly. All I have to go off of is Facebook['s] inaccurate data."
> Atribución: Drought, [BlackHatWorld journey thread](https://www.blackhatworld.com/seo/facebook-ads-clickbank-journey-to-10-000-month.1040654/) `[ANECDÓTICO]`

> **Traducción:** "Hay una discrepancia entre el número de leads que realmente generé y el número que reporta Facebook… Uso OptinMonster para el formulario y Drip para el email/autoresponder, y los dos no integran bien… ninguno de los Source Tags trackeó correctamente. Lo único que tengo es la data inexacta de Facebook."
>
> Tuvo además que *"hack together a way of tracking form submits with the Facebook Pixel, which might not be perfect."*
>
> **Lección:** el stack de tracking se valida ANTES de gastar el primer dólar. Si la atribución por fuente no funciona, optimizas a ciegas: no sabes qué creativo/audiencia/ad set genera la venta real. En afiliado esto es peor que en e-commerce porque la venta ocurre en el dominio de ClickBank (server-to-server), no en tu sitio.

**El problema estructural de CAPI en afiliado (institucional):**
- ClickBank usa la **Facebook Conversion API** para mandar eventos server-to-server. Para que la atribución funcione hay que asegurar que el **Meta Click ID (fbclid)** se anexe a los hoplinks de ClickBank. `[VERIFICADO]` ([AnyTrack](https://anytrack.io/connect-facebookads-and-clickbank), [ClickBank S2S docs](https://support.clickbank.com/en/articles/10535369-s2s-tracking-integration-meta-facebook-pixel))
- "CAPI issues rarely announce themselves with obvious errors—they quietly stop sending accurate data to Meta's algorithm, leaving campaigns to optimize on incomplete information." `[VERIFICADO]` ([Cometly](https://www.cometly.com/post/how-to-fix-facebook-conversion-api))
- **Lección:** los fallos de CAPI son silenciosos. No hay error rojo; simplemente el algoritmo optimiza con data incompleta. Hay que monitorear EMQ (Event Match Quality) y volumen de eventos activamente, no asumir que "está conectado = funciona".

**Sensación de "ClickBank no me muestra todas las ventas" (gap de atribución percibido).**

> "Either Facebook is sending shit traffic… or clickbank is not showing all my sales."
> Atribución: Maidos (1.5 años de afiliado), [BlackHatWorld: "feeling a little lost"](https://www.blackhatworld.com/seo/clickbank-affiliate-here-feeling-a-little-lost.1601068/) `[ANECDÓTICO]`

> "I have a feeling clickbank must be secretly gobbling up your money. I have 4-5 clickbank accounts, testing the same products, same pages, and when they get to $2000 a day they can shrink and no one will even buy anymore."
> Atribución: Good_Agency_Ads (Supreme Member, Jr. VIP), mismo thread. `[ANECDÓTICO]`

> **Traducción:** "Tengo la sensación de que ClickBank debe estar comiéndose tu dinero en secreto. Tengo 4-5 cuentas de ClickBank, testeando los mismos productos, las mismas páginas, y cuando llegan a $2000/día se encogen y ya nadie compra."
>
> **Interpretación honesta:** esto probablemente NO es ClickBank "robando", sino un cóctel de (a) atribución rota, (b) fatiga de creativo/audiencia al escalar, y (c) reembolsos que recortan el neto. Pero ilustra que cuando el tracking no es sólido, el afiliado pierde confianza en sus propios números y empieza a culpar a la plataforma. **Sin tracking limpio no hay diagnóstico.**

---

### 2.4 Errores de compliance (qué hace banear cuentas)

**Landing con tono de venta = detectada como afiliado puro.**

> "The landing page must have an informative tone and NOT a sales / marketing tone, otherwise the algorithms of FB Ads will detect it as pure affiliate marketing."
> Atribución: Chris Newman, [BlackHatWorld](https://www.blackhatworld.com/seo/can-i-send-facebook-ads-to-clickbank-offer.1504449/) `[CONSENSO COMUNIDAD]`

> **Traducción:** "La landing debe tener tono informativo y NO tono de venta/marketing, sino los algoritmos de FB Ads la detectan como puro marketing de afiliado."
> **Lección:** el bridge/pre-lander debe aportar valor real (contenido, quiz, artículo informativo), no ser un puente transparente a la oferta. Meta exige una landing "que poseas, con valor por sí misma".

**Cloaking: funciona pero es la zona roja absoluta.**

> "Facebook with Clickbank can be done with proper strategy and good cloaking."
> Atribución: Zera Api, [BlackHatWorld](https://www.blackhatworld.com/seo/can-i-send-facebook-ads-to-clickbank-offer.1504449/) `[ANECDÓTICO / blackhat]`

> **ADVERTENCIA:** el cloaking (mostrar a Meta una página y al usuario otra) viola explícitamente las políticas de Meta y puede derivar en **ban permanente del ad account, acción legal de Meta y responsabilidad civil** si hay fraude. `[VERIFICADO]` ([Meta Transparency Center](https://transparency.meta.com/policies/ad-standards/), [adlibrary.com sobre ad cloaking](https://adlibrary.com/posts/ad-cloaking-on-meta)). **Recomendación para el equipo: NO cloaking.** Es incompatible con un negocio sostenible y con el aislamiento de riesgo de una agencia.

**Claims de salud sin disclaimer = rechazo automático (regla 2026).**
- Meta ahora exige que TODOS los ads de suplementos incluyan el disclaimer *"This product is not intended to diagnose, treat, cure, or prevent any disease"* **en el copy del ad**, no solo en la landing. Sin eso = rechazo automático. `[VERIFICADO]` ([auditsocials Meta policy 2026](https://www.auditsocials.com/blog/meta-ad-policy-updates-2026-guide))
- Meta expandió el programa de verificación de anunciantes de salud para incluir marcas de suplementos y wellness: claims clínicos requieren **certificación LegitScript** o limitar el copy a lenguaje de wellness general. `[VERIFICADO]`
- **Lección crítica para nutra:** el nicho elegido (health/nutra) es precisamente el más vigilado. Antes de gastar, el equipo necesita (a) disclaimer obligatorio en cada ad, (b) decidir si va por certificación LegitScript o por copy de wellness suave, (c) entender que claims de "pierde X kilos" o "cura Y" son ban instantáneo.

---

### 2.5 Errores de cash flow (CDR, reembolsos, dormant fees)

**Customer Distribution Requirement (CDR): no cobras hasta cumplirlo.** `[VERIFICADO]`

> "You have to meet their CDR (customer distribution requirement) and make the correct number of sales with the correct number of payment methods."
> Atribución: Janet Sawyer, [Warrior Forum: "Clickbank Took My Money...Seeking Advice!"](https://www.warriorforum.com/main-internet-marketing-discussion-forum/732049-clickbank-took-my-money-seeking-advice.html)

> "Make sure you get 5 credit card transactions (all different and unique), and they will clear you for getting your funds sent to you."
> Atribución: Randall Magwood, mismo thread.

> **Regla oficial:** mínimo **5 ventas usando al menos 2 métodos de pago distintos** antes del primer pago. Diseñada para evitar fraude de rebates. `[VERIFICADO]`

**Dormant fees: tu balance positivo se evapora si no hay ventas.** `[VERIFICADO]`

> "Dormant accounts are subject to a charge of $1 per pay period after 90 days of no earnings, $5 per pay period after 180 days of no earnings, and $50 per pay period after 365 days of no earnings."
> Atribución: WillR, [Warrior Forum](https://www.warriorforum.com/main-internet-marketing-discussion-forum/732049-clickbank-took-my-money-seeking-advice.html)

> "Clickbank has charged me dormant fees and my account is back to $0."
> Atribución: Daveyz (original poster), mismo thread. `[ANECDÓTICO]`

> "ClickBank will deduct certain amount from your earnings every two weeks until your balance is zero. I have also lost $90 in this way."
> Atribución: jeffreyhuan, mismo thread. `[ANECDÓTICO]`

> **Traducción:** "ClickBank deduce cierta cantidad de tus ganancias cada dos semanas hasta que tu balance llega a cero. Yo también perdí $90 así."
> **Lección:** las dormant fees corren **incluso si todavía no cumpliste el CDR**. Si el equipo deja una cuenta con balance y sin ventas, el dinero se erosiona ($1→$5→$50 por periodo). No abrir la cuenta hasta estar listo para vender.

**Costo de cobro internacional (relevante para equipo en Chile / fuera de USA):**

> "my bank charges $50 for foreign checks. So I dont want to be paying $50 to the bank everytime i make some money."
> Atribución: Daveyz, [Warrior Forum](https://www.warriorforum.com/main-internet-marketing-discussion-forum/732049-clickbank-took-my-money-seeking-advice.html) `[ANECDÓTICO]`
> **Lección:** verificar el método de pago (wire vs cheque vs Payoneer) y su costo. Un cheque extranjero puede costar $50 por cobro. Configurar wire/Payoneer desde el inicio.

**Chargebacks: penalidad no reversible, incluso después de los 60 días.** `[VERIFICADO]` (es como CB documenta su propia política, citada por un seller)

> "A chargeback occurs when the cardholder goes directly to his or her bank to dispute a charge… a chargeback penalty has also been debited from your account… Regrettably, the chargeback penalty is not reversible even if the customer asks his or her bank to cancel the dispute or repurchases the product."
> Atribución: email de ClickBank citado por el seller "Mike", [Warrior Forum: "Is Clickbank's Refund Policy A Joke?"](https://www.warriorforum.com/main-internet-marketing-discussion-forum/326974-clickbanks-refund-policy-joke.html) `[VERIFICADO]`

> Contexto del seller: *"For the first time ever, I had a customer do a charge back a month after the 60 day Clickbank refund policy expired… So I've been wacked an additional fee for the chargeback that happens AFTER the money-back guarantee period is over."*
>
> **Traducción:** "Por primera vez, un cliente hizo un chargeback un mes después de que venció la política de reembolso de 60 días… Me golpearon con una fee adicional por un chargeback que ocurre DESPUÉS de que terminó el periodo de garantía."
> **Lección (para afiliado):** si te pagaron comisión y luego hay reembolso/chargeback, ClickBank retiene una **"return allowance"** y recupera lo pagado. En nutra, donde la tasa de reembolso es alta, esto recorta el neto de forma material. El ROAS bruto en Meta NO es tu ganancia real; hay que restar reembolsos.

---

## 3. Casos de éxito verificables (con números)

### Caso A: affLIFT: Nutra (Reduslim), España, +154% ROI `[VERIFICADO]`
Fuente: [affLIFT: "Case Study: 154% ROI on Nutra offer"](https://afflift.com/f/threads/case-study-154-roi-on-nutra-offer.9562/) (por LuckyOnline, media buyer de Rich Media)

| Métrica | Valor |
|---|---|
| Oferta | Reduslim (weight-loss) |
| GEO | España |
| Periodo | 1 May – 5 Jun 2022 (~5 semanas) |
| Total leads | 4,286 |
| Leads aprobados | 1,264 (29.49%) |
| Ad spend | $21,654 |
| Revenue bruto | $55,120 |
| **Profit** | **$33,466** |
| **ROI** | **154%** |

**Cómo lo lograron (criterios reales):** oferta evergreen (weight loss "nunca pasa de moda"), pre-lander recomendado por el affiliate manager, white page (sitio WP adaptado a gimnasios en español, 1 WP por cada 10-20 lanzamientos en cuentas de límite bajo) + black page (landing + order form con enfoque celebrity-endorsed tras varios split tests).
**Advertencia:** este caso usa la mecánica white page / black page (cloaking) típica de nutra agresivo. **Es exactamente la práctica que dispara bans y riesgo legal en Meta.** Sirve como referencia de *unit economics* posibles, NO como método replicable de forma compliant.

### Caso B: Warrior Forum: ClickBank direct linking vía Bing (no Meta) `[ANECDÓTICO]`
Fuente: [Warrior Forum: "Clickbank direct linking success"](https://www.warriorforum.com/main-internet-marketing-discussion-forum/1417316-affiliate-case-study-clickbank-direct-linking-success.html)

> "I tested three different products. Since then with one product I made sales. 15th Aug $245.16 / 16th Aug $203.96 / 17th Aug $102.21"
> Atribución: Thomas (WalkingYellow), primer fin de semana de testeo (~3 días). `[ANECDÓTICO]`

Mecánica: **Bing Ads** (no Facebook) con direct link a la sales page, bid en exact match del nombre del producto, hoplink en el tracking template. CPC ceiling $2-3 (a veces $5+). Regla del autor: *"spend 3x the commission payout before deciding profitability"* y *"junk a campaign earlier if it's not making sales."*
**Lección clave:** el direct linking que sí funciona estable es en **Bing/Google con tráfico de intención (brand bidding)**, no en Meta. Bing es más tolerante con afiliados.

### Caso C: STM / AdWords nutra `[ANECDÓTICO]`
Vía snippet de búsqueda: un afiliado reportó cruzar **$40K en julio 2018** corriendo tráfico AdWords a ofertas nutra (trial + straight sale); otro mencionó "5-figure profit months when direct-linking from AdWords". Fuente: STM Forum (contenido mayormente detrás de paywall, no verificable verbatim). `[ANECDÓTICO]`

### Caso D: El afiliado de mediano plazo (realismo) `[ANECDÓTICO]`
> "I have been a clickbank affiliate for 1.5 years now. I have been able to make some profit the last 5 months. Around 20 to 30k. But lately I feel like something is wrong… scaling has been almost impossible."
> Atribución: Maidos, [BlackHatWorld](https://www.blackhatworld.com/seo/clickbank-affiliate-here-feeling-a-little-lost.1601068/)
> **Lección:** 1.5 años para llegar a profit consistente ($20-30K en 5 meses), y aun así el escalado es el muro. Esto es lo "exitoso realista": no es pasivo, no es rápido, y plateau es la norma.

---

## 4. Cómo eligen ofertas los que sí ganan (criterios de foros)

Consolidado de affLIFT, Warrior Forum, Quora y docs de ClickBank: `[CONSENSO COMUNIDAD]` + `[VERIFICADO]`

1. **Gravity en el sweet spot, no el más alto.** Principiantes: gravity **15-70** (menos competencia, ventas probadas). Validados: **50-200**. Gravity = nº de afiliados únicos con comisión en las últimas 12 semanas, ponderado a ventas recientes. Gravity altísimo = saturado y lleno de afiliados que venden pero no son rentables. ([ClickBank Gravity explained](https://www.clickbank.com/blog/clickbank-gravity-score/))

2. **EPC > tu CPC.** Calcular Earnings Per Click apenas empiezas a promover, para confirmar que ganas más de lo que gastas por clic. *"calculate your EPC to make sure you're making more money than you're spending."* ([ClickBank FAQ](https://www.clickbank.com/blog/affiliate-marketing-faq/))

3. **Average Payout Value (APV) alto.** Ofertas con upsells/order bumps suben el AOV y dan margen para pagar tráfico caro.

4. **Calidad de la sales page del vendor + recursos disponibles.** Vendors que dan pre-landers, swipes, creativos probados. El media buyer de affLIFT usó el pre-lander que le recomendó su affiliate manager.

5. **Oferta evergreen sobre fad.** Weight-loss, dinero, relaciones, salud: demanda perpetua. *"Nothing lasts forever. Except, maybe, for the weight loss topic."* (LuckyOnline, affLIFT).

6. **Brand bidding como señal de validación.** Si ves afiliados pujando por keywords de marca de la oferta (ej. "mitolyn review", "is mitolyn legit"), es señal de que la conversión es alta:
> "if you see google ads, when you search those [brand] keywords, run by affiliates that means google ads conversion is high."
> Atribución: IM Dude (Elite Member), [BlackHatWorld](https://www.blackhatworld.com/seo/do-you-make-money-with-clickbank-want-your-honest-opinion.1812856/) `[ANECDÓTICO]`

7. **Tener la misma oferta en 2 redes (ClickBank + Digistore24).** Para A/B de plataforma y cobertura si una "quema" el link.

---

## 5. Expectativas realistas de timeline

- **Dato institucional duro:** promedio de **570 días desde crear la cuenta hasta el primer cheque** como afiliado ClickBank. `[VERIFICADO]` ([ClickBank blog "first sale"](https://www.clickbank.com/blog/how-to-make-your-first-sale-on-clickbank/)). Excepción: quien ya tiene audiencia o sabe correr ads puede generar comisiones casi de inmediato.
- **Primera venta vs primera venta rentable:** "first sale in about 3 weeks, but it was also a refund" (Vivian Murga, Quora). La primera venta puede llegar en semanas; la rentabilidad neta sostenida tarda mucho más. `[ANECDÓTICO]`
- **Caso Drought (Meta + ClickBank):** Día 1 = 7 leads a $3.85 CPA con $26.98 de spend. Tras ~$180 de spend total = **1 sola venta**, *"not sure if I will ever be breaking even, much less profitable."* Puso el proyecto en pausa. El objetivo era $10K/mes. `[ANECDÓTICO]`
- **Caso Maidos:** ~18 meses hasta profit consistente; aun así el escalado es el muro. `[ANECDÓTICO]`
- **Regla del media buyer:** *"spend 3x the commission payout before deciding profitability"*: no matar ni declarar ganador antes de gastar 3× el payout de comisión. `[CONSENSO COMUNIDAD]`
- **Learning phase de Meta:** ~50 conversiones/semana por ad set para salir del learning. Con CPA real de afiliado (a veces $30-100) eso son $1,500-$5,000/semana de spend *por ad set* para optimizar limpio. Implicación directa para capital $2-5K: alcanza para **1 test serio, no para "probar varias ofertas a la vez"**. `[VERIFICADO]`

**Síntesis de timeline honesto:** con $2-5K, mercado USA, nutra, lo realista es **3-6 meses de aprendizaje a pérdida o break-even** antes de tener una oferta+ángulo+tracking que funcione, asumiendo ejecución disciplinada. Quien proyecte ROAS positivo en mes 1 va a quemar el capital.

---

## 6. Lo que NADIE menciona pero deberían (gaps)

1. **La verdad incómoda del consenso de foros 2026:** la mayoría de los veteranos cree que ClickBank+afiliado clásico ya no es la mejor jugada.
   > "There are lot of ways to make money with clickbank but it ain't it."
> Atribución: >  IM Dude (Elite Member, 11K mensajes), [BlackHatWorld](https://www.blackhatworld.com/seo/do-you-make-money-with-clickbank-want-your-honest-opinion.1812856/) `[CONSENSO COMUNIDAD]`
   Los métodos que él lista como "que funcionan" son parasite SEO, forum spamming, sponsored posts, FB ads y native ads: varios de ellos black/grey hat. El espacio compliant + rentable es estrecho.

2. **El cuello de botella real es la monetización del lead, no el lead.** Casi todos los que fracasan generan leads baratos y luego no saben convertir:
   > "I managed to capture ~1600 leads in a month but ended up just breaking even and got discouraged."
> Atribución: >  cjmfootball8, [BlackHatWorld journey thread](https://www.blackhatworld.com/seo/facebook-ads-clickbank-journey-to-10-000-month.1040654/) `[ANECDÓTICO]`
   El email/autoresponder, la secuencia de nurture, el deliverability (no caer en "Promotions" de Gmail) son la mitad del negocio y casi nadie los planifica. Drought peleó con 15.4% de open rate y deliverability.

3. **El riesgo de plataforma es doble y simultáneo.** Puedes hacer todo bien en Meta y aun así perder por el lado de ClickBank (oferta que "se encoge", reembolsos, dormant fees, oferta retirada por el vendor). El afiliado tiene CERO control sobre la oferta: el vendor puede cambiar precio, sales page o cerrar la oferta de un día para otro. **No se construye activo propio**: es alquiler de tráfico hacia activo ajeno.

4. **Aislamiento de identidad / fingerprint.** Nadie principiante piensa en esto hasta que cae la primera cuenta y contamina las demás. Si el equipo va a operar Meta+nutra en serio, necesita desde el día 1: business managers separados, antidetect browser, proxies dedicados por cuenta, método de pago limpio. Es infraestructura, no detalle.

5. **El costo oculto de ser no-USA.** Cobro internacional ($50 por cheque extranjero), fricción fiscal cross-border, y a veces geo-restricciones de la oferta. Relevante directo para el equipo (Chile). Resolver método de pago (Payoneer/wire) y estructura fiscal ANTES de la primera venta.

6. **La métrica que importa no es ROAS bruto, es profit neto post-reembolso.** En nutra la tasa de reembolso es alta y los chargebacks pegan después de los 60 días con penalidad no reversible. El "154% ROI" de affLIFT ya descuenta esto (29% de approval rate de leads). Un afiliado que mira solo el revenue bruto de Meta se engaña.

---

## Apéndice: Fuentes consultadas

**Foros accedidos con cita verbatim (vía firecrawl):**
- [BlackHatWorld: Can I send Facebook ads to clickbank offer?](https://www.blackhatworld.com/seo/can-i-send-facebook-ads-to-clickbank-offer.1504449/)
- [BlackHatWorld: FB Ads + Clickbank Journey to $10,000/month (Drought)](https://www.blackhatworld.com/seo/facebook-ads-clickbank-journey-to-10-000-month.1040654/) + [page 2](https://www.blackhatworld.com/seo/facebook-ads-clickbank-journey-to-10-000-month.1040654/page-2)
- [BlackHatWorld: Clickbank affiliate here, feeling a little lost](https://www.blackhatworld.com/seo/clickbank-affiliate-here-feeling-a-little-lost.1601068/)
- [BlackHatWorld: Do you make money with Clickbank? (Honest opinion)](https://www.blackhatworld.com/seo/do-you-make-money-with-clickbank-want-your-honest-opinion.1812856/)
- [AffiliateFix: Is it possible to direct link to a Clickbank offer using Facebook Ads?](https://www.affiliatefix.com/threads/is-it-possible-to-direct-link-to-a-clickbank-offer-using-facebook-ads.175915/)
- [Warrior Forum: Can I get banned for clickbank products on facebook?](https://www.warriorforum.com/pay-per-click-search-engine-marketing-ppc-sem/1161023-can-i-get-banned-clickbank-products-facebook.html)
- [Warrior Forum: Clickbank Took My Money...Seeking Advice!](https://www.warriorforum.com/main-internet-marketing-discussion-forum/732049-clickbank-took-my-money-seeking-advice.html)
- [Warrior Forum: Is Clickbank's Refund Policy A Joke?](https://www.warriorforum.com/main-internet-marketing-discussion-forum/326974-clickbanks-refund-policy-joke.html)
- [Warrior Forum: Clickbank direct linking success (case study)](https://www.warriorforum.com/main-internet-marketing-discussion-forum/1417316-affiliate-case-study-clickbank-direct-linking-success.html)
- [affLIFT: Case Study: 154% ROI on Nutra offer](https://afflift.com/f/threads/case-study-154-roi-on-nutra-offer.9562/)
- [Quora: Why do people fail on ClickBank?](https://www.quora.com/Why-do-people-fail-on-ClickBank)
- [Quora: Why did I fail to sell ClickBank's product?](https://www.quora.com/Why-did-I-fail-to-sell-ClickBanks-product)

**Fuentes institucionales / políticas (verificación de reglas):**
- [ClickBank: How to Make Your First Sale (dato 570 días)](https://www.clickbank.com/blog/how-to-make-your-first-sale-on-clickbank/)
- [ClickBank: Gravity Score explained](https://www.clickbank.com/blog/clickbank-gravity-score/)
- [ClickBank: Return & chargeback / return allowance](https://support.clickbank.com/en/articles/10535293-will-i-get-paid-a-commission-if-the-sale-is-refunded)
- [ClickBank: S2S / Meta Pixel CAPI integration](https://support.clickbank.com/en/articles/10535369-s2s-tracking-integration-meta-facebook-pixel)
- [Meta Transparency Center: Ad Standards](https://transparency.meta.com/policies/ad-standards/)
- [AuditSocials: Meta Ad Policy Updates 2026 (disclaimer suplementos)](https://www.auditsocials.com/blog/meta-ad-policy-updates-2026-guide)
- [ROIAds: Test budget for affiliate campaigns](https://roiads.co/blog/affiliate-test-budget-for-ad-campaigns/)
- [AnyTrack: Connect Facebook Ads to ClickBank](https://anytrack.io/connect-facebookads-and-clickbank)
- [Multilogin: Buy aged Facebook accounts (riesgo fingerprint)](https://multilogin.com/blog/buy-facebook-aged-accounts/)

**Acceso bloqueado (documentado):** Reddit (r/Affiliatemarketing, r/PPC, r/FacebookAds) rechazó WebFetch, WebSearch (dominio bloqueado para el user-agent) y firecrawl ("we do not support this site"). El contenido de Reddit solo se pudo ver vía snippets de búsqueda general, no como cita verbatim verificable. Threads identificados pero no citables verbatim: *"What I learned after a failed product launch on ClickBank"* (r/Affiliatemarketing), *"Devastated!! $400 ad spent and only 1 sale!!"* (r/PPC), *"Those who started practicing with Affiliate product?"* (r/PPC).
