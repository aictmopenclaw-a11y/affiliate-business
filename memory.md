# Memory · Reglas Inviolables

> Este archivo contiene reglas que **NO se pueden romper bajo ninguna circunstancia.**
> A diferencia de `CLAUDE.md` (que se compacta y puede perder detalle), `memory.md` debe leerse **íntegro antes de cualquier acción operativa**.
> Solo Romi puede modificarlo. Cambios requieren consenso de los 3 + entrada en `decisions-log.md`.

**Última actualización:** 2026-04-28 (post estudio viabilidad)
**Owner:** Romi

---

## 00 · Reglas derivadas del estudio de viabilidad (Decisión #006)

**Antes de cualquier ejecución de affiliate:**
1. Leer `00-viabilidad/VIABILIDAD-MAESTRO.md` completo
2. Confirmar escenario aprobado por equipo (A/B/C en `decisions-log.md`)
3. Si escenario B: respetar stop-loss máximo $2,500 USD en 90 días
4. NO empezar con SpA constituida — operar test inicial como persona natural
5. NO comprar Skalers Pro de entrada — empezar con Skalers Start ($47)
6. NUNCA comprar Skalers Mastery ($2,197) ni Ads License ($12K) año 1

**Stop-loss obligatorios test affiliate:**
- Día 30: si CTR <1% Y CPC >$2 → STOP
- Día 60: si ROAS <0.5x sostenido 14 días → STOP
- Día 90: si ROAS <1.3x sostenido 14 días → STOP

**Stops operativos (no negociables):**
- Si Cris dedica > 25% tiempo al test → STOP (descuida OpenClaw)
- Si OpenClaw pierde cliente por falta atención → STOP
- Si compliance/legal toma > 4h/semana → STOP
- Si algún miembro pierde sueño → STOP

**El plan no es "ganar plata con affiliate" — es validar si es viable canal complementario rentable sin canibalizar OpenClaw.**

---

## 01 · Compliance de salud / nutra

Trabajamos en nicho salud. Errar acá = baneo de cuenta + multas FTC + posible querella.

### NUNCA afirmar
- "Cura X enfermedad"
- "Tratamiento médico para Y"
- "Resultados garantizados"
- "Sin efectos secundarios"
- "Aprobado por la FDA" (salvo que el vendor lo tenga literal con número de aprobación)
- "Pierde X kilos en Y días" (sin disclaimer)
- "Reemplaza tu medicamento"
- Comparaciones directas con fármacos prescritos
- Testimonios sin disclaimer "resultados individuales"

### SIEMPRE incluir
- Disclaimer "Resultados individuales pueden variar"
- "Estas afirmaciones no han sido evaluadas por la FDA" (cuando aplica)
- "Consulta a tu médico antes de comenzar cualquier suplemento"
- Foco en **estilos de vida y bienestar**, no en cura/diagnóstico

### Política antes de publicar
Antes de cualquier ad, landing o copy nuevo en nicho salud:
1. Romi revisa contra esta lista
2. Si hay duda → no publicar, escalar al equipo
3. Documentar en `07-learning/swipe-files/compliance-flags.md` cualquier red flag detectado

---

## 02 · Aislamiento de proyectos

Este proyecto **NO es un cliente de OpenClaw**. Es proyecto separado del trío Romi-Cris-Dali.

### Reglas duras
- **NUNCA referenciar clientes OpenClaw** (Kyest, Argos, Bestmed, Powerlink, Gogopower, TheLungo, OneHealthMed) en este repo
- **NUNCA reutilizar credenciales** entre OpenClaw y affiliate-business (cuentas Meta, Google, MCPs, scripts)
- **NUNCA mezclar tracking** — pixeles, GA4, dominios deben ser exclusivos de este proyecto
- Si Cris trabaja en este proyecto y luego en OpenClaw, **`/clear` obligatorio entre sesiones**
- Estructura societaria SpA es **distinta** a OpenClaw — facturación separada, contabilidad separada

### En caso de duda
Si en cualquier momento aparece info que parece de un cliente OpenClaw, **detener y preguntar**. No documentar nada cruzado.

---

## 03 · Fiscal y financiero (no negociable)

### Cobros
- **TODO cobro de ClickBank entra a Wise Business SpA**, nunca a cuenta personal
- Cada payout = 1 factura exportación electrónica emitida por SpA
- W-8BEN-E debe estar **vigente** al activar cuenta. Renovar cada 3 años
- FATCA + CRS: Wise reporta al SII desde 2017. **Nada queda oculto** — siempre declarar

### Tarjetas y pagos
- Pago Meta/Google Ads: tarjeta crédito SpA (BCI Pyme / Santander Pyme)
- Backup obligatorio: Revolut Romi vinculado como segundo método
- **NUNCA usar N26** para flujos del negocio (es personal de Romi)
- **NUNCA cargar Wise directo** en Meta (no emite tarjeta para residentes Chile)

### Conversión USD ↔ CLP
- Mantener USD en USD lo máximo posible
- Solo convertir a CLP lo necesario para sueldos / contador / gastos locales
- **NUNCA convertir USD → CLP → USD** (pérdida 1-3% cada vuelta)

### Contador
- F29 declarado y pagado **antes del día 12** de cada mes
- F22 anual con margen, no a último momento
- Si contador propone algo dudoso → consultar antes de firmar

---

## 04 · Reglas técnicas inviolables (Cris owner)

### Cuentas Meta Ads
- Mínimo **2 cuentas publicitarias** desde día 1 (principal + backup)
- Mínimo **2 métodos de pago activos** por cuenta
- Pixel Helper test obligatorio antes de cualquier campaña live
- Nunca lanzar campaña sin **conversion event** validado

### Tracking
- Cada oferta = 1 tracking ID único en HopLink ClickBank
- Cada landing = Meta Pixel + GA4 + ClickBank tracking probados
- Eventos críticos: PageView, ViewContent, InitiateCheckout, Purchase
- Si tracking falla → **no escalar presupuesto** hasta resolver

### Dominios
- Dominio dedicado por nicho (no mezclar)
- Cloudflare con SSL obligatorio
- WHOIS privacy ON

### Scripts y automatizaciones
- Credenciales solo en `.env` (nunca en código)
- Scripts production con error handling
- Routines tienen alarma a Slack si fallan 2 corridas seguidas

---

## 05 · Reglas creativas inviolables (Dali owner)

### Producción
- Todo creativo final pasa por **naming convention**: `[oferta]_[angle]_[formato]_v[XX].mp4`
- Avatares HeyGen: scripts pre-aprobados por Romi (no improvisar)
- UGC sintético Creatify: **disclaimer si la persona no es real** (compliance FTC)

### Brand
- Sin paletas que choquen con vendor (revisar VSL primero)
- Logos legibles en 9:16 móvil (test obligatorio)
- Sin música con copyright (solo Epidemic / Artlist / royalty-free verificado)

### Hall of Winners
- Documentar metadata completa: hook, angle, formato, ROAS, días activo
- **Nunca borrar** un winner antiguo (referencia futura)

---

## 06 · Reglas de equipo

### Comunicación
- WhatsApp **solo emergencias fuera de horario** (cuenta baneada, fraude detectado)
- Decisiones operativas en Slack
- Decisiones tipo 02 y 03 → documentar en `decisions-log.md`
- EOD update obligatorio en #general (1 línea por persona)

### Almuerzo
- 13:00-14:00 sin pantallas. **Es ley.** Equipos remotos sin almuerzo se queman en 4 meses.

### Vacaciones / días libres
- Avisar mínimo 1 semana antes
- Quien sale deja handoff de su dominio
- Acceso de emergencia documentado

### Conflictos
- Desacuerdo en dominio → gana owner
- Desacuerdo cross-domain → escalar al sync semanal
- Conflicto personal → conversar 1:1 en menos de 48h

---

## 07 · Reglas para Claude (operativas)

### Antes de cualquier acción
1. Leer `CLAUDE.md` + este `memory.md` + `estado-actual.md`
2. Si tarea es cliente-facing (ad copy, landing, email) → revisar reglas 01 (compliance salud)
3. Si tarea es técnica (tracking, pixels) → revisar reglas 04 (técnicas)
4. Si tarea involucra dinero → revisar reglas 03 (fiscal)

### Output
- Siempre 3 variantes para A/B (regla OpenClaw heredada — aplica acá también)
- Especificar fuente de datos en reportes
- Marcar pendientes con `[PENDIENTE]`
- Sin emojis salvo solicitud explícita

### Confirmación obligatoria antes de
- Publicar cualquier ad / landing / email
- Tocar configuración Meta Ads (presupuesto, audiencias, eventos)
- Cambiar pixels / tracking / dominios
- Modificar este archivo `memory.md` o `CLAUDE.md`

---

## 08 · Lo que NUNCA hacemos (regla resumen)

- ❌ Claims médicos sin disclaimer
- ❌ Cobros ClickBank a cuenta personal
- ❌ Cargar Wise directo en Meta
- ❌ Mezclar este proyecto con OpenClaw
- ❌ Lanzar campaña sin pixel validado
- ❌ Subir presupuesto > +30% sin aviso
- ❌ Bajar presupuesto bajo el "pricing floor" del winner
- ❌ Convertir USD → CLP → USD (pérdida cambio)
- ❌ WhatsApp para decisiones tipo 02/03
- ❌ Skipear el almuerzo 13-14h
- ❌ Trabajar en este folder con `/clear` pendiente desde sesión OpenClaw

---

*Si alguna regla deja de tener sentido, se discute en retrospectiva mensual y se actualiza con consenso de los 3. Hasta ese momento, se respeta.*
