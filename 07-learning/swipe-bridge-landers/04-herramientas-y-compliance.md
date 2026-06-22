# Herramientas, spy tools y compliance Meta · referencia

> Cómo construir el bridge lander, con qué espiar a otros afiliados, y qué reglas de Meta respetar para no quemar la cuenta. Datos verificados 2026 (precios cambian, re-verificar antes de comprar).

```kpi
value: Carrd
label: Builder para validar
delta: $19/año
---
value: Convertri
label: Builder para escalar
delta: ~$53/mes anual
---
value: Ad Library
label: Spy tool para empezar
delta: gratis
```

## 1. Builders de landers (para construir el bridge)

| Builder | Plan base | Velocidad | Para afiliado nutra |
|---|---|---|---|
| **Carrd** | {g}$19/año | {g}Muy alta | Para EMPEZAR y validar. 1 página, sin multi-step ni A/B, pero barato y rápido |
| **Convertri** | {g}~$53/mes anual | {g}Muy alta (410ms, CDN propio) | Para ESCALAR. Multi-step, A/B test, editor libre. Sin integración CPA nativa |
| **HTML propio + Cloudflare Pages** | {g}$0-15/mes | {g}Máxima | Si hay alguien con HTML (nosotros). Control total, replica cualquier funnel, gratis en CF Pages |
| **LanderLab** | {a}$129/mes | Alta | Hecho para afiliados (IA + integra redes CPA), pero caro. Entra con volumen |
| **Unbounce** | {a}$74/mes | Media-alta | A/B testing fuerte, pero no orientado a afiliados y caro |
| **ClickFunnels** | {r}$97-147/mes | Media | Overkill para un bridge. Cobra fee por venta. Mejor para infoproductos |

**Recomendación para nosotros:** validar con **Carrd** ($19/año) o directamente **HTML propio en Cloudflare Pages** (gratis, ya sabemos codear y el render del repo nos da la base). Pasar a **Convertri** solo si necesitamos A/B testing serio y multi-step sin tocar código.

## 2. Spy tools (encontrar landers y ads de otros)

| Tool | Precio/mes | Plataformas | ¿Revela el lander destino? |
|---|---|---|---|
| **Meta Ad Library** | {g}Gratis | FB + IG | No directo (clic manual). Igual es la primera capa obligatoria |
| **BigSpy** | {g}$9-99 (trial $1) | 10 plataformas | Parcial. Bueno para empezar multiplataforma |
| **Anstrex** | $80-125 | Native + Push | {g}Sí + descarga el lander completo (ripper). Solo si corremos native/push |
| **AdSpy** | $149 | Solo FB + IG | {g}Sí, busca por URL destino + filtra por red (ClickBank). Para Meta avanzado |
| **AdPlexity** | $199-249 (por canal) | Mobile/Native/Desktop | {g}Sí + descarga .zip + cadena de redirección. Avanzado, caro |
| **PowerAdSpy** | $69-399 | 10 plataformas | Sí, pero datos no siempre frescos |

**Recomendación para nosotros:** **Meta Ad Library (gratis)** como base diaria, más el **trial de $1 de BigSpy** para probar. Saltar a **AdSpy** ($149) recién cuando tengamos campañas rentables y queramos espiar por red de afiliados y URL de destino. Ojo: ningún spy revela el lander si el afiliado usa cloaking (que además es causa de ban en Meta).

## 3. Swipe file: herramientas y cómo organizarlo

### Herramientas de swipe
| Tool | Precio/mes (anual) | Para quién |
|---|---|---|
| **Swipekit** | {g}$26 | La más barata. Guarda video + transcripción + screenshot de la landing. Para empezar |
| **Foreplay** | {a}$49 | El estándar. Extension que guarda desde la Ad Library, briefs con IA. Cuando crece el volumen |
| **Atria** | {r}$129 | Todo-en-uno con IA y búsqueda semántica. Caro, para equipos con volumen |
| **Notion + Ad Library** | {g}$0 | Template gratis + biblioteca local. Suficiente para arrancar |

> Aviso: MagicBrief cierra el 31 de julio de 2026 (lo compró Canva). No suscribirse.

Para nosotros: arrancar con **Ad Library (gratis) + esta biblioteca local**; Swipekit ($26) si el volumen lo pide.

### Metodología de los media buyers profesionales (gratis, aplica ya)

**Scoring sin subjetividad, por días activo** (no estrellas):
```bars
14+ dias activo = ganador, guardar | 100 | green
7-13 dias = prometedor, guardar [TEST] | 60 | blue
Menos de 7 dias = esperar | 25 | red
```
La lógica: si un anunciante lo mantiene 14+ días, está convirtiendo. Es la señal más confiable y gratis.

**Tags obligatorios por cada ad guardado** (mínimo 3 dimensiones): formato (static/video/UGC/carousel), tipo de hook (pain/curiosity/social-proof/authority/scarcity/result), ángulo (testimonial/before-after/listicle), plataforma y etapa de funnel (frío/retargeting).

**Workflow semanal (30-60 min):** filtrar la Ad Library por 14+ días activo, guardar las top 20-30 de la oferta, taggear al momento. Antes de cada campaña: identificar el patrón dominante y escribir el brief con los ads de referencia adjuntos.

- **Nuestra biblioteca local** (`07-learning/swipe-bridge-landers/`) ya cumple el rol base sin costo: taxonomía, ejemplos reales, templates de ads y swipe de las finalistas.

## 4. Compliance Meta para bridge pages (lo más importante)

Esto decide si la cuenta sobrevive. Tres reglas críticas primero:

```bars
Coherencia ad-bridge-oferta | 100 | green
No cloaking (mostrar lo mismo a Meta y al usuario) | 100 | green
Sin claims de salud absolutos | 100 | green
```

### Las 3 reglas que más matan cuentas
1. **Congruencia claim por claim** entre anuncio, bridge y oferta. Si el ad dice "apoya la energía" y el bridge dice "elimina el cansancio crónico", Meta lo marca. Todo el funnel debe contar la misma historia con el mismo nivel de promesa.
2. **Nunca cloaking.** Mostrar a Meta una página y al usuario otra es causa de baneo permanente (no solo rechazo del ad). El bridge que ve el revisor de Meta debe ser el mismo que ve el comprador.
3. **Sin claims de salud absolutos ni curativos.** Prohibido "cura", "elimina la diabetes", "revierte". Usar lenguaje de apoyo: "ayuda a mantener", "apoya", "promueve". Nada de garantizar resultados médicos.

### Checklist de la bridge page (qué SÍ debe tener)
- [ ] Disclaimer de afiliado (FTC): declarar que ganas comisión.
- [ ] Disclaimer médico: "no sustituye consejo médico, resultados no garantizados".
- [ ] Política de privacidad, términos y contacto visibles (Meta los exige).
- [ ] Coherencia visual y de mensaje con el anuncio.
- [ ] Tono informativo (advertorial), no de venta agresiva en la parte superior.

### Qué NO poner (rojo Meta)
- Antes/después de cuerpo o resultados médicos (muy restringido).
- "¿Sufres de [condición]?" asumiendo la condición del usuario (viola la política de "personal health").
- Testimonios con promesas específicas de resultado.
- Imitar logos o formato de medios reales (CNN, Fox) sin marcarlo: causa baneo.

### LegitScript
Para suplementos, Meta puede exigir certificación **LegitScript** del anunciante (no del afiliado) para correr ciertas categorías. Si el vendor la tiene, baja el riesgo. Verificar con el affiliate manager.

## Cómo lo aplicamos nosotros

1. Primer test: bridge page en **HTML propio (Cloudflare Pages)** o Carrd, advertorial informativo, congruente con el ad, con todos los disclaimers.
2. Spy diario en **Meta Ad Library** de la oferta elegida para modelar ángulos vivos.
3. Nada de cloaking, nada de claims absolutos. El objetivo es durar, no un test que quema la cuenta.

---

*Fuentes: reviews 2026 de AdSpy, BigSpy, Anstrex, PowerAdPy, AdPlexity (winninghunter, afftank, redtrack); pricing oficial de Carrd, Convertri, LanderLab, Unbounce, ClickFunnels; políticas públicas de Meta sobre salud y afiliados. Precios cambian: re-verificar antes de comprar.*
