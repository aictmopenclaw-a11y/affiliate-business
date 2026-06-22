# SOP 07 · Producción Batch de Creativos (10-15 variantes/sprint)

**Owner:** Dali
**Frecuencia:** 2x semana (martes + jueves recomendado)
**Tiempo:** 4h por batch
**Inputs:** brief de Romi (SOP 02), assets disponibles, HeyGen + Creatify cuentas activas
**Output:** 10-15 variantes finales en `03-creatives/production/[campaña]/final-cuts/` + notificación a Cris

---

## Pasos

### 1. Recibir brief en Slack #creativos (5 min)
- Leer brief completo
- Aclarar dudas con Romi por DM si hay ambigüedad
- Confirmar deadline

### 2. Cowork organiza assets (15 min)
Prompt sugerido:
```
"Tengo este brief: [pegar brief]
Necesito que me hagas:
1. Lista de assets que necesito buscar en Freepik (términos exactos)
2. Lista de scripts para HeyGen avatares (3 variantes, 30-45 seg cada uno)
3. Lista de prompts para Creatify UGC (4-5 variantes)
4. Estructura de carpetas en /03-creatives/production/[campaña]/

Output: lista accionable, sin texto extra."
```

### 3. Generar avatares HeyGen (45 min)
- Script pre-aprobado por Romi (NO improvisar texto)
- 3 variantes:
  - Variante A: hook directo (3 seg + body)
  - Variante B: hook curioso ("¿sabías que...")
  - Variante C: hook problema ("si tienes X...")
- Avatar consistente con audiencia (mujer 35-45 latina, etc.)
- Voz energía media-alta
- Background limpio (sin logos visibles)

### 4. Generar UGC sintético Creatify (60 min)
- 4-5 variantes
- Prompts con detalle: persona, escena, emoción, transición
- Si Creatify devuelve calidad pobre → regenerar con prompt más específico
- Naming temporal: `creatify_[fecha]_v1`, etc.

### 5. Edición final CapCut/Adobe (90 min)
- Para cada variante final:
  - Hook diferenciado (variar primeros 3 seg)
  - Body consistente del mismo angle
  - CTA estandarizado (último 2 seg con texto + voice)
  - Transiciones limpias
- 3 formatos por concepto ganador:
  - 9:16 (reels, stories)
  - 1:1 (feed Instagram)
  - 16:9 (raro, solo si Romi lo pide)

### 6. Naming convention (10 min)
Formato: `[oferta]_[angle]_[formato]_v[XX].mp4`

Ejemplos:
- `oferta001_curiosidad_9x16_v01.mp4`
- `oferta001_problema_1x1_v03.mp4`
- `oferta001_lifestyle_9x16_v05.mp4`

### 7. Drop en final-cuts (10 min)
- Subir a `03-creatives/production/[campaña-XX]/final-cuts/`
- Crear thumbnail preview de cada uno
- Documentar en `metadata.md`:
  ```
  | Archivo | Angle | Hook | Voice-over | Avatar/UGC |
  |---|---|---|---|---|
  | oferta001_curiosidad_9x16_v01.mp4 | Curiosidad | "¿Sabías que..." | Voz Maria | HeyGen Sara |
  ```

### 8. QA self-check (15 min)
Para cada variante:
- [ ] Hook claro en primeros 3 seg
- [ ] Audio nivelado (no muy bajo, no clipping)
- [ ] Texto legible en mobile (no muy chico)
- [ ] CTA visible last 2 seg
- [ ] Sin watermarks de templates / IA
- [ ] Sin música con copyright

### 9. Notificar a Cris (5 min)
Slack #creativos:
```
@Cris — batch [campaña-XX] listo
📁 /03-creatives/production/[campaña-XX]/final-cuts/
✅ X variantes finales (3 angles × 3 formatos = 9 typically)
🔍 Metadata en metadata.md
🚀 Listas para upload Meta cuando puedas
```

---

## Checklist pre-cierre

- [ ] 10-15 variantes finales producidas
- [ ] 3 angles distintos cubiertos
- [ ] 3 formatos por angle ganador (mínimo)
- [ ] Naming convention respetada
- [ ] metadata.md actualizado
- [ ] QA self-check completo
- [ ] Slack notificado a Cris

---

## Errores frecuentes

1. Cambiar el angle estratégico (eso es decisión de Romi, no de producción)
2. Hooks débiles en primeros 3 seg → sin retención
3. Texto pequeño en mobile → ilegible
4. Música copyrighted → strike YouTube/Meta
5. Avatares HeyGen poco humanos (cherry-pick los mejores frames)
6. UGC Creatify visiblemente sintético (descartar y regenerar)
7. Naming inconsistente → no se puede analizar después

---

## Historial

- **v0.1 · 2026-04-28** — estructura inicial
