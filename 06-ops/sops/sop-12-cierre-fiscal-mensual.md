# SOP 12 · Cierre Fiscal Mensual con Contador

**Owner:** Romi (con apoyo Cris en data)
**Frecuencia:** Mensual · días 1-5 del mes (mes M+1 cierra mes M)
**Tiempo:** 90 min total distribuido en 5 días
**Inputs:** ClickBank reports, Meta + Google ads spend, facturas locales
**Output:** F29 declarado y pagado antes del **día 12** + facturas exportación emitidas
**Skill relacionado:** `affiliate-financial-cross-border.md`

---

## Calendario detallado

### Día 1 (1ro del mes M+1) — Cris export data
- **Mañana:**
  - Export resumen cobros ClickBank del mes M (CSV)
  - Export resumen gastos Meta Ads del mes M (CSV)
  - Export Google Ads si aplica
  - Export herramientas con factura (Wise statement, suscripciones SaaS)
- Subir todo a `06-ops/fiscal/YYYY-MM/raw-exports/`
- Notificar a Romi: "Data del mes M lista en fiscal/YYYY-MM/"

### Día 2 — Romi consolida
- Crear `06-ops/fiscal/YYYY-MM.md`:

```markdown
# Cierre Fiscal · YYYY-MM

## Cobros ClickBank
| Fecha payout | Monto USD | Conversión CLP | Tipo cambio |
|---|---|---|---|
| YYYY-MM-DD | $X | $X | $X |
| ... | ... | ... | ... |
| **Total mes** | **$X USD** | **$X CLP** | |

## Gastos
### Ad spend
| Plataforma | Monto USD | CLP equiv |
|---|---|---|
| Meta Ads | $X | $X |
| Google Ads | $X | $X |

### Herramientas (con factura)
| Servicio | Monto USD | CLP equiv |
|---|---|---|
| Landerlab | $X | $X |
| ClickFunnels | $X | $X |
| ... | ... | ... |

### Operacionales locales
| Item | Monto CLP |
|---|---|
| Contador | $X |
| Banco mantención | $X |
| Cloudflare / dominios | $X |

## Resumen
- **Revenue total:** $X CLP
- **Costos totales:** $X CLP
- **Profit pre-impuestos:** $X CLP
```

### Día 3 — Romi emite facturas exportación
- Por cada payout de ClickBank → 1 factura exportación electrónica
- Sistema: SII oficial o software (Bsale, Defontana, Buk)
- Datos:
  - Receptor: ClickBank Inc. (RUT genérico extranjero · pedir al contador exacto)
  - Servicio: "Servicios de marketing digital — comisión por afiliación"
  - Monto: USD del payout × tipo cambio del día (TC SII publicado)
  - Tasa IVA: **0% — Exportación de servicios** (Art. 12 letra E N°16)
- Guardar PDFs en `06-ops/fiscal/YYYY-MM/facturas/`

### Día 4 — Romi envía pack al contador
Pack consolidado en email + Drive compartido:
- `YYYY-MM.md` (resumen del cierre)
- Carpeta `facturas/` con PDFs exportación
- Carpeta `raw-exports/` con CSVs Meta + ClickBank
- Facturas locales recibidas en el mes (PDF de proveedores)

Mensaje al contador:
```
Hola [contador],
Pack mes YYYY-MM listo:
- X facturas exportación emitidas
- $X USD revenue (= $X CLP)
- $X CLP gastos
Quedo atenta a F29 antes del día 12.
```

### Día 5 — Contador declara F29
- Contador presenta F29 ante SII
- Confirmación de pago de impuestos
- Romi recibe confirmación por email + sube a `06-ops/fiscal/YYYY-MM/F29-confirmado.pdf`

### Día 12 (deadline duro SII)
- F29 declarado y pagado
- Si no, multa por mora (~ $50K CLP + intereses)

---

## Anual · F22 (abril del año siguiente)

- Contador prepara F22
- Romi revisa antes de firmar
- Idealmente declarar antes del último día de plazo (no a último momento)
- Documentar en `06-ops/fiscal/YYYY-anual/`

---

## Checklist mensual

- [ ] Día 1: Cris exportó data (cobros + spend + herramientas)
- [ ] Día 2: Romi consolidó en `YYYY-MM.md`
- [ ] Día 3: Facturas exportación emitidas (1 por payout)
- [ ] Día 4: Pack enviado al contador
- [ ] Día 5: F29 declarado por contador
- [ ] Día 12: F29 pagado y confirmado
- [ ] Archivos en `fiscal/YYYY-MM/` ordenados
- [ ] Confirmación equipo en Slack

---

## Errores frecuentes

1. Atrasar día 1-2 → cascada: F29 no se alcanza al día 12
2. No emitir factura exportación por payout → SII detecta vía CRS
3. Convertir USD a CLP solo para hacer la factura → pérdida innecesaria
4. No guardar tipo de cambio del día → contador no puede declarar bien
5. Mezclar gastos personales con SpA → pesadilla auditable

---

## Historial

- **v0.1 · 2026-04-28** — estructura inicial
