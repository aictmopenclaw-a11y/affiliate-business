# SOP 04 · Setup de Funnel Completo (Oferta → Live Ads)

**Owner:** Cris
**Frecuencia:** Por oferta nueva (después de SOP 02)
**Tiempo:** 4-6h
**Inputs:** brief de Romi (SOP 02), creativos de Dali (SOP 07)
**Output:** funnel live con $50/día + alarma Slack
**Skills:** `affiliate-funnel-structure.md`, `affiliate-clickbank.md`

---

## Pasos

### 1. HopLink ClickBank (15 min)
- Login ClickBank → Account → Promote
- Buscar oferta → "Create HopLink"
- Definir tracking ID base (ej. `cris_w17_oferta001`)
- Copiar HopLink y guardar en `02-offers/[oferta-XX]/tracking.md`

### 2. Landing en Landerlab (60-90 min)
- Login Landerlab
- Clonar template del nicho (advertorial, quiz, pre-VSL según brief)
- Adaptar:
  - Hook headline al brief
  - Story arc al angle
  - Beneficios específicos del producto
  - CTA al HopLink (con tracking ID)
- Imágenes WebP optimizadas (< 300 KB cada una)
- Footer con disclaimers obligatorios (ver `affiliate-compliance-nutra.md`)

### 3. Tracking · pixels (30 min)
- Meta Pixel del Business Manager
- GA4 property + measurement ID
- ClickBank tracking en HopLink
- Eventos custom: ViewContent (50% scroll), InitiateCheckout (CTA click)

### 4. Test pixel (15 min)
- Chrome extension: **Meta Pixel Helper**
- Cargar landing → debe mostrar pixel ID + eventos
- Click CTA → InitiateCheckout debe disparar
- Si no: revisar JS y reintentar antes de seguir

### 5. Dominio + Cloudflare (30 min)
- Registrar dominio en Namecheap o Cloudflare Registrar (~$10/año)
- Apuntar DNS a Landerlab (A record o CNAME según docs)
- Activar Cloudflare proxy + SSL Universal
- Test HTTPS funciona y redirige HTTP → HTTPS

### 6. QA con checklist (30 min)
Crear `04-tech/landings/[campaña-XX]/test-checklist.md` y completar:
- [ ] Landing carga < 3s en mobile
- [ ] Hook headline legible sin zoom
- [ ] CTA visible above the fold
- [ ] Pixel Meta validado
- [ ] GA4 disparando page_view
- [ ] HopLink correcto (test click → llega al VSL del vendor)
- [ ] Disclaimers en footer (todos los obligatorios)
- [ ] Política privacidad + términos accesibles
- [ ] Test en iPhone real
- [ ] Test en Android real
- [ ] Test con bloqueador de ads activo

### 7. Cuenta publicitaria Meta (30 min)
- Crear nueva cuenta publicitaria dedicada en Business Manager
- Agregar 2 métodos de pago (tarjeta SpA + Revolut backup)
- Setup conversion event: Purchase (vía CAPI desde postback ClickBank)
- Si CAPI aún no configurado, usar Initiate Checkout como proxy temporal

### 8. Subir creativos finales de Dali (20 min)
- Crear campaign Sales con Bidcap (CPM máximo razonable según economics)
- Audience: Advantage+ por defecto (Hispano-US, edad según brief)
- Budget: $50/día inicial
- Programar 3-5 creativos diferentes en un solo ad set (test inicial)
- Naming: `[oferta]_[angle]_[formato]_v[XX]`

### 9. Live + alarma Slack (10 min)
- Activar campaña
- Configurar alarma en Slack #datos:
  - Si CPA > $X (definir threshold según economics) → notificar
  - Si frequency > 3 → notificar
  - Si cuenta recibe warning Meta → notificar inmediato

### 10. Postback ClickBank → Meta CAPI (PENDIENTE — setup avanzado)
- Configurar postback URL custom en ClickBank
- Servidor backend (Vercel / Cloudflare Workers)
- Hash email + match a click_id
- POST a Meta CAPI con event="Purchase"
- **Documentar en `04-tech/scripts/capi-postback-setup.md`**

---

## Checklist pre-cierre

- [ ] HopLink generado y guardado
- [ ] Landing en Landerlab live + adaptada al brief
- [ ] Pixel Meta validado con Helper
- [ ] GA4 disparando eventos
- [ ] Dominio + Cloudflare + SSL OK
- [ ] QA completo en mobile
- [ ] Cuenta publicitaria con 2 métodos de pago
- [ ] Creativos cargados con naming convention
- [ ] Campaign live $50/día
- [ ] Alarmas Slack configuradas
- [ ] Notificación a Romi que está live

---

## Errores frecuentes

1. Lanzar sin validar pixel → todo el spend no entra a optimización
2. Olvidar disclaimers footer → disapproval Meta
3. Una sola tarjeta de pago → si falla, campaña muere
4. Naming inconsistente → no puedes analizar después
5. Test en desktop solo → 90% del tráfico es mobile

---

## Historial

- **v0.1 · 2026-04-28** — estructura inicial
