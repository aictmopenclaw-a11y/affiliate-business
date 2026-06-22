# 07. Análisis financiero comparativo: ¿cuál es el costo de oportunidad real de elegir affiliate marketing?

**Fecha del análisis:** 2026-04-28
**Capital base de comparación:** USD $11.000
**Horizonte:** 12 meses
**Equipo:** 3 personas — Cris (estrategia + tech + paid media), Romi (contenido + estrategia + copy), Dali (creativo + visual)
**Mercados de operación posibles:** Chile (CLP), Australia (AUD), USA/Global (USD)

> Este documento se construye sobre la data ya recopilada en este folder (`01-clickbank-deep-dive.md`, `02-viabilidad-modelo.md`, `03-legal-fiscal-cross-border.md`, `04-casos-competencia.md`) y la complementa con benchmarks externos investigados con firecrawl en abril 2026. La pregunta no es "¿se puede ganar dinero con X?" — todas estas opciones tienen casos exitosos. La pregunta es: **dado un capital fijo, un equipo fijo y un tiempo fijo, ¿cuál tiene el mejor expected value ajustado por riesgo y por skill match?**

> **Convenciones de fuentes (clave de lectura):**
> - `[Oficial]` — fuente primaria (plataforma, regulador, API, encuesta de la propia plataforma)
> - `[Survey]` — encuesta de tercero independiente (Authority Hacker, Indie Hackers, Statista)
> - `[Industry blog]` — análisis de medio especializado (puede tener sesgo comercial — se anota cuando aplica)
> - `[Estimación OpenClaw]` — cálculo derivado por nosotros con metodología explícita
> - `[Anecdótico]` — caso individual (Reddit, Twitter, post de creador) — usar como triangulación, no como base

---

## Tabla maestra (lectura rápida — el resto del documento son las defensas)

| # | Modelo | Inversión inicial realista (USD) | Tiempo a break-even (mediana) | Probabilidad de éxito año 1 | Income realista año 1 (USD/mes neto al mes 12) | Defensibilidad 3-5 años | Match con equipo R+C+D |
|---|---|---|---|---|---|---|---|
| 1 | **Affiliate ClickBank (paid media)** | $8K-15K | 3-9 meses si funciona / nunca si no | 20-30% | $0-5K (mediana real ~$0-2K, tail $10K+) | Baja (vendor risk + plataforma risk) | Alto (Cris paid + Romi copy + Dali video) |
| 2 | **Dropshipping Shopify** | $3.5K-8K | 4-8 meses si funciona | 10-20% | $0-3K (mediana ~$500-2K) | Muy baja (sin marca, sin moat) | Alto |
| 3 | **eCommerce DTC marca propia** | $15K-50K+ | 12-24 meses | 15-25% | -$2K a +$2K (mayoría aún en pérdida al mes 12) | Media-alta si construye marca | Medio |
| 4 | **Print-on-Demand (Etsy/Shopify)** | $500-2K | 3-9 meses si pega un design hit | 5-15% | $0-1K (mediana ~$100-500) | Muy baja (saturado, copia inmediata) | Alto en diseño (Dali) |
| 5 | **Micro-SaaS bootstrap** | $2K-8K (capital) + 1500-3000 hrs dev | 6-18 meses | 10-20% para llegar a $1K MRR | $0-2K MRR mediana | Alta (recurring, switching cost) | Medio-bajo (sin fundador-developer dedicado) |
| 6 | **Agencia digital** | $3K-10K | 1-3 meses (ya hay clientes) | 70-85% | $5K-20K | Alta (relaciones + casos) | **Muy alto (es lo que ya hacen)** |
| 7 | **Cursos / coaching / educación** | $2K-8K | 3-12 meses si hay audiencia | 20-40% | $1K-15K (huge variance) | Media (depende de marca personal) | Alto si capitalizan agency expertise |
| 8 | **Newsletter monetizada** | $500-3K | 12-24 meses | 10-20% | $100-2K al llegar a 1K subs (~12 meses típico) | Media-alta (audiencia propia) | Medio (Romi sí, otros menos) |
| 9 | **Content creator (YT/TikTok/IG)** | $1K-5K (equipo) | 12-36 meses | 5-15% | $0-2K | Media-alta (audiencia propia) | Alto en producción (Dali) |
| 10 | **Trading / crypto activo** | $11K | N/A — modelo de juego suma cero | 10-20% beat market | -$11K a +$2K-3K esperado | N/A (no es negocio) | Bajo |
| 11 | **Amazon FBA / arbitrage físico** | $5K-15K | 6-18 meses | 10-20% | $0-3K (60% rentabiliza eventualmente, no en año 1) | Baja (Amazon controla) | Bajo |
| 12 | **Servicios freelance/consultoría** | $500-2K | 1-3 meses | 80-95% | $6K-25K combinado (3 personas) | Media (dependiente de cada uno) | **Muy alto** |

> **Lectura rápida:** los dos modelos con mejor probabilidad/skill match son agencia (ya lo hacen) y servicios freelance. Affiliate y dropshipping comparten un perfil similar de "alto upside / alta probabilidad de no-funcionar". DTC, micro-SaaS y newsletter son los modelos de mayor defensibilidad pero requieren más tiempo del que cabe en 12 meses para llegar a break-even.

---

## 1. Baseline: Affiliate Marketing ClickBank (lo que ya investigamos)

**Resumen de lo que dice el folder previo** (`01-clickbank-deep-dive.md`, `04-casos-competencia.md`):

- ClickBank es real, paga, infraestructura sólida desde 1998. `[Oficial — clickbank.com]`
- Comisiones 50-75% del producto. Ticket promedio del nicho health/wealth: $30-150 USD. `[Oficial]`
- El modelo dominante en 2024-2026 es **paid traffic** (Meta Ads, YouTube Ads, native ads) hacia VSL/landing del vendor.
- **Earning data (la parte importante):**
  - 81.2% de affiliate marketers (cualquier red, no solo CB) gana >$20K/año. `[Survey AffiliateWP — sample sesgado: solo respondieron quienes facturaban]`
  - **Authority Hacker survey (2024):** average $8.038/mes, pero la mediana real es mucho menor; 9.45x diferencia entre +3 años de experiencia vs. principiantes. `[Survey Authority Hacker, n=2266]`
  - **PostAffiliatePro:** principiantes año 1 ganan **$0-1.000/mes**. `[Industry blog — pero coincide con todos los foros]`
  - Caso panchoval (Chile, $5M USD acumulados en CB, vive de esto): outlier público, 2-3 años a tiempo completo + reinvirtiendo $8M+ en ads. `[Anecdótico — entrevistas YT y declaraciones propias]`

**Inversión realista para el equipo R+C+D con $11K USD:**
- Test budget Meta/YouTube: $6K-8K en 3-6 meses (200-400 USD/día por 30-90 días)
- Tooling (ClickFunnels/Replug/Voluum tracking/spy tools): $200-500/mes × 6-12 meses = $1.5K-3K
- LLC + EIN + payment infra: $500-1.500
- Buffer / iteración creativa: $1.5K-3K
- **Total runway:** $11K alcanza para ~2-4 ciclos de testing. Suficiente para validar 1-2 ofertas si hay disciplina, no para "darse el lujo" de mucho error.

**Probabilidad de break-even año 1:** **20-30%.** Ese rango sale de:
- ~10-20% de affiliates con paid traffic logran ofertas profitables sostenidas (consenso foros + Authority Hacker)
- El equipo R+C+D **sube esa base** porque ya domina paid media + creativo + copy (Cris hace esto para clientes, Romi hace copy, Dali hace video). No están aprendiendo desde cero.
- Pero **baja por la curva de aprendizaje del nicho** (CB nicho US health/wealth ≠ ads para clínicas chilenas).

**Income realista año 1 si funciona:** $0-5K USD/mes neto al mes 12. La curva típica es 6-9 meses de pérdida + 3-6 meses de profit creciente. Tail risk al alza: $10K+ USD/mes si encuentran una oferta que escale.

**Defensibilidad:** **Baja.** Riesgos documentados:
- Vendor cambia comisión / pausa la oferta sin aviso (común)
- Ad account bans (Meta es restrictivo con CB nicho)
- Compliance creciente (FTC, ASIC, Sernac — ver `03-legal-fiscal-cross-border.md`)
- ClickBank puede deplatform (raro pero ocurre)

**Tail al alza:** modelo de agencia de media buying (lo que hace Pancho ahora) — vendor te contrata como buyer interno cobrando rev share. Requiere primero ser top affiliate.

**Expected Value (EV) año 1:**
- P(éxito) × Upside esperado: 0.25 × ($30K profit año 1) = **+$7.5K**
- P(fracaso) × Capital perdido: 0.75 × ($8K perdidos) = **-$6K**
- **EV neto ≈ +$1.500 USD** + valor de aprendizaje (skill paid media internacional)

> Ojo: este EV no incluye costo de oportunidad del tiempo de las 3 personas. Si Romi, Cris y Dali dedican 50% de su tiempo a esto durante 12 meses, el costo de oportunidad de no facturar agencia/freelance en ese tiempo es **mucho mayor que $11K**.

---

## 2. Dropshipping Shopify (2024-2026)

**Tamaño y viabilidad del mercado:**
- Mercado global $543B en 2026, proyectado $1.25T en 2030 (CAGR 22%). `[Sellers Commerce 2026]`
- 27% de ecommerce mundial usa dropshipping como modelo primario (~7.7M tiendas activas). `[Sellers Commerce 2026]`
- Sigue creciendo, pero entrada cada vez más comoditizada.

**Costo real de arranque (no marketing):**
- Shopify Basic: $39/mes USD = $468/año `[Oficial Shopify]`
- Apps imprescindibles (DSers/AutoDS, theme premium, reviews app, email): $80-200/mes `[Oficial / industry]`
- Dominio + email: $50-100/año
- LLC + payment processor setup: $500-1.500
- **Subtotal infra: $2K-4K año 1**

**Costo de marketing realista (la parte cara):**
- **Shopify oficial:** punto de partida realista es **$200-300 primer mes** — pero esto es para "una tienda funcionando", no para "tienda profitable". `[Oficial Shopify, sesgado a la baja porque vende plataforma]`
- **Reddit r/dropship consenso:** "necesitas $1.500 mínimo solo en ad cost; cada test de producto cuesta $200-300". `[Anecdótico pero unánime]`
- **ShipToTheMoon 2026:** budget realista 3 meses de testing = **$3.500-8.000 USD**. `[Industry blog]`
- **Printkk 2026:** $2.000-3.500 si product research está bien hecho. `[Industry blog]`
- **Estimación OpenClaw:** con $11K, 1 tienda, ~10-15 product tests a $300-500 c/u + escalado del ganador. Razonable.

**Tasa de éxito real:**
- **Drop Ship Lifestyle (Anton Kraly, autoridad del sector):** "solo 10-20% de tiendas alcanzan rentabilidad consistente". `[Industry — autor con curso, sesgo a relativizar el número, pero coincide con literatura]`
- **Sellers Commerce:** mismo rango, 10-20%. `[Industry]`
- Margen típico: **15-30% neto** después de COGS, shipping, ads, fees. `[Sellers Commerce + Drop Ship Lifestyle, consenso]`
- Manufacturers que dropshipean ganan 18% más profit margin que venta directa (12.2% vs 10.3%). `[Sellers Commerce, survey 350 manufacturers 2024]`

**Income año 1 realista:**
- **Doba (industry blog):** "first-year sellers part-time hacen $6.000-25.000 net profit anual". `[Industry — sesgo a la alza, no especifica mediana vs. promedio]`
- **Reddit consenso 2025:** 80%+ de tiendas no llegan a $1K MRR. Las que pegan, llegan a $3K-15K MRR pero requieren scaling capital adicional.
- **Estimación realista:** $0-3K USD/mes al mes 12. Mediana probable $500-2K si el equipo no cae en los 80% que abandonan.

**Skills match con R+C+D:** **Alto.**
- Cris: paid media (la skill #1 en dropshipping moderno)
- Romi: copy de product page + ad copy
- Dali: creative video (UGC-style ads que funcionan en TikTok/Meta)

**Defensibilidad:** **Muy baja.**
- Cero diferenciación de producto (competencia copia tu winning product en 48h via ad spy tools)
- Sin marca, sin lista de email propia robusta
- AliExpress/CJ supplier risk (cambian precio, descontinuan)
- Plataforma risk (Shopify acct bans, Meta acct bans)
- Margen colapsando con CPMs altos

**EV año 1:**
- P(éxito) × Upside: 0.15 × ($20K profit año 1) = **+$3K**
- P(fracaso) × Capital perdido: 0.85 × ($6K perdidos) = **-$5.1K**
- **EV neto ≈ -$2.100 USD** + skill adquirida en ecommerce ops

> Dropshipping tiene **peor EV que affiliate** para este equipo, principalmente porque el upside del ganador es similar pero la probabilidad de fracaso es mayor y agrega complejidad operativa (atención al cliente, reembolsos, supplier issues).

---

## 3. eCommerce DTC con marca propia

**Diferencia clave vs. dropshipping:** producto propio, marca, inventario, brand assets. Tiempo a break-even mucho más largo, defensibilidad real.

**Inversión inicial realista:**
- **Producto + inventario inicial (small batch MOQ):** $5K-20K dependiendo del vertical
- **Branding + packaging + fotografía:** $2K-8K
- **Web (Shopify + theme + apps):** $1K-3K año 1
- **Inventario buffer + working capital:** $5K-15K (el "hidden cost" más común)
- **Ads + content marketing primer 6 meses:** $5K-20K
- **Total realista: $20K-50K mínimo para un lanzamiento serio**

> **$11K USD no es suficiente para una marca DTC competitiva.** Permitiría lanzar con MOQ chinos, pero sin runway real para apagar incendios (returns, defective batches, ad scaling).

**Tiempo a break-even:**
- **Common Thread Co + Attn Agency:** "DTC profitability benchmarks 2026" — la mayoría de DTC bootstrapped no es contribution-margin positive hasta el mes 12-18. `[Industry blog, autor reputado]`
- **Brookings/maccelerator data:** 73% de DTC brands fallan entre $10M-$50M de revenue por hidden scaling costs (talent $200K-400K/exec, tech $500K+ ERP, working capital). `[Industry]` — esto es para brands que ya escalaron, no para la fase inicial, pero ilustra cuánto capital requiere el modelo.
- **Mediana realista para bootstrap con $11K:** no llegan a break-even en año 1; mejor caso es hacer pre-orders → manufactura → primer batch vendido → reinvertir.

**Probabilidad de éxito año 1:** 15-25% si se define éxito como "revenue >$50K año 1 y tendencia positiva". <5% si éxito = "salario mínimo para los 3 fundadores".

**Income año 1:**
- Realista: -$2K a +$2K USD/mes — la mayoría aún en pérdida o break-even.
- Caso bueno: $5K-15K/mes de revenue (no profit) al mes 12.

**Defensibilidad:** **Media-alta** si se construye marca real. Es el único modelo de esta lista que puede valer 3-10x revenue en exit a 5 años (vs. affiliate que vale 0 sin tu activo personal).

**Skills match:** Medio. Falta operations + supply chain skills. Romi en estrategia + Dali en branding ayudan, Cris en paid media para escalar.

**EV año 1:**
- P(éxito en sentido amplio = base sólida construida) × Valor activo: 0.25 × $30K equity value = **+$7.5K** (no cash, valor empresa)
- P(fracaso) × Capital perdido: 0.75 × ($10K) = **-$7.5K**
- **EV cash-on-cash ≈ -$5K año 1** + opción real significativa (la marca puede valer mucho año 2-3)

> DTC es un juego de **2-3 años**, no de 12 meses. Con $11K es el modelo equivocado.

---

## 4. Print-on-Demand (Printful/Printify + Etsy/Shopify)

**Costo de arranque (la parte buena):**
- $0 inventario (el provider imprime on-demand)
- Etsy listing fee: $0.20 por listing
- Shopify si se usa: $39/mes
- Diseño: tiempo de Dali (no cash)
- Marketing: $0 si Etsy SEO + organic / $200-2K/mes si paid

**Total cash burn mínimo para validar:** $500-2.000.

**Margen real:**
- **Printful (oficial):** "good profit margin 20-40%". `[Oficial Printful — sesgo, vende la plataforma]`
- **Reddit r/printondemand consenso:** $25 shirt - $11 print cost - $2 Etsy fees - shipping = **$8-12 ganancia bruta** (~30-40%).
- **Realidad:** márgenes razonables si el design es original; **terriblemente saturado** en categorías genéricas (frases motivacionales, animales con sombrero, "funny dad" shirts).

**Income realista año 1:**
- Mediana de tiendas POD en Etsy: **$0-100/mes**. La mayoría no logra >10 ventas/mes.
- **Top 10% de tiendas:** $1K-5K/mes con 1-3 designs hit.
- **Top 1%:** $10K+/mes (ej: tiendas con TikTok orgánico viral).

**Probabilidad año 1:** 5-15% para llegar a $1K/mes neto.

**Saturación 2024-2026:**
- Sí, está saturado en categorías obvias. AI-generated designs (MidJourney, DALL-E) inundaron Etsy 2023-2024.
- Aún hay nichos no commodity-zados: micro-comunidades de hobbies, ocupaciones específicas, fandoms locales.
- Etsy ha ido bajando reach orgánico de POD para favorecer "handmade real".

**Skills match:** Alto en diseño (Dali). Bajo retorno por hora — escalar requiere muchos designs (volumen).

**Defensibilidad:** **Muy baja.** Designs se copian en horas (literal). Único moat: marca personal del creador o nicho microsegmentado.

**EV año 1:**
- P(éxito = $1K+/mes) × Upside: 0.10 × $10K = **+$1K**
- P(fracaso) × Capital: 0.90 × ($1.5K) = **-$1.4K**
- **EV ≈ -$400** pero con muy bajo capital en riesgo.

> POD funciona como **side hustle de un solo creador** (Dali en este caso), no como negocio para 3 personas. Mal uso del equipo completo.

---

## 5. Micro-SaaS bootstrap

**Inversión inicial:**
- Capital: $2K-8K (hosting, domain, Stripe, tools, ads iniciales)
- **Tiempo de developer:** 1.500-3.000 horas para construir + iterar MVP. **Esta es la inversión real.**

**Tiempo a $1K MRR (la métrica north star de Indie Hackers):**
- **Indie Hackers analysis (Stripe-verified data):** mediana 8-9 meses, percentil 25 = 5 meses, percentil 75 = 12 meses. `[Survey con datos Stripe verificados, n>1000]`
- Solo el ~25% de proyectos lanzados llega a $1K MRR. La mayoría muere antes.

**Probabilidad año 1:**
- Llegar a $1K MRR: **20-25%** (data Indie Hackers).
- Llegar a $10K MRR: **<5%**.
- Llegar a "salario para 3 personas" ($10K+ MRR): **<3%** en año 1.

**Income realista año 1:** $0-2K MRR mediana para los que sobreviven.

**Skills match con R+C+D:** **Bajo en el bottleneck crítico.**
- Cris hace tech para clientes, pero **no es full-stack developer dedicado a un producto SaaS**.
- Sin developer fundador a tiempo completo, contratar dev = $5K-15K/mes en LATAM, $15K-30K/mes en USA = se come el capital en 1-2 meses.
- Romi y Dali aportan en marketing y diseño, pero el cuello de botella es producto.

**Defensibilidad:** **Alta** si llega a tracción. Recurring revenue, switching costs, posibilidad de exit (Tiny Acquisitions, Microns, etc., compran micro-SaaS por 2-4x ARR).

**EV año 1:**
- P(éxito) × Upside: 0.20 × ($15K ARR año 1 = ~$1K MRR) = **+$3K**
- P(fracaso) × Capital perdido: 0.80 × ($6K + tiempo dev) = **-$5K cash + tiempo**
- **EV ≈ -$2K + opción real grande (puede convertirse en negocio real año 2-3)**

> Sin un cofundador-developer, este modelo no aplica para este equipo.

---

## 6. Agencia digital (lo que ya hacen)

**Inversión inicial:**
- $11K es **mucho más de lo necesario** para arrancar agency. Realista: $3K-10K para tooling, branding, web, primeros ad creatives propios.
- OpenClaw ya está operando: el costo "marginal" de doblar capacidad es esencialmente $0.

**Tiempo a break-even:**
- Si ya hay clientes (caso OpenClaw): **break-even desde el mes 1**.
- Para lanzar nueva agency desde 0: **1-3 meses al primer cliente**, 4-6 meses al segundo y tercero.

**Modelo de revenue:**
- **Retainer mensual:** rango global $1.5K-25K/mes. `[InfluenceFlow 2026 — survey global]`
- **Mediana 3 personas en LATAM:** $2K-5K USD/cliente/mes. `[Reddit r/DigitalMarketing 2025]`
- **Performance + retainer híbrido:** lo que OpenClaw ya practica.
- **CMO fractional:** $4K-10K/mes part-time.

**Tiempo a $10K USD/mes combinado (3 personas):**
- 2-3 retainers de $3K-5K cada uno = $9K-15K/mes
- Realistic: **3-6 meses si hay outbound activo**.

**Probabilidad de éxito año 1:** **70-85%** llegar a $10K USD/mes facturación con 3 personas full-time. Ya validado por la operación actual.

**Defensibilidad:** **Alta.** Casos, testimonios, relaciones. Switching cost para el cliente es real.

**Skills match:** **Máximo.** Es exactamente lo que el equipo hace. Romi (estrategia + creativo orgánico), Cris (paid + tech), Dali (visual + producción). Es la combinación canónica de marketing performance.

**EV año 1:**
- P(éxito) × Upside: 0.80 × ($120K facturación año 1, ~$60K profit a 3) = **+$48K**
- P(fracaso) × Capital perdido: 0.20 × ($5K) = **-$1K**
- **EV ≈ +$47K USD año 1**

> El elephant in the room: **OpenClaw ya tiene EV de $47K+ con la ruta agencia**. Cualquier otra opción debe vencer este número o complementarla, no reemplazarla.

---

## 7. Cursos / coaching / educación digital

**Inversión inicial:**
- Plataforma (Kajabi $149/mes, Teachable $39/mes, Hotmart 9.9% fee): $500-2K año 1
- Producción de curso (video, edición, materiales): $1K-5K si se hace in-house (Dali edita)
- Marketing inicial (ads + content): $3K-8K
- **Total realista: $5K-15K**

**Tiempo a primera venta:** 1-3 meses si ya hay audiencia. 6-12 meses si hay que construirla.

**Income realista año 1:**
- **Kajabi (oficial):** "$0 a $50K+/mes; promedio creators exitosos $1K-10K/mes". `[Oficial Kajabi, sesgo positivo]`
- **Teachable (oficial):** "full-time creators hasta $10K/mes". `[Oficial Teachable]`
- **Realidad LATAM (Hotmart):** muchos creators chilenos/argentinos llegan a $1K-5K USD/mes con audiencias 5K-50K seguidores. `[Anecdótico cruzando casos públicos]`
- Caso ejemplo Reddit: "vendí curso por $6M USD en 2 años" — outlier extremo, requiere marca + tracción previa. `[Reddit /Entrepreneur]`

**Probabilidad año 1:** 20-40% para llegar a $2K-5K USD/mes neto.

**Skills match:** **Alto si capitalizan agency expertise.** OpenClaw ya tiene know-how en performance marketing → curso "agencia desde 0" o "Meta Ads para clínicas LATAM" = activo monetizable. Dali produce video, Romi escribe copy, Cris da expertise.

**Defensibilidad:** Media. Depende de marca personal del creador. Cursos canibalizables (refunds, piratería).

**EV año 1:**
- P(éxito) × Upside: 0.35 × ($30K facturación año 1) = **+$10.5K**
- P(fracaso) × Capital perdido: 0.65 × ($5K) = **-$3.25K**
- **EV ≈ +$7.25K** + activo (curso) que sigue vendiendo año 2+

> Cursos es **complementario** al modelo agencia, no sustituto. Reusan expertise, generan leads, posicionan a los founders como autoridades.

---

## 8. Newsletter monetizada

**Inversión inicial:**
- Beehiiv (free tier o $49/mes paid) o Substack (10% fee): $0-600/año
- Tiempo de producción: 5-15 hrs/semana de Romi (alta calidad)
- Crecimiento (paid subs growth, cross-promo, Boosts): $500-3K si se acelera

**Tiempo a 1.000 subs paying:**
- Newsletter típico: **12-24 meses** para llegar a 1K subscribers totales (no paying), de los cuales 5-20% paga = 50-200 paying subs.
- Casos rápidos (con audiencia social previa): 3-6 meses.

**Income realista al hito 1.000 subs:**
- **Beehiiv (oficial 2025):** "1K subs = $100-2K/mes con monetización mixta (ads + premium + affiliates)". `[Oficial Beehiiv, sesgo a la alza]`
- **Modelo paid premium:** 5-20% conversion × $5-15/mes = $250-3K/mes a 1K subs.
- **Modelo ads (Beehiiv Ad Network):** $20-160/mes a 1K subs con buenos opens.
- **Realidad:** la mayoría de newsletters de hobbystas no rebasa $200/mes en año 1.

**Casos de referencia:**
- **Lenny's Newsletter:** $1.5M+/año (estimado público), 10+ años de experiencia previa como PM en Airbnb. `[Anecdótico — outlier]`
- **Saeed Ezzati (Beehiiv case study):** $150K/año desde nicho específico. `[Beehiiv]`
- **The Hustle (sold to HubSpot $27M):** 7+ años para llegar.

**Probabilidad año 1:** 10-20% llegar a $500+/mes. <5% llegar a "salario digno".

**Skills match:** Medio. Romi tiene la skill (escritura, estrategia editorial). Cris y Dali aportan menos.

**Defensibilidad:** **Media-alta.** Lista propia de email = activo real, transferible, vendible.

**EV año 1:**
- P(éxito) × Upside: 0.15 × ($6K año 1) = **+$0.9K**
- P(fracaso) × Capital perdido: 0.85 × ($1K cash + tiempo Romi) = **-$0.85K**
- **EV ≈ ~$0** cash, pero **el activo construido vale año 2-3**.

> Newsletter es un juego de **2-5 años**. Buena complemento, mal sustituto.

---

## 9. Content creator (YouTube / TikTok / Instagram)

**Inversión inicial:**
- Equipo grabación (cámara + micro + iluminación): $1K-3K si se sube nivel
- Edición (Dali ya hace): $0
- Time investment: 15-30 hrs/semana sostenidas

**Tiempo a monetización:**
- **YouTube YPP (oficial):** 1.000 subs + 4.000 hrs watch time. Realidad: **1-3 años** para creators sin background. `[Oficial YouTube + Reddit r/PartneredYoutube consenso]`
- **TikTok Creator Rewards:** 10K followers + 100K views/30 días. Más rápido pero pago bajísimo.
- **Patrocinios (la verdadera monetización):** llegan con 10K-50K followers en nicho relevante.

**Income realista año 1:**
- Reddit consenso: "después de 2 años monetizado, $15-20/día = $450-600/mes". `[Anecdótico unánime]`
- Sponsorships: $200-2.000/post si llegas a 10K-50K seguidores en nicho.
- Casos rápidos: <5% logran $1K+/mes en año 1.

**Probabilidad año 1:** 5-15% llegar a $1K+/mes.

**Skills match:** Alto en producción (Dali edición, Romi guión, Cris estrategia de growth). **Pero requiere fundador-personaje al frente** — la cámara necesita una cara.

**Defensibilidad:** **Media-alta.** Audiencia es activo propio, pero plataforma risk (cambio de algoritmo) es real.

**EV año 1:**
- P(éxito) × Upside: 0.10 × ($10K año 1) = **+$1K**
- P(fracaso) × Capital perdido: 0.90 × ($2K) = **-$1.8K**
- **EV ≈ -$0.8K** cash, audiencia construida vale año 2+.

> Funciona **sumado a otra cosa** (apoyo a agency o curso), no como negocio principal año 1.

---

## 10. Trading / crypto / inversión activa

**Realidad documentada (no MLM, no scam):**
- **Quantified Strategies:** **62-82% de retail CFD traders pierden dinero.** `[Industry — recopilación datos brokers oficiales]`
- **AFbis:** profitability rate forex retail **<25%, más realista ~10%** en periodos largos. `[Industry — meta-análisis]`
- **Goat Funded Trader:** institutionals 8-15% anual; top 25% retail 10-25%; mid retail entre +5% y -20%. `[Industry — vendedor de prop accounts, sesgo motivacional]`
- **CFD broker disclosures (regulación EU/Australia):** "68-89% de cuentas pierden dinero" — texto legal obligatorio en cada anuncio. `[Oficial regulatorio]`

**Capital y skills:**
- $11K USD permite operar pero con un solo error grande de gestión = -50% de cuenta.
- Aprender trading sostenible serio: 2-3 años de práctica, no 12 meses.

**Income año 1 esperado para el equipo:**
- **Sharpe ratio realista para principiante disciplinado:** 0.3-0.7 (aceptable pero no genial).
- **Retorno esperado año 1:** -50% a +20% del capital. Mediana ~-10% a 0%.
- En USD sobre $11K: **-$5.500 a +$2.200**, mediana **-$1.000 a $0**.

**Skills match:** Bajo. Ninguno del equipo tiene track record verificable.

**Defensibilidad:** N/A. No es negocio, es especulación.

**EV año 1:**
- P(beat market = +10% real) × Upside: 0.20 × $2K = **+$0.4K**
- P(perder) × Capital: 0.80 × $4K perdidos = **-$3.2K**
- **EV ≈ -$2.8K**

> Trading no aplica como ruta de negocio para este equipo. **Descartar.**

---

## 11. Amazon FBA / arbitrage físico

**Inversión inicial:**
- Producto + manufactura (private label, MOQ típico 200-500 unidades): $3K-10K
- Shipping + Amazon inbound fees: $500-2K
- Branding + listing photography + creative: $500-1.500
- PPC Amazon Ads inicial: $1K-3K
- Cuenta + LLC + UPC codes + insurance: $500-1.500
- **Total: $5K-15K para 1 SKU correctamente lanzado**

**Tasa de éxito documentada:**
- **Panda-Boom 2026:** "60% de sellers eventualmente rentabilizan, pero muchos queman capital antes de llegar". `[Industry blog]`
- **Helium 10 / Jungle Scout (2024):** 50% de nuevos sellers que sobreviven primer año hacen $1K-25K/mes; **mediana ~$1.5K/mes**, **38% rentables en primeros 3 meses**, 65% en año 1. `[Industry — sesgo a la alza, son tools que venden a sellers]`
- **Realidad Reddit r/AmazonFBATips 2024-2025:** "barrier creciente, fees subiendo, capital required mucho mayor que hace 3 años".

**Income año 1:** $0-3K USD/mes neto, mediana ~$500-1.500.

**Probabilidad año 1:** 10-20% llegar a $2K+/mes neto consistente.

**Skills match:** **Bajo.** Requiere supply chain, sourcing China, listing optimization (SEO Amazon es un mundo aparte). No matchea con skills agency.

**Defensibilidad:** **Baja.** Amazon controla la plataforma. Hijackers, listing suspensions, fee increases. Single-platform risk extremo.

**EV año 1:**
- P(éxito) × Upside: 0.15 × $15K = **+$2.25K**
- P(fracaso) × Capital: 0.85 × $8K = **-$6.8K**
- **EV ≈ -$4.5K**

> FBA es peor opción que dropshipping para este equipo. Más capital required, más complejidad operativa, mismo skill mismatch.

---

## 12. Servicios profesionales freelance / consultoría

**Modelo:** cada uno de los 3 facturando proyectos/horas en su skill, con OpenClaw como umbrella opcional.

**Inversión inicial:**
- Web personal / portfolio: $200-1K
- LinkedIn Premium + Sales Navigator: $80-150/mes
- CRM lite (Notion, Pipedrive lite): $0-30/mes
- **Total realista: $500-2K**

**Tarifa realista por persona:**
- **Cris (paid media + tech):** $50-150/hora en LATAM, $100-250/hora con clientes USA/AU. `[Thumbtack, ZipRecruiter, Upwork data 2025]`
- **Romi (estrategia + content):** $40-120/hora.
- **Dali (creative + video):** $40-100/hora.

**Income año 1 combinado realista:**
- Cada persona facturando 60-100 hrs/mes a $50-100/hora promedio = $3K-10K/mes c/u
- **Total 3 personas: $9K-30K USD/mes** una vez que el pipeline está lleno (mes 3-6)

**Probabilidad de éxito año 1:** **80-95%** llegar a $10K USD/mes combinado. Es el modelo de menor riesgo de la lista.

**Skills match:** **Máximo.** Es exactamente lo que ya saben hacer.

**Defensibilidad:** **Media.** Cada freelancer es reemplazable individualmente, pero el conjunto + relaciones + marca personal = activo real.

**EV año 1:**
- P(éxito) × Upside: 0.90 × ($150K facturación año 1) = **+$135K**
- P(fracaso) × Capital: 0.10 × $1.5K = **-$0.15K**
- **EV ≈ +$135K USD**

> Freelance/consulting tiene **el mejor EV de toda la tabla por orden de magnitud**. La diferencia con agencia es que aquí los 3 facturan independiente vs. bajo brand común. Son complementarios.

---

## Tabla de Expected Value comparada

| # | Modelo | EV año 1 (USD, cash-on-cash) | Capital expuesto | Tiempo a primera señal de éxito | Skill match |
|---|---|---|---|---|---|
| 12 | Servicios freelance | **+$135K** | $1.5K | 1 mes | Máximo |
| 6 | Agencia digital | **+$47K** | $5K | 1-3 meses | Máximo |
| 7 | Cursos / educación | **+$7.25K** | $5K | 3-6 meses | Alto |
| 1 | Affiliate ClickBank | **+$1.5K** | $8K | 3-9 meses | Alto |
| 8 | Newsletter | **~$0** | $1K | 6-12 meses | Medio |
| 4 | Print-on-Demand | **-$0.4K** | $1.5K | 3-9 meses | Medio (solo Dali) |
| 9 | Content creator | **-$0.8K** | $2K | 12+ meses | Alto producción |
| 5 | Micro-SaaS | **-$2K** | $6K | 6-12 meses | Bajo (sin dev) |
| 2 | Dropshipping | **-$2.1K** | $6K | 4-8 meses | Alto |
| 10 | Trading | **-$2.8K** | $11K | N/A | Bajo |
| 11 | Amazon FBA | **-$4.5K** | $8K | 6-18 meses | Bajo |
| 3 | DTC marca propia | **-$5K cash / +opción real** | $10K+ | 12-24 meses | Medio |

> **Lectura crítica:** todo modelo con EV negativo año 1 puede tener EV positivo a 3-5 años si construye activo (DTC, micro-SaaS, newsletter, content creator, marca affiliate site). El problema es que en este horizonte de 12 meses con capital limitado, no hay margen para apostar a opciones reales sin asegurar runway base.

---

## Costo de oportunidad real de elegir affiliate

**El cálculo honesto:**

Si el equipo dedica 100% de su tiempo a affiliate marketing:
- **EV affiliate año 1: +$1.5K**
- **EV agencia + freelance año 1 que dejarían de hacer: +$135K (freelance) + ~$47K (agencia)**
- **Costo de oportunidad = ~$180K USD año 1**

Aunque affiliate funcione bien (top quartile = $5K-10K/mes profit al mes 12), el upside máximo realista año 1 ($30K-60K) **ni siquiera empata** lo que el equipo ya puede facturar haciendo lo que sabe hacer.

**Donde affiliate sí compite:**
- **Año 2-3, no año 1.** Si en año 1 una persona (ej. Cris) dedica 20% del tiempo a aprender el modelo CB con $5K-8K de capital, año 2 puede tener una oferta que escale con CTR/EPC validados.
- **Como tercera línea de revenue diversificada**, no como apuesta principal.
- **Si el equipo está estancado** y agencia/freelance no están escalando — pero ese no es el caso aquí (OpenClaw está creciendo).

---

## Skills match — análisis cruzado

| Skill | Romi | Cris | Dali | Mejor uso conjunto |
|---|---|---|---|---|
| Estrategia + planning | ✅ | ✅ | ⚪ | Agencia, consultoría, cursos |
| Copy + content escrito | ✅ | ⚪ | ⚪ | Newsletter, agencia, cursos, affiliate landing |
| Paid media (Meta/Google) | ⚪ | ✅ | ⚪ | Agencia, affiliate, dropshipping, DTC |
| Tech / scripts / automatización | ⚪ | ✅ | ⚪ | Agencia premium, micro-SaaS, ops interna |
| Visual / diseño / video | ⚪ | ⚪ | ✅ | POD, content creator, agencia, cursos |
| Sales / outbound | ⚪ | ⚪ | ⚪ | **Gap** — todos lo evaden |
| Operations / supply chain | ⚪ | ⚪ | ⚪ | **Gap** — descalifica DTC y FBA |

**Modelos donde los 3 perfiles se enchufan al máximo:** Agencia, cursos, affiliate (paid), DTC si tuvieran ops.
**Modelos donde 1 persona carga todo:** POD (Dali), Newsletter (Romi), micro-SaaS (Cris).
**Modelos que no cuadran con ningún perfil:** Trading, FBA, dropshipping puro a escala.

---

## Defensibilidad cross 3-5 años

| Modelo | Activo construido | Vendible / transferible | Plataforma risk |
|---|---|---|---|
| Agencia | Cartera clientes + casos + brand | Sí (3-5x EBITDA típico) | Bajo |
| Cursos | Marca personal + lista email + IP curso | Parcial | Medio |
| Newsletter | Lista email + brand editorial | Sí (2-5x ARR) | Bajo |
| DTC | Marca + datos cliente + producto | Sí (3-10x revenue) | Medio |
| Micro-SaaS | Código + MRR + customer base | Sí (2-4x ARR) | Medio |
| Content creator | Audiencia social | Limitado (audience leakage) | Alto |
| Affiliate | Skill + posiblemente sitio SEO | Bajo (dependencia vendor) | Alto |
| Dropshipping | Operación + ad accounts | Bajo (winning product cesa) | Alto |
| FBA | Listing + reviews | Sí pero condicionado a Amazon | Muy alto |
| POD | Designs library | Limitado | Alto |
| Freelance | Skill personal + red contactos | No transferible | Medio |
| Trading | N/A | N/A | N/A |

**Top 3 por defensibilidad:** Agencia, Newsletter, DTC (con marca real).

---

## Si yo fuera el equipo R+C+D, esto haría

**La recomendación honesta:** no es "elige uno" — es **portfolio inteligente con asimetría a favor del modelo que ya funciona**.

### Asignación recomendada de los $11K USD y del año

**80% del capital y tiempo: doblar la apuesta en agencia (OpenClaw)**
- $5K en sales/outbound estructurado (LinkedIn Sales Nav, herramientas de cold email, retargeting de prospects)
- $3K en posicionamiento de autoridad (case studies pagados de calidad, web upgrade, paid PR si aplica)
- $1K en operaciones internas (mejor tooling, automatización ahorro tiempo de los 3)
- **Meta:** llevar agencia de su nivel actual a $20K-40K USD/mes en 12 meses.
- **EV proyectado: +$50K a +$150K incremental.**

**15% del capital y tiempo: lanzar curso/educación complementario al expertise agencia**
- $1K en producción y plataforma (Dali edita, Romi guiona, Cris da expertise)
- $500 en ads de validación / pre-venta antes de producir
- **Meta año 1:** primera versión del curso, $5K-15K facturados. Activo que sigue vendiendo año 2+.
- **Bonus:** el curso genera leads de agencia (los alumnos que prefieren contratar antes que aprender).

**5% del capital y tiempo: experimento controlado affiliate (no abandonar la opción)**
- $500-800/mes durante 3-4 meses = $2K-3K total
- **Una sola persona** (Cris) testea 2-3 ofertas CB en paid Meta/YT con disciplina de stop-loss.
- **Meta:** validar si hay tracción REAL antes de escalar capital. Si en 4 meses no hay señal de profitabilidad → kill.
- **Si hay señal:** año 2 escalar con $20K-30K de capital reinvertido desde agencia.

### Por qué NO recomiendo affiliate como apuesta principal

1. **EV agencia (+$47K) > EV affiliate (+$1.5K) por 30x.** Matemática básica.
2. **El equipo ya tiene clientes.** Pasar de "agency en marcha" a "lanzar negocio nuevo" es siempre más caro de lo que se piensa (energía, foco, compliance, infra paralela).
3. **Affiliate USA tiene fricción legal-fiscal real para LATAM** (ver `03-legal-fiscal-cross-border.md`). LLC, EIN, US bank, ITIN — no triviales.
4. **El equipo NO tiene developer dedicado** y eso elimina micro-SaaS como opción defensible. Afilliate es la otra opción "tecnológica" que tampoco juega a sus fortalezas únicas.
5. **El upside del affiliate (caso panchoval) requirió 2-3 años a tiempo completo + capital para reinvertir 8-figure.** Eso no es plausible en año 1 con $11K.

### Por qué NO recomiendo dropshipping ni DTC ni FBA

- Dropshipping: peor risk-adjusted que affiliate, más operacional.
- DTC: capital insuficiente, horizonte equivocado.
- FBA: skill mismatch + plataforma risk extrema.

### Si REALMENTE quieren validar affiliate (porque hay convicción o curiosidad estratégica)

**Test mínimo viable, 90 días, $3K USD máximo:**
- Mes 1: setup infra (LLC + bank + ClickBank account + tracking) — $800
- Mes 2: 3 ofertas CB seleccionadas con criterio (gravity 30+, EPC >$1, vendor con VSL fuerte) × $500 ad spend cada una = $1.500
- Mes 3: doblar la mejor oferta o matar todo — $700
- **Decision tree:**
  - Si alguna oferta es ROAS >1.2 sostenido → escalar con $5K más en mes 4-6.
  - Si nada llega a ROAS 1.0 → cerrar test, archivar aprendizaje, foco 100% en agencia.

Esto **NO consume el capital de agencia, NO distrae al equipo completo, y produce data real** para decidir año 2.

---

## Resumen ejecutivo (1 página para el equipo)

**Pregunta original:** ¿Affiliate marketing es la mejor opción para los $11K USD y 12 meses?

**Respuesta corta:** No. Hay 2 alternativas con EV materialmente mejor (agencia +$47K, freelance +$135K) y 1 complementaria con buen ratio (cursos +$7.25K).

**Por qué affiliate parece atractivo y por qué engaña:**
- Tail risk al alza es real (panchoval existe).
- Pero la mediana de outcomes año 1 es flat-cero, no positiva.
- El costo de oportunidad de no hacer agencia/freelance en ese tiempo es 30-90x el upside esperado de affiliate.

**Recomendación:**
1. **Doblar agencia** (80% recursos) — es donde el equipo ya gana.
2. **Lanzar curso complementario** (15%) — capitaliza expertise agencia, genera activo.
3. **Test controlado affiliate** ($3K, 90 días, 1 persona) — para validar opción año 2 sin distraer núcleo.
4. **Kill list:** dropshipping, DTC año 1, FBA, trading, micro-SaaS sin dev fundador.

**Triggers para reconsiderar:**
- Si agencia se estanca 3 meses seguidos sin crecer → reasignar 30% a affiliate o cursos agresivos.
- Si test affiliate de 90 días muestra ROAS >1.5 sostenido → escalar a $20K-30K año 2.
- Si Dali quiere lanzar marca DTC propia (lifestyle visual) → módulo separado, no usa capital agencia.

---

## Notas metodológicas

**Sobre el cálculo de EV:**
- "Upside esperado" = ganancia neta esperada en escenario de éxito (no upside máximo del 1%).
- "Capital perdido" = no asume pérdida total siempre — para modelos con activos parciales (DTC, newsletter) se asume parcial.
- EV es **expected value cash-on-cash año 1**, NO incluye:
  - Valor de activo construido (importante en DTC, newsletter, content)
  - Costo de oportunidad del tiempo (importante para todos)
  - Skill aprendida (importante para affiliate, micro-SaaS)
- Para decisión real, sumar:
  - +Activo año 2-3 (DTC, newsletter, content suben +30-100%)
  - -Costo oportunidad agencia/freelance (cualquier opción que NO sea agencia/freelance se penaliza otros $50K-150K)

**Sobre las probabilidades de éxito:**
- Rangos derivados de meta-análisis de fuentes citadas, ajustados al contexto específico de un equipo con skill marketing pero no skill especifica del modelo (ej. dropshipping operations, FBA sourcing China, trading psychology).
- Asumimos disciplina y dedicación razonable — no perfección, no abandono.

**Sobre los rangos de income:**
- Cuando hay mucha varianza, se reporta tanto mediana como tail. La diferencia entre "promedio" y "mediana" en estos modelos es enorme — el promedio está distorsionado por outliers. La mediana es la que importa para decidir.

**Sobre fuentes con sesgo comercial:**
- Plataformas (Shopify, Beehiiv, Kajabi, Printful, Helium 10) tienden a inflar números porque venden la herramienta. Se anota cuando aplica y se cruza con foros de practitioners (Reddit, IndieHackers).
- Industry blogs de creators con cursos (Drop Ship Lifestyle, Authority Hacker) tienen sesgo similar. Útiles como direccional, no como verdad.

**Sobre lo que falta investigar más a fondo:**
- Casos verificables de equipos LATAM (no USA) en cada modelo — la mayoría de data es US-centric. Realidad LATAM puede tener mejor margen (costo equipo más bajo) pero peor acceso a payment processors y plataformas premium.
- Análisis fiscal específico cliente Chile + Australia + USA combinado para cada modelo — solo cubierto a fondo para affiliate en `03-legal-fiscal-cross-border.md`.
- Update del documento con data 2026 H2 en 6 meses — varios benchmarks (CPMs Meta, conversion rates) se mueven rápido.

---

## Fuentes principales (verificables)

**Affiliate:**
- Authority Hacker affiliate marketing survey 2024 (n=2.266) — https://www.authorityhacker.com/affiliate-marketing-survey/
- Ahrefs affiliate marketing statistics 2024 — https://ahrefs.com/blog/affiliate-marketing-statistics/
- ClickBank customer stories (panchoval) — https://www.clickbank.com/customer-stories/

**Dropshipping:**
- Sellers Commerce 2026 statistics — https://www.sellerscommerce.com/blog/dropshipping-statistics/
- Drop Ship Lifestyle success rate — https://www.dropshiplifestyle.com/dropshipping-success-rate-statistics/
- Shopify oficial cost guide 2026 — https://www.shopify.com/blog/how-much-does-it-cost-to-start-dropshipping
- ShipToTheMoon 2026 budget breakdown — https://www.shiptothemoon.com/dropshipping-startup-costs-breakdown/

**DTC:**
- Attn Agency DTC profitability benchmarks 2026 — https://www.attnagency.com/blog/dtc-profitability-benchmarks-2026
- MAccelerator hidden costs of scaling — https://maccelerator.la/en/blog/enterprise/hidden-cost-scaling-dtc-brands/
- Common Thread Co DTC analysis — https://commonthreadco.com/blogs/ecommerce-playbook/dtc-evolution-rebirth-2025

**Print-on-Demand:**
- Printful profit margin guide — https://www.printful.com/blog/what-is-a-good-profit-margin-for-print-on-demand
- Printful Etsy profitability 2026 — https://www.printful.com/blog/is-etsy-print-on-demand-profitable

**Micro-SaaS:**
- Indie Hackers $1K MRR analysis (Stripe-verified) — https://www.indiehackers.com/post/it-takes-5-months-to-reach-1k-in-mrr-491742f806
- Indie Hackers community founder reports — https://www.indiehackers.com/

**Agencia:**
- InfluenceFlow digital marketing agency pricing 2026 — https://influenceflow.io/resources/digital-marketing-agency-pricing-complete-2026-guide-to-costs-models-roi/
- Seven Figure Agency retainer fee models — https://sevenfigureagency.com/5-digital-agency-retainer-fee-models-explained/
- Get Monetizely agency pricing structures — https://www.getmonetizely.com/articles/how-much-should-digital-marketing-retainers-cost-a-complete-guide-to-agency-pricing-structures

**Cursos:**
- Kajabi profitability 2025 — https://www.kajabi.com/blog/is-selling-online-courses-profitable
- Teachable creator earnings — https://www.teachable.com/blog/how-much-content-creators-make

**Newsletter:**
- Beehiiv 1K subs revenue 2025 — https://www.beehiiv.com/blog/how-much-money-can-you-make-from-1-000-newsletter-subscribers-in-2025

**Content creator:**
- Reddit r/PartneredYoutube zero-to-monetized — https://www.reddit.com/r/PartneredYoutube/comments/1qqhii0/people_who_started_youtube_from_zero_how_long_did/
- Digiday creator monetization breakdown — https://digiday.com/marketing/what-it-takes-to-get-paid-by-youtube-tiktok-and-other-social-platforms/

**Trading:**
- Quantified Strategies CFD statistics — https://www.quantifiedstrategies.com/cfd-trading-statistics/
- Good Money Guide CFD risk warnings (regulatorio) — https://goodmoneyguide.com/trading/risk-warning-loss-percentages/
- AFbis forex profitability analysis — https://www.afbis.com/what-percentage/

**FBA:**
- Panda-Boom Amazon FBA success rate 2026 — https://www.panda-boom.com/resources/blog/amazon-fba-success-rate/
- Helium 10 seller earnings 2024 — https://www.helium10.com/blog/how-much-amazon-sellers-make/

**Freelance:**
- ZipRecruiter freelance marketing consultant salary — https://www.ziprecruiter.com/Salaries/Freelance-Marketing-Consultant-Salary
- Twine marketing consultant rates — https://www.twine.net/blog/marketing-consultant-hourly-rates/
- Reddit r/DigitalMarketing freelancer rates 2024 — https://www.reddit.com/r/DigitalMarketing/comments/1ggy7m1/freelancers_whats_your_hourly_rate/

---

**Próximos pasos sugeridos para el equipo:**
1. Discutir esta tabla en sesión de equipo (Romi + Cris + Dali + idealmente Pancho como referencia external).
2. Si hay desacuerdo sobre las probabilidades, ajustarlas y recomputar EV — la metodología está documentada para iterar.
3. Si se decide ir por la opción **agencia + curso + test affiliate controlado**, redactar OKRs Q2-Q4 2026 con los thresholds de "kill" para el experimento affiliate (ROAS, plazo).
4. Volver a leer este documento en 90 días para validar predicciones.

[PENDIENTE]: Caso de equipo LATAM 3 personas que haya hecho transición agencia → cursos exitosamente — buscar 2-3 ejemplos verificables (Daniel Bonifaz / Crehana? Vilma Núñez? Convertkit-style en español?).
[PENDIENTE]: Análisis ROI específico curso "Meta Ads para clínicas LATAM" o similar con TAM real estimado.
