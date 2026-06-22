#!/usr/bin/env python3
"""
ClickBank Offer Scorer · Affiliate Business
Aplica el framework de 11 criterios + math economics para Hispano-US.
Genera reporte markdown con veredicto go/no-go.

Uso:
    python3 .tools/offer-scorer.py                    # modo interactivo
    python3 .tools/offer-scorer.py --batch file.json  # modo batch
    python3 .tools/offer-scorer.py --template         # genera template JSON
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path("/Users/cristobaltejero/Projects/affiliate-business")
OFFERS_DIR = REPO_ROOT / "02-offers"

# ANSI colors for terminal
class C:
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    C = '\033[96m'
    W = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

# === 5 HARD FAILS (cualquiera = SKIP automático) ===
HARD_FAILS = [
    {
        "id": "disease_claims",
        "question": "¿El VSL hace claims de enfermedades específicas? (ej: 'cura diabetes', 'elimina cancer')",
        "fail_if": True,
        "explanation": "Disease claims = ban Meta + posible FTC enforcement. Auto-disqualify.",
    },
    {
        "id": "no_paid_traffic",
        "question": "¿La tools page del vendor PROHÍBE paid traffic (Meta, Google, etc.)?",
        "fail_if": True,
        "explanation": "Si prohíbe paid traffic, no podemos operar. Skip.",
    },
    {
        "id": "low_aov",
        "question": "¿Avg $/sale es MENOR a $50 USD?",
        "fail_if": True,
        "explanation": "AOV <$50 → margen muy apretado en Hispano-US (CPCs $1.20-2.50). No viable.",
    },
    {
        "id": "low_initial",
        "question": "¿Initial $/sale es MENOR a $25 USD? (lo que entra en la PRIMERA venta)",
        "fail_if": True,
        "explanation": "Initial bajo → no llegas a Customer Distribution Requirement (5 ventas) rápido. Cash inmovilizado.",
    },
    {
        "id": "high_refund",
        "question": "¿El refund rate es MAYOR a 25%? (verificable en Reddit/Skalers/grupos)",
        "fail_if": True,
        "explanation": "Refund >25% destruye economics. ClickBank cobra los refunds del afiliado.",
    },
]

# === 6 POSITIVE SIGNALS (>4 de 6 = TEST candidate) ===
POSITIVE_SIGNALS = [
    {
        "id": "vendor_age",
        "question": "¿El vendor tiene 3+ años en ClickBank? (verificable en marketplace)",
        "weight": 1,
    },
    {
        "id": "vsl_updated",
        "question": "¿El VSL muestra señales de actualización reciente? (testimonios recientes, A/B test visible)",
        "weight": 1,
    },
    {
        "id": "am_responsive",
        "question": "¿El affiliate manager respondió a tu email en <48h? (test antes de promover)",
        "weight": 1,
    },
    {
        "id": "capi_documented",
        "question": "¿La tools page documenta CAPI postback / Meta integration?",
        "weight": 1,
    },
    {
        "id": "recurring_rebill",
        "question": "¿Tiene Avg Rebill Total > $0? (subscription / continuity = LTV)",
        "weight": 1,
    },
    {
        "id": "bilingual_offer",
        "question": "¿Funciona en español Y inglés? (más flexibility geo)",
        "weight": 1,
    },
]

# === 4 MÉTRICAS NÚMERICAS ===
def collect_metrics(interactive=True, data=None):
    """Recolecta las 4 métricas numéricas críticas."""
    if interactive:
        print(f"\n{C.BOLD}{C.B}── MÉTRICAS NUMÉRICAS ──{C.END}\n")
        m = {}
        m["initial_per_sale"] = float(input(f"{C.C}Initial $/sale (USD): ${C.END}") or 0)
        m["avg_per_sale"] = float(input(f"{C.C}Avg $/sale (USD): ${C.END}") or 0)
        m["gravity"] = float(input(f"{C.C}Gravity score: {C.END}") or 0)
        m["avg_rebill"] = float(input(f"{C.C}Avg Rebill Total (USD, 0 si no aplica): ${C.END}") or 0)
        m["commission_pct"] = float(input(f"{C.C}Commission % (ej: 75 para 75%): {C.END}") or 0)
        m["estimated_conv_rate"] = float(input(f"{C.C}Estimated landing→sale conv rate % (ej: 1.5): {C.END}") or 1.5)
        return m
    else:
        return data["metrics"]

def evaluate_metrics(m):
    """Evalúa las 4 métricas y devuelve score + análisis."""
    results = []

    # Initial $/sale
    if m["initial_per_sale"] >= 25:
        results.append(("✓", f"Initial $/sale ${m['initial_per_sale']} >= $25", "ok"))
    else:
        results.append(("✗", f"Initial $/sale ${m['initial_per_sale']} < $25 (HARD FAIL)", "fail"))

    # Avg $/sale
    if m["avg_per_sale"] >= 80:
        results.append(("✓", f"Avg $/sale ${m['avg_per_sale']} >= $80", "ok"))
    elif m["avg_per_sale"] >= 50:
        results.append(("⚠", f"Avg $/sale ${m['avg_per_sale']} >= $50 (mínimo)", "warn"))
    else:
        results.append(("✗", f"Avg $/sale ${m['avg_per_sale']} < $50 (HARD FAIL)", "fail"))

    # Gravity
    g = m["gravity"]
    if 30 <= g <= 150:
        results.append(("✓", f"Gravity {g} en sweet spot 30-150", "ok"))
    elif g < 30:
        results.append(("⚠", f"Gravity {g} < 30 (sin tracción · riesgo)", "warn"))
    elif g > 200:
        results.append(("⚠", f"Gravity {g} > 200 (saturado · necesitas creativos muy diferenciados)", "warn"))
    else:
        results.append(("⚠", f"Gravity {g} alta (150-200 · competencia alta)", "warn"))

    # Avg Rebill (bonus)
    if m["avg_rebill"] > 0:
        results.append(("✓", f"Avg Rebill ${m['avg_rebill']} (LTV bonus)", "ok"))
    else:
        results.append(("○", f"Sin rebill (no es disqualifier)", "info"))

    return results

def calculate_economics(m):
    """Calcula CPA breakeven y compara con CPC industry Hispano-US."""
    net_per_sale = m["avg_per_sale"] * (m["commission_pct"] / 100)
    rpc = (net_per_sale * m["estimated_conv_rate"]) / 100  # revenue per click

    cpc_breakeven = rpc
    cpc_target_1_3x = rpc / 1.3
    cpc_target_2x = rpc / 2.0

    # Hispano-US CPC industry: $1.20-2.50 nutra
    cpc_industry_low = 1.20
    cpc_industry_high = 2.50

    if cpc_target_1_3x >= cpc_industry_high:
        verdict = ("✓✓", "VIABLE · margen amplio en Hispano-US", "ok")
    elif cpc_target_1_3x >= cpc_industry_low:
        verdict = ("✓", "VIABLE · margen ajustado en Hispano-US", "ok")
    elif cpc_breakeven >= cpc_industry_low:
        verdict = ("⚠", "BORDERLINE · break-even posible · escalado difícil", "warn")
    else:
        verdict = ("✗", "NO VIABLE · CPC breakeven debajo del industry promedio", "fail")

    return {
        "net_per_sale": net_per_sale,
        "rpc": rpc,
        "cpc_breakeven": cpc_breakeven,
        "cpc_target_1_3x": cpc_target_1_3x,
        "cpc_target_2x": cpc_target_2x,
        "cpc_industry_low": cpc_industry_low,
        "cpc_industry_high": cpc_industry_high,
        "verdict": verdict,
    }

def collect_hard_fails(interactive=True, data=None):
    """Recolecta respuestas a los 5 hard-fails."""
    if interactive:
        print(f"\n{C.BOLD}{C.R}── 5 HARD-FAILS (cualquiera = SKIP automático) ──{C.END}\n")
        responses = {}
        for hf in HARD_FAILS:
            print(f"\n{C.Y}{hf['question']}{C.END}")
            print(f"  {C.W}{hf['explanation']}{C.END}")
            ans = input(f"  {C.C}[s/n]: {C.END}").strip().lower()
            responses[hf["id"]] = (ans == "s")
        return responses
    else:
        return data["hard_fails"]

def evaluate_hard_fails(responses):
    """Evalúa hard-fails. Si alguno es True → auto-skip."""
    failed = []
    for hf in HARD_FAILS:
        if responses[hf["id"]] == hf["fail_if"]:
            failed.append((hf["id"], hf["question"], hf["explanation"]))
    return failed

def collect_positive_signals(interactive=True, data=None):
    """Recolecta respuestas a los 6 positive signals."""
    if interactive:
        print(f"\n{C.BOLD}{C.G}── 6 POSITIVE SIGNALS (>4 de 6 = TEST) ──{C.END}\n")
        responses = {}
        for ps in POSITIVE_SIGNALS:
            print(f"\n{C.G}{ps['question']}{C.END}")
            ans = input(f"  {C.C}[s/n]: {C.END}").strip().lower()
            responses[ps["id"]] = (ans == "s")
        return responses
    else:
        return data["positive_signals"]

def evaluate_positive_signals(responses):
    """Cuenta positive signals."""
    score = sum(1 for ps in POSITIVE_SIGNALS if responses[ps["id"]])
    return score, [(ps["id"], ps["question"], responses[ps["id"]]) for ps in POSITIVE_SIGNALS]

def collect_metadata(interactive=True, data=None):
    """Recolecta metadata de la oferta."""
    if interactive:
        print(f"\n{C.BOLD}{C.M}── METADATA OFERTA ──{C.END}\n")
        return {
            "name": input(f"{C.C}Nombre oferta: {C.END}").strip(),
            "vendor": input(f"{C.C}Vendor: {C.END}").strip(),
            "vsl_url": input(f"{C.C}URL VSL: {C.END}").strip(),
            "tools_page_url": input(f"{C.C}URL tools page: {C.END}").strip(),
            "category": input(f"{C.C}Categoría (dental/microbiome/audio-vsl/weight/etc): {C.END}").strip(),
            "language": input(f"{C.C}Idioma (es/en/bilingual): {C.END}").strip(),
            "geo": input(f"{C.C}Geos permitidos (us-hispano/us/latam/global): {C.END}").strip(),
        }
    else:
        return data["metadata"]

def make_verdict(hard_fails_count, positive_score, economics_verdict):
    """Veredicto final basado en los 3 factores."""
    if hard_fails_count > 0:
        return ("SKIP", f"{hard_fails_count} hard-fail(s) detectado(s) · auto-disqualify", "fail")

    if economics_verdict[2] == "fail":
        return ("SKIP", "Economics no viables · CPC breakeven debajo industry", "fail")

    if positive_score >= 5 and economics_verdict[2] == "ok":
        return ("TEST FUERTE", f"{positive_score}/6 positive signals + economics viables", "ok")

    if positive_score >= 4 and economics_verdict[2] in ("ok", "warn"):
        return ("TEST", f"{positive_score}/6 positive signals · candidato viable", "ok")

    if positive_score >= 3:
        return ("WAIT", f"{positive_score}/6 positive signals · backlog · explorar más antes de testear", "warn")

    return ("SKIP", f"{positive_score}/6 positive signals (insuficiente) + sin hard-fails", "warn")

def print_terminal_summary(metadata, hard_fails, metrics_eval, positive_score, economics, verdict):
    """Print resumen colored al terminal."""
    print(f"\n{'═' * 60}")
    print(f"{C.BOLD}{C.W}RESULTADO · {metadata['name']}{C.END}")
    print(f"{'═' * 60}\n")

    # Hard fails
    if hard_fails:
        print(f"{C.R}{C.BOLD}HARD-FAILS DETECTADOS ({len(hard_fails)}):{C.END}")
        for hf in hard_fails:
            print(f"  {C.R}✗ {hf[1]}{C.END}")
        print()
    else:
        print(f"{C.G}✓ Sin hard-fails{C.END}\n")

    # Metrics
    print(f"{C.BOLD}MÉTRICAS:{C.END}")
    for icon, msg, status in metrics_eval:
        color = {"ok": C.G, "warn": C.Y, "fail": C.R, "info": C.W}[status]
        print(f"  {color}{icon} {msg}{C.END}")
    print()

    # Economics
    e = economics
    print(f"{C.BOLD}ECONOMICS:{C.END}")
    print(f"  Net per sale: ${e['net_per_sale']:.2f}")
    print(f"  Revenue per click (RPC): ${e['rpc']:.2f}")
    print(f"  CPC breakeven (1.0x): ${e['cpc_breakeven']:.2f}")
    print(f"  CPC target 1.3x: ${e['cpc_target_1_3x']:.2f}")
    print(f"  CPC target 2.0x: ${e['cpc_target_2x']:.2f}")
    print(f"  CPC industry Hispano-US: ${e['cpc_industry_low']:.2f}-${e['cpc_industry_high']:.2f}")
    icon, msg, status = e["verdict"]
    color = {"ok": C.G, "warn": C.Y, "fail": C.R}[status]
    print(f"  {color}{icon} {msg}{C.END}\n")

    # Positive signals
    print(f"{C.BOLD}POSITIVE SIGNALS: {positive_score}/6{C.END}\n")

    # Verdict
    label, reason, status = verdict
    color = {"ok": C.G, "warn": C.Y, "fail": C.R}[status]
    print(f"{'═' * 60}")
    print(f"{color}{C.BOLD}VEREDICTO: {label}{C.END}")
    print(f"{color}{reason}{C.END}")
    print(f"{'═' * 60}\n")

def generate_markdown(metadata, m, hard_fail_responses, hard_fails, metrics_eval, positive_responses, positive_score, economics, verdict):
    """Genera reporte markdown."""
    label, reason, _ = verdict
    e = economics
    e_icon, e_msg, _ = e["verdict"]

    md = f"""# Oferta Scoring · {metadata['name']}

**Fecha evaluación:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Evaluador:** Cris (auto-scorer)
**Veredicto:** **{label}**

---

## Metadata

- **Vendor:** {metadata['vendor']}
- **VSL URL:** {metadata['vsl_url']}
- **Tools page:** {metadata['tools_page_url']}
- **Categoría:** {metadata['category']}
- **Idioma:** {metadata['language']}
- **Geos permitidos:** {metadata['geo']}

---

## Métricas numéricas

| Métrica | Valor | Status |
|---|---|---|
| Initial $/sale | ${m['initial_per_sale']:.2f} | {"✓" if m['initial_per_sale'] >= 25 else "✗ HARD FAIL"} |
| Avg $/sale | ${m['avg_per_sale']:.2f} | {"✓" if m['avg_per_sale'] >= 80 else "⚠" if m['avg_per_sale'] >= 50 else "✗ HARD FAIL"} |
| Gravity | {m['gravity']} | {"✓" if 30 <= m['gravity'] <= 150 else "⚠"} |
| Avg Rebill | ${m['avg_rebill']:.2f} | {"✓ bonus" if m['avg_rebill'] > 0 else "○ sin rebill"} |
| Commission % | {m['commission_pct']}% | — |
| Conv rate estimado | {m['estimated_conv_rate']}% | — |

---

## Hard-Fails (5 criterios)

"""
    if hard_fails:
        md += f"**❌ {len(hard_fails)} HARD-FAIL(S) DETECTADO(S) · AUTO-DISQUALIFY**\n\n"
        for hf in hard_fails:
            md += f"- ✗ **{hf[1]}**\n  - {hf[2]}\n"
    else:
        md += "**✓ Sin hard-fails**\n\n"
        for hf in HARD_FAILS:
            md += f"- ✓ {hf['question']}\n"

    md += f"""

---

## Economics · Math

```
Net per sale: ${e['net_per_sale']:.2f}
Revenue per click (RPC): ${e['rpc']:.2f}

CPC breakeven (1.0x ROAS): ${e['cpc_breakeven']:.2f}
CPC target 1.3x ROAS: ${e['cpc_target_1_3x']:.2f}
CPC target 2.0x ROAS (winner): ${e['cpc_target_2x']:.2f}

CPC industry Hispano-US nutra: ${e['cpc_industry_low']:.2f}-${e['cpc_industry_high']:.2f}
```

**Veredicto economics: {e_icon} {e_msg}**

---

## Positive Signals (6 criterios) · Score: {positive_score}/6

"""
    for ps in POSITIVE_SIGNALS:
        check = "✓" if positive_responses[ps["id"]] else "○"
        md += f"- {check} {ps['question']}\n"

    md += f"""

---

## Veredicto Final

# {label}

**Razón:** {reason}

### Próximos pasos

"""
    if label.startswith("TEST"):
        md += """1. Crear folder `02-offers/[oferta-XX]/` con esta evaluación
2. Romi ejecuta SOP 02 brief creativo (8 textos por nivel consciencia)
3. Cris setup técnico SOP 04 (landing + CAPI postback)
4. Dali producción 5-10 creativos diversificados
5. Live con $50/día budget mes 1 · stop-loss día 30
"""
    elif label == "WAIT":
        md += """1. Mover a `01-niches/backlog/` para re-evaluar mes 2
2. Investigar más profundo: contactar AM, leer reviews, validar refund rate
3. Si en 2 semanas confirma positive signals adicionales → TEST
"""
    else:  # SKIP
        md += """1. Mover a `01-niches/archive/` con razón documentada
2. Continuar buscando ofertas en próximo SOP 01 (semanal)
3. NO insistir con esta oferta
"""

    md += f"""

---

## Referencias

- Framework completo: `01-ejecucion-2026/clickbank-2026-research/02-offer-selection-framework.md`
- Maestro ClickBank 2026: `01-ejecucion-2026/clickbank-2026-research/MAESTRO-CLICKBANK-2026.md`
- Roadmap 90 días: `01-ejecucion-2026/04-ROADMAP-90-DIAS.md`

---

*Generado por offer-scorer.py · 11 criterios + math economics Hispano-US*
"""
    return md

def save_report(metadata, md):
    """Guarda reporte en 02-offers/[slug]/scoring-YYYY-MM-DD.md"""
    slug = metadata['name'].lower().replace(' ', '-').replace('_', '-')
    folder = OFFERS_DIR / f"oferta-{slug}"
    folder.mkdir(parents=True, exist_ok=True)
    filename = f"scoring-{datetime.now().strftime('%Y-%m-%d-%H%M')}.md"
    filepath = folder / filename
    filepath.write_text(md, encoding='utf-8')
    return filepath

def generate_template():
    """Genera template JSON para batch mode."""
    template = {
        "metadata": {
            "name": "Nombre de la oferta",
            "vendor": "Vendor name",
            "vsl_url": "https://...",
            "tools_page_url": "https://...",
            "category": "dental | microbiome | audio-vsl | weight-loss | other",
            "language": "es | en | bilingual",
            "geo": "us-hispano | us | latam | global",
        },
        "metrics": {
            "initial_per_sale": 47.0,
            "avg_per_sale": 147.0,
            "gravity": 65,
            "avg_rebill": 0.0,
            "commission_pct": 75.0,
            "estimated_conv_rate": 1.5,
        },
        "hard_fails": {
            "disease_claims": False,
            "no_paid_traffic": False,
            "low_aov": False,
            "low_initial": False,
            "high_refund": False,
        },
        "positive_signals": {
            "vendor_age": True,
            "vsl_updated": True,
            "am_responsive": False,
            "capi_documented": True,
            "recurring_rebill": False,
            "bilingual_offer": True,
        }
    }
    template_path = REPO_ROOT / ".tools" / "offer-template.json"
    template_path.write_text(json.dumps(template, indent=2), encoding='utf-8')
    print(f"\n✓ Template generado: {template_path}")
    print(f"\nUso: python3 .tools/offer-scorer.py --batch .tools/offer-template.json")

def main():
    parser = argparse.ArgumentParser(description="ClickBank Offer Scorer · 11-criterion framework")
    parser.add_argument("--batch", help="Path to JSON file with offer data")
    parser.add_argument("--template", action="store_true", help="Generate template JSON")
    args = parser.parse_args()

    if args.template:
        generate_template()
        return

    if args.batch:
        data = json.loads(Path(args.batch).read_text())
        metadata = data["metadata"]
        m = data["metrics"]
        hard_fail_responses = data["hard_fails"]
        positive_responses = data["positive_signals"]
        interactive = False
    else:
        # Interactive mode
        print(f"\n{C.BOLD}{C.W}╔══════════════════════════════════════════════════════════╗{C.END}")
        print(f"{C.BOLD}{C.W}║  ClickBank Offer Scorer · 11-Criterion Framework         ║{C.END}")
        print(f"{C.BOLD}{C.W}║  Hispano-US optimized · Affiliate Business              ║{C.END}")
        print(f"{C.BOLD}{C.W}╚══════════════════════════════════════════════════════════╝{C.END}\n")

        metadata = collect_metadata(interactive=True)
        hard_fail_responses = collect_hard_fails(interactive=True)
        m = collect_metrics(interactive=True)
        positive_responses = collect_positive_signals(interactive=True)

    # Evaluate
    hard_fails = evaluate_hard_fails(hard_fail_responses)
    metrics_eval = evaluate_metrics(m)
    positive_score, _ = evaluate_positive_signals(positive_responses)
    economics = calculate_economics(m)
    verdict = make_verdict(len(hard_fails), positive_score, economics["verdict"])

    # Print terminal summary
    print_terminal_summary(metadata, hard_fails, metrics_eval, positive_score, economics, verdict)

    # Generate markdown
    md = generate_markdown(metadata, m, hard_fail_responses, hard_fails, metrics_eval, positive_responses, positive_score, economics, verdict)

    # Save
    if metadata.get("name"):
        filepath = save_report(metadata, md)
        print(f"{C.G}{C.BOLD}✓ Reporte guardado:{C.END}")
        print(f"  {filepath}\n")
        print(f"{C.W}Para abrir:{C.END}")
        print(f"  open \"{filepath}\"\n")

if __name__ == "__main__":
    main()
