# Offer Scorer · Cómo usarlo

Script para evaluar ofertas ClickBank en <30 min usando el framework de 11 criterios + math economics Hispano-US.

---

## Uso rápido

### Modo interactivo (recomendado para evaluar 1 oferta)

```bash
cd ~/Projects/affiliate-business
python3 .tools/offer-scorer.py
```

Te pregunta:
1. Metadata oferta (nombre, vendor, URLs, categoría, idioma, geo)
2. 5 hard-fails (s/n cada uno)
3. Métricas numéricas (initial $/sale, avg $/sale, gravity, rebill, comisión, conv rate estimada)
4. 6 positive signals (s/n cada uno)

Output:
- Resumen colored en terminal
- Reporte markdown guardado en `02-offers/oferta-[slug]/scoring-YYYY-MM-DD-HHMM.md`
- Veredicto final: TEST FUERTE / TEST / WAIT / SKIP

**Tiempo:** 5-10 min por oferta.

### Modo batch (para evaluar varias ofertas a la vez)

1. Generar template:
```bash
python3 .tools/offer-scorer.py --template
```

2. Editar `.tools/offer-template.json` con datos reales

3. Ejecutar:
```bash
python3 .tools/offer-scorer.py --batch .tools/offer-template.json
```

Para evaluar varias, copia el template con nombres distintos:
```bash
cp .tools/offer-template.json .tools/oferta-prodentim.json
cp .tools/offer-template.json .tools/oferta-audifort.json
# ...editar cada uno...
python3 .tools/offer-scorer.py --batch .tools/oferta-prodentim.json
python3 .tools/offer-scorer.py --batch .tools/oferta-audifort.json
```

---

## Los 11 criterios

### 5 Hard-Fails (cualquiera = SKIP automático)

1. **Disease claims** en VSL → ban Meta + FTC
2. **Tools page prohíbe paid traffic** → no operable
3. **Avg $/sale < $50** → margen muy apretado Hispano-US
4. **Initial $/sale < $25** → no llegas a Customer Distribution Requirement rápido
5. **Refund rate > 25%** → destruye economics

### 6 Positive Signals (>4 de 6 = TEST candidate)

1. **Vendor 3+ años** en ClickBank
2. **VSL actualizado recientemente** (señal A/B testing activo)
3. **Affiliate manager respondió <48h** a tu email test
4. **CAPI postback documentado** en tools page
5. **Recurring rebill** > $0 (LTV bonus)
6. **Funciona español + inglés** (más flexibility)

### 4 Métricas numéricas críticas

- Initial $/sale (target ≥$25)
- Avg $/sale (target ≥$80, mínimo $50)
- Gravity (sweet spot 30-150 en 2026)
- Avg Rebill (bonus si subscription)

### Math economics automática

Calcula:
- Net per sale = Avg $/sale × Commission %
- Revenue per click (RPC) = Net × Conv rate
- CPC breakeven (1.0x ROAS) = RPC
- CPC target 1.3x ROAS sostenible
- CPC target 2.0x ROAS (winner threshold)

Compara contra CPC industry Hispano-US ($1.20-2.50 nutra).

---

## Veredictos

| Veredicto | Cuándo |
|---|---|
| **TEST FUERTE** | 0 hard-fails + 5+ positive signals + economics viable |
| **TEST** | 0 hard-fails + 4+ positive signals + economics viable o borderline |
| **WAIT** | 0 hard-fails + 3 positive signals (backlog) |
| **SKIP** | Cualquier hard-fail O economics no viables O <3 positive signals |

---

## Workflow operativo recomendado

### Semanal (Romi · SOP 01)

1. Lunes: investigar 20 ofertas en ClickBank Marketplace
2. Martes: pre-filtro · descartar las obviamente malas (10 sobreviven)
3. Miércoles: ejecutar `offer-scorer.py` para los top 5
4. Jueves: TEST FUERTE → preparar brief creativo (SOP 02)
5. Viernes: presentar al sync · decisión final equipo

### Por oferta (~10 min)

```bash
python3 .tools/offer-scorer.py
# responde las preguntas...
# revisa output markdown...
# si TEST → continúa a SOP 04 setup técnico
```

---

## Output guardado

Cada scoring genera:
- `02-offers/oferta-[slug]/scoring-YYYY-MM-DD-HHMM.md`

Si vuelves a evaluar la misma oferta semanas después, se guarda con timestamp distinto · puedes comparar evolution.

---

## Limitaciones

- **Refund rate** y **AM responsiveness** requieren research manual previo (no auto-detectable)
- **VSL updated** es subjetivo · revisar testimonios fechados / comentarios recientes
- **Conv rate estimada** debe ser conservadora al inicio (1-1.5%) · ajustar después con data real
- **CPC industry** es promedio nutra Hispano-US · puede variar por sub-niche

---

## Próximas mejoras (futuras)

- Auto-scrape ClickBank Marketplace para gravity histórico
- Integration con Meta Ads Library API para verificar saturación
- Auto-detección AOV via VSL scraping
- Comparativa side-by-side de múltiples ofertas
- Export a Notion / Sheets para tracking centralizado

---

*Script v1.0 · 2026-04-29 · framework basado en `01-ejecucion-2026/clickbank-2026-research/02-offer-selection-framework.md`*
