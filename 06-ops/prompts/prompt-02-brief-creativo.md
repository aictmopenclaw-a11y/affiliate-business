# Prompt 02 · Brief Creativo Romi → Dali

**Owner:** Romi (input) · Dali (output recipient)
**Cuándo usar:** SOP 02 paso 2 — generar brief estructurado de oferta nueva
**Output esperado:** brief listo para drop en Slack #creativos

---

## Prompt

```
Toma esta oferta y arma un brief creativo para producción de 5 ads variantes en Meta Ads.

CONTEXTO:
- Equipo: Romi (estrategia), Cris (ads), Dali (producción visual)
- Mercado: hispano-US, mujeres 25-45
- Stack creativo: HeyGen (avatares), Creatify (UGC), CapCut/Adobe (edición), Freepik (stock)
- Formatos prioritarios: 9:16 (reels), 1:1 (feed), 16:9 (stories ocasional)

OFERTA:
- Nombre: [nombre del producto]
- URL VSL: [link]
- AOV: $X
- Comisión por venta: $X
- Categoría dolor: [articulaciones / sueño / peso / energía / etc.]

AUDIENCIA:
- Demo: [edad, género, ubicación]
- Psico: [dolores específicos, deseos, miedos, lenguaje]

HOOK GANADOR DETECTADO (de SpyHero o VSL del vendor):
"[hook específico]"

GENERA:

1. **5 angles distintos** (no variantes del mismo angle — ÁNGULOS estratégicos diferentes)

Para cada angle:
- Hook (5-7 palabras máximo, en español hispano-US)
- Opening visual (qué se ve en los primeros 3 seg)
- Transición central (cómo se conecta con el body)
- CTA (último 2 seg)

2. **Especificar formato prioritario por angle** (9:16 / 1:1 / 16:9)

3. **Lista de assets necesarios:**
- Búsquedas Freepik (términos exactos)
- Scripts HeyGen (3 variantes de 30-45 seg con guión literal)
- Prompts Creatify (4-5 variantes de UGC)
- B-roll IA si aplica

4. **Recordatorios de compliance:**
- Claims que NO podemos hacer en este nicho
- Disclaimers obligatorios en el ad
- Restricciones del vendor (de tools page)

OUTPUT: brief estructurado en markdown, secciones claras, lenguaje directo. Esto va a Dali a producción inmediata. NO uses emojis. Sin texto extra.
```

---

## Tips de uso

- **Pegar el VSL link**, no copiar el guión completo (Cowork puede ver el HTML)
- Especificar audiencia con **detalle psicográfico**, no solo demografía
- El hook ganador detectado es **input crítico** — sin eso, los angles serán genéricos
- Si Cowork devuelve angles muy parecidos entre sí, repreguntar: "Estos 3 son variantes del mismo angle. Dame 3 angles realmente distintos."

---

## Reglas para validar el output (Romi)

Antes de pasar a Dali:
- [ ] 5 angles **realmente distintos** (no variaciones del mismo)
- [ ] Hooks de 5-7 palabras (más es lentitud de carga mental)
- [ ] CTA específico (no "compra ya", sí "ver el video completo")
- [ ] Assets accionables (Dali sabe exactamente qué buscar)
- [ ] Compliance recordatorio incluido

---

## Variantes del prompt

### Variante para refresh de creativo (post-fatiga)
```
Tengo este creativo en fatiga (frequency 3.4, CTR cayendo):
[archivo + metadata]

Era un winner (ROAS 3.1 inicial). Necesito refrescar SIN cambiar el angle estratégico.

Genera:
1. Elementos NO tocar (esencia ganadora)
2. Variables a alterar (5 opciones específicas)
3. 5 variantes a producir, naming continuando v06 - v10
4. Para cada variante: qué cambia exactamente (hook visual / voice / opening / etc.)
```

### Variante para escalar a YouTube Ads (Fase 3)
```
Tengo este winner Meta (ROAS 2.5x sostenido):
[archivo + metadata]

Quiero escalarlo a YouTube Ads. Diferencias clave:
- Atención del usuario es distinta (más larga, pero requiere hook fuerte)
- Formato puede ser más largo (15-60 seg)

Genera:
1. Versión adaptada del mismo angle para YouTube (15-30 seg + 60 seg)
2. Hook adaptado al contexto YouTube (no "swipe up", sí "click el link descripción")
3. Especificaciones técnicas (formato 16:9 horizontal típico)
```
