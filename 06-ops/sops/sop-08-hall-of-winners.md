# SOP 08 · Mantenimiento del Hall of Winners

**Owner:** Dali
**Frecuencia:** Cada vez que un creativo rompe ROAS 2.5x (notificado por Cris)
**Tiempo:** 15 min por winner archivado
**Inputs:** notificación Cris en Slack, creativo original
**Output:** archivo en `03-creatives/winners/` con metadata completa

---

## Pasos

### 1. Recibir notificación Slack
Cris postea cuando detecta winner:
```
🏆 Winner detectado · oferta001_curiosidad_9x16_v01.mp4
ROAS: 3.1 · Días activo: 7 · Spend: $245 · Conv: 18
@Dali archivar en Hall + más variantes
```

### 2. Copiar creativo a winners (2 min)
- Copiar (NO mover) de `03-creatives/production/[campaña]/final-cuts/` a `03-creatives/winners/[YYYY-MM]-[oferta]-[hookname].mp4`
- Mantener original en producción para referencia

### 3. Documentar metadata (8 min)
Crear `03-creatives/winners/[YYYY-MM]-[oferta]-[hookname].md`:

```markdown
# Winner · oferta001_curiosidad_9x16_v01

**Archivado:** YYYY-MM-DD
**Oferta:** oferta-001-[nombre]
**Angle:** Curiosidad
**Formato:** 9:16

## Performance
- ROAS: 3.1
- Días activo: 7
- Spend total: $245 USD
- Conversiones: 18
- CPA: $13.61
- CTR: 2.4%
- Frequency: 2.1

## Elementos visuales clave
- **Hook (primeros 3 seg):** "¿Sabías que las latinas en Miami..."
- **Color dominante:** [naranja cálido / blanco / etc]
- **Formato del hook:** texto + voice over + zoom in
- **Transición principal:** corte directo a producto en mano
- **Voice-over:** energía media-alta, tono cómplice
- **Música:** [tipo - upbeat lifestyle]
- **Avatar/UGC:** HeyGen Sara
- **CTA visual:** texto grande "VER MÁS" + flecha

## Por qué creemos que ganó
[Hipótesis de Dali — se valida después con patrones del Hall]

## Variantes a producir (10x)
- v06: mismo hook, voice-over distinta (más juvenil)
- v07: mismo hook, color dominante azul
- v08: mismo angle, hook ligeramente distinto
- v09: 1:1 versión del mismo
- v10: 16:9 versión para retargeting
- ...
```

### 4. Producir 5-10 variantes inmediatas (resto del tiempo o sprint siguiente)
- Mismo angle, variar elementos secundarios
- NO cambiar el angle estratégico
- Naming: `[oferta]_[angle]_[formato]_v[XX]` continuando el correlativo

---

## Revisión mensual del Hall (parte de SOP 11 retro)

Una vez al mes, Dali analiza el Hall:
- ¿Qué tienen en común los winners del último mes?
- ¿Qué color, hook style, voice-over tipo?
- ¿Qué angles dominaron?
- Output: insight visual para próximo brief de Romi

---

## Checklist por winner

- [ ] Creativo copiado a `winners/` (NO movido)
- [ ] Metadata.md creado con todos los campos
- [ ] Hipótesis de por qué ganó documentada
- [ ] Lista de 5-10 variantes propuestas para próximo sprint
- [ ] Slack #creativos confirmado

---

## Errores frecuentes

1. Mover (no copiar) → pierdes referencia en producción
2. No documentar metadata completa → no puedes detectar patrones
3. Producir variantes que cambian el angle (eso ya es brief nuevo)
4. Esperar a "tener tiempo" → el momentum del winner se pierde

---

## Historial

- **v0.1 · 2026-04-28** — estructura inicial
