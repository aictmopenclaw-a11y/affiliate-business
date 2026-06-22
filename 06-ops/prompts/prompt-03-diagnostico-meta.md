# Prompt 03 · Diagnóstico Semanal Meta Ads

**Owner:** Cris
**Cuándo usar:** SOP 06 paso 2 — análisis weekly de export Meta Ads
**Output esperado:** bullets para Slack #datos · sin tabla larga, solo accionables

---

## Prompt

```
Analiza este CSV exportado de Meta Ads Manager (últimos 7 días):
[paste CSV o adjuntar archivo]

CONTEXTO:
- Negocio: affiliate marketing ClickBank
- Mercado: hispano-US
- Stack: Meta Ads como canal primario, Bidcap strategy
- Target ROAS: > 1.5x (kill < 1.0 después de 5 días)
- Frequency target: < 3 (refresh si > 3)
- Commission ceiling: $X CPA breakeven (variable por oferta)

NECESITO:

1. **ROAS por campaña** con flag de fatiga (frequency > 3 = warning rojo)
2. **Top 3 creativos** por CTR + Top 3 por CPA (los mejores en cada métrica)
3. **Bottom 3 a pausar** (con razón específica)
4. **Audiencia con mejor performance** (si hay breakdown por audience disponible en el export)
5. **Bid strategy + budget allocation sugerida** para próxima semana
6. **Una hipótesis no obvia** que valga testear (ej. "el angle X parece subir cuando se combina con formato Y")

OUTPUT: bullets para Slack #datos. Sin tabla larga, solo accionables. Máximo 15 bullets totales. Cada bullet máximo 2 líneas.

NO uses emojis salvo:
- 🟢 ROAS > 2.0
- 🟡 ROAS 1.0-2.0
- 🔴 ROAS < 1.0
- ⚠️ Frequency > 3

Empieza con un summary line de 1 frase con el highlight de la semana.
```

---

## Tips de uso

- **Si el CSV es enorme** (>500 filas), dame primero un resumen pre-procesado:
  - Group by campaign + sumar spend, conv, calc ROAS
  - Top 10 ad creatives por spend
- **Spend mínimo para considerar** (ignorar ruido): $10 USD
- **Día mínimo para evaluar:** 3 días (si está en fase de aprendizaje, no killear)

---

## Cuándo NO usar este prompt

- Primer día live → no hay data suficiente
- Después de cambio mayor (audience nueva, budget +50%) → re-aprendizaje, esperar 3-5 días
- Cuando el problema es claramente técnico (pixel roto) → no es análisis de performance, es debug

---

## Variantes del prompt

### Variante para análisis mensual (más profundo)
```
Analiza este CSV de Meta Ads de los últimos 30 días.

Quiero análisis profundo:
1. Tendencia ROAS semana a semana (¿está subiendo, bajando, estable?)
2. Top 5 creativos por revenue absoluto
3. Patrones por día de la semana (¿algún día performa diferente?)
4. Patrones por hora (si breakdown disponible)
5. Comparativa por angle estratégico (Curiosidad vs Problema vs Lifestyle, etc.)
6. Insights para próximo mes:
   - ¿Qué funcionó? ¿Por qué?
   - ¿Qué no funcionó? ¿Por qué creemos?
   - ¿Qué probar próximo mes?

Output: documento estructurado en markdown para retro mensual.
```

### Variante para detectar fraude de tráfico
```
Sospecho que parte del tráfico es fraudulento (clicks sin conversiones a tasas anormales).

Analiza este CSV y dame:
1. Campañas con CTR > 3% PERO conv rate < 0.3% (red flag)
2. Anomalías por día (spikes inusuales)
3. Audiencias con CTR anormalmente alto (>2x el promedio)
4. Si hay placement breakdown: ¿algún placement particular concentra fraude?

Recomendación: ¿qué excluir / pausar / monitorear?
```

### Variante para preparar reporte ejecutivo (mensual)
```
Convierte este CSV de 30 días en un reporte ejecutivo estilo "for CEO":
- 1 frase top-line con el dato más importante
- 3 wins del mes (números específicos)
- 3 misses del mes con razón
- 1 decisión estratégica que recomendamos para próximo mes

Output: 1 página máximo. Lenguaje claro, sin jerga técnica innecesaria.
```
