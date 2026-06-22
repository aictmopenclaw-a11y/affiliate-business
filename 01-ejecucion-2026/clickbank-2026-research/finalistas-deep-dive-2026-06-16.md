# Deep dive finalistas · ProDentim vs Prostadine vs Kerassentials · 2026-06-16

> Análisis cruzando 3 fuentes reales: métricas del marketplace ClickBank + validación en Meta Ad Library + reputación/refund (web). Para decidir la primera oferta jugando seguro.

## Tabla comparativa (3 dimensiones)

| Dimensión | ProDentim | Prostadine | Kerassentials |
|-----------|-----------|------------|---------------|
| Nicho | Dental (probiótico oral) | Próstata (hombres 50+) | Hongos uñas |
| Gravity | {g}99.9 | {a}34.1 | {a}39.3 |
| AOV | {g}$156.61 | {a}$135.22 | {g}$154.11 |
| CVR marketplace | {g}**0.98%** | {g}0.87% | {r}0.40% |
| EPC | {g}$1.44 | {g}$1.20 | {r}$0.62 |
| CPA disponible | {g}Sí + Direct Tracking | {g}Sí + Direct Tracking | {a}Sí |
| **Ads activos Meta US** | {r}**73 (saturado)** | {g}10 (poco saturado) | {a}16 |
| Saturación | {r}Alta | {g}**Baja** | {a}Media |
| Reputación | {r}95K clientes, pero quejas de refund en Trustpilot | {g}**4.98/5 (19.6K reviews), 60d honrado** | {a}Legítima, "refund difficulties" reportadas |
| Swipe disponible | {g}**Enorme (73 ads)** | {r}Limitado (10 ads) | {a}Bueno (16 ads, ángulos top) |

```compare
ProDentim
Gravity | 99.9 | 100
CVR | 0.98% | 98
AOV | $156.61 | 92
Ads activos Meta | 73 | 100
EPC | $1.44 | 100

Prostadine (top)
Gravity | 34.1 | 34
CVR | 0.87% | 87
AOV | $135.22 | 79
Ads activos Meta | 10 | 14
EPC | $1.20 | 83

Kerassentials
Gravity | 39.3 | 39
CVR | 0.40% | 40
AOV | $154.11 | 91
Ads activos Meta | 16 | 22
EPC | $0.62 | 43
```

## Perfil por oferta

### ProDentim (dental)
- **Fuerte:** CVR más alto (0.98%), máxima validación en Meta (73 ads), muchísimo swipe para modelar. Dental tiene audiencia amplia. CPA + Direct Tracking.
- **Débil:** la más saturada (73 afiliados compitiendo sube CPMs y la subasta). Bandera de reputación: en Trustpilot algunos reportan que no honran el money-back y que el soporte no contesta. Consumidores enojados pueden reportar el ad a Meta y poner en riesgo la cuenta.
- **Swipe de ángulos vivos:** "My Dentist Got Mad When I Showed Her THIS", "Breath & Gum Problems", "95,000+ People Love Their Healthier Smile", "The Oral Health Video People Over 55 Are Watching".

### Prostadine (próstata)
- **Fuerte:** el mejor balance validación/competencia (validada con solo 10 ads = poca pelea en la subasta). CVR 0.87%. La mejor reputación de las tres (4.98/5, 19.6K reviews, 60 días honrados, FDA/GMP). CPA + Direct Tracking. Nicho de próstata = audiencia específica (hombres 50+) con CPMs potencialmente más baratos. Ángulos de ad muy potentes.
- **Débil:** menos swipe (10 ads) que ProDentim. Audiencia más acotada (techo de escala menor en el corto plazo). Claims de salud masculina exigen cuidado en Meta.
- **Swipe de ángulos vivos:** "The Treatment For The BPH Killed Him", "1 in 7 Long-Term Finasteride Users Develop Post-Finasteride Syndrome" (ángulo miedo + anti-fármaco, muy fuerte).

### Kerassentials (hongos uñas)
- **Fuerte:** ángulos de ad excelentes y fáciles de modelar ("Read This Before Your Next Lamisil Prescription", "Read This If You Hide Your Feet At Pool Parties"). Nicho muy específico = segmentación clara. AOV alto ($154).
- **Débil:** CVR más bajo (0.40%), exige mejor pre-lander para convertir. "Refund difficulties" reportadas. Nicho estacional (verano, pies descubiertos).

## Veredicto (criterio: jugar seguro, ganar confianza, no quemar plata)

**1ª opción: Prostadine.** Es la que mejor encaja con "jugar seguro":
- Validada en Meta pero poco saturada (10 ads): más fácil ser rentable con presupuesto chico, porque no peleas la subasta contra 73 afiliados.
- Mejor reputación de las tres: protege la salud de la cuenta Meta (menos consumidores enojados reportando).
- CVR 0.87% + CPA flat disponible (la síntesis marca CPA como menos riesgoso para empezar).
- Ángulos anti-finasteride ya probados que podemos modelar.

**2ª opción: ProDentim.** Mejor para cuando queramos escalar volumen: 73 ads de swipe reducen el riesgo creativo y el CVR es el más alto. La dejaría para fase 2, cuando la cuenta esté curtida y podamos pelear un nicho más competido. Ojo con la bandera de refunds.

**3ª opción: Kerassentials.** Buena tercera, sobre todo por lo modelables que son sus ángulos. CVR más bajo la hace algo más exigente para un primer test.

## KPIs de la finalista recomendada · Prostadine

```kpi
value: $135.22
label: AOV (ticket promedio)
delta: +CPA flat disponible
---
value: 0.87%
label: CVR marketplace
---
value: 4.98/5
label: Reputación Trustpilot
delta: 19.6K reviews
---
value: 10
label: Ads activos Meta US
delta: Baja saturación
```

## Plan de ataque si vamos con Prostadine (conectado a la síntesis)

1. **Aplicar al programa** (requiere aprobación): escribir a affiliates@prostadine-product.com pidiendo acceso + términos de CPA + creativos. Mencionar que corremos Meta US.
2. **Bridge page propia** (nunca direct link): advertorial estilo "Men's Health Insider" con el ángulo BPH/anti-finasteride, tono informativo, captura de email (opt-in) antes del HopLink. Esto es el modelo lead-gen que sí controlamos.
3. **Tracking ANTES del primer dólar:** fbclid en el HopLink + CAPI/postback, validar con una compra de $1.
4. **Presupuesto test:** estructura simple, kill al ad que gastó 3x el payout sin venta, no tocar la campaña 24-72h, declarar ganador solo tras break-even sobre Initial $/sale a 7 días.
5. **Compliance Meta:** disclaimer en bridge page, sin claims médicos absolutos, ángulo de "soporte natural" no "cura".

## Pendiente para cerrar (no bloquea la decisión, sí el lanzamiento)

- **Titular de la cuenta ClickBank** ("Frank Wilson walter"): resolver a nombre de quién se cobra (W-8BEN + Wise) antes de la primera venta.
- Aplicar y obtener aprobación de afiliado en la oferta elegida (Prostadine y FemiCore requieren approval).

```example
title: Escenario break-even · Prostadine test inicial

Supuesto: Payout afiliado = 50% de AOV = $67.61 por venta.
CVR del marketplace = 0.87% (1 venta por cada ~115 clicks).

Regla del doc: matar ad si gasta 3× el payout sin venta.
Kill threshold = 3 × $67.61 = $202.83 por ad.

Break-even de la bridge page:
- Si pagas $0.80 CPC y necesitas 115 clicks → costo por venta = $92.00
- Margen por venta = $67.61 - $92.00 = -$24.39 (pérdida inicial esperada mientras optimizas)
- Para romper break-even necesitas bajar CPC a ~$0.59 o subir CVR a 1.15%

Meta del test: declarar ganador solo tras break-even sobre $67.61 a 7 días (como indica el doc).
Presupuesto máximo test = 3 ads × $202.83 = $608.49 para liquidar sin venta.
```

*Datos al 2026-06-16. Métricas de marketplace y conteo de ads en Meta cambian a diario: re-verificar antes de lanzar.*
