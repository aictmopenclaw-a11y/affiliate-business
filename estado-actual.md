# Estado Actual · Affiliate Business

> Este archivo se actualiza **cada 15 min en sesión activa + tras cada acción importante**.
> Es el "snapshot" del proyecto. Quien retoma debe poder continuar leyendo solo este archivo.

**Última actualización:** 2026-06-17 (CIERRE DE SESIÓN · research ClickBank a fondo + shortlist 15 ofertas + deep dive finalistas + one-pager agencia)
**Quién está activo:** nadie · sesión cerrada
**Próxima sesión planeada:** definir titular real de la cuenta + registrar dominio de la agencia + redactar email de aplicación a Prostadine

---

## 📦 Para retomar la próxima sesión (lectura en 5 min)

### Lo que se hizo el 2026-06-17 (research ClickBank a fondo)
- **24 videos ClickBank+Meta transcritos** (criterio: solo recientes 2025-2026, los viejos descartados). Síntesis cruzada videos + foros: `01-ejecucion-2026/clickbank-2026-research/SINTESIS-VIDEOS-FOROS-2026.md`
- **Cuenta ClickBank de TEST** creada (titular "Frank Wilson walter") solo para explorar el marketplace. ES DESECHABLE. La cuenta real será otra al momento de operar.
- **Shortlist de 15 ofertas** con datos reales del marketplace (venta directa + leads): `shortlist-15-ofertas-2026-06-16.md`
- **Validación en Meta Ad Library** de finalistas: `validacion-meta-ad-library-2026-06-16.md` (ProDentim 73 ads activos, Prostadine 10, Kerassentials 16, VisiFlora 0)
- **Deep dive finalistas**: `finalistas-deep-dive-2026-06-16.md`. Recomendación: **Prostadine #1** para primer test (validada pero poco saturada, mejor reputación 4.98/5, CPA), ProDentim #2 (más swipe, más competida).
- **One-pager de la agencia** para postular: `06-ops/agencia/onepager-truenorth-media.html` (nombre provisional TrueNorth Media, email/dominio son placeholders).

### Decisiones de estructura tomadas
- **Sin SpA hasta avanzar.** Se arranca como persona natural (Cris): W-8BEN + Wise personal. Migrar a SpA cuando el modelo se valide.
- **La "agencia" es presentación, no entidad legal.** Identidad de media-buyer (nombre + dominio + email + one-pager) para subir la aprobación con affiliate managers. No requiere empresa registrada.
- **Nickname ClickBank definitivo:** `truenorth` (backups: harbor, meridian). SOP: `06-ops/sops/sop-00-crear-cuenta-clickbank.md`.

### Pendiente inmediato (orden sugerido)
1. **Definir titular real** de la cuenta de operación (Cris persona natural). La de "Frank Wilson" era solo test.
2. **Registrar dominio de la agencia** + crear email corporativo → reemplazar placeholders del one-pager.
3. **Redactar email de aplicación** al affiliate manager de Prostadine (acompaña al one-pager).
4. **Crear cuenta ClickBank real** (nickname truenorth) + W-8BEN + Wise.
5. **Bridge page** anti-finasteride + tracking CAPI (validar con compra de $1) antes de gastar en ads.

### Aprendizaje técnico de la sesión
- Pipeline de transcripción: los background tasks del harness se mueren a los ~15 min, pero un proceso lanzado con **`nohup` desacoplado sobrevive**. Para tareas largas (whisper, etc.), usar nohup + un vigía liviano, no el background task directo.

### Estado del repo / push
- Commits locales en main. **NO hay remote configurado y `gh` no está instalado** en esta máquina, así que el push NO se pudo hacer en esta sesión.
- Para pushear: crear el repo privado en GitHub (`aictmopenclaw-a11y/affiliate-business`) desde la web, luego:
```bash
cd ~/Projects/affiliate-business
git remote add origin https://github.com/aictmopenclaw-a11y/affiliate-business.git
git push -u origin main
```
- Nota: los `.html` están en `.gitignore` (se regeneran desde `.md` con `.tools/render.py`). El one-pager se versionó forzado por ser un asset sin `.md` fuente.

---

## 🚨 ALERTA CRÍTICA · Estudio de viabilidad cambia el panorama

**Tras 8 investigaciones independientes, la data sugiere:**
- $11K USD es subcapitalización para affiliate full
- Probabilidad break-even año 1 con Escenario A: 25-35%
- Probabilidad wipeout total: 30-40%
- Costo de oportunidad vs escalar OpenClaw: ~$180K USD/año
- Pancho Val real pero con red flags (vive más del curso que del affiliate)

**Recomendación data-driven:** Escenario B (Portfolio Asimétrico)
- $7K OpenClaw escalado
- $1.5K producto educativo propio
- $2.5K test affiliate 90 días con stop-loss

**Documentos críticos a leer ANTES del primer sync:**
- `00-viabilidad/VIABILIDAD-MAESTRO.md` — TL;DR + veredicto
- `00-viabilidad/PLAN-COMERCIAL.md` — plan ejecutable Escenario B
- `00-viabilidad/PLAN-INVERSION.md` — comparativa 3 escenarios
- `00-viabilidad/research-fuentes/` — 8 reportes detallados con fuentes

**Decisión pendiente:** #006 en `00-meta/decisions-log.md` (escenario A/B/C)

---

## 🎯 Fase actual

**Pre-Fase 01 · Setup del sistema**

Aún no hemos arrancado oficialmente. Estamos construyendo el repo + infra antes del primer sync con Romi y Dali.

**Próximo hito:** primer sync semanal lunes 11AM → validar playbook + arrancar Fase 01.

---

## ✅ Hecho esta semana

### Sesión 1 (setup inicial)
- [x] Convertir playbook HTML a Markdown (`playbook.md`)
- [x] Convertir dossier estratégico HTML a Markdown (`dossier-estrategico.md`)
- [x] Crear estructura de carpetas completa (00-meta a 07-learning)
- [x] Crear `CLAUDE.md` maestro con reglas para Claude Cowork
- [x] Crear `memory.md` con reglas inviolables (compliance, fiscal, técnico)
- [x] Crear `team-charter.md` con estructura accionaria 50/25/15/10
- [x] Crear `decisions-log.md` con primeras 5 decisiones del playbook
- [x] Crear 4 skills de affiliate (clickbank, funnel, compliance, fiscal)
- [x] Crear 12 SOPs base + INDICE
- [x] Crear 3 prompts plantilla (research, brief, diagnostico)
- [x] Crear `cruce-cursos-aplicado.md` (versión 1)
- [x] Inicializar Git con 2 commits
- [x] Crear `SETUP-GITHUB.md` con instrucciones para invitar Romi/Dali

### Sesión 2 (cruce cursos Felipe Vergara)
- [x] M04 Felipe Vergara — 25/25 transcripciones leídas
- [x] M05 Felipe Vergara — 12/56 transcripciones disponibles, las clave leídas
- [x] M07 Felipe Vergara — transcripciones en proceso (0/16 al cierre)
- [x] Crear `felipe-vergara-m04-aplicado.md` (síntesis completa con templates de copy por nivel)
- [x] Crear `felipe-vergara-m05-aplicado.md` (síntesis con framework presupuesto + estructura por historial)
- [x] Crear `felipe-vergara-m07-aplicado.md` (provisional, esperando transcripciones)
- [x] Actualizar `cruce-cursos-aplicado.md` con referencias a los 3 documentos nuevos
- [x] Identificar cambios concretos a SOPs derivados de los cursos (documentados en cada documento aplicado)

---

## 🔄 En progreso (background)

- [ ] **Transcripción Felipe Vergara** — corriendo en background, ~111 archivos pendientes (M05 + M07 + otros módulos), ~2-4h estimadas. Ver `/tmp/transcripcion-felipe.log`. Tras completar, actualizar `m05-aplicado.md` (sección "Pendientes") y reescribir `m07-aplicado.md` con detalle real de Felipe.

---

## ⏳ Pendiente próxima sesión

### Aplicar cambios derivados a SOPs
- [ ] **SOP 01:** agregar paso validar 3 boosters de oferta (gratis/garantía/pago fácil) + framework 5 pasos cálculo presupuesto Felipe
- [ ] **SOP 02:** reemplazar "5 angles" por "8 textos en 4 niveles de consciencia"
- [ ] **SOP 04:** rehacer paso 8 con estructura 3-conjunto inicial · elevar paso 10 (CAPI) a bloqueante
- [ ] **SOP 06:** agregar checklist pre-decisión (3 preguntas Felipe: budget / historial / objetivo)
- [ ] **SOP 07:** agregar regla "test entity ID" (3 personas + 3 artes + 2 formatos mínimo)
- [ ] **Skill nuevo `affiliate-niveles-consciencia.md`** consolidando framework M04 con templates aplicados

### Push a GitHub
- [ ] Crear repo privado en GitHub `affiliate-business`
- [ ] `git remote add origin` + push -u origin main
- [ ] Invitar Romi y Dali como Maintainers

---

## ⏳ Pendiente esta semana (post-sync)

### Romi
- [ ] Contactar 3 contadores especializados → elegir 1
- [ ] Confirmar status Wise actual (routing 084 vs 026)
- [ ] Definir nombre comercial y giro de SpA
- [ ] Iniciar trámite Empresa en un Día (semana 2)

### Cris
- [ ] Instalar Claude Code + configurar `~/.claude/CLAUDE.md` global del proyecto
- [ ] Crear cuenta ClickBank temporal a nombre individual
- [ ] Llenar W-8BEN inicial
- [ ] Setup Business Manager Meta (preparado para 2 cuentas)

### Dali
- [ ] Activar HeyGen + Creatify trial
- [ ] Comenzar library inicial Freepik
- [ ] Documentar workflow IA visual (Loom + transcripción Claude)

### Los 3
- [ ] Setup Notion compartido + workspace estructura
- [ ] Comprar Skalers Pro (Pancho Val) — Romi y Cris hacen curso, Dali módulo creativos

---

## ⛔ Bloqueado

- **Apertura cuenta SpA bancaria** → necesita SpA constituida primero (semana 3)
- **Skill `affiliate-meta-ads`** → esperando transcripción curso Felipe Vergara (módulos 1, 4, 5, 7)

---

## 🧭 Decisiones pendientes (5 del lunes)

Status al 2026-04-28:

| # | Decisión | Status |
|---|---|---|
| 01 | SpA Pro Pyme con división 50/25/15/10 | ⏳ pendiente sync lunes |
| 02 | Empezar ClickBank o algo más simple | ⏳ pendiente sync lunes |
| 03 | Hispano-US o LATAM puro | ⏳ pendiente sync lunes |
| 04 | Comprar Skalers Pro de Pancho Val | ⏳ pendiente sync lunes |
| 05 | Quién contacta al contador | ⏳ pendiente sync lunes |

Todas se documentan en `00-meta/decisions-log.md` cuando se tomen.

---

## 📊 Métricas (placeholder · empieza Fase 02)

| Métrica | Target | Actual | Status |
|---|---|---|---|
| MER | > 1.5 | — | sin tráfico aún |
| ROAS por campaña | > 1.5x | — | — |
| SOPs documentadas | 12 | 0/12 | iniciando |
| Ofertas activas | 1 (fase 1) → 5 (fase 4) | 0 | en research |
| CV30 (USD) | > $5K | $10K capital inicial | OK |

---

## 📅 Próximas reuniones

- **Lunes XX/04 · 11:00** — Primer sync oficial los 3
- **Viernes XX/05 · 14:00** — Cierre semana 1

---

## 💬 Notas para próxima sesión

- Confirmar si Romi puede activar Loom para grabar primera SOP (selección oferta) en vivo
- Cris: revisar si cuenta Wise actual de Romi tiene routing 084 (Community Federal Savings) o 026 (otro) — afecta quién puede recibir ACH
- Dali: validar costo real Atria + HeyGen + Creatify combinado vs lo presupuestado ($59-129 + $30-90 USD/mes)
- Los 3: confirmar fecha exacta del primer sync semanal

---

## 🗂 Quién mira qué archivos primero

| Si vuelves a esta sesión y eres... | Lee primero |
|---|---|
| Romi | `playbook.md` cap 1-3 + `dossier-estrategico.md` cap 5-10 + `memory.md` reglas 01, 03, 06 |
| Cris | `playbook.md` cap 4-6 + `memory.md` reglas 04 + `06-ops/sops/` lista completa |
| Dali | `playbook.md` cap 4-6 + `memory.md` reglas 05 + `03-creatives/templates/` |

---

*Template basado en estado-actual.md de OpenClaw — cada cliente del equipo principal lo usa así.*
