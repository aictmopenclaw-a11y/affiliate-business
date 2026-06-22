# SOP 06 · Análisis Semanal y Decisión de Scaling

**Owner:** Cris
**Frecuencia:** Lunes 10AM (antes del sync de las 11AM)
**Tiempo:** 90 min
**Inputs:** export Meta Ads últimos 7 días, ClickBank weekly summary
**Output:** weekly report en `05-data/weekly-reports/YYYY-WW.md` + decisión scaling presentada en sync

---

## Pasos

### 1. Export data (10 min)
- Meta Ads Manager → Reports → últimos 7 días (vs. 7 días previos)
- Métricas: spend, impressions, clicks, CTR, CPC, CPA, ROAS, frequency
- Breakdown: by campaign, ad set, ad creative
- Export CSV → `05-data/raw-exports/YYYY-WW-meta-export.csv`
- ClickBank → Reports → últimos 7 días → CSV con orders + refunds

### 2. Análisis con Claude Cowork (30 min)
- Abrir `06-ops/prompts/prompt-03-diagnostico-meta.md`
- Pegar CSV (puede que el archivo necesite resumen previo si es grande)
- Cowork devuelve:
  - Top 3 creativos por CTR
  - Top 3 creativos por CPA
  - Bottom 3 a pausar
  - Audiencia con mejor performance
  - 1 hipótesis no obvia para testear

### 3. Decisiones de scaling (15 min)

**Regla scale (Pancho Val + Skalers):**
- Campaña con ROAS > 2.0x sostenido 5 días + frequency < 2.5 → escalar **+30%** budget
- NO escalar > 30% en una sola movida (Meta entra a re-aprendizaje)

**Regla kill:**
- Campaña con ROAS < 1.0x después de 5 días con > $50 spend → pausar
- Campaña con CPA > 2x commission ceiling después de 3 días → pausar
- "3x Kill Rule": si gastaste 3x el CPA target sin conversión, kill

**Regla iterate:**
- ROAS 1.0-2.0x → mantener budget, refresh creativos (SOP 09)
- Frequency > 3 → trigger SOP 09 sin debate

### 4. Decisiones documentadas (15 min)
Crear `05-data/weekly-reports/YYYY-WW.md`:

```markdown
# Weekly Report · Semana XX (YYYY-MM-DD a YYYY-MM-DD)

## Top line
- Spend total: $X USD
- Conversiones: X
- Revenue: $X USD
- ROAS overall: X.XX
- Margen neto: $X USD
- vs semana anterior: +/-X%

## Decisiones tomadas
### Scale
- [Campaña X] · ROAS 2.3 · budget $50 → $65 (+30%)

### Kill
- [Campaña Y] · ROAS 0.7 después de 5 días → pausar

### Iterate
- [Campaña Z] · frequency 3.4 → SOP 09 refresh creativo

## Hipótesis a testear próxima semana
- [Hipótesis no obvia]

## Necesidades del equipo
- Romi: [si necesita oferta nueva]
- Dali: [si necesita batch de variantes]
- Cris: [si necesita resolver algo técnico]
```

### 5. Presentación en sync (15 min)
- En sync 11AM (SOP 10), Cris presenta primero
- Slides simples (puede ser en Notion o solo el .md proyectado)
- Foco: números → decisiones → necesidades

### 6. Ejecución decisiones (5 min post-sync)
- Aplicar scale en Meta Ads Manager
- Aplicar kill (pausar, NO eliminar)
- Notificar Dali si hay refresh requests

---

## Checklist

- [ ] Export Meta + CB de últimos 7 días
- [ ] CSV en `05-data/raw-exports/`
- [ ] Análisis Cowork ejecutado
- [ ] Top 3 / Bottom 3 identificados
- [ ] Decisiones scale/kill/iterate documentadas
- [ ] Weekly report en `05-data/weekly-reports/`
- [ ] Presentado en sync lunes
- [ ] Ejecución post-sync confirmada

---

## Errores frecuentes

1. Escalar > 30% → re-aprendizaje destructivo
2. Killear a los 2 días → no le diste a Meta tiempo de optimizar
3. No documentar decisión → no aprendes patrones
4. Saltar la math (decidir por feeling) → erosión de margen
5. Aplicar mismo budget a todas las campañas → no priorizas winners

---

## Historial

- **v0.1 · 2026-04-28** — estructura inicial
