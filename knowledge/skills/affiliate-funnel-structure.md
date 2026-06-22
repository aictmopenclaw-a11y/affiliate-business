# Skill · Estructura de Funnel Affiliate

> **Cuándo cargar este skill:** antes de armar landing intermedia, antes de configurar pixels, cuando se debate el tipo de pre-lander.
> **Owner conceptual:** Cris (técnico) + Romi (mensajería)
> **Última actualización:** 2026-04-28

---

## El funnel completo

```
[Ad Meta] → [Nuestra landing intermedia] → [VSL del vendor] → [Checkout vendor] → [Comisión]
```

**Lo crítico:** la landing intermedia es **nuestra única ventaja competitiva**. El VSL y el checkout son del vendor (todos los afiliados los usan iguales). La landing intermedia es donde:
1. Pre-vendemos al usuario
2. Filtramos tráfico (los que no califican rebotan antes del VSL)
3. Capturamos data nuestra (pixel, GA, eventos)
4. Construimos brand percibido (el usuario cree que somos la marca)

---

## 4 tipos de landing intermedia

### 1. Advertorial (texto largo formato editorial)
**Cuándo usar:** ofertas nutra/health donde la "historia" del producto es clave. Convierte en audiencias 45+.

**Estructura:**
- Hook headline (problema-doloroso)
- Sub-hook (validación: "miles de mujeres en USA están descubriendo...")
- Story de un personaje arquetipo (cuento)
- Reveal del producto/método
- Beneficios específicos
- CTA al VSL del vendor (botón claro: "Ver el video completo")

**Pro:** alta conversión en frío
**Contra:** caro de producir, difícil de escalar a multiple variantes

### 2. Quiz (preguntas → resultado personalizado)
**Cuándo usar:** ofertas que aplican a sub-segmentos diferentes (ej. cremas para "tu tipo de piel"). Convierte en audiencias 25-45.

**Estructura:**
- Pregunta inicial enganchadora
- 4-7 preguntas de calificación
- "Procesando tu resultado..." (dramático)
- Resultado personalizado + reveal del producto
- CTA al VSL

**Pro:** alta engagement, captura email opcional, los que terminan están altamente calificados
**Contra:** complejo de armar bien, puede sentirse "manipulador" si está mal hecho

### 3. Pre-VSL (video corto introductorio)
**Cuándo usar:** cuando el VSL del vendor es muy largo (15+ min) y necesitas pre-calificar tráfico.

**Estructura:**
- Video corto 60-90 seg
- Tu propio host hablando (HeyGen avatar funciona bien)
- Setup del problema + "lo que vas a ver te va a sorprender"
- Botón → VSL del vendor

**Pro:** filtra a los que no quieren ver video largo
**Contra:** menor variabilidad creativa, tu host puede no convertir tan bien como el del vendor

### 4. Listicle / Comparison (top 3 productos de la categoría)
**Cuándo usar:** nichos saturados donde "comparación" es un keyword search potente.

**Estructura:**
- Headline: "Los 3 mejores [producto] del 2026"
- Pseudo-revisión objetiva (con escala arbitraria)
- Producto del vendor en posición #1 (siempre)
- Botón → VSL

**Pro:** funciona muy bien con Google Ads search
**Contra:** menos efectivo en Meta Ads (cold traffic), más riesgo legal (puede parecer engañoso si está mal hecho)

---

## Recomendación inicial

**Empezar con advertorial** para nuestro perfil (mujeres 25-45 hispano-US salud/wellness).

**Por qué:**
- Más probado en nicho nutra
- Permite testear muchos hooks/angles distintos sobre la misma estructura
- Más fácil de iterar
- SpyHero muestra que es el formato dominante en hispano-US

---

## Anatomía detallada de una landing advertorial

### Above the fold
- **Logo dummy** o headline-only (no marca real, "marca" se construye en la mente)
- **Headline (H1)** — 6-12 palabras, hook directo
  - Bueno: "El truco de mañana que las mujeres en Miami están usando"
  - Malo: "Producto X cambiará tu vida"
- **Sub-hook** — validación social o problema
- **Imagen hero** — persona arquetipo (no producto)

### Mitad superior
- **Story arc** — un personaje arquetipo del target tiene el problema
  - 2-3 párrafos de identificación
  - 1 momento de "¿y si hubiera otra forma?"
- **Reveal** — descubrió este método/producto
- **Pseudo-mecánica** — ciencia simplificada (sin claims dudosos)

### Mitad inferior
- **Beneficios concretos** — 3-5 bullets, específicos
- **Validación** — "miles ya lo están usando", testimonio simple si aplicable
- **Garantía** — "60 días sin riesgo" (la del vendor)
- **CTA primario** — "Ver el video completo" (NO "comprar ahora")

### Footer
- **Disclaimers obligatorios** (claims salud, FTC, resultados individuales)
- Contacto (email genérico, NO datos reales)
- Política privacidad (templates legales online)

---

## Tracking · qué pixels y eventos disparar

### Meta Pixel
- **PageView** (auto, en `<head>`)
- **ViewContent** custom event al 50% scroll (señal de engagement)
- **InitiateCheckout** custom event al click en CTA (botón a VSL)
- **Purchase** vía CAPI/postback (NO en la landing — disparado desde callback ClickBank)

### Google Analytics 4
- Page view default
- Event "scroll_50" / "scroll_75" / "scroll_100"
- Event "cta_click" en cada CTA

### ClickBank tracking
- HopLink con `tid=` único por variante (ver `affiliate-clickbank.md`)
- Postback URL configurada para enviar conversiones a Meta CAPI

### Postback Meta CAPI (crítico para ROAS)
ClickBank confirma venta → ClickBank envía postback → tu servidor → Meta CAPI Purchase event con email hasheado del comprador.

**Sin esto:** Meta no aprende qué clicks convirtieron y la optimización Advantage+ se vuelve ciega.

**Setup:**
- Servidor backend (puede ser serverless: Cloudflare Workers / Vercel)
- ClickBank → postback URL custom
- Hash email + match al click ID
- POST a Meta CAPI con event_name="Purchase", value, currency

Cris arma esto en SOP 04 (setup funnel).

---

## Tiempos de carga · benchmark obligatorio

| Métrica | Target | Crítico |
|---|---|---|
| LCP (Largest Contentful Paint) | < 2.5s | < 4s |
| FID (First Input Delay) | < 100ms | < 300ms |
| CLS (Cumulative Layout Shift) | < 0.1 | < 0.25 |
| Total page weight | < 500 KB | < 1.5 MB |

**Razón:** mobile en USA con datos limitados. Si la landing tarda 6+ seg, el usuario rebota antes de leer el headline.

**Cómo hackearlo:**
- Imágenes WebP (no PNG/JPG)
- Lazy load para imágenes below the fold
- CSS inline crítico (no external)
- JavaScript mínimo (solo tracking)
- CDN obligatorio (Cloudflare gratis es suficiente)

---

## Mobile first · 90% del tráfico Meta es mobile

### Reglas inviolables
- **CTAs grandes** (mínimo 48px de alto, ancho completo)
- **Headline legible sin zoom** (font-size mínimo 18px en mobile)
- **Sin pop-ups** (Meta los penaliza)
- **Botón sticky** opcional (CTA flotante al scroll)

### QA antes de live
- Test en iPhone 13/14 (resolución más común)
- Test en Android tipo Samsung A series (presupuesto medio)
- Test con 3G simulado en Chrome DevTools
- Test con bloqueador de ads (algunos usuarios lo tienen)

---

## Compliance · disclaimers obligatorios

### En footer (siempre)
- "Resultados individuales pueden variar"
- "Estas afirmaciones no han sido evaluadas por la FDA" (si nicho salud)
- "Consulta a tu médico antes de comenzar cualquier suplemento"
- Política de privacidad y términos
- "Affiliate disclosure" — "esta página puede contener enlaces de afiliados"

### En above the fold (a veces)
- Si haces claims agresivos, considera disclaimer visible (FTC lo exige en algunos estados)

---

## A/B testing · qué probar

### Niveles 1 (alto impacto)
- **Hook headline** (el de mayor impacto)
- **Imagen hero**
- **Copy del CTA** ("Ver video" vs "Continuar" vs "Descubrir")

### Nivel 2 (medio impacto)
- Color del CTA
- Orden de bullets de beneficios
- Story arc (personaje masculino vs femenino)

### Nivel 3 (bajo impacto · no priorizar al inicio)
- Font choice
- Background color
- Tamaño de imágenes

**Principio:** test 1 variable a la vez en Landerlab. Significancia estadística mínima 200 conversiones por variante (no rates aleatorios con n=20).

---

## Anti-patterns que matan funnels

1. **Logo de marca real arriba** — destruye la sensación de descubrimiento
2. **Pop-up "antes de irte"** — Meta lo penaliza con disapproval
3. **CTAs múltiples** — uno solo, claro
4. **Botón "comprar ahora"** en landing intermedia — el flow es comprar en el VSL del vendor, no en nuestra landing
5. **Botón "saltar al video"** muy arriba — perdemos pre-venta
6. **Demasiados beneficios genéricos** — 3-5 específicos > 15 genéricos
7. **Texto en imágenes** (no escaneable, no SEO)
8. **Auto-play video con audio** — Meta lo flagea
9. **Pretender ser news site** — disclaimer obligatorio "Advertorial" si simulas formato editorial

---

## Tools page del vendor · LEER COMPLETO

Antes de armar landing, leer la "tools page" del vendor (link en marketplace ClickBank). Contiene:
- Banners pre-aprobados
- Email swipes
- Restricciones (no brand bidding, no native, etc.)
- Compliance específico
- Voice-overs descargables (a veces)

**Si el vendor restringe X y tú lo haces igual, te corta comisiones retroactivas.**

---

## Workflow Cris · setup landing nueva (resumen SOP 04)

1. Recibe brief de Romi en Slack
2. Decide tipo de landing (advertorial / quiz / pre-VSL / listicle)
3. Clona template del nicho en Landerlab
4. Adapta: hook, story, beneficios, CTA según brief
5. Sube imágenes WebP optimizadas
6. Configura pixels: Meta + GA4 + ClickBank tracking
7. **Test pixel con Meta Pixel Helper**
8. Registra dominio nuevo (Namecheap / Cloudflare Registrar)
9. Cloudflare con SSL forzado
10. QA con checklist `04-tech/landings/[campaña]/test-checklist.md`
11. Live + alarma Slack si CPA > X

---

## Recursos

- **Landerlab docs:** landerlab.io/docs
- **Meta Pixel Helper:** chrome extension oficial
- **PageSpeed Insights:** pagespeed.web.dev
- **WebPageTest:** webpagetest.org (más detallado)
- **Compliance reference:** ftc.gov/business-guidance/advertising-marketing

---

*Este skill se actualiza cuando: cambia el algoritmo Meta y obliga a refactor de landings, descubrimos un patrón nuevo de conversión, o ClickBank cambia reglas de tracking.*
