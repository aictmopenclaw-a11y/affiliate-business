# Skill · Operación Financiera Cross-Border (Chile ↔ USA)

> **Cuándo cargar este skill:** antes de configurar Wise / ClickBank / banco SpA, antes del cierre fiscal mensual, antes de cualquier conversación con el contador.
> **Owner conceptual:** Romi (con apoyo Cris en aspectos técnicos)
> **Última actualización:** 2026-04-28

---

## El stack financiero (visión 1 página)

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENTE USA compra                    │
│                  (vía nuestro HopLink)                   │
└──────────────────────────┬──────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│                       ClickBank                          │
│  Descuenta 7.5% + $1 + transaction fees por venta       │
│  Acumula nuestra comisión (60-90% del precio vendor)    │
└──────────────────────────┬──────────────────────────────┘
                           ↓
                  (semanal o quincenal)
                           ↓
┌─────────────────────────────────────────────────────────┐
│                   Wise Business SpA                      │
│         Recibe USD vía ACH (gratis) · 1-2 días           │
│       Mantiene saldo USD · convierte 0.43% al medio      │
└──────────┬──────────────────────────────┬───────────────┘
           ↓ 60-70%                       ↓ 30-40%
    ┌──────────────┐              ┌──────────────────┐
    │ Queda USD    │              │ Convertir a CLP  │
    │ para ads     │              │                  │
    │ (Meta cobra  │              │ Va a banco SpA   │
    │  vía tarjeta │              │ (BCI / Santander │
    │  SpA + back- │              │  Pyme)           │
    │  up Revolut) │              │                  │
    └──────────────┘              │ Sueldos · contad │
                                  │ Gastos locales   │
                                  └──────────────────┘
```

---

## Por qué SpA y no Persona Natural

| Aspecto | Persona Natural | SpA Pro Pyme |
|---|---|---|
| Tributación efectiva | ~35% (Global Complementario) | 25% sobre utilidades + Global solo si retiras |
| Deducción de gastos | Casi nada | TODO (ad spend, herramientas, contador, oficina) |
| Recibir USD ACH | Bloqueado (FATCA) | Vía Wise Business gratis |
| Factura de exportación | No puedes emitir | Sí (exenta IVA) |
| Recuperar IVA crédito | No | Sí (de gastos chilenos) |
| Setup | Cero | $0 portal Empresa en un Día |
| Costo recurrente | $0 | $250-350K CLP/mes contador |

**Decisión:** SpA con régimen 14D N°8 transparente. Documentado en `decisions-log.md` #001.

---

## Régimen Pro Pyme · 14D N°3 vs 14D N°8 transparente

### 14D N°3 (general)
- 25% impuesto Primera Categoría sobre utilidades
- Distribución a socios genera Global Complementario adicional
- Doble carga si retiras todas las utilidades

### 14D N°8 transparente (lo que elegimos)
- Las utilidades **se trasladan directo a los socios** sin pasar por Primera Categoría
- Cada socio paga Global Complementario sobre su parte (escala progresiva 0-40%)
- **Evita doble tributación** — ideal para 3 socios que reinvierten o retiran proporcionalmente

**Confirmar con contador antes de elegir formalmente.** El régimen se elige al iniciar actividades.

---

## Wise Business · qué hace y qué no

### Hace ✅
- Recibe USD vía ACH (routing y account number gringos reales)
- Mantiene saldo en 50+ monedas (USD, EUR, GBP, etc.)
- Convierte a CLP a 0.43% del tipo de cambio medio (mejor que cualquier banco chileno)
- Soporta multi-divisa simultánea
- Integra con QuickBooks / Xero
- Aprobación rápida (0-2 días)

### NO hace ❌
- **No emite tarjeta de débito para residentes chilenos** (limitación crítica)
- No recibe wire transfer USD a costo cero (algunos sí, otros con fee)
- No es banco — no da línea de crédito, no opera como cuenta de ahorro

### Setup Wise Business
1. Crear cuenta en **wise.com/business**
2. Verificación con docs SpA (RUT empresa, escritura constitución, iniciación actividades)
3. Aprobación en 0-2 días hábiles
4. Costo único setup ~$35-50 USD (varía por país)
5. Solicitar datos USD ACH (routing 084 Community Federal Savings o similar)
6. Confirmar que ClickBank acepta esos datos (test con payout pequeño primero)

### Lo que importa para ClickBank
ClickBank requiere:
- Routing number USA (Wise lo da)
- Account number USA (Wise lo da)
- Nombre titular = nombre cuenta = nombre SpA (sin "Inc" ni "LLC")

---

## Pago de Meta y Google Ads · 3 caminos

### Camino α (recomendado para arranque)
**Tarjeta crédito empresarial SpA + Backup Revolut Romi**
- BCI Pyme o Santander Pyme — habilitar transacciones internacionales
- Vincular como método principal en Meta
- Vincular Revolut Romi como backup

**Pro:**
- 100% formal, deducible, factura clara
- Si una falla, la otra cubre automáticamente
- Sin riesgo de baneo Meta

**Contra:**
- Mark-up de moneda 1-3% en banco chileno cuando Meta cobra
- Requiere espera para que el banco apruebe internacional

### Camino β (alternativa)
**PayPal Business chileno**
- Wise → PayPal Business → Meta Ads
- 100% trazable, todo dentro de SpA

**Pro:**
- PayPal sí está en Chile (Camino directo)
- Trazabilidad fiscal

**Contra:**
- PayPal cobra 3-5% si conviertes USD → CLP
- Más fees acumulados que camino α

### Camino γ (futuro · cuando > $15K USD/mes)
**LLC USA + Wise Business US**
- Constituir LLC en Wyoming o Delaware (~$300-500 USD setup + ~$50 USD/año)
- Wise Business US emite tarjeta real
- Cero fricción con Meta/Google
- Setup completo $1-2K USD inicial

**Pro:** setup definitivo para escala
**Contra:** complejidad fiscal dual (Chile + USA), prematuro hoy

---

## Estrategia · 2 métodos de pago siempre activos

**Es lo que hacen los media buyers serios.**

Si Meta intenta cobrar y la primera tarjeta falla por:
- Límite excedido
- Bloqueo del banco (sospecha de fraude)
- Validación pendiente
- Tarjeta vencida

**Cobra automáticamente con la segunda y la campaña no se detiene.**

Una campaña en pausa puede destruir el rendimiento que tomó semanas construir (Meta vuelve a "fase de aprendizaje" cada vez que pausa).

---

## Factura de exportación electrónica · el secreto

### Por qué importa
Servicios prestados a entidad sin domicilio en Chile (ClickBank Inc.) califican como **exportación de servicios**. Esto significa:
- **Exento de IVA** (Art. 12 letra E N°16 Ley IVA)
- **Permite recuperar IVA crédito** de gastos locales chilenos (oficina, software, contador, herramientas con factura local)

### Cómo funciona en la práctica
1. ClickBank te paga $X USD vía Wise
2. Emites factura de exportación electrónica a "ClickBank Inc." (RUT genérico extranjero)
3. La factura se declara en F29 mensual como "exportación servicios"
4. El IVA crédito de tus gastos locales se compensa contra otros débitos

### Datos para emitir factura
- Emisor: tu SpA
- Receptor: ClickBank Inc. (datos a confirmar con contador, hay RUT genérico extranjero estándar)
- Servicio: "Servicios de marketing digital — comisión por afiliación"
- Monto: USD del payout convertido a CLP al tipo de cambio del día
- Tasa IVA: **0% — Exportación de servicios**

### Frecuencia
1 factura por payout. Si ClickBank paga semanal, son 4 facturas/mes. Si paga quincenal, 2 facturas/mes.

### Cómo emitir
- Sistema oficial SII: factura electrónica (gratis para Pyme)
- Sistemas privados: Bsale, Buk, Defontana, etc. (más amigables, $20-50K CLP/mes)
- **El contador suele incluirlo en su servicio** — confirmar al contratar

---

## W-8BEN-E · evita perder 30%

### Qué es
Formulario IRS (USA) que declara que tu empresa NO es US Person, y por tanto califica para tratado de doble tributación entre Chile y USA.

### Sin él
ClickBank retiene **30% de cada payout** automáticamente para IRS.

### Con él (vigente)
Retención = 0% (tratado Chile-USA evita doble tributación).

### Cómo llenar
1. Descargar formulario oficial: irs.gov/forms-pubs/about-form-w-8-ben-e
2. Completar con datos SpA (Chapter 3 status: Active NFFE / Corporación)
3. Indicar país: Chile
4. Indicar tratado: Article 7 (Business Profits) — exención de retención en USA
5. Subir a ClickBank → Account → Payee Information
6. **Renovar cada 3 años**

### Errores comunes
- Marcar "Foreign Government" cuando somos empresa privada
- No firmar con representante legal autorizado
- No actualizar si cambia razón social

**Recomendación:** que lo revise el contador antes de subir.

---

## FATCA + CRS · qué saben las autoridades

### FATCA (USA)
USA exige a bancos extranjeros (incluyendo Wise) reportar cuentas de US Persons. **Como SpA chilena con socios chilenos, FATCA no aplica directamente** pero Wise igualmente reporta cumplimiento.

### CRS (Common Reporting Standard)
Estándar OCDE — Wise reporta a la jurisdicción del titular (Chile) los movimientos.
**El SII chileno sabe lo que entra a Wise SpA.**

### Implicancia
**Nada queda oculto.** Lo que no se declare = multas + intereses + posible querella tributaria.

**La regla:** todo USD que entra se registra como factura de exportación. Sin excepciones.

---

## Cierre fiscal mensual · proceso (SOP 12)

### Días 1-5 del mes (mes M+1 cierra mes M)

**Día 1 (Cris)**
- Export resumen cobros ClickBank de mes M
- Export resumen gastos: Meta Ads, Google Ads, Wise, herramientas con factura

**Día 2 (Romi)**
- Consolida en `06-ops/fiscal/YYYY-MM.md`
- Revisa diferencias vs proyección

**Día 3 (Romi)**
- Emite facturas de exportación (1 por payout)
- Sube a SII
- Genera PDF para registro

**Día 4 (Romi)**
- Envía pack consolidado al contador (Drive compartido)
- Incluye: facturas emitidas, gastos con factura local, planilla resumen

**Día 5 (Contador)**
- Declara F29 (mensual)
- Pago de impuestos correspondientes
- Confirma con Romi por Slack

**Día 12 (deadline duro SII)**
- F29 debe estar declarado y pagado
- Si no, multa por mora

---

## Costos reales primer trimestre

| Item | Setup | Mensual | Trimestre 1 |
|---|---|---|---|
| Constitución SpA | $0 | — | $0 |
| Iniciación SII | $0 | — | $0 |
| Cuenta corriente bancaria | ~$10K CLP | $0-15K CLP | $35K CLP |
| Wise Business setup | ~$40 USD | $0 | $40 USD |
| Contador | $0 | $250-350K CLP | $750-1,050K CLP |
| Tarjeta crédito empresarial | $0 | $0 (algunos $5K CLP) | $0-15K CLP |
| **Total Setup + Trimestre 1** | | | **~$1.1M CLP + $40 USD** ≈ **$1,400 USD** |

Con capital inicial $11K USD, quedan ~$9.6K USD para herramientas + ad spend + Skalers Pro.

---

## Distribución de utilidades (preliminar)

### Mes 1-6 (validación)
- 70% reinversión (caja para escalar winners)
- 30% distribución según % accionario

### Mes 7-12 (sistema validado)
- 50% reinversión
- 50% distribución

### Año 2+ (operación madura)
- 40% reinversión
- 60% distribución

**Decisión:** se discute caso a caso en retro mensual hasta validar primer winner.

---

## Lo que NUNCA hacemos

1. ❌ Cobrar ClickBank a cuenta personal sin facturar
2. ❌ Convertir USD → CLP → USD (pérdida 1-3% cada vuelta)
3. ❌ Cargar Wise directo en Meta (no emite tarjeta para Chile)
4. ❌ Usar N26 para flujos del negocio (es personal)
5. ❌ Skipear factura de exportación (FATCA/CRS reportan)
6. ❌ Atrasarse en F29 (multa por mora)
7. ❌ Mover plata a cuenta de otro socio sin documentar
8. ❌ Operar sin W-8BEN-E vigente

---

## Cuando llegamos a $15K USD/mes consistente

Trigger para evaluar:
- Constituir LLC USA (Wyoming o Delaware)
- Wise Business US para tarjeta real
- Holding structure: LLC USA poseé acciones SpA Chile
- Asesoría fiscal dual (contador chileno + CPA USA)

**Decisión documentada en `decisions-log.md` cuando se tome.**

---

## Recursos

- **Wise Business:** wise.com/business
- **W-8BEN-E:** irs.gov/forms-pubs/about-form-w-8-ben-e
- **SII Régimen Pro Pyme:** sii.cl/destacados/regimen_propyme
- **Empresa en un Día:** empresaenundia.cl
- **Contador recomendado:** [PENDIENTE — Romi elige en semana 1]

---

*Este skill se actualiza cuando: cambia régimen tributario chileno, cambia estructura societaria, cambia política Wise/ClickBank.*
