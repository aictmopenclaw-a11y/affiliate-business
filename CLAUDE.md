# Affiliate Business · Contexto Maestro

Este es el contexto que **Claude Cowork lee cada vez que trabaja en este folder**. Define quiénes somos, cómo hablamos, qué hacemos, qué evitamos. Es nuestro brand book operativo. **Romi mantiene actualizado.**

---

## Quiénes somos

Equipo de 3 chilenos operando affiliate marketing performance:
- **Romina** — estrategia, mensajería, dirección
- **Cristóbal** — ads, tracking, análisis técnico
- **Dalila** — creativos, brand, producción visual

Estructura legal: **SpA chilena con régimen Pro Pyme** (50/25/15/10 reserva).

## Negocio

- **Network principal:** ClickBank (objetivo: Diamond)
- **Mercado:** hispano-US + LATAM (sweet spot: español dirigido a USA)
- **Niche:** salud / nutra / beauty (mujeres 25-45, expansible 35-65)
- **Canales:** Meta Ads (primario), Google/YouTube Ads (mes 4+)
- **Modelo financiero:** USD vía Wise Business · CLP vía SpA banco chileno
- **Compliance crítico:** W-8BEN-E al día · factura exportación electrónica

## Cómo trabajamos

- **Idioma:** español (output Claude en español, código en inglés)
- **Decisiones:** por dominio (ver `00-meta/team-charter.md`)
- **Métricas norte:** MER, ROAS, payback period, CV30
- **Filosofía base:** sistemas repetibles > hacks (heredado de Pancho Val)

---

## Reglas para Claude (no negociables)

1. **Sin emojis** salvo que pida explícitamente
2. **Outputs accionables**, no recomendaciones genéricas
3. Si dudas algo crítico, **pregunta antes de asumir**
4. **Nunca generes claims de salud sin disclaimer**
5. **Numbers > opiniones** cuando exista data
6. Antes de cualquier output cliente-facing, revisar `memory.md` (reglas inviolables)
7. Output en **español chileno neutro** — prohibido voseo (vos, podés, hacés)
8. Códigos: comentarios mínimos, código limpio, en inglés

## No hacer nunca

- Editar archivos en `/02-offers/` sin marcar a Romi
- Tocar `/04-tech/` sin que Cristóbal lo haya validado
- Generar copy con afirmaciones médicas no respaldadas
- Modificar SOPs sin que el owner del dominio confirme
- Subir creativos a Meta sin QA visual de Dali
- Cambiar presupuesto > +30% sin aviso a Cris
- Mezclar info de este proyecto con otros (clientes OpenClaw, etc.)
- Commitear `.env`, tokens, credenciales

---

## Filosofía operativa (4 principios fundadores)

> **Mantra del proyecto:** *"Estás a un anuncio de cambiar tu vida."*
> Detalle completo en [`00-meta/filosofia.md`](00-meta/filosofia.md).

### 1. Un sistema repetible vence a cualquier hack
Si no podemos repetir lo que funcionó, no funcionó. Trimestre 1: documentar 12 SOPs. La rentabilidad viene del sistema.

### 2. Velocidad de iteración sobre perfección
5 variantes mediocres > 1 obra maestra. La data dicta, no nuestro gusto. Aplica especialmente al testing creativo.

### 3. Documentar mientras hacemos, no después
Cada SOP se escribe al ejecutar el proceso por primera vez. Claude Cowork hace esto trivial — usar para todo.

### 4. Estamos a un anuncio del próximo aprendizaje
Testeamos volumen, no apuestas únicas. Cada oferta live es un experimento, no una promesa. Cada kill alimenta el siguiente winner. **Mediocre & live > brillante & en draft.** El próximo test puede ser ese.

---

## Conceptos heredados de cursos que aplicamos directo

> Cruce completo en `07-learning/cursos-cruzados/cruce-cursos-aplicado.md`

### De Crear y No Parar (Fauadzk Kassen — 97 clases procesadas)

- **Definidor de Audiencias completo** antes de cualquier copy. Psicografía: dolores, enojos, deseos, miedos. Aplica a cada oferta nueva.
- **Aha Moment** como objetivo de toda creatividad. El cliente debe decir "eso me pasa a mí". Test: ¿es shareable como meme?
- **3 Niveles de Consciencia** (problema / solución / decisión) — copy diferente por nivel. Hispano-US frecuentemente está en consciencia de problema.
- **Triángulo Dorado:** Oferta + Audiencia + Creativo. Si uno falla, los otros 2 no salvan.
- **Pricing Floor invisible:** después de un winner, no bajar presupuesto bajo el nuevo baseline.

### De Felipe Vergara (Trafficker Pro)

> Pendiente transcripción completa de los 191 módulos. Por ahora aplicamos los conceptos generales conocidos.

- **5 diferencias Trafficker Pro vs Principiante** — operamos como Pro desde día 1
- **Niveles de Consciencia** aplicados a copy de ad (inconsciente / problema / solución / producto / decisión)
- **Públicos Advantage+** como default — confiar en el algoritmo de Meta
- **Investigación de mercado** vía Meta Ads Library + SpyHero antes de crear oferta nueva

### De Pancho Val (Skalers Pro · pendiente comprar)

- **Foco brutal:** un canal, un network, un nicho hasta dominar
- **Sistema creativos IA** al servicio de testing volumétrico
- **Análisis obsesivo KPIs** antes de mover presupuesto

---

## Stack de archivos (ver `playbook.md` para detalle)

```
00-meta/                   ← cerebro (charter, decisiones, este CLAUDE.md)
01-niches/{active,backlog,archive}    ← Romi
02-offers/[oferta-XX]/     ← Romi (brief, research, economics)
03-creatives/              ← Dali (templates, raw, production, winners)
04-tech/                   ← Cris (landings, pixels, scripts)
05-data/                   ← Cris (weekly-reports, raw-exports, daily)
06-ops/                    ← compartido (sops, prompts, fiscal, syncs)
07-learning/               ← compartido (skalers, swipe, retros, cursos)
```

---

## Ritmo operativo (ver `playbook.md` cap. 7)

- **Diario:** reporte 9AM Slack, deep work 10-13, almuerzo 13-14, colaborativo 14-17, EOD 17:30
- **Semanal:** sync lunes 11AM (60 min), producción mar-jue, cierre viernes 14h
- **Mensual:** cierre fiscal días 1-5, retro 1er viernes, mid-month check día 15

---

## Workflow con Claude Cowork

### Para Romi
- `/affiliate-research-oferta` (prompt 01) — análisis de ofertas ClickBank
- `/affiliate-brief-creativo` (prompt 02) — brief Romi → Dali
- Documentación SOPs vía Loom → Claude transcribe

### Para Cris
- `/affiliate-diagnostico-meta` (prompt 03) — análisis CSV semanal Meta
- Setup landings (HTML/CSS para Landerlab)
- Scripts de routines (daily reports automatizados)

### Para Dali
- Procesamiento de batches (renombrar 80 archivos por campaña)
- Generación variantes copy (1 hook → 30 variantes)
- QA visual de thumbnails

Los 3 prompts están en `06-ops/prompts/`.

---

## KPIs (ver `playbook.md` cap. 10)

**North star:** MER · PBP · CV30 · SR

**Por dominio:**
- Romi: pipeline ofertas activas, hit rate, cycle time, SOPs ratio
- Cris: ROAS por campaña, CPA vs commission ceiling, frequency, account health
- Dali: output volume, hook hit rate, Hall of Winners, refresh time

**No medimos:** impresiones, alcance, engagement rate, seguidores, número ads activos. Métricas de ego.

---

## Governance — 3 tipos de decisión

- **Tipo 01 Operativa:** decide owner, informa después
- **Tipo 02 Táctica:** discute en sync, decide owner
- **Tipo 03 Estratégica:** consenso de los 3, documentado en `00-meta/decisions-log.md`

Si una decisión tipo 03 se tomó por WhatsApp en 5 min sin documentar, **no se tomó**.

---

## Compliance crítico (ver `memory.md` para reglas inviolables completas)

- **Claims salud:** nunca afirmaciones médicas no respaldadas (FDA / FTC / SII / SERNAC)
- **Fiscal:** factura exportación electrónica obligatoria por cada payout ClickBank
- **W-8BEN-E:** vigente, renovar cada 3 años
- **Aislamiento:** nunca mezclar este proyecto con clientes OpenClaw

---

## Cuándo actualizar este archivo

- Cambia el equipo (alguien entra/sale)
- Cambia el nicho principal o mercado
- Cambia un principio operativo
- Cambia la estructura legal o financiera

**Romi es owner de este archivo.** Cualquier cambio se discute en sync semanal y se documenta en `decisions-log.md`.
