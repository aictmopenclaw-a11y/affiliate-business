# SOP 09 · Refresh Creativo cuando hay Fatiga

**Owner:** Dali
**Frecuencia:** Cuando frequency > 3 en un creativo (notificado por Cris)
**Tiempo:** 2h
**Inputs:** notificación Cris, creativo original con fatiga
**Output:** 5 variantes nuevas en 24h (mismo angle, distintas variables)

---

## Pasos

### 1. Recibir notificación Slack
Cris postea cuando detecta fatiga:
```
⚠️ Fatiga detectada · oferta001_curiosidad_9x16_v01.mp4
Frequency: 3.4 · CTR bajando 0.8% (vs 2.1% inicial)
@Dali refresh ASAP — mismo angle, variantes nuevas
```

### 2. Análisis con Cowork (15 min)
Prompt:
```
"Tengo este creativo en fatiga: [archivo + metadata]
Era un winner (ROAS 3.1, CTR 2.1% inicial). Ahora frequency 3.4 y CTR cayó.

Análisis: ¿qué del creativo era el hook? ¿qué se puede mantener intacto y qué cambiar para refrescar?

Devuélveme:
1. Elementos que NO debo cambiar (esencia ganadora)
2. Variables a alterar para refrescar (5 opciones)
3. Lista de 5 variantes específicas a producir"
```

### 3. NO cambiar el angle (regla dura)
- Si el angle estratégico era "curiosidad" → todas las variantes son "curiosidad"
- Cambiar angle = brief nuevo de Romi, no refresh

### 4. Producir 5 variantes (90 min)
Variables a alterar:
- **Hook visual:** mismo concepto, encuadre/composición distinta
- **Voice-over:** cambiar voz (mismo género, otra persona/tono)
- **Opening 3 seg:** cambiar transición de entrada
- **Color dominante:** misma paleta general, acento distinto
- **Avatar/UGC:** misma persona arquetipo, otro modelo HeyGen

Naming continuando correlativo:
- `oferta001_curiosidad_9x16_v06.mp4`
- `oferta001_curiosidad_9x16_v07.mp4`
- ...

### 5. QA self-check (15 min)
- [ ] Mantienen el angle del original
- [ ] Cada variante es diferenciable visualmente
- [ ] Audio nivelado
- [ ] Naming correlativo

### 6. Drop y notificación (5 min)
- Subir a `03-creatives/production/[campaña-XX]/final-cuts/`
- Slack #creativos:
```
✅ Refresh oferta001_curiosidad listo
5 variantes nuevas: v06 - v10
@Cris listo para reemplazar v01 en Meta cuando puedas
```

### 7. Cris ejecuta swap en Meta (5 min)
- Pausar v01 (NO eliminar — queda en Hall)
- Activar v06-v10 en mismo ad set
- Mantener budget igual

---

## Trigger automático
El reporte diario (SOP 05) marca frequency > 3 con flag rojo. Si Cris no triggerea SOP 09 dentro de 24h, alarma escalada a Romi.

---

## Errores frecuentes

1. Cambiar el angle → es brief nuevo, no refresh
2. Producir variantes idénticas (no diferenciables)
3. Esperar > 48h → la fatiga ya quemó el ad set
4. Eliminar v01 → pierdes el Hall reference
5. Cambiar formato (9:16 → 1:1) → es campaña distinta, no variante

---

## Historial

- **v0.1 · 2026-04-28** — estructura inicial
