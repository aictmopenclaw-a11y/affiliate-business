# Estructura bulletproof de Meta Ads para affiliate (sin romper cuentas)

> *Estás a un anuncio de cambiar tu vida.*
> Y a un error de estructura de perder la cuenta. Romper una cuenta de Meta te tira semanas atrás: pierdes el pixel entrenado, el historial de gasto, el aprendizaje del algoritmo y, en el peor caso, arrastras a las cuentas asociadas. Montar bien el árbol desde el día 1 es la diferencia entre escalar y recomenzar.

**Mercado:** USA inglés · **Nicho:** nutra / health · **Capital de arranque:** $2-5K USD · **Fecha:** 2026-06-22

Este documento define cómo un equipo que arranca HOY monta toda la jerarquía de Meta Business sin que le baneen cuentas. Cruza las fuentes internas del repo (síntesis de 17 videos + foros, errores documentados, skill de funnel) con el modelo actual de Meta Business 2026 (Business Portfolio, Datasets, CAPI). 

**Cómo leer las marcas de confianza:**
- `[FUENTE REPO]` = sale de los videos/foros investigados o de un skill interno, con cita.
- `[BEST-PRACTICE]` = estándar general de Meta Business 2026 / consenso de la industria, no atado a una fuente del repo.
- `[CRITERIO]` = juicio operativo de este documento donde la fuente no da un número exacto; se marca como tal, no se inventa dato.

Aviso honesto de los foros: el consenso 2026 es que Meta puede banear afiliados de ClickBank "tarde o temprano, uses landing page o no" (peux pas, BlackHatWorld) `[FUENTE REPO]`. Ninguna estructura es 100% inmune. Lo que esta guía hace es bajar drásticamente la probabilidad y aislar el daño cuando ocurra.

---

## 1. El árbol completo (jerarquía Meta)

Toda la operación cuelga de una sola raíz: un perfil personal de Facebook real. De ahí baja el Business Portfolio (el contenedor de negocio), y dentro viven los activos. Debajo del ad account está la jerarquía de campaña.

```
[Perfil personal de Facebook]  (raíz · persona real · admin)
│
`-- [Business Portfolio]  (antes "Business Manager" · el contenedor del negocio)
    │
    |-- [Ad Account(s)]  (donde vive el gasto y las campañas)
    |   |
    |   `-- [Campaign]  (objetivo: Sales / Purchase)
    |       |
    |       `-- [Ad Set]  (presupuesto CBO, audiencia, placements, optimización)
    |           |
    |           |-- [Ad]  (creativo 1 · hook A)
    |           |-- [Ad]  (creativo 2 · hook B)
    |           `-- [Ad]  (creativo 3 · hook C)
    |
    |-- [Páginas de Facebook]  (1 por marca/landing · calentada antes de gastar)
    |   `-- [Cuentas de Instagram]  (vinculadas a la página)
    |
    |-- [Datasets]  (antes "Pixel" · evento del navegador + servidor)
    |   `-- [CAPI]  (Conversions API · eventos server-to-server desde ClickBank)
    |
    |-- [Dominios verificados]  (tu bridge page · verificación por DNS/meta-tag)
    |
    |-- [Métodos de pago]  (tarjeta limpia y dedicada · 1 por ad account)
    |
    `-- [Usuarios y roles]  (admin persona real · System Users para API · 2FA)
```

**Qué es cada nivel (de arriba a abajo):**

- **Perfil personal de Facebook (raíz).** Tu identidad real en Meta. Todo lo demás cuelga de aquí. Si este perfil cae (por actividad sospechosa, login desde fingerprint sucio, etc.), todo lo que administra queda en riesgo. Por eso el perfil tiene que ser sano: antigüedad, foto, amigos, actividad normal, 2FA. `[BEST-PRACTICE]` Los grandes usan perfiles falsos descartables a escala, pero eso es endgame, no arranque (ver sección 5).
- **Business Portfolio** (Meta renombró "Business Manager" a "Business Portfolio" en 2024-2025). Es el contenedor que agrupa ad accounts, páginas, datasets, dominios y usuarios bajo una sola entidad de negocio. Permite separar tu vida personal de tu operación y dar permisos granulares. `[BEST-PRACTICE]`
- **Ad Account.** La unidad donde se crean campañas y se carga el método de pago. Tiene su propio límite de gasto y su propio historial de confianza con Meta. Cuentas nuevas arrancan con límites bajos que suben con buen comportamiento. `[BEST-PRACTICE]`
- **Páginas de Facebook + cuentas de Instagram.** La identidad pública desde la que corren los ads. Meta penaliza páginas frías o recién creadas que de golpe gastan. Param lo confirma: hay que "calentar" la página con engagement antes de correr ads `[FUENTE REPO, N3-SH71IXrbp-A 04:40]`.
- **Datasets (antes Pixel) + CAPI.** El dataset es el contenedor de eventos de conversión. Incluye el pixel del navegador y la Conversions API (eventos server-to-server). En el flujo affiliate, la venta ocurre en el dominio de ClickBank, así que el Purchase llega por CAPI/postback, no por el pixel de tu landing `[FUENTE REPO, affiliate-funnel-structure.md]`. Thomas Owen lo llama directamente "data set aka pixel" al armar la campaña `[FUENTE REPO, N2-txOcKycyAgc 09:24]`.
- **Dominios verificados.** Tu bridge page corre en un dominio propio que verificas en el Business Portfolio (DNS o meta-tag). La verificación de dominio es la que te da control sobre la configuración de eventos y sube la confianza ante Meta. `[BEST-PRACTICE]`
- **Métodos de pago.** Tarjeta dedicada a la operación. Nunca compartir la misma tarjeta entre cuentas que quieres mantener aisladas: Meta usa el método de pago como una de las señales para vincular cuentas y propagar bans `[FUENTE REPO, foros: si cae una cuenta caen las asociadas]`.
- **Usuarios y roles / System Users.** Quién accede y con qué permiso. El admin es la persona real; los System Users son identidades no-humanas para conectar herramientas vía API (lo que Jordan usa para lanzar creativos en masa) `[FUENTE REPO, N2-Aq0TfaAdSmY 53:55]`. 2FA obligatorio en todos.
- **Campaign → Ad Set → Ad.** La jerarquía operativa dentro del ad account. La campaña define el objetivo (para affiliate: Sales optimizado a Purchase). El ad set lleva el presupuesto (CBO), la audiencia, los placements y la optimización. Los ads son los creativos. Jordan es tajante: "ningún top affiliate optimiza a clicks de botón", se optimiza a Purchase `[FUENTE REPO, N2-Aq0TfaAdSmY 42:16]`.

---

## 2. Cada nivel: cuántos tener, regla anti-ban

| Nivel | Qué es | Cuántos al arrancar | Regla bulletproof |
|---|---|---|---|
| **Perfil personal FB** | Identidad raíz, admin de todo | 1 (real, sano, con antigüedad) | 2FA siempre. Login desde IP/dispositivo estable. Nunca administrar desde el mismo fingerprint que una cuenta baneada `[FUENTE REPO, Multilogin]` |
| **Business Portfolio** | Contenedor del negocio | 1 limpio y aislado | Aislado de cualquier otro negocio (en nuestro caso, aislado de OpenClaw) `[FUENTE REPO, plan §Fase 0]`. No mezclar verticales de riesgo |
| **Ad Account** | Donde vive el gasto | 1, máximo 2 | 1 tarjeta por cuenta. Respetar el límite de gasto inicial, no forzarlo. No correr 2 ofertas de riesgo distinto en la misma cuenta `[CRITERIO]` |
| **Página FB + IG** | Identidad pública del ad | 1 página + 1 IG | Calentar con engagement $1-10/día ~1 semana antes de gastar `[FUENTE REPO, N3-SH71IXrbp-A 04:40]`. Nombre y branding consistentes con la landing |
| **Dataset (Pixel) + CAPI** | Eventos de conversión | 1 dataset, CAPI conectado | Validar con compra real de $1 ANTES de gastar; ver el Purchase en Events Manager en 30 min `[FUENTE REPO, SINTESIS §3 + funnel skill]` |
| **Dominio verificado** | Tu bridge page | 1 dominio propio | Verificado por DNS. Bridge con tono informativo, NUNCA direct link del HopLink `[FUENTE REPO, consenso foros]` |
| **Método de pago** | Tarjeta de la operación | 1 limpia y dedicada | No compartir tarjeta ni IP entre cuentas a aislar `[FUENTE REPO, foros]` |
| **Usuarios / roles** | Acceso y permisos | 1 admin real (+ System User si API) | 2FA en todos. Roles mínimos necesarios. System User solo si conectas herramientas `[BEST-PRACTICE]` |
| **Campaign** | Objetivo de la campaña | 1 (Sales/Purchase) | Optimizar a Purchase, no a clicks ni leads `[FUENTE REPO, N2-Aq0TfaAdSmY 42:16]`. Alineado a Andromeda: consolidar, no fragmentar `[FUENTE REPO, N2-txOcKycyAgc 37:21]` |
| **Ad Set** | Presupuesto + audiencia | 1 CBO, broad, USA aislado | Audiencia broad, geo USA aislado, edad según oferta `[FUENTE REPO, N3-SH71IXrbp-A 09:54]`. Placements limpios (sin Audience Network) |
| **Ad** | Creativos | 3-5 por ad set | Cada uno un ángulo distinto (problema / beneficio / prueba social) `[FUENTE REPO + regla OpenClaw 3 variantes]`. Diversidad creativa es lo que el algoritmo necesita `[FUENTE REPO, Thomas Owen]` |

---

## 3. Paso a paso de setup (en orden)

Este es el orden exacto para montar el árbol. No saltarse pasos: cada uno construye confianza para el siguiente.

1. **Sanear el perfil personal de Facebook.** Usa un perfil real con antigüedad, foto, amigos y actividad normal. Activa 2FA. Define un dispositivo e IP estables desde donde lo administrarás siempre. *Por qué:* es la raíz; un perfil frío o sospechoso contamina todo lo que cuelga de él `[BEST-PRACTICE]`.

2. **Crear el Business Portfolio** (business.facebook.com → crear portfolio). Nómbralo como tu marca de salud, con tu nombre real y email de negocio. *Por qué:* separa la operación de tu identidad personal, da permisos granulares y es donde vivirán los demás activos `[BEST-PRACTICE]`. Mantenlo aislado de cualquier otro negocio `[FUENTE REPO, Fase 0]`.

3. **Crear / conectar la Página de Facebook** (y la cuenta de Instagram vinculada). Branding consistente con la bridge page. *Por qué:* es la identidad pública del anuncio; tener página + IG amplía placements y da credibilidad.

4. **Calentar la página (warm-up).** Antes de tocar conversiones, corre engagement con $1-10/día durante ~1 semana `[FUENTE REPO, N3-SH71IXrbp-A 04:40]`. *Por qué:* una página recién creada que de golpe gasta en conversiones es señal roja para Meta (detalle en sección 4).

5. **Comprar y verificar el dominio.** Registra tu dominio (ej. Namecheap/Cloudflare), monta la bridge page, y verifícalo en el Business Portfolio por DNS o meta-tag. *Por qué:* la verificación de dominio te da control de la configuración de eventos y sube tu confianza ante Meta `[BEST-PRACTICE]`. La bridge debe tener tono informativo, mobile-first, carga < 3s `[FUENTE REPO, funnel skill]`.

6. **Crear el Dataset (antes Pixel).** En Events Manager crea el dataset y coloca el pixel en el `<head>` de la bridge. Configura los eventos: PageView, ViewContent (50% scroll), InitiateCheckout (click al CTA) `[FUENTE REPO, funnel skill]`. *Por qué:* es el cerebro de medición; sin eventos, el algoritmo optimiza a ciegas.

7. **Conectar CAPI (Conversions API).** El Purchase NO se dispara en tu landing (la venta ocurre en ClickBank). Configura el postback ClickBank → Meta CAPI: en ClickBank, Integrations → Postback/Pixels → Facebook, rol Affiliate, dominio verificado, y anexa `&fbclid={fbclid}&traffic_source=facebook` al HopLink `[FUENTE REPO, SINTESIS §3]`. *Por qué:* sin CAPI, Meta no aprende qué clicks convirtieron y la optimización a Purchase se vuelve ciega `[FUENTE REPO, funnel skill]`. Los fallos de CAPI son silenciosos: "no anuncian errores obvios, simplemente dejan de mandar data precisa" (Cometly) `[FUENTE REPO]`.

8. **Validar el tracking con una compra de $1 ANTES de gastar.** Haz una compra real de prueba y verifica que el evento Purchase aparece en Events Manager en ~30 min, con buen Event Match Quality (EMQ) `[FUENTE REPO, SINTESIS §3 + caso Drought]`. *Por qué:* el caso Drought de los foros optimizó con tracking roto y terminó decidiendo a ciegas. No avanzar si no trackea `[FUENTE REPO]`.

9. **Crear el Ad Account.** Dentro del Business Portfolio. Zona horaria USA, moneda USD. *Por qué:* lo creas tarde a propósito, cuando el resto del árbol ya está sano, para no tener una cuenta "vacía y nueva" llamando la atención.

10. **Agregar el método de pago.** Una tarjeta limpia y dedicada a esta cuenta. *Por qué:* compartir tarjeta/IP entre cuentas es una de las señales que Meta usa para vincularlas y propagar un ban `[FUENTE REPO, foros]`.

11. **Configurar usuarios y roles.** Admin = persona real con 2FA. Si vas a conectar herramientas por API más adelante, crea un System User con permiso mínimo. *Por qué:* roles mínimos reducen la superficie de riesgo; el System User es la vía limpia para automatización `[FUENTE REPO, N2-Aq0TfaAdSmY 53:55]`.

12. **Crear la primera campaña en PAUSED.** Objetivo Sales, optimización a Purchase, dataset conectado, 1 ad set CBO broad USA, 3-5 ads con ángulos distintos. Déjala en PAUSED hasta revisar todo y dar OK explícito. *Por qué:* nunca activar sin verificación final (regla operativa OpenClaw). Revisas placements, audiencia, tracking y copy antes de prender.

---

## 4. Protocolo de warm-up (lo que más salva cuentas)

El warm-up es la práctica que más reduce bans en cuentas nuevas. La lógica: una cuenta/página/perfil nuevo que de golpe gasta fuerte en un nicho vigilado (nutra) es exactamente el patrón que dispara revisiones. Subir gradual le enseña a Meta que eres un anunciante normal.

**Lo que SÍ dicen las fuentes del repo:**
- **Página:** calentar con engagement a $1-10/día durante al menos ~1 semana antes de correr conversiones `[FUENTE REPO, N3-SH71IXrbp-A 04:40]`. Param lo trata como requisito, no opción.
- **Plan interno:** Fase de warm-up de Semana 2-3, con engagement $1-10/día, "mínimo 1 semana" antes del lanzamiento del test `[FUENTE REPO, SINTESIS §6 timeline]`.
- **Presupuesto de arranque del test (post warm-up):** CBO $50-100/día `[FUENTE REPO, SINTESIS §6]`. Foros: para payout alto lo ideal es $150-200/día, pero con $2-5K hay que estirar `[FUENTE REPO]`.

**Calendario sugerido para los primeros 7-14 días `[CRITERIO]` (las fuentes dan los extremos: $1-10/día de warm-up y $50-100/día de test; la rampa intermedia es criterio operativo de este documento, no un dato de fuente):**

| Días | Foco | Gasto | Qué hacer | Qué NO hacer |
|---|---|---|---|---|
| 1-3 | Calentar página | $1-5/día | Engagement / page likes / post boost suave. Postear contenido normal | No correr conversiones. No tocar el ad account |
| 4-7 | Seguir calentando | $5-10/día | Subir engagement gradual. Validar tracking con compra $1 | No saltar a Purchase todavía. No subir de golpe |
| 8-10 | Primer test suave | $50/día CBO | Lanzar campaña Sales→Purchase, 3-5 creativos | No matar ads en < 24-72h `[FUENTE REPO]`. No subir budget |
| 11-14 | Lectura inicial | $50-100/día | Dejar correr, juntar data. Aplicar criterio de kill 3x payout | No escalar aún. No tocar ganadores prematuramente |

**Reglas de comportamiento durante el warm-up:**
- **No prender y apagar ads por impaciencia.** Tratar los ads como dados es el error #2 de Blanchard; no se decide con < 24-72h de data `[FUENTE REPO, N3-L2mO5trX3io 02:33]`.
- **Subir gradual, nunca de golpe.** Duplicar el gasto día a día es aceptable cuando hay data; saltar de $10 a $500 es señal roja `[CRITERIO]`.
- **No copiar-pegar la landing del vendor.** "Facebook no quiere copy-paste, tu cuenta puede ir a suspensión dura" (Param) `[FUENTE REPO, N3-SH71IXrbp-A 05:46]`.
- **Learning phase de Meta:** ~50 conversiones/semana por ad set para salir del learning `[FUENTE REPO, foros]`. Con CPA de afiliado esto implica que el capital alcanza para 1 test serio, no para varios a la vez.

---

## 5. Reglas bulletproof anti-ban

Las críticas, en orden de impacto:

1. **NUNCA direct linking del HopLink desde Meta. Bridge page propia obligatoria.** Es el error #1 y más repetido de todos los foros. "No hagas direct link, mi compañero y yo perdimos varias cuentas" (Social God) `[FUENTE REPO]`. "NO! Te van a banear eventualmente" (T J Tutor, admin AffiliateFix) `[FUENTE REPO]`. Param lo confirma en vivo: en el ad va la URL de TU website, el affiliate link va dentro de la landing `[FUENTE REPO, N3-SH71IXrbp-A 16:18]`. El direct linking que sí es estable es en Bing/Google con tráfico de intención, no en Meta `[FUENTE REPO, foros caso B]`.

2. **Bridge page con tono informativo, no de venta.** "La landing debe tener tono informativo y NO de venta/marketing, sino los algoritmos de FB la detectan como puro marketing de afiliado" (Chris Newman) `[FUENTE REPO]`. La bridge debe aportar valor real (advertorial, quiz, artículo), no ser un puente transparente `[FUENTE REPO, funnel skill]`.

3. **Dominio verificado + disclaimers de salud.** Verifica el dominio en el Business Portfolio. En nutra, Meta exige el disclaimer "This product is not intended to diagnose, treat, cure, or prevent any disease" en el copy del ad, no solo en la landing; sin eso = rechazo automático (regla 2026) `[FUENTE REPO, AuditSocials]`. Claims tipo "pierde X kilos" o "cura Y" son ban instantáneo. Copy de wellness suave o certificación LegitScript `[FUENTE REPO]`.

4. **Perfil personal sano + 2FA.** Cuenta vieja no te salva por sí sola: hay un caso de foros de una cuenta de FB de 5 años deshabilitada por promover afiliado `[FUENTE REPO, tc888 Warrior Forum]`. Pero un perfil sano, estable y con 2FA reduce el riesgo de revisión.

5. **No compartir tarjetas ni IP entre cuentas.** "Una cuenta limpia puede ser flageada en horas si Facebook detecta que se accede desde el mismo fingerprint que una cuenta baneada" (Multilogin) `[FUENTE REPO]`. Si cae una cuenta, pueden caer las asociadas por estas señales `[FUENTE REPO, foros]`.

6. **Antidetect browser / perfiles aislados: cuándo SÍ y cuándo NO.**
   - **NO al arrancar.** Con 1 BM limpio y 1-2 ad accounts, el antidetect agrega costo y complejidad sin beneficio claro. Las "farmed accounts" baratas tienen alto riesgo de ban `[FUENTE REPO, Multilogin]`. Es el GAP de infra que las fuentes reconocen como no resuelto para principiantes `[FUENTE REPO, SINTESIS §2]`.
   - **SÍ más adelante,** si operas múltiples cuentas en serio: ahí necesitas business managers separados + antidetect browser + proxies dedicados por cuenta + método de pago limpio, o contaminas unas con otras `[FUENTE REPO, foros gap 4]`.

7. **El endgame de seguridad (agency accounts) NO se persigue todavía.** El #1 actual de ClickBank (Jordan) no gana la guerra de bans con antidetect, sino con **agency accounts oficiales de Meta + exemption tags**: su empresa se volvió Meta Certified Partner, "es tan fácil correr Facebook, las cuentas son estables, nada se banea" `[FUENTE REPO, N2-Aq0TfaAdSmY 57:57]`. Los exemption tags se los dan gratis por mostrar que no corren "cosas locas" `[FUENTE REPO, 54:56]`. El umbral para acceder a eso es ~$3M/año de spend y una relación cultivada con reps de Meta `[FUENTE REPO, 56:32]`. Conclusión honesta: la guerra de bans se gana subiendo de liga, no peleándola con herramientas de ocultación. Para nosotros, eso está a años; arrancamos con 1 BM limpio. **Y NUNCA cloaking:** Jordan lo usa pero es zona roja absoluta (ban permanente + riesgo legal) e incompatible con un negocio sostenible `[FUENTE REPO]`.

---

## 6. Errores que rompen cuentas (de los foros)

| Error | Por qué mata la cuenta | Cómo evitarlo |
|---|---|---|
| **Direct linking del HopLink desde Meta** | Ban casi garantizado; si cae una cuenta, caen las asociadas. Consenso de todos los foros `[FUENTE REPO]` | Bridge page propia con tono informativo, siempre. La URL del ad es tu dominio, no el HopLink |
| **Landing con tono de venta** | Los algoritmos la detectan como "puro marketing de afiliado" y la flagean (Chris Newman) `[FUENTE REPO]` | Advertorial/quiz/artículo que aporta valor por sí mismo. No puente transparente |
| **Copiar-pegar la landing del vendor** | "Facebook no quiere copy-paste, tu cuenta puede ir a suspensión dura" (Param) `[FUENTE REPO, N3-SH71IXrbp-A 05:46]` | Customizar siempre: hook, story, beneficios propios. Nunca duplicar |
| **Claims de salud sin disclaimer** | Rechazo automático (regla Meta 2026): el disclaimer va en el copy del ad, no solo en la landing `[FUENTE REPO, AuditSocials]` | Disclaimer obligatorio en cada ad. Wellness suave o LegitScript. Cero "cura/pierde X kilos" |
| **Cloaking (white/black page)** | Viola explícitamente políticas Meta: ban permanente, posible acción legal `[FUENTE REPO, Meta Transparency]` | NO cloaking. Incompatible con negocio sostenible, aunque el caso affLIFT 154% ROI lo haya usado |
| **Página fría que gasta de golpe** | Cuenta/página nueva con gasto súbito en nicho vigilado = patrón de revisión | Warm-up $1-10/día ~1 semana antes de conversiones (Param) `[FUENTE REPO]` |
| **Compartir tarjeta/IP/fingerprint** | "Cuenta limpia flageada en horas si se accede desde el fingerprint de una baneada" (Multilogin) `[FUENTE REPO]` | 1 tarjeta por cuenta, IP/dispositivo estable, no administrar desde fingerprint sucio |
| **Comprar cuentas "aged" sin aislar** | Alto riesgo de ban; contaminas la nueva si compartes fingerprint con una baneada `[FUENTE REPO, Multilogin]` | Al arrancar, no comprar cuentas; operar 1 BM propio limpio |
| **Cuenta vieja como falsa seguridad** | Cuenta de FB de 5 años deshabilitada por promover afiliado `[FUENTE REPO, tc888 Warrior Forum]` | La antigüedad ayuda pero no inmuniza; igual respetar todas las reglas |
| **Tracking roto (caso Drought)** | Optimizas a ciegas; no sabes qué apagar ni escalar; pierdes confianza en tus números `[FUENTE REPO]` | Validar fbclid + CAPI/postback con compra $1 ANTES de gastar |
| **Pausar/cortar ads en < 24-72h** | Decides sin data; tratas ads como dados (error #2 de Blanchard) `[FUENTE REPO, N3-L2mO5trX3io 02:33]` | Kill budget escrito; matar el ad set (no bajarle budget) solo tras 3x payout sin venta |

**Casos reales investigados (referencia):**
- **Drought** (BlackHatWorld): tracking roto + targeting solo desktop "por flojera de hacer la landing mobile" → 1 venta tras ~$180, proyecto en pausa `[FUENTE REPO]`.
- **affLIFT Reduslim** (España): 154% ROI ($33,466 profit), pero usó white/black page (cloaking) → unit economics posibles, método NO replicable de forma compliant `[FUENTE REPO]`.
- **tc888** (Warrior Forum): cuenta de 5 años deshabilitada por afiliado, cierre permanente tras apelar con ID `[FUENTE REPO]`.

---

## 7. Qué montar HOY para nuestro caso

**Situación:** Cris tiene su cuenta personal de Facebook. Capital $2-5K, recién empezando, nicho nutra/health, mercado USA. La cuenta ClickBank planificada usa el nickname `truenorth` y el dominio `truhealthdaily.com` está en cola de compra (tareas internas pendientes).

### Estructura MÍNIMA viable a montar hoy

```
[Perfil personal FB de Cris]  (sano, 2FA, IP estable)
`-- [1 Business Portfolio]  (aislado de OpenClaw)
    |-- [1 Ad Account]  (USD, 1 tarjeta dedicada limpia)
    |-- [1 Página FB + 1 IG]  (calentar $1-10/día ~1 semana)
    |-- [1 Dataset/Pixel + CAPI]  (postback ClickBank, validado con compra $1)
    |-- [1 Dominio verificado]  (truhealthdaily.com · bridge informativa)
    `-- [1 campaña en PAUSED]  (Sales→Purchase, 1 CBO broad USA, 3-5 ads)
```

### Qué NO hacer todavía

- **NO** montar 10 ad accounts ni múltiples Business Portfolios. 1 limpio y aislado.
- **NO** antidetect browser ni proxies. Innecesario y riesgoso con 1 BM `[FUENTE REPO]`.
- **NO** comprar cuentas "aged". Alto riesgo de ban por fingerprint `[FUENTE REPO]`.
- **NO** perseguir agency accounts / exemption tags. Umbral ~$3M/año, a años de distancia `[FUENTE REPO]`.
- **NO** cloaking, jamás. Ni siquiera el caso de 154% ROI lo justifica.
- **NO** direct linking. Siempre bridge propia.
- **NO** probar varias ofertas a la vez. El capital alcanza para 1 test serio bien hecho `[FUENTE REPO]`.

### Checklist de arranque

```checklist
[ ] Perfil personal FB sano: foto, antigüedad, amigos, actividad normal
[ ] 2FA activado en el perfil personal
[ ] IP/dispositivo estable definido para administrar siempre desde ahí
[ ] 1 Business Portfolio creado y aislado de OpenClaw
[ ] 1 Página FB + 1 cuenta IG vinculada, branding consistente
[ ] Warm-up de la página: engagement $1-10/día durante ~1 semana
[ ] Dominio truhealthdaily.com comprado
[ ] Dominio verificado en el Business Portfolio (DNS/meta-tag)
[ ] Bridge page lista: tono informativo, mobile-first, carga < 3s
[ ] 1 Dataset/Pixel creado, eventos PageView + ViewContent + InitiateCheckout
[ ] CAPI conectado: postback ClickBank -> Meta, fbclid en el HopLink
[ ] Tracking validado con compra real de $1, Purchase visible en Events Manager
[ ] 1 Ad Account creado (USD), 1 tarjeta limpia y dedicada agregada
[ ] Roles: admin persona real con 2FA; System User solo si hay API
[ ] Disclaimer de salud listo en el copy de cada ad
[ ] 1 campaña Sales->Purchase en PAUSED: 1 CBO broad USA, 3-5 ads, ángulos distintos
[ ] Kill budget escrito antes de prender ($500-800 primer test)
[ ] OK explícito del equipo antes de pasar la campaña a ACTIVE
```

---

*Documento interno. Las marcas `[FUENTE REPO]` salen de los videos/foros investigados o de skills internos, con su cita; `[BEST-PRACTICE]` es estándar Meta Business 2026 / industria; `[CRITERIO]` es juicio operativo de este documento donde la fuente no da un número exacto (señalado, no inventado). Fuentes principales: `01-ejecucion-2026/clickbank-2026-research/SINTESIS-VIDEOS-FOROS-2026.md`, `00-viabilidad/research-fuentes/09-errores-foros-clickbank-meta.md`, `knowledge/skills/affiliate-funnel-structure.md`, transcripciones N2-Aq0TfaAdSmY (Jordan/Robin Bouwman), N2-_-OnRxjaWMM y N2-txOcKycyAgc (Thomas Owen), N3-SH71IXrbp-A (Param). GAP reconocido: no existe aún un SOP de infra anti-ban para montar 1 BM limpio sin acceso a agency accounts; esta guía es el primer paso.*
