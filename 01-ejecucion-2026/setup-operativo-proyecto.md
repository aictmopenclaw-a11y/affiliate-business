# Setup operativo del proyecto (orden de arranque)

> La base organizacional antes de Meta Ads. El email es la llave maestra: ClickBank, Meta, Notion, dominios y pagos cuelgan de él. Por eso va primero, y por eso se monta blindado.

**Equipo:** Cris (raíz técnica), Romi (contenido), Dali (creativos). **Marca:** TrueNorth.

---

## Orden correcto (no saltarse)

1. **Email Gmail dedicado** del proyecto (la raíz de todas las identidades).
2. **Labels, filtros y alias** en ese Gmail (orden desde el día 1, no después).
3. **Notion** (el cerebro visual del proyecto, espejo del repo).
4. **Ecosistema por oferta** (estructura de carpetas replicable).
5. **Meta Ads** (recién con la base lista, ver documentos ya creados).

La regla: cada paso usa al anterior. El email registra ClickBank/Meta/Notion/dominios. Por eso si el email queda desordenado o inseguro, arrastra todo.

---

## 1. Email Gmail del proyecto

### Nombre
Recomendado: **`truenorthmedia@gmail.com`** (marca de agencia, profesional, no revela "affiliate" ni "clickbank").

Alternativas por si está tomado: `truenorth.media@gmail.com` · `gotruenorthmedia@gmail.com` · `truenorthhq@gmail.com`.

`[CRITERIO]` No uses un nombre que revele el negocio (nada de "affiliate", "clickbank", "ads"). El email aparece en registros que terceros pueden ver.

### Reglas de creación
- **Dedicado y aislado.** Solo para este proyecto. No mezclar con OpenClaw ni con correos personales. Mismo principio de aislamiento que en Meta.
- **Lo administra Cris** (es la raíz, igual que es admin de los Business Portfolios). Romi y Dali reciben acceso a lo que les toca, no las llaves del email.
- **Seguridad (obligatoria, es la llave maestra):**
  - 2FA con app authenticator (Google Authenticator / Authy), no solo SMS.
  - Email de recuperación + teléfono de recuperación configurados.
  - Guardar los códigos de respaldo en 1Password.
  - `[CRITERIO]` Si cae este email, cae el acceso a todo. Trátalo como la cuenta más crítica del proyecto.

---

## 2. Labels, filtros y alias (orden desde el día 1)

Gmail usa "carpetas" como **labels anidados** con `/`. Estructura propuesta:

```
Ofertas/
   Ofertas/01-Dental
   Ofertas/02-Idiomas
   Ofertas/03-WeightLoss
Plataformas/
   Plataformas/ClickBank
   Plataformas/Meta
   Plataformas/Dominios-Namecheap
   Plataformas/Pagos-Wise
Herramientas/
   Herramientas/Notion
   Herramientas/Landing-Tracking
Finanzas/
   Finanzas/Payouts
   Finanzas/Impuestos-W8BEN
Equipo/
Compliance/
Archivo/
```

### El truco que mantiene todo ordenado solo: alias con "+"

Gmail entrega a tu bandeja cualquier correo enviado a `tuemail+loquesea@gmail.com`. Usas un alias distinto al registrarte en cada plataforma, y un filtro lo etiqueta automáticamente:

| Al registrarte en | Usa este alias | Filtro auto-etiqueta a |
|---|---|---|
| ClickBank | `truenorthmedia+clickbank@gmail.com` | Plataformas/ClickBank |
| Meta / Facebook | `truenorthmedia+meta@gmail.com` | Plataformas/Meta |
| Namecheap (dominios) | `truenorthmedia+dominios@gmail.com` | Plataformas/Dominios-Namecheap |
| Wise (pagos) | `truenorthmedia+wise@gmail.com` | Plataformas/Pagos-Wise |
| Notion | `truenorthmedia+notion@gmail.com` | Herramientas/Notion |
| Oferta 1 (vendor) | `truenorthmedia+oferta1@gmail.com` | Ofertas/01-Dental |

Ventaja extra anti-spam: si un alias empieza a recibir spam, sabes exactamente qué plataforma filtró tu correo.

### Crear un filtro (1 vez por alias)
Gmail → Configuración → Filtros → Crear filtro → campo "Para": `truenorthmedia+clickbank@gmail.com` → Crear filtro → marcar "Aplicar etiqueta: Plataformas/ClickBank" (y "Saltar bandeja de entrada" si quieres que vaya directo a la carpeta).

---

## 3. Notion (cerebro del proyecto)

`[CRITERIO]` Misma doctrina que OpenClaw: **el repo es la fuente de verdad, Notion es la capa visual** para el equipo (Romi y Dali viven mejor en Notion que en archivos).

### Workspace
Crear el workspace con el mismo email (`truenorthmedia+notion@`). Plan free alcanza para arrancar.

### Databases a crear
| Database | Para qué | Campos clave |
|---|---|---|
| **Ofertas** | Pipeline de ofertas evaluadas | Nicho, gravity, AOV, payout, estado (test/activa/kill), score |
| **Campañas** | Cada campaña Meta por oferta | Oferta, ad account, presupuesto, ROAS, estado |
| **Creativos** | Biblioteca de Dali | Oferta, ángulo, tipo, link, performance |
| **Tareas** | To-do del equipo | Responsable (Cris/Romi/Dali), estado, deadline |
| **Finanzas** | Payouts y gastos | Oferta, ingreso, ad spend, neto, fecha |
| **SOPs** | Procedimientos | Igual que el repo, espejo |
| **Aprendizajes** | Lo que funciona y lo que no | Tipo, oferta, insight |

### Vistas útiles
- Tablero (kanban) por estado para Ofertas y Tareas.
- Calendario para Campañas.
- Galería para Creativos.

---

## 4. Ecosistema por oferta (estructura replicable)

Cada oferta es un stack aislado (ver `meta-ads-estructura-bulletproof`, sección 8). Su carpeta replica esta estructura:

```
ofertas/01-dental/
   brief.md             (avatar, niveles de consciencia, ángulos)
   copy/                (hooks, primary text 5x5, headlines)
   creativos/           (assets de Dali, naming cliente-campaña-NN)
   bridge/              (la landing de esta oferta)
   tracking.md          (pixel, dataset, CAPI, postback, fbclid)
   meta/                (estructura de campaña, audiencias)
   reportes/            (resultados, kill/scale)
   estado.md            (dónde va esta oferta hoy)
```

Cada oferta tiene además su propio: dominio, dataset/pixel, página FB/IG, ad account, tarjeta (regla de aislamiento).

---

## 5. Meta Ads (recién acá)

Con la base lista, se ejecuta lo ya documentado:
- **Estructura bulletproof:** `meta-ads-estructura-bulletproof`
- **Roles del equipo:** `meta-ads-roles-equipo-agencia`
- **Bridge pages:** `bridge-pages-playbook` + plantillas en `04-tech/bridge-pages/`

---

## Checklist de arranque operativo

```checklist
[ ] Email truenorthmedia@gmail.com creado (o alternativa disponible)
[ ] 2FA con authenticator + recuperación + códigos en 1Password
[ ] Labels creados (Ofertas, Plataformas, Herramientas, Finanzas, Equipo, Compliance, Archivo)
[ ] Filtros de alias "+" configurados (clickbank, meta, dominios, wise, notion)
[ ] Notion: workspace creado con el email del proyecto
[ ] Notion: 7 databases creadas (Ofertas, Campañas, Creativos, Tareas, Finanzas, SOPs, Aprendizajes)
[ ] Estructura de carpetas por oferta definida en el repo
[ ] Recién entonces: arrancar setup de Meta Ads
```

---

*Documento operativo. El email y su seguridad son la base de todo lo demás. `[CRITERIO]` = decisión organizativa de este documento; el resto se apoya en los documentos de estructura ya creados.*
