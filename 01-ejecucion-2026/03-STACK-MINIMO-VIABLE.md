# Stack Mínimo Viable · Hispano-US confirmado

> **Mercado: Hispano-US** (confirmado 2026-04-29) → necesita tools adicionales vs LATAM.
> Asume capital $2-3K (con advertencia) o $5K (recomendado).

---

## Stack Hispano-US · ~$215/mes (vs $93 LATAM, vs $650 playbook original)

### Esencial (mes 1)

| Tool | Costo/mes | Por qué Hispano-US |
|---|---|---|
| **ClickBank** | $0 | Network base · Cuenta gratis |
| **Meta Business Manager** | $0 | 2 BM mínimo (Hispano-US bans más frecuentes) |
| **Landerlab** | $49 | Landing pages affiliate-friendly |
| **Cloudflare** | $0 | DNS + SSL + Worker para CAPI |
| **Dominio** | $1 ($12/año) | 1 dominio dedicado |
| **HeyGen Starter** | $24 | Avatares latinos para Hispano-US |
| **Freepik Pro** | $15 | Stock visual base |
| **Skalers Start** | $47 one-time ($4/mes amortizado) | Comprar semana 1 |
| **Wise Personal** | $0 | Recibir USD ClickBank |
| **Hosting CAPI** | $0-5 | Cloudflare Workers free tier |
| **Multilogin (antidetect)** ⚠ | **$99** | **OBLIGATORIO Hispano-US** · multi-cuentas Meta sin baneo cascada |
| **Total esencial** | **~$192/mes** | |

### Mes 2 · Skalers Pro post-validation
| Tool | Costo | Cuándo |
|---|---|---|
| **Skalers Pro** | $497 one-time ($42/mes amortizado) | Mes 2 si Start vale + setup completo |

**Stack total mes 2 en adelante:** **~$234/mes**

### Tools opcionales (mes 2-3 según resultados)

| Tool | Costo/mes | Cuándo agregar |
|---|---|---|
| **Atria** | $59 | Si producción >10 creativos/sem |
| **Creatify** | $30 | Mes 2 para UGC sintético |
| **SpyHero** | $49 | Mes 2 para espionaje (priority Hispano-US porque saturado) |
| **Klaviyo Free** | $0 hasta 250 contactos | Si capturamos email pre-VSL mes 4+ |
| **CB Engine** | $30 | Mes 2 si necesitamos gravity histórico |

---

## Por qué cortamos del stack original

### Tools eliminadas
- ❌ **ClickFunnels:** Landerlab más barato y enfocado affiliate
- ❌ **Atria de entrada:** $59/mes desde día 1 cuando no producimos volumen aún
- ❌ **Creatify de entrada:** HeyGen Starter alcanza para validar
- ❌ **SpyHero de entrada:** Meta Ads Library gratis hace lo mismo para empezar
- ❌ **Multilogin:** solo necesario con multi-cuentas Meta agresivo (no en mes 1)
- ❌ **Notion Plus:** Slack free + Drive es suficiente al inicio
- ❌ **Loom:** opcional, free tier alcanza
- ❌ **Wise Business:** **Wise Personal** es suficiente para test inicial (no SpA aún)

### Tools que sí necesitas (pero más baratas)
- ✓ Landerlab basic ($49) en lugar de tier alto
- ✓ HeyGen Starter ($24) en lugar de Creator ($89)
- ✓ Freepik Pro ($15) — base
- ✓ Skalers Start ($47) en lugar de Pro

---

## Setup técnico paso a paso

### Cuentas a crear (semana 1)

#### 1. ClickBank
- URL: clickbank.com → Sign Up
- A nombre de **Cris** (persona natural, NO SpA aún)
- W-8BEN inicial (no W-8BEN-E)
- Wise USD account number como receptor
- **Tiempo:** 30 min

#### 2. Wise Personal (si no tienes)
- URL: wise.com
- Cuenta personal Cris
- Activar USD account (datos USA: routing + account number)
- Setup tarjeta debit Wise (sí emite para personas naturales chilenas)
- **Tiempo:** 1-2 días aprobación

#### 3. Meta Business Manager
- URL: business.facebook.com
- Crear BM nuevo (no usar el de OpenClaw — aislamiento)
- Agregar 2 ad accounts (1 principal, 1 backup)
- Agregar 2 métodos de pago: tarjeta SpA si tienes, sino tarjeta personal Cris + Wise debit como backup
- **Tiempo:** 2-3 horas + 1 día verificación

#### 4. Landerlab
- URL: landerlab.io
- Plan basic $49/mes
- 14-day trial gratis para empezar
- **Tiempo:** 30 min

#### 5. HeyGen
- URL: heygen.com
- Plan Starter $24/mes
- Free trial 7 días para validar
- **Tiempo:** 15 min

#### 6. Cloudflare + Dominio
- Comprar 1 dominio en Namecheap (~$12/año)
- Apuntar DNS a Cloudflare
- Activar SSL Universal
- **Tiempo:** 1 hora

#### 7. Hosting CAPI postback (Cloudflare Workers)
- Crear cuenta Cloudflare developers (free tier)
- Worker simple para recibir webhook ClickBank → POST a Meta CAPI
- **Tiempo:** 4-6 horas (Cris con Claude Code)

---

## Donde Claude Code te da ventaja real

### Automatizaciones que valen 10+ horas/semana

#### 1. Daily Meta report automático
**Sin Claude Code:** Cris exporta CSV manual cada mañana, hace cálculos en Sheets, postea en Slack. ~30 min/día = 3.5h/sem.

**Con Claude Code:**
- Routine programada `/affiliate-daily-report`
- Lee Meta API + ClickBank API
- Genera markdown summary + alerts
- Auto-post a Slack #affiliate-data
- **Tiempo Cris:** 5 min revisión

**Setup inicial:** 4-6 horas. Recuperación: 2 semanas.

#### 2. CAPI postback handler
**Sin Claude Code:** contratar dev freelance ($300-500) o dejarlo sin CAPI (ROAS calculado mal).

**Con Claude Code:**
- Cloudflare Worker en JavaScript
- Cris describe en español lo que necesita
- Claude Code escribe + debuggea
- **Costo:** $0 + ~6 horas Cris

#### 3. Generación de creativos a escala
**Sin Claude Code:** Dali produce 5-10 creativos/sem manual.

**Con Claude Code + HeyGen:**
- Script que toma brief de Romi
- Llama HeyGen API con 10 variaciones
- Llama Creatify API (mes 2)
- Output: 10 mp4 con naming convention listo
- **Tiempo Dali:** review 1h vs producción 6-8h

#### 4. Análisis de offers ClickBank
**Sin Claude Code:** Romi entra al marketplace, scroll, anota top 20.

**Con Claude Code + scraping:**
- Script que scrape ClickBank marketplace
- Filtros: gravity 30-100, español, salud
- Output: ranked CSV con métricas
- **Tiempo Romi:** review 30min vs research 3h

---

## Capital allocation Hispano-US · 3 escenarios

### Escenario "Bootstrap $2,500" (mínimo apretado)

| Categoría | Mes 1 | Mes 2 | Mes 3 | Total |
|---|---|---|---|---|
| Skalers Start + Pro | $47 | $497 | — | $544 |
| Tools esenciales (Landerlab + HeyGen + Freepik) | $88 | $88 | $88 | $264 |
| Multilogin antidetect | $99 | $99 | $99 | $297 |
| Dominios + infra | $20 | $5 | $5 | $30 |
| **Setup + tools subtotal** | **$254** | **$689** | **$192** | **$1,135** |
| Ad spend Meta Hispano-US | $300 | $400 | $600 | $1,300 |
| Reserva refunds + account replace (10%) | $0 | $50 | $100 | $150 |
| **Total mensual** | **$554** | **$1,139** | **$892** | **$2,585** |

**Excede $2,500 en $85.** Para que cuadre:
- Cortar Multilogin mes 1 (riesgo más alto baneo)
- Posponer Skalers Pro a mes 3 (después de primer winner)

**⚠ Probabilidad break-even este escenario: 20-25%**

### Escenario "Realista $5,000" (recomendado Hispano-US)

| Categoría | Mes 1 | Mes 2 | Mes 3 | Total |
|---|---|---|---|---|
| Skalers Start + Pro | $47 | $497 | — | $544 |
| Tools esenciales | $88 | $88 | $88 | $264 |
| Multilogin antidetect | $99 | $99 | $99 | $297 |
| Atria + Creatify (mes 2) | — | $89 | $89 | $178 |
| Dominios + infra + buffer | $50 | $20 | $20 | $90 |
| **Setup + tools** | **$284** | **$793** | **$296** | **$1,373** |
| Ad spend Meta Hispano-US | $700 | $1,000 | $1,500 | $3,200 |
| Reserva refunds + account replace | $50 | $150 | $200 | $400 |
| **Total mensual** | **$1,034** | **$1,943** | **$1,996** | **$4,973** |

**Cabe en $5,000 con $27 de margen.** Ad spend razonable ($35-50/día) para Hispano-US.

**Probabilidad break-even: 35-40%**

### Escenario "Profesional $7,000"

| Categoría | Mes 1 | Mes 2 | Mes 3 | Total |
|---|---|---|---|---|
| Skalers Start + Pro | $47 | $497 | — | $544 |
| Tools completas (todas) | $187 | $187 | $187 | $561 |
| Multilogin + SpyHero | $148 | $148 | $148 | $444 |
| Buffer + reserva | $100 | $100 | $200 | $400 |
| **Setup + tools** | **$482** | **$932** | **$535** | **$1,949** |
| Ad spend Meta Hispano-US | $1,000 | $1,500 | $2,500 | $5,000 |
| **Total mensual** | **$1,482** | **$2,432** | **$3,035** | **$6,949** |

**Cabe en $7,000 con $51 de margen.** Operación profesional.

**Probabilidad break-even: 45-55%**

---

## Setup que NO necesitas año 1

### NO constituir SpA aún
- Operar como persona natural (Cris) bajo boleta de honorarios para test inicial
- Si funciona y vamos a escalar mes 4+ → ahí constituir SpA
- **Ahorro mes 1-3:** $750 USD en contador + setup

### NO LLC USA
- Solo cuando llegues a $5K+ USD/mes consistente
- Mes 6+ mínimo

### NO antidetect browser (al inicio)
- Solo necesario con multi-cuentas Meta
- Al inicio: 1 BM, 2 ad accounts → no necesario
- Agregar mes 2-3 si escalas a 3+ accounts

### NO CRM (Klaviyo, etc.)
- Sin email capture en pre-VSL → no necesitas CRM
- Si decides agregar quiz con email mes 4+ → ahí evaluar Klaviyo

### NO Notion Plus pago
- Slack free + Drive free + GitHub (este repo) es suficiente

---

## Comparativa total

| | Playbook original | Stack mínimo viable |
|---|---|---|
| **Setup mes 1** | $2,547 | $555 |
| **Mensual recurrente** | $943/mes | $93/mes |
| **Total 12 meses** | $13,863 | $1,461 |
| **Capital para ad spend** | -$2,863 (déficit) | $1,539 (sobra) |

**El stack mínimo te deja $1,539 USD efectivos para ad spend** vs déficit del playbook original.

---

## Decisión rápida

**Si confirmas LATAM + $2-3K + automatización Claude Code:**
- Stack mínimo del cuadro inicial ($93/mes)
- Setup esta semana
- Skalers Start únicamente
- Ad spend $400 mes 1 → $700 mes 2 → $1,000 mes 3

**Si decides Hispano-US:**
- Mismo stack + agregar Skalers Pro mes 2 (+$497)
- Multilogin mes 2 (+$99/mes)
- Total mensual sube a $216
- Ad spend cae a $300/$500/$700 — más justo pero viable

---

*Stack mínimo viable · 86% más barato que playbook original · más capital para validar.*
