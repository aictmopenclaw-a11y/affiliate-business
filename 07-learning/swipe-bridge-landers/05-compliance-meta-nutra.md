# Compliance Meta para nutra/salud · guía accionable

> Lo que decide si la cuenta sobrevive. Mezcla texto oficial de políticas de Meta, reglas de la FTC y consenso de operadores 2026. Para afiliados de suplementos/salud corriendo bridge pages en Meta.

```kpi
value: 159M
label: Ads removidos por Meta en 2025
---
value: 10.9M
label: Cuentas dadas de baja (scam)
delta: -riesgo si copias a esos
---
value: ene-2025
label: Cuentas H&W ya no optimizan a compra
```

## 1. Claims: la línea entre suplemento y medicamento

El criterio no es el producto, es el CLAIM. Apenas un claim nombra una enfermedad o promete un resultado terapéutico, Meta lo trata como medicamento y lo rechaza.

Texto oficial de Meta: los anuncios no pueden afirmar ni implicar que el producto puede tratar, curar, prevenir, mitigar o diagnosticar una enfermedad o condición médica.

| Prohibido (claim de enfermedad) | Permitido (estructura-función) |
|---|---|
| {r}Cura la artritis | {g}Apoya la comodidad articular |
| {r}Trata la ansiedad | {g}Promueve una sensación de calma |
| {r}Elimina el colesterol malo | {g}Ayuda a mantener niveles saludables |
| {r}Combate la fatiga crónica | {g}Contribuye a niveles normales de energía |
| {r}Para personas con diabetes | {g}Apoya el bienestar metabólico general |
| {r}Reduce el azúcar 40% | {g}Ingredientes reconocidos por la tradición |

Verbos prohibidos: cura, trata, previene, elimina, revierte, controla. Frases prohibidas: "clínicamente probado" sin datos, "garantizado", "recomendado por médicos" sin evidencia, "milagroso", "alivio instantáneo".

## 2. Atributos personales (la regla más violada)

Texto oficial: los anuncios no pueden contener contenido que afirme o implique atributos personales, incluida la salud física o mental de la persona.

En la práctica, el copy NUNCA puede referirse a la condición del usuario, ni de forma neutra:
- {r}"Si tienes diabetes..." = rechazo directo
- {r}"Para personas con presión alta..." = rechazo directo
- {r}"Para los que enfrentan picos de azúcar" = flagged
- {g}Se habla del producto y sus ingredientes, no del estado del usuario.

Operadores reportan que desde inicio de 2026 Meta detecta el framing indirecto en segunda persona, con la tasa de rechazo subiendo fuerte en esta categoría.

## 3. Before/after: prohibido explícito

Texto oficial prohíbe: comparaciones lado a lado de transformación para pérdida de peso, primeros planos pellizcando grasa, y generar autopercepción negativa. La IA de Meta también marca "transformaciones implícitas" (producto junto a persona fit, testimonial en video de alguien que se ve saludable).

## 4. Cloaking: ban de cuenta + dominio + demanda

Mostrar a Meta una página y al usuario otra. Cómo lo detecta Meta: IPs residenciales de revisión, fingerprinting, comparación por IA de lo que ve el bot vs el usuario, el propio Pixel reportando la URL real, y correlación cross-cuenta (liga BMs, IPs, Pixels y métodos de pago).

```funnel
Ad removido | 5
Cuenta de ads deshabilitada | 4
Business Manager baneado | 3
Dominio baneado (auto-rechazo futuro) | 2
Ban permanente + demanda legal | 1
```

Implicación crítica: como Meta traza redes completas, un ban contamina los BMs nuevos creados desde la misma infraestructura (misma IP, Pixel, tarjeta, dominio). En 2026 Meta presentó demandas legales por cloaking. **No vale la pena. Nunca.**

## 5. Coherencia ad-lander (continuidad editorial)

Meta revisa el ad y la landing como una sola experiencia. Errores que rechazan cuentas técnicamente correctas:
- El claim escala entre ad y página (ad: "apoya la energía"; página: "elimina la fatiga"): rechazo.
- El producto del ad no es el de la página (bait-and-switch).
- Oferta del ad distinta a la de la página (o expirada).
- Ad educativo que salta a hard-sell abrupto en la página.

Por esto los advertoriales (página editorial) convierten mejor en frío: mantienen la narrativa del ad a la compra sin salto abrupto.

## 6. Checklist obligatorio de la bridge page

Sin estos elementos, la cuenta se cae (lento o rápido):

- [ ] **Privacy policy** linkada en el footer (su ausencia es trigger de ban).
- [ ] **Terms of service** linkados.
- [ ] **Contacto** visible (email, dirección o teléfono).
- [ ] **Política de reembolso** accesible.
- [ ] **Disclaimer FDA** (mercado US), prominente, no en letra chica: "These statements have not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease."
- [ ] **Disclaimer de resultados** en cualquier testimonial ("results may vary").
- [ ] **Disclosure de afiliado** (FTC, obligatorio) visible ANTES del fold: "Advertisement" / "Sponsored". La tag nativa de Meta no basta.
- [ ] Todos los links y botones funcionan, mobile-optimizada.
- [ ] El dominio visible del ad coincide con el destino real.
- [ ] Sin pop-up que bloquee el contenido antes de leer.

## 7. Urgencia y escasez: solo si es real

- {r}Countdown que se reinicia o nunca expira: violación inmediata (Meta lo detecta).
- {r}"Stock limitado" / "solo 3 disponibles" sin inventario real.
- {g}Urgencia basada en la situación del usuario, oferta con fecha de expiración real.

## 8. Testimonios

- {g}Permitido: experiencia en primera persona ("duermo mejor desde la 2da semana"), timeframes realistas, certificaciones de terceros (NSF, GMP), citar estudios de ingredientes.
- {r}Prohibido: testimonios con diagnóstico o cura, resultados atípicos sin disclosure, imágenes de celebridades sin permiso (Meta usa reconocimiento facial), reviews falsos.

## 9. LegitScript: ¿obligatorio?

```compare
Suplementos wellness general (top)
Requiere LegitScript | No | 0
Bloqueador real | Claims y coherencia | 100

CBD / farmacia / adicciones / telemedicina
Requiere LegitScript | Sí, obligatorio | 100
Costo | $975 setup + $1-2K/año | 70
```

Para suplementos sin CBD, LegitScript NO es el bloqueador. El bloqueador real son los claims del ad y la coherencia ad-lander. La certificación, si aplica, la tiene el vendor, no el afiliado.

## 10. Cambio crítico (enero 2025): optimización H&W

Meta restringió a las marcas de salud y bienestar de optimizar campañas hacia eventos de fondo de funnel (compra, add-to-cart). Ahora deben optimizar a **Landing Page Views** o **Engagement**, salvo aprobación explícita. La cuenta se clasifica como H&W automáticamente si la URL menciona condiciones médicas, el Pixel captura eventos en páginas de condiciones, o el historial cae en salud. Afecta la estructura técnica de la campaña, no solo el copy.

## Las 10 reglas no negociables

1. Solo +18 para ads de suplementos y pérdida de peso.
2. Cero claims de cura/tratamiento de enfermedad, ni indirectos.
3. Before/after de pérdida de peso: prohibido por política literal.
4. El copy no puede referirse a ninguna condición de salud del usuario.
5. Cloaking lleva a ban de BM + dominio + demanda. Nunca.
6. Landing coherente con el ad en producto, claim, tono y oferta.
7. Privacy policy + contacto + reembolso en la bridge, sí o sí.
8. Disclaimer FDA en la landing (mercado US).
9. Disclosure de afiliado visible antes del fold (FTC), no solo la tag de Meta.
10. Cuentas H&W no optimizan a compra desde enero 2025: usar Landing Page Views.

---

*Fuentes: políticas oficiales de Meta (transparency.meta.com: health-wellness, drugs-pharmaceuticals, fraud-scams), FTC (disclosures para afiliados), LegitScript, y operadores especializados 2026 (Forge Digital, AuditSocials, Accelerated Digital Media, Jon Loomer). Verificar políticas en la fuente antes de lanzar: cambian seguido.*
