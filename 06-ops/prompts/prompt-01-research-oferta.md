# Prompt 01 · Research de Oferta ClickBank

**Owner:** Romi
**Cuándo usar:** SOP 01 paso 2 — análisis preliminar de top 20 ofertas filtradas
**Output esperado:** tabla en markdown lista para pegar en Notion

---

## Prompt

```
Eres mi analista de afiliación. Te paso 5 productos de ClickBank que estoy considerando para nuestro negocio de affiliate marketing performance.

CONTEXTO DE NUESTRO NEGOCIO:
- Equipo de 3: Romi (estrategia), Cris (tech/ads), Dali (creativos)
- Mercado: hispano-US (mujeres 25-45, expansible 35-65)
- Nicho preferente: salud / nutra / beauty
- Stack: Meta Ads como canal primario, Landerlab para landings, ClickBank network
- Capital inicial: $11K USD
- Objetivo trimestre 1: validar 1 funnel a ROAS sostenido > 1.3x

PARA CADA UNO DE LOS 5 PRODUCTOS, DAME:

1. **Score 1-10 de fit** con nuestro perfil (mujeres 25-45 hispano-US, salud/beauty)
2. **AOV estimado** y **comisión típica** que estarían pagando afiliados similares
3. **3 ángulos creativos potenciales** basados en lo que sugiere el VSL del vendor
4. **Riesgos visibles** (refund rate alto si lo conoces, claims dudosos del vendor, saturación de mercado, restricciones de ClickBank/Meta)
5. **Veredicto: TEST / SKIP / WAIT** con justificación de 2 líneas

PRODUCTOS:
[paste de los 5 productos con sus métricas: nombre, vendor, gravity, AOV declarado, comisión declarada, idioma, geo]

OUTPUT: tabla en markdown con columnas:
| # | Producto | Score | AOV | Comisión | Angles | Riesgos | Veredicto |

Después de la tabla, danos tu **recomendación final** sobre cuál arrancar a TEST esta semana, con 3-4 frases de justificación.

NO uses emojis. Sin texto extra.
```

---

## Tips de uso

- Pegar **5 productos máximo** por corrida (no 20 — el contexto se pierde)
- Si la respuesta es muy genérica, repreguntar con: "Sé más específico en los ángulos, dame hooks reales que un copywriter usaría"
- Si te sugiere algo que no calza con el playbook, recordar el contexto y repreguntar

---

## Cuándo NO usar este prompt

- Si la oferta tiene gravity < 15 (sin tracción) — no perder el time del análisis
- Si la oferta es de un nicho completamente fuera (ej. crypto, gambling) — pasar directo a SKIP
- Si ya tenemos winner activo del mismo vendor — riesgo de canibalización

---

## Variantes del prompt

### Variante para evaluar oferta única en profundidad
```
Profundiza solo en este producto: [URL VSL + nombre vendor].

Quiero:
1. Análisis del VSL: estructura (problema, solución, pricing, urgencia, garantía)
2. Hooks que el vendor usa en copy de tools page
3. Angle propuesto para nuestro target (mujer 35-45 hispano-US)
4. Math de economics: si AOV es $X y comisión $Y, ¿cuál es el CPA breakeven asumiendo 1.5% conv rate?
5. Compliance flags específicos (claims dudosos del vendor que NO podemos repetir)

Output: análisis estructurado en bullets, accionable.
```

### Variante para comparar 2 ofertas head-to-head
```
Comparame estas 2 ofertas en detalle:
A: [oferta A]
B: [oferta B]

Criterios:
- Fit con nuestro target
- Economics (AOV, comisión, CPA breakeven)
- Saturación competitiva
- Variabilidad creativa posible (¿cuántos angles distintos puedo armar?)
- Riesgo de compliance

Veredicto: ¿con cuál arranco esta semana y cuál va a backlog?
```
