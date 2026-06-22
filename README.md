# Affiliate Business · Sistema Operativo

> Sistema completo de operación para affiliate marketing performance · ClickBank + Meta Ads · Hispano-US.
> Equipo: Romina · Cristóbal · Dalila.
> SpA chilena con régimen Pro Pyme.

---

## ¿Qué es este repo?

Este repo contiene **todo el sistema operativo** del negocio de affiliate marketing:

- **Playbook completo** (filosofía, roles, herramientas, ritmo)
- **Reglas inviolables** (compliance, fiscal, técnicas)
- **12 SOPs** que componen toda la operación
- **4 skills técnicos** (ClickBank, funnels, compliance nutra, cross-border financiero)
- **3 prompts plantilla** para Claude Cowork
- **Estructura de archivos** para offers, creativos, tech, data, ops, learning
- **Cruce con cursos procesados** que aplicamos al stack

**Es nuestro contrato operativo.** Si algo no está aquí, lo improvisamos.

---

## Cómo arrancar (lectura obligatoria, en orden)

### 1. Los archivos meta (15 min)
- [`CLAUDE.md`](CLAUDE.md) — contexto maestro para Claude Cowork
- [`memory.md`](memory.md) — reglas inviolables (no negociables)
- [`estado-actual.md`](estado-actual.md) — dónde estamos hoy

### 2. El playbook completo (45 min)
- [`playbook.md`](playbook.md) — sistema operativo capítulos 1-11
- [`dossier-estrategico.md`](dossier-estrategico.md) — modelo, ClickBank, fiscal, roadmap 30 días

### 3. Roles y decisiones (15 min)
- [`00-meta/team-charter.md`](00-meta/team-charter.md) — accionistas + dominios + KPIs
- [`00-meta/decisions-log.md`](00-meta/decisions-log.md) — decisiones tomadas con justificación

### 4. Tu rol específico (30 min)
- **Si eres Romi:**
  - Skills: `knowledge/skills/affiliate-clickbank.md` + `affiliate-financial-cross-border.md`
  - SOPs: 01, 02, 03, 12 (los que tú manejas)
  - Prompts: `06-ops/prompts/prompt-01-research-oferta.md` + prompt-02
- **Si eres Cris:**
  - Skills: `affiliate-funnel-structure.md` + `affiliate-compliance-nutra.md`
  - SOPs: 04, 05, 06 (los técnicos)
  - Prompts: `06-ops/prompts/prompt-03-diagnostico-meta.md`
- **Si eres Dali:**
  - Skill: `affiliate-compliance-nutra.md` (claims que NO se pueden hacer)
  - SOPs: 07, 08, 09 (producción + Hall of Winners + refresh)

### 5. Cruce con cursos que estudiamos (lectura opcional pero recomendada)
- [`07-learning/cursos-cruzados/cruce-cursos-aplicado.md`](07-learning/cursos-cruzados/cruce-cursos-aplicado.md)

---

## Estructura del repo

```
affiliate-business/
├── README.md                       # este archivo
├── CLAUDE.md                       # contexto maestro Claude Cowork
├── memory.md                       # reglas inviolables
├── estado-actual.md                # dónde estamos hoy
├── playbook.md                     # sistema operativo completo
├── dossier-estrategico.md          # modelo de negocio + fiscal + roadmap
│
├── 00-meta/                        # cerebro del proyecto
│   ├── team-charter.md             # accionistas, roles, KPIs
│   └── decisions-log.md            # decisiones documentadas
│
├── 01-niches/                      # owner: Romi
│   ├── active/                     # nichos en testing actual
│   ├── backlog/                    # pipeline de exploración
│   └── archive/                    # nichos descartados
│
├── 02-offers/                      # owner: Romi
│   └── [oferta-XX]/                # un folder por oferta
│       ├── brief.md
│       ├── research.md
│       ├── economics.md
│       └── compliance.md
│
├── 03-creatives/                   # owner: Dali
│   ├── templates/
│   ├── raw-assets/
│   ├── production/[campaña-XX]/
│   │   ├── v1-hooks/
│   │   ├── v2-bodies/
│   │   └── final-cuts/
│   └── winners/                    # hall of fame ganadores
│
├── 04-tech/                        # owner: Cris
│   ├── landings/[campaña-XX]/
│   ├── pixels-config/
│   ├── scripts/                    # automatizaciones
│   └── backups/
│
├── 05-data/                        # owner: Cris
│   ├── daily/
│   ├── weekly-reports/
│   ├── raw-exports/
│   └── dashboards/
│
├── 06-ops/                         # compartido
│   ├── sops/                       # las 12 SOPs + INDICE
│   ├── prompts/                    # 3 prompts plantilla Cowork
│   ├── syncs/                      # notas sync semanal
│   ├── fiscal/                     # cierres mensuales
│   ├── facturas/                   # PDFs facturas exportación
│   └── contratos/
│
├── 07-learning/                    # compartido
│   ├── cursos-cruzados/            # cruce con cursos estudiados
│   ├── skalers-notes/              # notas Skalers Pro (post-compra)
│   ├── swipe-files/                # ads ganadores otros + análisis competitivo
│   └── retrospectivas/             # retros mensuales
│
└── knowledge/                      # skills cargables bajo demanda
    └── skills/
        ├── affiliate-clickbank.md
        ├── affiliate-funnel-structure.md
        ├── affiliate-compliance-nutra.md
        └── affiliate-financial-cross-border.md
```

---

## Convenciones de nombres

- **Archivos:** kebab-case con fecha al inicio cuando aplique (`2026-04-28-retrospectiva.md`)
- **Carpetas:** prefijos numéricos (`01-`, `02-`, etc.) para orden visual
- **Ofertas:** `oferta-001-[nombre-corto-vendor]`
- **Creativos:** `[oferta]_[angle]_[formato]_v[XX].mp4`
- **Reportes weekly:** `YYYY-WW.md` (semana ISO)
- **Reportes mensuales:** `YYYY-MM.md`

---

## Workflow Git

### Branches
- `main` — estado actual del proyecto
- `feature/[descripción]` — para cambios estructurales (ej. nueva SOP)
- No usamos PR review interna (somos 3) — push directo a main con commit descriptivo

### Commits
- `feat:` — nueva funcionalidad / SOP / skill
- `actualizar:` — actualización de data / estado / decisión
- `fix:` — corrección
- `docs:` — solo documentación

### Reglas duras
- **NUNCA** commitear `.env`, credenciales, tokens
- **NUNCA** force push a main
- **Pull antes de push** siempre (somos 3 trabajando en paralelo)
- Si Romi/Cris/Dali editan el mismo archivo → coordinar por Slack antes

---

## Stack tecnológico (high level)

- **Affiliate Network:** ClickBank
- **Ads:** Meta Ads (primario), Google/YouTube Ads (Fase 3+)
- **Landings:** Landerlab
- **Tracking:** Meta Pixel + GA4 + ClickBank tracking + CAPI postback
- **Creativos IA:** HeyGen (avatares), Creatify (UGC)
- **Stock:** Freepik Pro
- **Espionaje:** SpyHero + Meta Ads Library
- **Swipe files:** Atria
- **Comunicación:** Slack
- **Docs:** Notion + este repo Git
- **Archivos compartidos:** Google Drive
- **Finanzas:** Wise Business (USD) + BCI/Santander Pyme (CLP)
- **AI workflow:** Claude Code (Cris) + Claude Cowork (los 3)

Detalle completo: [`playbook.md`](playbook.md) cap 3.

---

## Roadmap (4 fases · 12 meses)

| Fase | Mes | Objetivo único |
|---|---|---|
| 01 | 1 | Construir el fundamento (sistema operacional listo para gastar) |
| 02 | 2-3 | Encontrar el primer winner (ROAS sostenido > 1.3x por 14 días) |
| 03 | 4-6 | Escalar lo que funciona ($50/día → $500/día con ROAS > 1.5x) |
| 04 | 7-12 | Sistema escalable ($1K-2K/día sostenido con margen sano) |

Detalle completo: [`playbook.md`](playbook.md) cap 8.

---

## ¿Qué NO está en este repo?

- **Credenciales** — viven en `.env` local de cada uno (nunca commitear)
- **Creativos pesados** — videos finales en Google Drive compartido (no Git)
- **Datos personales de comprador** — viven en ClickBank, no nuestro
- **Información financiera sensible** — solo agregada (no extractos bancarios)
- **Información de clientes OpenClaw** — proyecto separado, aislamiento total

---

## Cuándo actualizar este README

- Cambia la estructura de carpetas
- Se agrega skill nuevo
- Cambia el stack tecnológico (mayor)
- Cambia un rol o accionariado

---

## Quién hace qué

| Tarea | Owner |
|---|---|
| Mantener este repo en orden | Cris |
| Mantener `CLAUDE.md` y `memory.md` actualizados | Romi |
| Mantener `estado-actual.md` día a día | Quien esté activo |
| Actualizar SOPs cuando proceso cambia | Owner del SOP |
| Crear skill nuevo | Quien identifique gap |
| Documentar decisión | Owner de la decisión |

---

## Contacto

- Romi · [PENDIENTE email + Slack]
- Cris · [PENDIENTE]
- Dali · [PENDIENTE]

---

*Repo privado. Compartido solo entre los 3 socios.*
*Versión inicial: 2026-04-28.*
