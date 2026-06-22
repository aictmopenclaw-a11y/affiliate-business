# Roadmap 90-120 Días · Hispano-US confirmado

> **Mercado: Hispano-US ✓** (decisión 2026-04-29)
> Equipo de 3 con automatización Claude Code · capital $2-3K bootstrap o $5K recomendado.
> Timeline ajustado: **90 días con $5K · 120 días con $2-3K**.

---

## Resumen visual

```
SEMANA 1 ────► Setup técnico + Skalers Start
SEMANA 2-3 ──► Selección oferta + primer funnel
SEMANA 4 ────► Live con $300 ad spend (validation)
SEMANA 5-8 ──► Iteración + búsqueda winner
SEMANA 9-12 ─► Validation final + decisión scale
DÍA 90 ──────► Decisión continuar/cerrar
```

---

## SEMANA 1 · Setup (días 1-7)

**Objetivo:** infraestructura lista para empezar a gastar.

### Lunes (Día 1)
- [ ] **Cris:** confirmar mercado en sync 30min (LATAM vs Hispano-US)
- [ ] **Cris:** comprar Skalers Start ($47) en Whop
- [ ] **Cris:** crear cuenta ClickBank (persona natural, W-8BEN básico)
- [ ] **Cris:** activar Wise Personal USD account si no tiene
- [ ] **Romi:** leer Skalers Start módulos 1-2 (2h)
- [ ] **Dali:** crear cuenta HeyGen Starter trial (gratis 7 días)

### Martes (Día 2)
- [ ] **Cris:** crear Meta Business Manager dedicado
- [ ] **Cris:** agregar 2 ad accounts + 2 métodos de pago
- [ ] **Cris:** crear cuenta Landerlab (trial 14 días)
- [ ] **Cris:** comprar dominio (~$12) + setup Cloudflare
- [ ] **Romi:** leer Skalers Start módulos 3-5 (2h)

### Miércoles (Día 3)
- [ ] **Cris:** Cloudflare Worker básico para CAPI postback (Claude Code) — 4h
- [ ] **Cris:** Pixel Meta + GA4 setup en dominio test
- [ ] **Romi:** leer Skalers Start bonus + tomar notas
- [ ] **Dali:** explorar HeyGen — generar 3 avatares latinos test (2h)

### Jueves (Día 4)
- [ ] **Cris:** automatizar daily report con Claude Code (script Python que lee Meta API)
- [ ] **Romi:** ejecutar SOP 01 selección oferta — investigar 20 ofertas LATAM ClickBank
- [ ] **Dali:** library inicial Freepik (vectores nutra/health en español)

### Viernes (Día 5)
- [ ] **Sync 1h** los 3:
  - Romi presenta top 5 ofertas candidatas
  - Cris confirma stack técnico funciona
  - Dali muestra avatares HeyGen
  - **Decisión grupal:** 1 oferta TEST esta semana

### Sábado/Domingo (Día 6-7)
- [ ] **Romi:** brief creativo de la oferta elegida (SOP 02)
- [ ] **Cris:** terminar setup CAPI + test postback con conversión fake
- [ ] **Dali:** producir 5 creativos iniciales (3 angles × HeyGen + Freepik)
- [ ] **Día 7 final:** decisión Skalers Pro (window money-back)

**Status fin semana 1:**
- ✓ Stack técnico operativo
- ✓ 1 oferta TEST seleccionada
- ✓ 5 creativos listos
- ✓ Decisión Pro tomada

**Inversión acumulada:** ~$155 USD

---

## SEMANA 2-3 · Primer funnel completo (días 8-21)

**Objetivo:** funnel live con tracking funcionando.

### Semana 2 · Construcción

**Cris (12-15h):**
- [ ] Adaptar template Landerlab para la oferta
- [ ] Implementar copy de Romi en landing
- [ ] Subir creativos de Dali
- [ ] Validar Pixel + CAPI con Meta Pixel Helper
- [ ] QA mobile (iPhone + Android)
- [ ] Test con 1 click manual end-to-end
- [ ] Setup alarmas Slack (CPA threshold, frequency, account warnings)

**Romi (8-10h):**
- [ ] Refinar copy landing (3 iteraciones)
- [ ] Generar 8 textos para ads (2 por nivel consciencia: Inconsciente, Problema, Solución, Producto)
- [ ] Validar compliance con disclaimer obligatorio
- [ ] Investigar competencia en Meta Ads Library (10 ads ganadores LATAM)

**Dali (8-10h):**
- [ ] Producir 5 creativos adicionales (total 10 listos)
- [ ] Diversificar formatos: 5 reel 9:16 + 3 feed 1:1 + 2 stories 16:9
- [ ] Mix tipos: 3 demostración + 3 testimonio + 2 aspiracional + 2 educativo
- [ ] Naming convention aplicada
- [ ] metadata.md para cada creativo

### Semana 3 · Test interno

- [ ] **Cris:** dry-run completo (sin gastar plata aún)
- [ ] **Cris:** simular conversión → verificar postback CAPI llega a Meta
- [ ] **Romi:** review final copy + compliance
- [ ] **Dali:** review final creativos
- [ ] **Sync los 3:** check pre-launch

**Status fin semana 3:**
- ✓ Funnel completo end-to-end
- ✓ 10 creativos diversificados
- ✓ Tracking validado
- ✓ Listo para go-live

**Inversión acumulada:** ~$248 USD

---

## SEMANA 4 · Validation Live · Hispano-US (días 22-28)

**Objetivo:** validar que CTR > 1% y CPC < $1.50-2.00 (Hispano-US)

### Setup campaña Hispano-US

**Configuración Meta:**
- 1 campaña Sales con CAPI Purchase event
- 3 conjuntos:
  - Conjunto A: Advantage+ Audience (recomendación Felipe Vergara M05)
  - Conjunto B: Detailed (intereses Hispano-US salud · español)
  - Conjunto C: Lookalike pendiente (esperar 50 conv para activar)
- Budget escenario $5K: $25/día por conjunto = $50/día activos = $700 mes 1
- Budget escenario $2-3K: $15/día por conjunto = $30/día = $400 mes 1
- 5 anuncios por conjunto (10 total activos)
- **Multilogin obligatorio** desde día 1 (Hispano-US bans frecuentes)

### Día 22-25 · Primeros 4 días
- Daily report 9 AM en Slack
- Cris revisa 5 min · marca status
- Sin tocar nada (Meta en learning phase)

### Día 26-28 · Primer análisis
- Métricas a 7 días:
  - CTR por creativo
  - CPC promedio (target Hispano-US < $2)
  - Conv rate landing → CTA
  - Frequency
  - Customer Distribution Requirement progress (5 ventas + 2 métodos pago)

### **STOP-LOSS día 30 · Hispano-US**
| Métrica | Min para continuar | Acción si menor |
|---|---|---|
| CTR | > 1% | Refresh creativos |
| CPC | < $2.00 Hispano-US | Pausar conjunto, revisar audiencia/oferta |
| Conv rate landing | > 15% | Iterar landing |
| Frequency | < 3 | Refresh creativos urgente |

**Si los 3+ fallan → STOP, pérdida $400-700, post-mortem.**

**⚠ Hispano-US tip:** si Meta banea 1-2 cuentas en mes 1, NO es señal de cerrar (es expectativa). Reemplazar BMs preparados (por eso Multilogin desde día 1).

**Status fin semana 4:**
- 🟢 Si pasa → continuar a semana 5
- 🔴 Si falla → STOP definitivo, capturar aprendizajes

**Inversión acumulada:** ~$555 USD

---

## SEMANA 5-8 · Búsqueda Winner (días 29-56)

**Objetivo:** ROAS > 0.8x sostenido 14 días en al menos 1 conjunto.

### Loop iterativo (cada semana)

**Lunes:** Cris análisis weekly + decisión scaling/killing/iterate
- Top 3 creativos por CTR
- Bottom 3 a pausar
- Scale ganadores +30% si ROAS > 1.5x
- Kill perdedores si ROAS < 0.5x x 5 días

**Martes-Miércoles:** Dali produce 5-7 creativos nuevos basados en data
- Refresh angles ganadores
- Test 1 angle nuevo

**Jueves:** Cris sube creativos nuevos al mejor conjunto
- Mantener naming convention
- Pausar peor performer del conjunto

**Viernes:** sync 30min los 3
- Status data
- Decisiones próxima semana

### Hitos esperados

| Semana | Hito |
|---|---|
| 5 | Primer conjunto identificado como ganador potencial |
| 6 | ROAS conjunto top > 1.0x |
| 7 | ROAS sostenido > 1.0x x 7 días |
| 8 | ROAS sostenido > 0.8x mínimo · validación |

### **STOP-LOSS día 60:**
- Si ROAS < 0.5x sostenido 14 días después de iterar → STOP
- Pérdida acumulada: $1,200-1,500 USD
- Post-mortem completo, capturar aprendizajes en repo

**Inversión acumulada (si continúa):** ~$1,255 USD

---

## SEMANA 9-12 · Validation Final · Escalado controlado (días 57-90)

**Objetivo:** ROAS > 1.3x sostenido 14 días + decisión continuar.

### Semana 9-10 · Optimización winner

- Escalar conjunto winner +30% Hispano-US
  - $5K escenario: $25/día → $33/día
  - $2-3K escenario: $15/día → $20/día
- Esperar 5 días post-scale
- Si ROAS mantiene > 1.3x → +30% más
- Producción Dali: 5-10 variantes adicionales del winner

### Semana 11 · Test pivote a LATAM (si Hispano-US no funciona)

Si ROAS Hispano-US < 0.8x sostenido al día 60, considerar **pivote a LATAM** mes 3:
- Adaptar mismo funnel a México + Colombia
- Budget restante distribuido en LATAM (CPCs 5x menores)
- Última oportunidad antes de STOP definitivo

### Semana 12 · Preparación día 90

- Compilación completa de aprendizajes
- Doc post-test con: qué funcionó, qué no, por qué
- Math final: total invertido vs total revenue
- Recomendación Fase 4 (escalado serio) o STOP o pivote

### **STOP-LOSS día 90 · Hispano-US**
- Si ROAS < 1.3x sostenido 14 días → STOP
- Si revenue acumulado < $1,000 → STOP (Hispano-US AOVs altos · debería ser > $1K)
- Si Customer Distribution Requirement no se cumplió día 60 → ALERTA (cuenta riesgo dormant fees)

### **Triggers para CONTINUAR:**
- ROAS > 1.3x sostenido 14 días en al menos 1 conjunto
- Revenue > $1,500 acumulado (ajustado para Hispano-US AOVs)
- Sistema documentado (SOPs ejecutables)
- Multilogin + multi-cuentas operacional sin crisis
- Equipo OK para seguir

**Inversión acumulada (si continúa):**
- Escenario $5K: ~$5,000 USD
- Escenario $2-3K: ~$2,500-2,800 USD

---

## DÍA 90 · Decisión final

### Si PASA validation
**Continuar a Fase 4 con caja generada por affiliate (NO con capital nuevo del equipo):**
- Mes 4-6: escalar a $30-50/día
- Mes 7-9: agregar oferta 2
- Mes 10-12: evaluar producto educativo o LLC USA

### Si FALLA validation
**STOP definitivo y captura de aprendizajes:**
- Doc post-mortem en `07-learning/2026-XX-affiliate-postmortem.md`
- Pérdida real: ~$2,500 USD
- Aprendizajes capturados aplicables a OpenClaw clientes
- Equipo no quemado, agencia sigue

---

## Distribución de tiempo por persona

### Cris (10-15h/sem promedio)
- Semana 1: 15h (setup técnico denso)
- Semana 2-3: 12h (construcción + automatización)
- Semana 4-12: 8-10h (operación + análisis weekly)
- **Total 90 días:** ~120 horas

### Romi (8-10h/sem promedio)
- Semana 1: 10h (Skalers + selección oferta)
- Semana 2-3: 10h (briefs + compliance)
- Semana 4-12: 6-8h (decisiones + sync)
- **Total 90 días:** ~95 horas

### Dali (6-10h/sem promedio)
- Semana 1: 6h (HeyGen setup + library inicial)
- Semana 2-3: 12h (producción inicial 10 creativos)
- Semana 4-12: 6-8h (refresh semanal)
- **Total 90 días:** ~85 horas

**Total equipo:** ~300 horas en 90 días = $50/h shadow rate × 300 = $15K en costo de oportunidad.

**Esto debe pesar en la decisión.** Si los 3 podrían facturar OpenClaw $50/h, costo total proyecto = $15K + $2.5K capital = $17.5K vs revenue esperado.

---

## Decisiones de equipo durante el roadmap

| Decisión | Cuándo | Quién decide |
|---|---|---|
| Comprar Skalers Pro | Día 7 | Equipo (sync) |
| Cambiar oferta TEST | Día 14 si CTR <1% | Romi (operativa) |
| Agregar tools (Atria, Creatify) | Día 30 si necesidad | Cris + presupuesto |
| Constituir SpA | Día 60+ si validation | Equipo (estratégica) |
| Test Hispano-US paralelo | Día 75+ si LATAM funciona | Equipo |
| STOP definitivo | Día 30/60/90 según stop-loss | Cris (operativa, no debate) |
| Continuar Fase 4 | Día 90 si pasa | Equipo (estratégica) |

---

## Comunicación durante el roadmap

### Daily (sin meeting)
- 9 AM: Slack #affiliate-data — Cris auto-post métricas
- 5 min revisión Cris (decisiones operativas mismo día)
- EOD: 1 línea por persona (status + bloqueos)

### Weekly (lunes 11 AM, 30 min)
- Cris: data + decisiones scaling
- Romi: pipeline ofertas + bloqueos
- Dali: producción + bloqueos
- Decisiones del equipo

### Monthly (días 30, 60, 90)
- Stop-loss check
- P&L
- Decisión continuar/STOP

---

## Lo que está en el repo para apoyar

- `affiliate-clickbank.md` — selección de oferta, gravity, AOV math
- `affiliate-funnel-structure.md` — anatomía landing intermedia
- `affiliate-compliance-nutra.md` — claims permitidos/prohibidos
- 12 SOPs ejecutables
- 3 prompts plantilla Cowork (research, brief, diagnóstico)
- 4 documentos cruce Felipe Vergara

**Todo es accesible desde index.html.**

---

## Si pasas día 90 y validas

**Lo que cambia mes 4+:**
- Constituir SpA chilena (~$50K CLP setup + $300 USD/mes contador)
- Migrar W-8BEN-E a SpA
- Agregar tools que pospusiste (Atria, Creatify)
- Aumentar ad spend a $50-100/día por conjunto winner
- Considerar LLC USA mes 6+

---

*Roadmap 90 días · ejecutable lunes próximo · adaptable a feedback weekly.*
