# Skill · ClickBank Operativo

> **Cuándo cargar este skill:** antes de seleccionar oferta, antes de configurar HopLink, antes de armar economics de una oferta nueva.
> **Owner conceptual:** Romi
> **Última actualización:** 2026-04-28

---

## ¿Qué es ClickBank?

Network de afiliados especializada en productos digitales y físicos de **info-products, salud/nutra, y fitness**. Diferenciador clave vs CPA networks: **ecosistema maduro**, vendors entregan VSL + landing + emails ya optimizados, y comunidad de afiliados que comparte playbooks reales.

**Modelo:** vendor sube producto → afiliado obtiene HopLink (URL única) → cliente compra vía HopLink → ClickBank tracking asigna comisión.

**Comisión típica:** 50-90% del precio (sí, el vendor se queda con menos del 50% en muchos casos — el volumen de afiliados lo compensa).

---

## Métricas para evaluar una oferta

### Las 4 que importan

| Métrica | Qué es | Target | Bandera roja |
|---|---|---|---|
| **Average Payout** | USD que ganamos por venta | $80+ | < $50 (no escala) |
| **Conversion Rate** | % VSL → compra | 1-2% | < 0.5% |
| **Gravity Score** | Algo de momentum + cantidad afiliados activos últimos 12 sem | 30-100 | < 15 (sin tracción) o > 200 (saturado) |
| **AOV** (Average Order Value) | Precio promedio | $150+ | < $80 |

### Cómo leer Gravity correctamente

**Gravity NO es ventas absolutas.** Es un score que pondera afiliados únicos que generaron al menos una venta últimas 12 semanas. Score alto = oferta validada por otros + competencia alta. Score bajo = oferta nueva o quemada.

- **Gravity 30-100** — sweet spot para empezar (validada pero no saturada)
- **Gravity 100-200** — oferta caliente, más competencia, mejor para affiliates con cuenta madura
- **Gravity > 200** — gigante, requiere creatividades muy diferenciadas para destacar
- **Gravity < 15** — riesgo: o es nueva sin validar o el VSL no convierte

### Métricas extra a chequear en marketplace

- **Initial $/sale** — primera comisión (si hay upsells, después suben)
- **Avg %/sale** — % comisión promedio (incluyendo upsells)
- **Avg Rebill** — ingresos recurrentes (si producto es subscription)
- **Activated** — % productos en marketplace activos
- **Refund rate** — buscarlo en grupos de Skalers o Reddit /r/AffiliateMarketing (ClickBank no lo expone públicamente)

---

## Status tiers de afiliado

| Tier | Ventas anuales | Beneficios |
|---|---|---|
| **Standard** | < $100K USD | Acceso básico al marketplace |
| **Platinum** | $250K+ USD | Account manager, eventos, soporte prioritario |
| **Diamond** | $5M+ USD | CPAs negociados directos, ofertas exclusivas pre-lanzamiento, acceso al annual summit |

**Por qué importa:** Diamond te da acceso a ofertas que NO están públicas. Pancho Val opera principalmente con Diamond ofertas que él consigue antes que el resto. Para llegar a Platinum hay un baile de fake-it-til-you-make-it que Skalers Pro enseña (aceptable porque ClickBank lo tolera mientras facturas).

---

## Selección semanal de oferta · Proceso (SOP 01)

1. **Login marketplace ClickBank** → filtrar por categoría (Health & Fitness · Nutrición)
2. **Filtrar por idioma:** Spanish (incluye ofertas hispano-US y LATAM)
3. **Sort por Gravity descendente** → exportar top 20 a CSV
4. **Ejecutar Prompt 01** (research de ofertas) con Claude Cowork
5. **Top 5 finalistas:** revisar VSL completo del vendor
6. **Anotar:**
   - Hooks que usa el vendor en el VSL
   - Angles que probaron en sus ads (revisar en SpyHero / Meta Ads Library con el dominio del vendor)
   - Garantías y precios (precio entrada + upsells)
   - Categoría dolor (¿articulaciones? ¿sueño? ¿peso? ¿próstata?)
7. **Economics math:**
   ```
   AOV × Comisión × Conv rate estimada × CPA breakeven
   = ¿podemos pagar X por click y aún ser rentables?
   ```
8. **Decisión:** 1 oferta a TEST esta semana, 2 a backlog, 2 archive
9. **Crear folder en `02-offers/[oferta-XX]/`** con `brief.md` inicial

---

## HopLink · Tracking link

Estructura típica: `https://hop.clickbank.net/?affiliate=[TU_AFILIADO]&vendor=[VENDOR]&tid=[TRACKING_ID]`

**Tracking ID es crítico:** úsalo para distinguir variantes de ad / landing / audiencia. Ejemplos:
- `tid=fb_a1_h3` (Facebook, audience 1, hook 3)
- `tid=ig_quiz_v2` (Instagram, landing tipo quiz, versión 2)
- `tid=adv_cris_w17` (cuenta advertiser Cris, semana 17)

**Convención del equipo:** definir en `04-tech/pixels-config/tracking-id-convention.md` antes de primer launch.

---

## Diamond ofertas vs Marketplace público

### Marketplace público
- Todos pueden verlo y promoverlo
- Mayor competencia
- Menor comisión negociada (la default del vendor)

### Diamond / negociadas
- Vendor ofrece CPAs especiales a top afiliados
- Pueden incluir: rev share más alto, CPA fijo en lugar de %, ofertas pre-launch, scripts personalizados, exclusividad geográfica
- Acceso vía: Skalers comunidad, ClickBank Account Manager (a partir Platinum), networking en summits

**Camino para llegar:** primer winner público → escalar a Platinum → activar Account Manager → preguntar por Diamond ofertas en nuestro nicho.

---

## Refund rates y por qué importan

**ClickBank cobra los refunds al afiliado.** Si vendiste $1000 esta semana y la próxima refundean $300, ClickBank descuenta de tu próximo payout.

**Refund rates típicos:**
- Productos físicos nutra: 5-15% (normal)
- Productos digitales (cursos/ebooks): 8-20%
- Garantías 60 días: refund rate sube al final del período

**Cómo investigar refund rate antes de promover:**
- Preguntar en grupo Skalers
- Buscar en Reddit /r/AffiliateMarketing reviews del producto
- Pedir al vendor (algunos lo comparten transparente, otros no)
- **Si refund rate > 25%, no promover** — destruye economics

---

## Productos físicos vs digitales

| Aspecto | Físico | Digital |
|---|---|---|
| AOV típico | $150-350 | $47-197 |
| Comisión | 50-75% | 75-90% |
| Refund rate | 5-15% | 8-20% |
| Tiempo de cobro | 2-4 semanas | 1-2 semanas |
| Compliance | Más estricto (FTC, FDA) | Menos estricto pero igual ojo |
| Volumen escalable | Limitado por stock vendor | Ilimitado |

**Recomendación arranque:** **productos físicos nutra**. Mayor AOV, mayor margen absoluto por venta, refund más predecible que digitales.

---

## Compliance crítico de ClickBank

### Lo que ClickBank prohíbe explícitamente
- Spam (email no solicitado)
- Misleading claims (afirmar resultados imposibles)
- Cookie stuffing
- Brand bidding sin permiso del vendor en Google Ads
- Ads que digan "Free" cuando el producto es pago

### Lo que el vendor a veces prohíbe (revisar tools page de cada oferta)
- Brand bidding (puede ser solo en algunos motores)
- Email marketing a listas frías
- Native ads (algunos vendors no quieren tráfico Outbrain/Taboola)
- Geos específicos (algunas ofertas solo USA, no LATAM)

### Trampa común
**El vendor te puede cortar comisiones retroactivamente** si violas sus reglas (incluso si ya vendiste). Siempre leer la tools page completa antes de comprar tráfico para una oferta nueva.

---

## Workflow estándar nueva oferta

```
1. Detección (sourceing)
   ↓
2. Research preliminar (Claude Cowork + Prompt 01)
   ↓
3. VSL completo + análisis de competencia (SpyHero)
   ↓
4. Decisión TEST / BACKLOG / ARCHIVE (Romi owner)
   ↓
5. Si TEST: crear folder /02-offers/[oferta-XX]/
   ├── brief.md           (mensajería + angles)
   ├── research.md        (vendor + competencia)
   └── economics.md       (math AOV × comisión × ROAS)
   ↓
6. Brief creativo a Dali (Prompt 02)
   ↓
7. Setup técnico Cris (SOP 04)
   ↓
8. Live con $50/día + alarma Slack
   ↓
9. Daily monitoring (SOP 05)
   ↓
10. Decisión semanal: scale / kill / iterate (SOP 06)
```

---

## Errores que NO cometer

1. **Promover oferta sin revisar VSL completo** — si el VSL no te convence a ti, no convierte
2. **Saltar la math de economics** — si CPA breakeven < $5, no es viable con Meta Ads
3. **Ignorar el refund rate** — un 30% de refunds destruye el ROAS calculado
4. **Brand bidding sin permiso** — baneo del vendor + comisiones canceladas retroactivas
5. **Usar tracking IDs no descriptivos** — pierdes 50% del valor del análisis
6. **Empezar con > $200/día** — no validamos a budgets altos
7. **No tener segundo método de pago** — primera tarjeta falla y la campaña muere

---

## Recursos externos

- **Marketplace:** clickbank.com/marketplace
- **Knowledge base oficial:** support.clickbank.com
- **Comunidad Skalers (Pancho Val):** [URL pendiente — Romi compra y comparte acceso]
- **Reddit:** r/AffiliateMarketing, r/clickbank
- **SpyHero:** spyhero.com (espiar competencia)
- **Meta Ads Library:** facebook.com/ads/library (filtrar por país USA + buscar keywords del nicho)

---

*Este skill se actualiza cuando: se cambian las reglas de ClickBank, se descubre un patrón nuevo en sourcing, se valida un workflow mejor.*
