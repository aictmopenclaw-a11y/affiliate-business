# Tactics Aplicables · Consolidación Cross-Fuente

> Síntesis de las tácticas accionables extraídas de las 9 fichas publicadas.
> Cada táctica clasificada: **Aplicable** / **Adaptable** / **No aplicable** para stack Hispano-US ClickBank + Meta Ads.

---

## Patrones convergentes (lo que dicen TODOS los serios)

### 1. Diversificación creativa es el cuello de botella post-Andromeda 2024-2026

**Quién lo dice:** Tier 11, Foxwell, Sanchez, Holiday, Hott
**Consenso:** 5 creativos/sem ya no alcanza. Andromeda quema variations 10x más rápido que pre-2024.

**Number convergente:** **20-50 creativos/sem** mínimo para sostener performance estable post-Andromeda.

**Aplicable:** SÍ.
**Implicancia para nuestro stack:** Dali debe escalar producción con HeyGen + Creatify para llegar a 20+ variantes/sem. NO es opcional.

---

### 2. CAPI postback es obligatorio, no opcional

**Quién lo dice:** Tier 11, Foxwell, ClickBank Affiliated (Venture Beyond ep 204)
**Consenso:** sin CAPI, Andromeda optimiza con data incompleta · ROAS calculado por Meta es ficticio.

**Aplicable:** SÍ.
**Implicancia para nuestro stack:** SOP 04 setup funnel · paso 10 (CAPI postback) es BLOQUEANTE. Cris debe armar Cloudflare Worker desde día 1. No "lo haremos cuando validemos" · sin esto el resto no sirve.

---

### 3. Profit engineering > vanity ROAS

**Quién lo dice:** Taylor Holiday (CTC) principalmente · refuerzo Tier 11
**Consenso:** ROAS bonito sin MER positivo es teatro. Pensar en margin contribution después de fees + refunds + tools.

**Aplicable:** SÍ con adaptación.
**Implicancia para nuestro stack:** offer-scorer ya calcula CPA breakeven · agregar checkbox "MER incluye fees ClickBank 7.5%+$1 + refunds 10-15% reservado?" en próxima versión del scorer.

---

### 4. Creative "ugly ads" > polished

**Quién lo dice:** Barry Hott (framework central), Sanchez, Shackelford
**Consenso:** ads con producción baja + autenticidad humana superan ads pulidos de agencia 70% del tiempo en DTC.

**Aplicable:** PARCIAL.
**Implicancia para nuestro stack:** Dali debe balancear · 70% "ugly real-looking" + 30% polished. NO sobre-producir HeyGen avatares con look comercial. Probar UGC sintético Creatify con setup casero.

---

### 5. Single-channel focus hasta validar

**Quién lo dice:** Ralph Burns, Taylor Holiday, ClickBank Affiliated speakers
**Consenso:** diversificar Meta+TikTok+YouTube en paralelo al inicio = mediocridad en todos.

**Aplicable:** SÍ.
**Implicancia para nuestro stack:** Meta Ads como único canal hasta mes 4-6. NO ceder a la tentación de "probar también TikTok Shop". Disciplina.

---

## Tácticas específicas por dimensión

### Selección de oferta

**De Tier 11 / Ralph Burns:**
- nCAC framework: track Net CAC con refunds + fees incluidos · target nCAC < AOV × 0.6
- [Aplicable] Aplicar a evaluación pre-test de cada oferta

**De ClickBank Affiliated (Venture Beyond ep 204):**
- Focus 1-3 verticales máximo (Venture Beyond solo: health, wellness, beauty)
- [Aplicable] Nosotros: nutra (dental + microbiome + audio-VSL) según research previo

**De Modern Retail / Dreamday PR:**
- DTC brands con affiliate hitting 25-35% revenue tienen integración profunda · no solo "links"
- [Adaptable] Para nosotros como afiliados: buscar vendors con tools page robusta + AM responsivo

---

### Setup Meta Ads

**De Tier 11 (Episode 719 nCAC framework):**
- 8 ad types principales: Hook variations + UGC + Demo + Listicle + Comparison + Authority + Lifestyle + Direct CTA
- Mix obligatorio: 30% UGC + 25% Demo + 20% Hook variations + resto distribuido
- [Aplicable] Plug directo a SOP 07 producción creativos

**De Foxwell Digital:**
- Cuenta Meta organizada con CBO (Campaign Budget Optimization) + Advantage+ Audience por default
- 30+ concepts/mes per offer activa (no 10)
- Niche angles > broad audiences
- Organic feed activo como input signal del ad ranking
- [Aplicable] Cris configurar BM con estas reglas desde día 1

**De Hott:**
- "Ugly ads" con texto overlay grande + Format vertical 9:16 obligatorio
- Hook visual en 1.5 seg, no 3 seg como pre-2024
- [Aplicable] Brief creativo Romi → Dali debe especificar 1.5 seg hook target

---

### CAPI + tracking

**De Tier 11 + Foxwell convergencia:**
- Setup CAPI con Conversions API Gateway (Meta oficial) si no se quiere mantener server propio
- Deduplicación obligatoria entre Pixel + CAPI (event_id match)
- 5-7 events trackeados mínimo: PageView, ViewContent, AddToCart, InitiateCheckout, Purchase (+ AddPaymentInfo si aplicable)
- [Aplicable] Cris arma Cloudflare Worker o usa CAPI Gateway Meta · ambos válidos

---

### Creative production

**De Sanchez (8 Key Principles):**
1. Hook = first 1.5 sec (no 3)
2. Pattern interrupt visual cada 3-5 sec
3. Subtitles always on (85% mobile sin audio)
4. UGC > studio (autenticidad bate producción)
5. Voiceover natural (no TTS robotic)
6. Direct CTA al menos 2 veces (no solo final)
7. Format 9:16 vertical priority absoluta
8. Length 15-30 sec sweet spot 2025+
- [Aplicable] Dali workflow Mon-Fri framework de Sanchez · adoptar tal cual

**De Hott (ugly ads framework):**
- Texto overlay con stroke (no shadow) para legibilidad mobile
- Colores contrastantes saturados (no minimal-aesthetic)
- "Real person filming with phone" look
- Captions hardcoded (no live captions Meta · son inestables)
- [Aplicable] Especificar en SOP 07

**De Shackelford (regulated brands):**
- Para health/nutra: testimoniales + disclaimer visible en frame
- Avoid before/after directos (Meta disapproval risk)
- "Lifestyle outcome" approach (mostrar el resultado de vida, no el cambio físico)
- [Aplicable] Crítico para compliance nutra (refuerza `affiliate-compliance-nutra.md`)

---

### Economics + escalado

**De Taylor Holiday (profit engineering):**
- MER (Marketing Efficiency Ratio) = Total Revenue / Total Ad Spend
- Target MER > 3x para DTC sustainable, > 2x para affiliate
- LTV pensar incluso para single-purchase (rebill stacks)
- [Adaptable] En affiliate sin email capture el LTV es del vendor · pensar en repeat por subscription rebill

**De Tier 11 (escalado vertical):**
- +30% max por movida budget · esperar 5-7 días learning Meta
- Si ROAS sostenido 14 días > 2x → escalar +50% una vez · luego volver a +30%
- [Aplicable] Plug directo a SOP 06 weekly analysis

**De Foxwell (escalado horizontal):**
- 4 caminos para escalar horizontal: nuevas creatives, nuevas audiencias, nuevos placements, nuevos canales
- Priorizar nuevas creatives + nuevas audiencias dentro de Meta antes de saltar canal
- [Aplicable] Roadmap mes 4+ cuando validemos winner

---

### Compliance + risk management

**De Shackelford (regulated brands):**
- Backup ad accounts mínimo 2 desde día 1 (no esperar al ban)
- Multilogin obligatorio para Hispano-US (bans 30-50% año 1 expectativa)
- Pre-aprobar versiones "safe" de cada ad antes de versión "aggressive"
- [Aplicable] Refuerza decisión Multilogin en STACK-MINIMO-VIABLE

**De ClickBank Affiliated (varios episodios):**
- Refund rate threshold ClickBank: 20% suspende 90 días · presupuestar 10-15% reserva
- Customer Distribution Requirement: 5 ventas + 2 métodos pago + 2 sem wait
- [Aplicable] Confirmado en research ClickBank 2026 previo

---

## Tactics NO aplicables a nuestro stack

Importante documentar lo que NO funciona para no perder tiempo:

| Táctica | Fuente | Por qué no aplica |
|---|---|---|
| B2B SaaS growth funnels | Aazar Ali Shad | No fit con stack ClickBank nutra |
| TikTok Shop affiliate | Iced Media (lead) | No es ClickBank · capa adicional de complejidad |
| Email marketing nurture flow | Multiple fuentes DTC | En affiliate no capturamos email · va al vendor |
| Influencer seeding programs | CTC, Dreamday PR | Requiere brand propio · no aplica a afiliados |
| PR-driven affiliate (Dreamday playbook) | Modern Retail | Requiere brand propio · adaptable solo Fase 4+ |
| Enterprise account-based marketing | Tier 11 ocasional | $50K+/mes budget mínimo · no para nosotros |

---

## Lo que NINGUNA fuente dice (gap detectado)

Cosas que esperaríamos encontrar pero ninguna fuente cubre profundo:

1. **Cross-border tax para afiliados LATAM operando US** — solo nuestra `affiliate-financial-cross-border.md` lo tiene
2. **W-8BEN-E proceso paso a paso para SpA chilena** — nadie cubre
3. **CAPI postback con servidor en LATAM** — Tier 11 menciona CAPI Gateway Meta como solución
4. **Refund rate management con vendor LATAM-friendly** — gap
5. **Specific Spanish-language Hispano-US benchmarks** — Pancho Val es el único que toca esto

Estos gaps confirman que nuestro repo aporta valor único en español + cross-border.

---

## Resumen ejecutivo de acción

### Top 10 tactics a aplicar mes 1

1. **Producir 20+ creativos/sem (no 5)** — Dali con HeyGen + Creatify [convergente]
2. **CAPI postback desde día 1** — Cris Cloudflare Worker [convergente]
3. **Hook visual 1.5 seg, no 3** — Sanchez + Hott
4. **8 ad types mix obligatorio** — Tier 11 framework
5. **Multilogin desde día 1 Hispano-US** — Shackelford regulated brands
6. **2 ad accounts backup minimum** — Shackelford
7. **MER tracking incluyendo fees ClickBank** — Holiday profit engineering
8. **nCAC framework con refunds reservados 10-15%** — Tier 11
9. **30+ concepts/mes per offer activa** — Foxwell
10. **"Ugly ads" 70% + polished 30% mix** — Hott

### Tactics a evaluar mes 2-3

- Conversions API Gateway vs server propio (Foxwell + Tier 11)
- ASC+ Shopping Campaigns para affiliate (Tier 11 mentioned)
- TikTok Spark Ads como secondary channel (Sanchez mencionado opcionalmente)
- Stable email capture pre-VSL (CTC playbook adaptado)

### Tactics a evaluar mes 4+

- Brand propio en lugar de afiliado (Dreamday PR playbook · si validamos affiliate)
- Multi-vendor affiliate diversification (Venture Beyond approach)
- Mid-market consulting offer (Foxwell model post-success)

---

*Tactics-aplicables v1.0 · 2026-04-29 · re-validar mensual con nueva data de tests reales*
