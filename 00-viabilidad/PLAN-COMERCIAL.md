# Plan Comercial · Affiliate Marketing Performance

> Plan basado en hallazgos de `VIABILIDAD-MAESTRO.md` y los 8 reportes de investigación.
> **NO ejecutar hasta que el equipo decida formalmente el escenario A/B/C.**
>
> Este plan asume **Escenario B (Portfolio Asimétrico)** porque es el recomendado por la data.
> Si el equipo decide Escenario A o C, este plan se reescribe.

---

## Objetivo de negocio (revisado vs playbook original)

**Original:** "$11K capital → operación sostenida $1K-2K/día con margen sano en 12 meses"

**Revisado data-driven:** "Validar en 90 días si affiliate marketing puede ser un canal complementario rentable para el equipo, con stop-loss máximo de $2.5K USD y sin descuidar OpenClaw."

---

## Las 4 fases revisadas

### Fase 0 · Pre-Test · 2 semanas (semana 1-2)

**Objetivo único:** preparar el terreno legal/técnico mínimo para arrancar test sin riesgo de compliance.

**Entregables:**
- [ ] Cris se registra en ClickBank con W-8BEN (NO W-8BEN-E aún, persona natural)
- [ ] Wise Personal de Cris configurado con datos USD ACH
- [ ] Cris: cuenta Meta Business Manager dedicada (separada de OpenClaw)
- [ ] Cris: cuenta Landerlab básica ($49/mes)
- [ ] Cris: cuenta Atria básica ($59/mes)
- [ ] Decisión: ¿Skalers Start ($47) o no?
- [ ] Definir 1 oferta TEST en ClickBank (categoría salud español hispano-US)
- [ ] Setup tracking básico: pixel + GA4 + UTMs

**Inversión Fase 0:** ~$200 USD

**Quién lidera:** Cris (20% de su tiempo)

---

### Fase 1 · Validación de Hipótesis · Día 1-30

**Objetivo único:** validar si podemos generar **CTR > 1% y CPC < $1.50** con los recursos disponibles.

**Entregables:**
- 1 funnel completo (advertorial + VSL del vendor)
- Mínimo 5 creativos diferentes producidos (Dali ayuda part-time, 2 horas)
- Spend total: $300 USD distribuido en 30 días ($10/día)
- Daily report en Slack #affiliate-test (channel temporal)

**Métricas de validación día 30:**
| Métrica | Mínimo (continuar) | Mínimo escalar |
|---|---|---|
| CTR | > 1% | > 1.5% |
| CPC | < $1.50 | < $1.00 |
| Landing CR (clic ad → clic CTA al VSL) | > 15% | > 25% |
| ROAS | > 0.5x | > 0.8x |

**STOP-LOSS día 30:** Si CTR < 1% Y CPC > $2.00 → **STOP, retorno parcial de aprendizajes y cerrar.**

**Inversión Fase 1:** $400 USD (tools $200 + ad spend $300 - solapamiento)

**Quién lidera:** Cris (estrategia + setup), Dali ayuda 2h producción

---

### Fase 2 · Búsqueda de Winner · Día 31-60

**Objetivo único:** llegar a **ROAS > 0.8x sostenido** durante 14 días con al menos 1 conjunto.

**Entregables:**
- Iterar el funnel basado en data Fase 1
- Producir 5-10 creativos adicionales (Dali, 4 horas semanales)
- Spend $500 USD durante el mes ($16-17/día)
- Setup CAPI postback funcionando (crítico)
- Test 2 audiencias diferentes (Detailed vs Open)

**Métricas validación día 60:**
| Métrica | Mínimo |
|---|---|
| ROAS sostenido 14 días | > 0.8x |
| Frequency | < 3 |
| CPA | < commission ceiling × 1.2 |

**STOP-LOSS día 60:** Si ROAS < 0.5x sostenido 14 días → **STOP.**

**Inversión Fase 2:** $700 USD (tools $200 + ad spend $500)

---

### Fase 3 · Validación Final · Día 61-90

**Objetivo único:** llegar a **ROAS > 1.3x sostenido 14 días** que valide tesis de viabilidad.

**Entregables:**
- Optimizar mejor conjunto Fase 2 (escalar +30%)
- Refresh creativos winners (3 variantes nuevas semanal)
- Spend $700-800 USD durante el mes ($25/día)
- Decisión documentada: continuar o cerrar

**Métricas validación día 90:**
| Métrica | Resultado |
|---|---|
| ROAS sostenido 14 días | > 1.3x |
| Comisiones brutas | > $1,000 USD |
| Sistema replicable | SOPs documentadas |

**Resultado A (PASA):** **Continuar Fase 4** con presupuesto adicional desde caja OpenClaw.

**Resultado B (FALLA):** **STOP definitivo.** Documentar aprendizajes en Notion knowledge base. NO doble apuesta.

**Inversión Fase 3:** $900 USD (tools $200 + ad spend $700)

---

### Fase 4 · Escalado Condicional · Mes 4-12 (SOLO SI Fase 3 PASA)

**Objetivo único:** escalar ROAS validado a **$3K-5K/mes neto sostenido**.

**Entregables:**
- Constituir SpA chilena (con presupuesto de OpenClaw, NO del test inicial)
- Setup LLC USA + Mercury bank account
- Migrar W-8BEN-E a SpA
- Activar campañas Meta multi-conjunto
- Producción creativa semanal (Dali medio tiempo dedicado)
- Reporting weekly al equipo

**Métricas validación trimestral:**
| Trimestre | Revenue mensual neto | Ad spend mensual |
|---|---|---|
| Q2 (mes 4-6) | $1K-3K | $500-1.5K |
| Q3 (mes 7-9) | $3K-5K | $1.5K-3K |
| Q4 (mes 10-12) | $5K-10K | $3K-5K |

**Inversión Fase 4:** $5K-8K USD (proveniente de caja OpenClaw, no del capital test inicial)

---

## Stop-loss totales (no negociables)

### Stop financiero
- Si total invertido test > $2,500 USD sin pasar Fase 2 → **STOP**
- Si total invertido > $5,000 USD sin pasar Fase 3 → **STOP**

### Stop operativo
- Si Cris dedica > 25% de su tiempo al test (mes 1-3) → **STOP** (está descuidando OpenClaw)
- Si OpenClaw pierde algún cliente por falta de atención → **STOP** (ya no es portfolio, es canibalización)
- Si compliance/legal complica más de 4 horas/semana → **STOP** (señal de mismatch)

### Stop emocional
- Si el equipo siente "FOMO" empujando a saltarse stops → **STOP** (señal cognitiva)
- Si alguien está perdiendo sueño por el test → **STOP** (no vale la salud mental)

---

## Estructura de testing por oferta

### Selección de la primera oferta TEST

Criterios duros (no negociables):
- [ ] Categoría: salud / nutra / wellness
- [ ] Idioma: español
- [ ] Geo: USA + LATAM permitidos
- [ ] Gravity: 30-100 (sweet spot validado)
- [ ] AOV: > $80 USD
- [ ] Comisión: > 60%
- [ ] Refund rate (si conocemos): < 20%
- [ ] VSL del vendor visible y completo
- [ ] Tools page del vendor sin restricciones brand bidding USA
- [ ] Sin claims FDA-restricted en VSL

**Owner selección:** Cris (con consulta a Romi para validar mensajería/copy)

### Estructura técnica del funnel test

```
[Ad Meta · 5-7 variantes en mismo conjunto]
          ↓
[Landing intermedia · Landerlab]
          ↓
   (CTA "Ver el video completo")
          ↓
[VSL del vendor · ClickBank]
          ↓
[Checkout vendor · ClickBank]
          ↓
[Postback ClickBank → Servidor → Meta CAPI]
```

**Compliance no negociable:**
- Disclaimer "Estas afirmaciones no han sido evaluadas por la FDA" en footer
- "Resultados individuales pueden variar" cerca de cada beneficio
- Affiliate disclosure visible
- Sin antes/después manipulado

---

## Plan de creativos (Dali · medio tiempo el primer mes, después según resultado)

### Mes 1 · Producción inicial
- 5 creativos diferenciados (test entity ID)
- 3 angles distintos (Curiosidad / Problema / Aspiracional)
- 2 formatos (9:16 + 1:1)
- Mix: 2 demostración + 2 testimonio + 1 educativo

### Mes 2 · Iteración basada en data
- Refresh de los 2 mejores
- 5 creativos adicionales explorando nuevos angles
- Mantener mix de formatos

### Mes 3 · Optimización winner
- 10 variantes del mejor angle (refresh anti-fatiga)
- Probar 1 formato nuevo (16:9 stories)

**Tiempo de Dali:** 4-6 horas/semana mes 1, 2-4 horas/semana mes 2-3

---

## Plan de comunicación con el equipo

### Frecuencia
- **Daily:** Cris postea métricas en Slack #affiliate-test (canal dedicado)
- **Weekly:** Cris presenta status en sync OpenClaw (15 min)
- **Mensual:** evaluación contra stop-loss + decisión continuar/parar

### Decisiones que requieren equipo
- Compra Skalers Start ($47): no requiere consenso (decisión Cris)
- Compra Skalers Pro ($497): requiere alineamiento equipo
- Continuar a Fase 2/3 si métricas dudosas: equipo
- Stop-loss disparado: documentar y notificar (no hay debate, se ejecuta)

---

## Plan de aprendizaje continuo

### Documentación obligatoria
- Cada sesión de testing → notas en `02-offers/[oferta-001]/test-log.md`
- Cada creativo testeado → metadata completa (hook, angle, formato, métricas)
- Cada decisión → entry en `00-meta/decisions-log.md`
- Cada aprendizaje → entry en `07-learning/`

### Knowledge base alimentado
Al cierre del test (día 90):
- Reporte ejecutivo de aprendizajes (qué funcionó, qué no, por qué)
- Si pasa: blueprint operativo refinado
- Si falla: post-mortem con causas raíz identificadas

**Esto es valor capturado SIEMPRE, independiente del resultado financiero.**

---

## Cuando NO ejecutar este plan

Razones legítimas para NO empezar el test:

1. **Cris no puede dedicar 4-6 horas/semana sin descuidar OpenClaw.** El test depende de Cris.
2. **OpenClaw tiene clientes pendientes de capacidad.** El costo de oportunidad sube.
3. **Cash flow personal del equipo está apretado.** $2.5K es plata real.
4. **Dali no puede dedicar 4-6 horas/semana.** Sin creativos no hay test válido.
5. **El equipo está estresado o saturado.** Un nuevo proyecto agrava.
6. **Hay disagreement no resuelto entre los 3.** Sin alineamiento total, no proceder.

**Si cualquiera de estas se cumple, ejecutar Escenario C (NO PROCEDER) por el momento.**

---

## Cuándo escalar a Fase 4 (post-validación)

Solo si TODAS estas condiciones se cumplen al día 90:

- [ ] ROAS > 1.3x sostenido 14 días en al menos 1 conjunto
- [ ] Comisiones brutas > $1,000 USD acumuladas (test 90 días)
- [ ] Sistema documentado en SOPs ejecutables
- [ ] Cris confirma puede dedicar 30-40% tiempo a Fase 4
- [ ] OpenClaw cash flow saludable (>3 meses runway)
- [ ] Equipo alineado en seguir
- [ ] No hay red flags legales/fiscales pendientes
- [ ] Capital adicional ($5-8K) disponible sin estresar caja personal

Si alguna no se cumple → **NO escalar.** El test cumplió su propósito (validar), pero las condiciones operativas no están dadas.

---

## Métricas de éxito del PLAN (no del negocio)

**Independiente de si llegamos a $5K/mes en affiliate, este plan es exitoso si:**

1. ✅ Capital máximo perdido: $2.5K USD (no $11K)
2. ✅ Tiempo OpenClaw protegido: < 25% del equipo
3. ✅ Aprendizajes documentados aplicables a clientes OpenClaw
4. ✅ Decisión informada (no por FOMO ni por sunk cost)
5. ✅ Compliance respetado (sin riesgos legales activados)
6. ✅ Salud del equipo mantenida (no burnout)

**Si pasa esto, el plan funcionó — independiente del resultado financiero del test.**

---

*Plan Comercial v1.0 · Para ejecutar SOLO bajo Escenario B aprobado por el equipo.*
