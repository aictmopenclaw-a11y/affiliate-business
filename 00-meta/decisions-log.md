# Decisions Log · Affiliate Business

> Registro de **decisiones tipo 02 (táctica) y tipo 03 (estratégica)**.
> Decisiones tipo 01 (operativa) se documentan en Slack o en `estado-actual.md`.
>
> **Si una decisión tipo 03 se tomó por WhatsApp en 5 min sin documentar, no se tomó.**

---

## Formato

```markdown
## Decisión #NNN · YYYY-MM-DD
**Tipo:** [Operativa | Táctica | Estratégica]
**Owner:** [Quien decide]
**Pregunta:**
[Qué se decide en una frase]

**Contexto:**
- [Hechos relevantes en bullets]

**Opciones consideradas:**
A. [opción 1]
B. [opción 2]
C. [opción 3]

**Decisión:**
[Opción elegida]

**Razón:**
- [Por qué se eligió esa opción]

**Cuándo revisamos:**
[Fecha o trigger]

**Firmado:** Romi · Cris · Dali (o quien aplique)
```

---

## Decisión #001 · 2026-04-28
**Tipo:** Estratégica
**Owner:** Romi (con consenso del equipo)
**Pregunta:**
¿Estructura legal del proyecto?

**Contexto:**
- 3 socios chilenos
- Operación cross-border (USD entrante, ads gasto USD, vida CLP)
- Capital inicial $11K USD
- No queremos doble carga tributaria
- Necesitamos deducibilidad de gastos (herramientas, ad spend, contador)

**Opciones consideradas:**
A. Persona Natural + Boletas Honorarios (cero setup, techo bajo, 35% efectivo)
B. EIRL (un dueño, no permite socios)
C. SpA Pro Pyme régimen 14D N°8 transparente (3 socios, escalable, deducible)
D. LLC USA + SpA Chile (optimización fiscal alta, costo $1-2K USD setup)

**Decisión:**
**Opción C — SpA Pro Pyme con régimen 14D N°8 transparente**

**Razón:**
- 3 socios → permite estructura accionaria clara (50/25/15/10 reserva)
- Escalable sin necesidad de migrar
- Deducible todo (Meta spend, herramientas, contador, oficina)
- Setup $0 (Empresa en un Día) → solo costo recurrente es contador (~$250K CLP/mes)
- Régimen 14D N°8 transparente evita doble tributación
- Opción D (LLC USA) se justifica solo a > $200K USD/año — prematuro hoy

**Cuándo revisamos:**
Mes 12 — si llegamos a $15K USD/mes consistente, evaluar agregar LLC USA como holding

**Firmado:** Romi · Cris · Dali

---

## Decisión #002 · 2026-04-28
**Tipo:** Estratégica
**Owner:** Romi
**Pregunta:**
¿Estructura accionaria de la SpA?

**Contexto:**
- 3 socios con aportes muy distintos al negocio
- Romi: estrategia, tiempo de gestión, dirección
- Cris: skill técnico crítico (sin él no hay funnels)
- Dali: skill creativo importante pero menor stakeholder en estrategia
- Necesitamos colchón para incorporaciones futuras

**Opciones consideradas:**
A. 33/33/33 (igualitario)
B. 50/25/25 (Romi mayoritaria, Cris y Dali iguales)
C. 50/25/15/10 reserva (Romi mayoritaria, Cris segundo, Dali tercero, 10% para futuro)
D. 40/30/20/10 reserva (más balanceado)

**Decisión:**
**Opción C — 50/25/15/10 reserva**

**Razón:**
- Reconoce que Romi lleva la estrategia + responsabilidad legal/financiera
- Cris tiene 25% por skill técnico crítico (no reemplazable rápido)
- Dali tiene 15% — refleja aporte creativo importante pero menor exposición a decisiones de negocio
- 10% reserva permite vesting para nuevo socio o ampliar a alguien que se gane equity

**Cuándo revisamos:**
- Si entra socio nuevo → se discute desde el 10% reserva
- Si alguien quiere subir su % → acuerdo unánime + ajuste vía pacto

**Firmado:** Romi · Cris · Dali

---

## Decisión #003 · 2026-04-28
**Tipo:** Estratégica
**Owner:** Romi (con consenso)
**Pregunta:**
¿Empezamos con ClickBank o validamos algo más simple primero (CPA networks LATAM)?

**Contexto:**
- ClickBank tiene curva de aprendizaje más alta
- AdCombo / DrCash tienen ad costs más bajos pero AOVs y volúmenes menores
- Pancho Val (caso benchmark) opera 100% en ClickBank
- Todo el ecosistema (Atria, SpyHero, comunidad Skalers, Diamond vendors) está optimizado para ClickBank

**Opciones consideradas:**
A. ClickBank desde día 1
B. Empezar AdCombo/DrCash 1-2 meses, después migrar a ClickBank
C. Híbrido: ClickBank principal + AdCombo como segunda red

**Decisión:**
**Opción A — ClickBank desde día 1**

**Razón:**
- La curva paga: AOVs $150+, comisiones 60-75%, vendors con VSL ya optimizado
- Comunidad Skalers + Pancho Val nos dan playbook directo sin tener que descubrir errores
- Empezar en network secundaria y migrar = perder 2 meses + tener que reaprender
- W-8BEN-E es el único trámite extra real, y se hace una vez

**Cuándo revisamos:**
- Mes 6 — si ya hay 2-3 winners en ClickBank, evaluar si tiene sentido agregar AdCombo como diversificación

**Firmado:** Romi · Cris · Dali

---

## Decisión #004 · 2026-04-28
**Tipo:** Estratégica
**Owner:** Romi (con consenso)
**Pregunta:**
¿Mercado primario · hispano-US o LATAM puro?

**Contexto:**
- Hispano-US: AOVs y CPCs gringos, menos competencia que inglés, requiere creativos más sofisticados
- LATAM puro (México, Argentina, Chile, Colombia): AOVs más bajos, menos comisión, pero lenguaje más cercano a nuestra experiencia chilena
- Nuestro skill cultural está afinado al target hispano-US (Romi tiene experiencia de target en beauty/wellness)

**Opciones consideradas:**
A. Hispano-US 100%
B. LATAM 100% (México como mercado ancla)
C. Híbrido: empezar LATAM (más barato) y migrar a hispano-US después
D. Empezar con hispano-US directo

**Decisión:**
**Opción D — Hispano-US 100% desde día 1**

**Razón:**
- Sweet spot real: AOVs gringos ($150+) con menos competencia que ofertas en inglés
- Nuestro skill cultural ya está afinado al target (mujeres 25-45 hispano-US)
- Empezar LATAM = aprender un mercado que después abandonaremos
- ClickBank tiene catálogo robusto en español dirigido a USA
- Pancho Val opera principalmente hispano-US y nos da la blueprint

**Cuándo revisamos:**
- Mes 9 — evaluar agregar inglés-US como segundo mercado si el equipo creció

**Firmado:** Romi · Cris · Dali

---

## Decisión #005 · 2026-04-28 · ⚠️ REVISADA tras estudio viabilidad
**Tipo:** Estratégica
**Owner:** Equipo
**Pregunta:**
¿Comprar Skalers Pro de Pancho Val antes de empezar?

**Contexto:**
- Costo: ~$497 USD (versión inicial) o ~$1.5M CLP (Pro completo)
- Construido sobre $8M USD de gasto real validado por Pancho
- Comunidad activa de 3,920 miembros (de los cuales **~2,632 son freebies**, solo ~1,370 paying)
- Soporte directo + drops de updates + ofertas Diamond pre-validadas

**Opciones consideradas:**
A. No comprar, aprender solos vía YouTube + foros
B. Comprar versión básica ($497)
C. Comprar Pro completo (~$1.5M CLP) — Romi y Cris hacen curso entero
D. Esperar a tener primer winner y entonces comprar para escalar
E. **(NUEVA)** Empezar con Skalers Start ($47) como validation purchase, upgrade solo si vale

**Decisión REVISADA tras `06-pancho-val-deep-dive.md`:**
**Opción E — Skalers Start ($47) primero, upgrade a Pro solo si valida valor**

**Razón del cambio:**
- Reviews de Skalers tienen patrones estadísticamente sospechosos (4.89-5.0 con counts idénticos 155-156 entre 4 productos)
- Whop tiene app "Review Reward" que da promo codes por reviews
- Sin reviews independientes en Trustpilot/Reddit
- Skalers tiene 7-day money-back guarantee — usar
- Pricing real verificado: Start $47 / Pro $497 / Mastery $2,197 / Ads License $12,000
- Si Start valida → upgrade a Pro
- **NUNCA comprar Mastery ni Ads License año 1** sin 6+ meses de resultados probados

**Cuándo revisamos:**
- Día 7 después de comprar Start → decisión upgrade Pro (window money-back)
- Mes 6 → evaluar si Pro está dando valor real

**Firmado:** Romi · Cris · Dali

---

## Decisión #006 · 2026-04-28 · CRÍTICA
**Tipo:** Estratégica
**Owner:** Equipo (consenso requerido)
**Pregunta:**
¿Cuál escenario de inversión adoptamos tras el estudio de viabilidad?

**Contexto:**
Estudio de viabilidad (8 investigaciones independientes) entrega hallazgos que cambian la tesis original:
- $11K USD es subcapitalización para affiliate full
- Probabilidad break-even año 1: 25-35%
- Probabilidad wipeout total: 30-40%
- Costo de oportunidad de elegir affiliate vs escalar OpenClaw: ~$180K USD/año
- Pancho Val verificable como real, pero income claims no auditables
- Authority Hacker, Affiliate Lab cerraron cursos 2024-2025

**Opciones:**
A. **FULL AFFILIATE** ($11K, 100% en affiliate) — NO RECOMENDADO por la data
B. **PORTFOLIO ASIMÉTRICO** ($7K OpenClaw + $1.5K educación + $2.5K test affiliate 90 días) — RECOMENDADO
C. **NO PROCEDER** ($11K 100% en escalar OpenClaw) — VÁLIDO si condiciones lo justifican

**Decisión:**
**[PENDIENTE — requiere consenso de los 3 en primer sync]**

**Recomendación basada en data:**
- Escenario B con stop-loss máximo $2.5K en 90 días
- Si test pasa los 3 hitos → continuar con caja generada por OpenClaw
- Si test falla → cerrar definitivo, capturar aprendizajes, no doble apuesta

**Documentos de soporte:**
- `00-viabilidad/VIABILIDAD-MAESTRO.md`
- `00-viabilidad/PLAN-COMERCIAL.md`
- `00-viabilidad/PLAN-INVERSION.md`
- 8 reportes en `00-viabilidad/research-fuentes/`

**Cuándo revisamos:**
- Día 30 → primera evaluación de stop-loss
- Día 60 → segunda evaluación
- Día 90 → decisión final continuar/parar
- Mes 6 → revisión escenario completo

**Firmado:** [PENDIENTE primer sync]

---

## Decisión #007 · 2026-04-29 · CONFIRMADA
**Tipo:** Estratégica
**Owner:** Cris (con confirmación equipo pendiente)
**Pregunta:**
¿Mercado primario · LATAM o Hispano-US?

**Contexto:**
Tras estudio de viabilidad + investigación ClickBank 2026 + selección de ofertas, el análisis data-driven recomendaba LATAM por:
- CPCs 5-6x menores ($0.20-0.40 vs $1.20-2.50)
- Más volumen para validar con $2-3K
- Probabilidad break-even mayor (35-45% vs 20-25%)
- Equipo nativo cultural

Pero el equipo elige Hispano-US por:
- Es el mercado de Pancho Val → Skalers Pro tácticas aplican directo
- AOVs y comisiones significativamente más altas ($147+ vs $97 LATAM)
- Mercado más sofisticado · skill OpenClaw lo aprovecha
- Camino natural a inglés-US después
- Comunidad Skalers concentrada acá → networking

**Opciones:**
A. LATAM (México + Colombia) — recomendación data-driven
B. Hispano-US — elección equipo
C. Inglés-US — descartada por capital insuficiente
D. Híbrido — descartada (foco brutal regla #1)

**Decisión:**
**Opción B — Hispano-US como mercado primario**

**Razón:**
- Foco en mercado donde Skalers Pro (que vamos a comprar) tiene máxima aplicación
- AOVs altos compensan CPCs caros si la conversión es decente
- Pivote a LATAM sigue disponible mes 3 si Hispano-US no funciona

**Implicancias acordadas:**
- Skalers Pro ($497) sí comprar mes 2 (no era el caso si LATAM)
- Multilogin antidetect ($99/mes) obligatorio desde mes 1 (Hispano-US bans)
- Capital recomendado sube a $5K idealmente · $2-3K es bootstrap riesgoso
- Timeline a 90 días con $5K · 120 días con $2-3K
- Sub-niches prioritarios: dental (ProDentim), microbiome (NewEra Protect), audio-VSL (Audifort)
- Evitar weight loss general (saturadísimo en Hispano-US)

**Riesgo aceptado:**
- Probabilidad break-even baja a 20-25% con $2-3K · 35-40% con $5K
- Probabilidad wipeout sube a 40-50% con $2-3K
- Posible pivote forzado a LATAM mes 3 si no funciona

**Cuándo revisamos:**
- Día 30 → primera evaluación stop-loss Hispano-US
- Día 60 → si ROAS < 0.8x sostenido → considerar pivote LATAM
- Día 90 → decisión final continuar / pivote / STOP

**Documentos actualizados consecuencia de esta decisión:**
- `01-ejecucion-2026/01-DECISION-MERCADO.md`
- `01-ejecucion-2026/02-DECISION-SKALERS.md`
- `01-ejecucion-2026/03-STACK-MINIMO-VIABLE.md`
- `01-ejecucion-2026/04-ROADMAP-90-DIAS.md`
- `01-ejecucion-2026/clickbank-2026-research/MAESTRO-CLICKBANK-2026.md`

**Decisión pendiente derivada:**
**#008 · Capital final: $2-3K (bootstrap), $5K (realista), o $7K (profesional)?**

**Firmado:** Cris (consensoo Romi+Dali pendiente sync)

---

## [Próximas decisiones a documentar — pendiente sync inicial]

### #006 · ¿Quién contacta al contador esta semana?
- **Tipo:** Operativa (pero tiene deadline duro → escalada)
- **Recomendación:** Romi
- **Status:** PENDIENTE confirmar en sync

### #007 · Stack inicial de herramientas — ¿activar todas el día 1 o por fases?
- **Tipo:** Táctica
- **Recomendación:** Por fases para no sangrar caja antes de validar
- **Status:** PENDIENTE definir en sync

### #008 · Workspace Notion — ¿Plus Team de día 1 o Free hasta mes 3?
- **Tipo:** Operativa
- **Recomendación:** Plus Team día 1 ($30/mes es marginal y ahorra dolor después)
- **Status:** PENDIENTE confirmar

---

*Cada nueva decisión se agrega arriba con número correlativo. Las decisiones revisadas y modificadas no se borran — se marca con "REVISADA YYYY-MM-DD" y se agrega el contexto del cambio.*
