# SOP 01 · Selección Semanal de Oferta ClickBank

**Owner:** Romi
**Frecuencia:** Semanal (recomendado: viernes para tener oferta lista lunes)
**Tiempo estimado:** 90 min
**Inputs requeridos:** acceso ClickBank Marketplace, Claude Cowork, SpyHero
**Output:** 1 oferta a TEST, 2 a backlog, 2 archive · folder en `02-offers/[oferta-XX]/` con brief inicial
**Skill relacionado:** `knowledge/skills/affiliate-clickbank.md`

---

## Pasos

### 1. Login y filtros (10 min)
- Login a clickbank.com/marketplace
- Filtros:
  - Category: **Health & Fitness** > **Nutritional** (o categoría de turno)
  - Language: **Spanish**
  - Sort: **Gravity descendente**
- Top 20 visibles → exportar a CSV (botón export o copy manual)

### 2. Análisis preliminar con Claude Cowork (20 min)
- Abrir prompt 01 en `06-ops/prompts/prompt-01-research-oferta.md`
- Pegar lista de 20 ofertas con sus métricas
- Cowork devuelve tabla rankeada por fit con nuestro perfil

### 3. Top 5 finalistas · revisión profunda (40 min)
Para cada uno de los 5 ofertas top:
- Click en producto → ver tools page del vendor
- Ver VSL completo (no skipear — si te aburre a ti, aburre al cliente)
- Anotar:
  - Hooks que usa el vendor
  - Angles principales del VSL
  - Garantías y precios (entrada + upsells)
  - Categoría dolor (articulaciones / sueño / peso / energía / próstata / menopausia / etc.)
  - Restricciones declaradas en tools page

### 4. Espionaje de competencia (15 min)
- SpyHero: buscar dominio del vendor + ofertas similares
- Ver: ¿qué ads están corriendo? ¿qué hooks dominan? ¿está saturado?
- Meta Ads Library complementario (gratis): buscar keywords del nicho en español, filtrar país USA

### 5. Math de economics (10 min)
Para cada finalista:
```
AOV × Comisión % = Comisión por venta
Comisión por venta × Conv rate estimada (1-2%) = Revenue por 100 clicks
Revenue por 100 clicks / 100 = Revenue per click (RPC)
RPC × 0.7 = CPA breakeven (target 70% margen sobre RPC)

Ejemplo:
$197 AOV × 75% comisión = $147.75 / venta
$147.75 × 1.5% conv = $2.21 RPC
$2.21 × 0.7 = $1.55 CPA breakeven
→ Si Meta nos cobra > $1.55/click, no es viable
```

### 6. Decisión (5 min)
- **1 oferta TEST** — la mejor combinación de fit + economics
- **2 ofertas BACKLOG** — prometedoras pero esperan a que TEST termine
- **2 ofertas ARCHIVE** — descartadas con razón documentada

### 7. Crear folder en `/02-offers/[oferta-XX]/` (10 min)
Estructura:
```
02-offers/oferta-001-[nombre-corto]/
├── brief.md          (mensajería + angles iniciales)
├── research.md       (vendor + competencia)
├── economics.md      (math AOV × comisión × ROAS)
└── compliance.md     (claims permitidos/prohibidos)
```

Templates en `06-ops/templates/oferta-template/` (PENDIENTE crear).

### 8. Notificar al equipo
- Slack #ofertas: "Nueva oferta TEST seleccionada esta semana: [nombre]. Brief en `02-offers/[oferta-XX]/`. Brief creativo a Dali sale mañana."
- Tag a Cris para que prepare slot técnico (SOP 04 inicia post brief)

---

## Checklist pre-cierre

- [ ] CSV de 20 ofertas guardado en `01-niches/active/[YYYY-WW]-clickbank-research.csv`
- [ ] Top 5 con análisis completo
- [ ] Decisión documentada (TEST / BACKLOG / ARCHIVE x cada una)
- [ ] Folder oferta TEST creado con 4 archivos
- [ ] Brief inicial en `brief.md` (mínimo: oferta + angle hipótesis + audiencia)
- [ ] Slack #ofertas notificado

---

## Errores frecuentes (no cometer)

1. Sortear solo por gravity sin chequear AOV / comisión
2. Skipear el VSL (si tú no lo terminas, tu tráfico tampoco)
3. Ignorar restricciones en tools page (te corta comisión retroactiva)
4. No hacer la math de economics (pierdes plata escalando algo no viable)
5. Elegir oferta solo porque "se ve potente" sin validar números

---

## Historial de versiones

- **v0.1 · 2026-04-28** — estructura inicial creada (Cris setup)
- **v1.0** — pendiente · primera ejecución por Romi con video Loom
