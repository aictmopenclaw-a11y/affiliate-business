# SOP 05 · Reporte Diario de KPIs (Automatizado)

**Owner:** Cris
**Frecuencia:** Diario · 9AM (automatizado vía Claude Code routine)
**Tiempo:** 5 min revisión humana
**Inputs:** Meta Ads API, ClickBank API
**Output:** post auto en Slack #datos + archivo en `05-data/daily/YYYY-MM-DD.md`

---

## Setup inicial (one-time · Cris)

### 1. Acceso a APIs
- **Meta Marketing API:** crear app en developers.facebook.com, obtener access token con permisos `ads_read`
- **ClickBank API:** Account → API Keys → generar API key + Developer key
- Guardar en `.env` (NUNCA en código):
  ```
  META_ACCESS_TOKEN=xxx
  META_AD_ACCOUNT_ID=act_xxx
  CLICKBANK_API_KEY=xxx
  CLICKBANK_DEVELOPER_KEY=xxx
  SLACK_WEBHOOK_URL=https://hooks.slack.com/...
  ```

### 2. Script base
Crear `04-tech/scripts/daily-report.py`:
```python
# Pseudo-código — implementación completa cuando Cris lo monte
import os
from datetime import datetime, timedelta

def fetch_meta_data(account_id, date):
    # GET /v19.0/{account_id}/insights
    # campos: spend, impressions, clicks, cpc, ctr, cpm, conversions
    pass

def fetch_clickbank_data(date):
    # GET /1.3/orders/list?startDate=X&endDate=X
    pass

def generate_markdown_report(meta_data, cb_data):
    # estructura abajo
    pass

def post_to_slack(report, webhook):
    # POST con summary
    pass

if __name__ == "__main__":
    yesterday = datetime.now() - timedelta(days=1)
    meta = fetch_meta_data(os.getenv("META_AD_ACCOUNT_ID"), yesterday)
    cb = fetch_clickbank_data(yesterday)
    report = generate_markdown_report(meta, cb)
    
    # Guardar archivo
    fname = f"05-data/daily/{yesterday.strftime('%Y-%m-%d')}.md"
    with open(fname, "w") as f:
        f.write(report)
    
    # Post a Slack
    post_to_slack(report, os.getenv("SLACK_WEBHOOK_URL"))
```

### 3. Routine en Claude Code
- `~/.claude/commands/affiliate-daily-report.md` o setup vía cron
- Ejecutar diario 8:55 AM
- Si falla 2x seguidas → alerta urgente Slack + email Cris

---

## Plantilla del reporte diario

```markdown
# Reporte Diario · YYYY-MM-DD

## Resumen ejecutivo
- 💰 Spend total: $XXX USD
- 📊 Conversiones: X
- 🎯 ROAS: X.XX
- 📈 vs día anterior: +/- X%
- ⚠️ Flags: [si hay anomalías]

## Por campaña
| Campaña | Spend | Conv | CPA | ROAS | Status |
|---|---|---|---|---|---|
| oferta-001-angle1 | $25 | 3 | $8.33 | 1.8 | ✅ healthy |
| oferta-001-angle2 | $25 | 1 | $25.00 | 0.6 | 🔴 kill candidate |

## Por creativo (top 5)
| Creativo | Impressions | CTR | CPA | Frequency |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## ClickBank
- Vendidos: X
- Comisión total: $X USD
- Refunds: X (-$X USD)
- Net: $X USD

## Acción sugerida
- [Auto-detectada por script: scale X · kill Y · investigar Z]
```

---

## Workflow diario (humano)

### 9:00 AM
- Routine corre, post aparece en Slack #datos
- Cris recibe ping push

### 9:05-9:10 AM
- Revisión 5 min:
  - ¿Métricas OK o hay anomalía?
  - ¿Algún ROAS >2.5x → notificar Dali para más variantes?
  - ¿Algún CPA 2x baseline → notificar Romi?
  - ¿Frequency > 3 en algún creativo → trigger SOP 09 (refresh)?

### 9:10 AM
- Marcar en Slack: ✅ revisado / ⚠️ requiere discusión

---

## Triggers automáticos del script

- **CPA > 2x baseline durante 24h** → tag urgente a Romi
- **ROAS > 2.5x sostenido 48h** → tag a Dali (más variantes)
- **Frequency > 3 en creativo** → tag a Dali (SOP 09 refresh)
- **Spend $0 en cuenta cuando debería gastar** → tag urgente Cris (problema de pago / pixel / bid)
- **Meta warning recibido** → tag urgente Cris

---

## Checklist setup inicial

- [ ] Meta API access token obtenido
- [ ] ClickBank API keys obtenidas
- [ ] `.env` configurado con todas las vars
- [ ] Script `daily-report.py` testeado manualmente
- [ ] Routine programada Claude Code (8:55 AM)
- [ ] Webhook Slack #datos configurado
- [ ] Test de end-to-end: routine genera reporte → Slack notifica
- [ ] Backup: si script falla, alerta urgente

---

## Historial

- **v0.1 · 2026-04-28** — estructura inicial
- **v1.0** — pendiente · cuando Cris implemente script real
