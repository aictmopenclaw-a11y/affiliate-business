# SOP 00 · Crear cuenta ClickBank (afiliado · Chile · no-US)

> **Owner:** Cris
> **Frecuencia:** una vez (setup inicial)
> **Tiempo:** 30-45 min
> **Prerequisito:** Wise Personal con cuenta USD activa (routing + account number USA)
> **Mercado:** USA inglés · operamos como afiliados (no vendors)
>
> Última actualización: 2026-06-14 · validar detalles finos contra videos oficiales ClickBank en `videos-clickbank-2026/transcripciones/`

---

## Antes de empezar · ten esto a mano

| Dato | Valor | Notas |
|---|---|---|
| **Nombre legal** | (como aparece en cédula) | Debe coincidir EXACTO para W-8BEN |
| **Email dedicado** | recomendado uno aparte de OpenClaw | Aislamiento |
| **Teléfono** | +56 9 XXXX XXXX | Con código país |
| **Dirección** | la de cédula | Para W-8BEN |
| **Account nickname** | `truenorth` (backups: `harbor`, `meridian`) | **PERMANENTE · no cambiable** |
| **Wise USD** | routing + account number USA | Para recibir pagos |
| **País del beneficiario** | Chile | Para tratado tributario |

---

## Paso 0 · El nickname (decisión irreversible)

El **account nickname** es tu affiliate ID. Reglas:
- 5-10 caracteres alfanuméricos, minúsculas
- **No se puede cambiar nunca**
- Aparece visible en cada HopLink (`hop.clickbank.net/?affiliate=NICKNAME&...`)
- El comprador puede verlo en la URL del navegador

**Por eso:** neutro, sin revelar oferta/marca/estrategia.

Puedes crear hasta **10 nicknames** dentro de la misma cuenta master (útil después para segmentar por niche/canal).

**Nickname elegido:** `truenorth` (si está tomado al crear: `harbor`, luego `meridian`)

---

## Paso 1 · Signup (10 min) · FORMULARIO REAL VERIFICADO 2026-06-14

URL directa: **accounts.clickbank.com/signup/**

El formulario tiene un aviso clave arriba:
> *"All fields are mandatory. Accurate information is required. Inaccurate information could result in a declined account."*

→ Por eso el nombre debe ser EXACTO al de la cédula. Info falsa = cuenta rechazada.

Campos en orden (todos obligatorios):

1. **Country:** cambiar de "United States of America" (default) a **Chile** (sí está en la lista)
2. **First Name:** nombre legal
3. **Last Name:** apellido legal
4. **Phone Number:** cambiar el prefijo de +1 (default US) a **+56** · luego el número
5. **Email Address:** el dedicado
6. **Password:** requisitos REALES y estrictos de ClickBank:
   - Mínimo **2 minúsculas**
   - Mínimo **2 mayúsculas**
   - Mínimo **2 números**
   - Mínimo **2 caracteres especiales** (`!@#$%^&*/`)
   - **Máximo 32 caracteres**
   - **Sin espacios**
   - Ejemplo válido: `TruHealth26!!aB` (guardar en 1Password)
7. Click **"Continue to Terms and Conditions"**
8. Se habilita el checkbox **"I have read and agree to the Terms and Conditions"** → marcarlo
9. Click **"Join ClickBank!"**

10. **Verificar email** (link que llega al correo)

> ⚠️ ClickBank a veces pide verificación adicional para no-US. Si pide documento, subir cédula. Normal.
> ⚠️ Hacer esto desde TU navegador con IP chilena (no automatización · no VPN). El anti-fraud de ClickBank flaggea sesiones raras.

---

## Paso 2 · Crear el nickname / account (5 min)

Tras primer login, ClickBank pide crear tu primer **account nickname**:

1. Ir a la sección de cuentas / "Create Account"
2. Ingresar el **nickname** decidido en Paso 0
3. Seleccionar tipo: **Affiliate** (no Vendor · vendor cuesta $49.95 setup)
4. Confirmar

> El nickname queda creado. Ya puedes generar HopLinks técnicamente, pero falta configurar pagos + tax para cobrar.

---

## Paso 3 · Configurar pagos (10 min)

Ir a **Settings → My Account → Payment Information** (o "Account Settings"):

### 3a · Payment threshold
- Mínimo: $10 USD
- Default: $100 USD
- **Recomendado arranque:** $50 USD (cobrar antes, validar que el flujo funciona)

### 3b · Payment method
ClickBank por defecto usa **cheque**. Cambiar a:
- **Direct Deposit** si Chile estuviera en la lista (NO está · solo México en LATAM)
- **Wire transfer** (funciona pero cobra fee ~$15-30)
- **Payoneer** (partner oficial ClickBank · alternativa sólida)
- **Workaround Wise USD ACH:** ingresar el routing + account number USA de Wise como si fuera cuenta US (documentado funcionando 2026)

> **Para nuestro caso:** intentar primero Wise USD ACH (routing + account number). Si ClickBank lo rechaza por validación de dirección US, fallback a Payoneer.

### 3c · Payment frequency
- Weekly o Biweekly
- **Recomendado:** Weekly (cash flow más rápido)

---

## Paso 4 · Tax form W-8BEN (10 min · CRÍTICO)

Sin esto, ClickBank retiene **30% de cada pago** (withholding IRS).

1. En Account Settings → buscar **Tax Information** / **Tax Form**
2. Seleccionar **W-8BEN** (persona natural no-US · NO W-8BEN-E que es para empresas)
3. Llenar:
   - **Name:** nombre legal exacto
   - **Country of citizenship:** Chile
   - **Permanent address:** dirección de cédula (Chile)
   - **Foreign Tax ID:** tu RUT (sin puntos, con guión · ej 12345678-9)
   - **Treaty claim:** Chile (tratado USA-Chile vigente desde feb 2024)
   - **Article / rate:** el formulario suele autocompletar la tasa reducida del tratado
   - **Firma:** nombre + fecha
4. Submit

> El tratado USA-Chile reduce el withholding. Sin W-8BEN = 30% retenido. Con W-8BEN = tasa reducida del tratado (mucho menor o 0% según tipo de ingreso).

---

## Paso 5 · Configurar el HopLink test (5 min)

Para confirmar que la cuenta funciona:

1. Ir a **Marketplace**
2. Buscar cualquier oferta (ej. categoría Health & Fitness)
3. Click **"Promote"** → genera HopLink con tu nickname
4. Verificar que el HopLink tiene formato: `https://NICKNAME.VENDOR.hop.clickbank.net` o `hop.clickbank.net/?affiliate=NICKNAME&vendor=VENDOR`

> Esto confirma que el nickname está activo. NO necesitas promover esta oferta · es solo test.

---

## Checklist final

- [ ] Cuenta creada + email verificado
- [ ] Nickname permanente decidido y creado
- [ ] Payment method configurado (Wise USD o Payoneer)
- [ ] Payment threshold $50
- [ ] **W-8BEN completado** (sin esto pierdes 30%)
- [ ] HopLink test generado OK

---

## Lo que NO hacer

- ❌ Nickname que revele marca/oferta (es visible en URLs)
- ❌ Saltarse el W-8BEN (30% retención)
- ❌ Usar cuenta Vendor (cuesta $49.95 · no la necesitamos como afiliados)
- ❌ Nombre que no coincida con cédula (rechazo W-8BEN)
- ❌ Mezclar con cuentas/datos de OpenClaw

---

## Recordatorios post-creación (Customer Distribution Requirement)

ClickBank no paga el primer payout hasta cumplir el **CDR**:
- Mínimo **5 ventas**
- Con al menos **2 métodos de pago distintos** entre los compradores (ej. 2 con Visa + 1 Mastercard + 2 PayPal)
- Después, esperar el ciclo de pago

Esto es normal · planificar cash flow asumiendo 2-4 semanas de lag desde la primera venta.

### Dormant account fees
Si no hay ventas:
- 90 días sin venta → $1/pay period
- 180 días → $5/pay period
- 365 días → $50/pay period

Plan: vender en mes 1 o pausar/cerrar cuenta si el test no avanza.

---

*SOP 00 · validar flujo exacto contra videos oficiales ClickBank cuando terminen de transcribir.*
