#!/usr/bin/env python3
"""
Markdown a HTML renderer · Affiliate Business · v2 (rediseño 2026)
Design system "Editorial claro de research": tema paper claro + dark toggle,
Newsreader + Public Sans + JetBrains Mono, medida 68ch, espaciado 8px,
data viz sin dependencias (stat cards, barras CSS, donut conic-gradient, sparklines SVG).
Sin dependencias externas (parser markdown custom).

Uso:
  python3 render.py            -> renderiza todos los .md + index
  python3 render.py <ruta.md>  -> renderiza solo ese archivo (prototipo, no toca index)
"""

import os
import re
import sys
import html as html_lib
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path("/Users/cristobaltejero/Projects/affiliate-business")
EXCLUDE_DIRS = {".git", ".tools", "node_modules", ".firecrawl"}

# === CSS DESIGN SYSTEM v2 ===
CSS = """
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

:root {
    /* light "warm paper" default */
    --bg: #faf7f0;
    --bg-elev: #ffffff;
    --bg-sunk: #f1ece0;
    --ink: #1c1a17;
    --ink-dim: #4a463f;
    --ink-mute: #87806f;
    --line: #e4ddcd;
    --line-strong: #cabfa6;
    --accent: #b5651d;
    --accent-soft: rgba(181, 101, 29, 0.10);
    --green: #4f7a4a;
    --green-soft: rgba(79, 122, 74, 0.12);
    --red: #b23a1f;
    --red-soft: rgba(178, 58, 31, 0.10);
    --amber: #c08a1e;
    --amber-soft: rgba(192, 138, 30, 0.12);
    --blue: #2f6f8f;
    --blue-soft: rgba(47, 111, 143, 0.10);
    --romi: #b5651d;
    --cris: #4f7a4a;
    --dali: #9c3f86;
    --shadow: 0 1px 2px rgba(28,26,23,0.04), 0 4px 16px rgba(28,26,23,0.06);
    --shadow-lift: 0 2px 6px rgba(28,26,23,0.07), 0 12px 32px rgba(28,26,23,0.10);

    /* 8px spacing scale */
    --s1: 4px; --s2: 8px; --s3: 12px; --s4: 16px; --s5: 24px;
    --s6: 32px; --s7: 48px; --s8: 64px; --s9: 96px;
    --radius: 12px;
    --radius-sm: 7px;
    --measure: 68ch;
}

[data-theme="dark"] {
    --bg: #14130f;
    --bg-elev: #1d1c18;
    --bg-sunk: #0c0b09;
    --ink: #f3eee2;
    --ink-dim: #c9c2b2;
    --ink-mute: #8d8676;
    --line: #2c2a25;
    --line-strong: #433f37;
    --accent: #e0a050;
    --accent-soft: rgba(224, 160, 80, 0.13);
    --green: #7fb377;
    --green-soft: rgba(127, 179, 119, 0.14);
    --red: #e07a55;
    --red-soft: rgba(224, 122, 85, 0.13);
    --amber: #e8b647;
    --amber-soft: rgba(232, 182, 71, 0.14);
    --blue: #6fb6d6;
    --blue-soft: rgba(111, 182, 214, 0.13);
    --romi: #e0a050;
    --cris: #7fb377;
    --dali: #d479bd;
    --shadow: 0 1px 2px rgba(0,0,0,0.3), 0 4px 16px rgba(0,0,0,0.35);
    --shadow-lift: 0 2px 6px rgba(0,0,0,0.4), 0 12px 32px rgba(0,0,0,0.5);
}

html { scroll-behavior: smooth; }

body {
    font-family: 'Public Sans', system-ui, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--ink);
    line-height: 1.65;
    font-size: 17px;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    overflow-x: hidden;
    transition: background 0.3s ease, color 0.3s ease;
}

::selection { background: var(--accent-soft); color: var(--ink); }

/* === READING PROGRESS BAR === */
.progress {
    position: fixed; top: 0; left: 0; height: 3px;
    background: var(--accent);
    z-index: 100; width: 0%;
    transition: width 0.1s ease;
}

/* === TOP BAR === */
.topbar {
    position: sticky; top: 0; z-index: 50;
    background: color-mix(in srgb, var(--bg) 88%, transparent);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--line);
    padding: var(--s3) var(--s6);
    display: flex; justify-content: space-between; align-items: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem; letter-spacing: 0.1em;
}
.topbar a.home { color: var(--accent); text-decoration: none; font-weight: 600; transition: opacity 0.15s; }
.topbar a.home:hover { opacity: 0.7; }
.topbar .right { display: flex; align-items: center; gap: var(--s5); }
.topbar .meta { color: var(--ink-mute); letter-spacing: 0.05em; }
.theme-toggle {
    background: var(--bg-elev); border: 1px solid var(--line);
    color: var(--ink-dim); width: 34px; height: 34px; border-radius: 50%;
    cursor: pointer; display: grid; place-items: center;
    transition: all 0.2s ease;
}
.theme-toggle:hover { border-color: var(--accent); color: var(--accent); transform: rotate(-15deg); }
.theme-toggle svg { width: 16px; height: 16px; }
.theme-toggle .moon { display: none; }
[data-theme="dark"] .theme-toggle .sun { display: none; }
[data-theme="dark"] .theme-toggle .moon { display: block; }

/* === LAYOUT === */
.layout {
    display: grid;
    grid-template-columns: 264px minmax(0, 1fr);
    max-width: 1180px;
    margin: 0 auto;
    gap: var(--s7);
    padding: var(--s7) var(--s6);
    align-items: start;
}

/* === SIDEBAR (TOC) === */
.sidebar {
    position: sticky; top: 84px; align-self: start;
    max-height: calc(100vh - 110px); overflow-y: auto;
    padding-right: var(--s3);
}
.sidebar::-webkit-scrollbar { width: 4px; }
.sidebar::-webkit-scrollbar-thumb { background: var(--line-strong); border-radius: 2px; }
.sidebar-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem; letter-spacing: 0.18em; color: var(--ink-mute);
    text-transform: uppercase; margin-bottom: var(--s4);
}
.toc-list { list-style: none; }
.toc-list li { margin: 1px 0; }
.toc-list a {
    color: var(--ink-mute); text-decoration: none;
    font-size: 0.86rem; line-height: 1.35; display: block;
    padding: var(--s2) var(--s3); border-left: 2px solid var(--line);
    transition: all 0.15s; border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
}
.toc-list a:hover { color: var(--ink); border-left-color: var(--line-strong); background: var(--bg-sunk); }
.toc-list a.active { color: var(--accent); border-left-color: var(--accent); background: var(--accent-soft); font-weight: 600; }
.toc-list .h3 { padding-left: var(--s5); font-size: 0.8rem; }
.toc-list .h4 { padding-left: var(--s6); font-size: 0.77rem; }

/* === MAIN CONTENT === */
.content { max-width: var(--measure); min-width: 0; padding-bottom: var(--s9); }
.content > * { max-width: 100%; }

.content-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem; letter-spacing: 0.08em; color: var(--ink-mute);
    text-transform: uppercase; margin-bottom: var(--s6);
    display: flex; gap: var(--s4); flex-wrap: wrap; align-items: center;
}
.content-meta .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--accent); display: inline-block; }
.content-meta span { display: inline-flex; align-items: center; gap: var(--s2); }

/* === TYPOGRAPHY === */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Newsreader', Georgia, serif;
    color: var(--ink); line-height: 1.18; letter-spacing: -0.01em;
    font-weight: 600; text-wrap: balance;
}
h1 { font-size: 2.8rem; line-height: 1.08; margin-bottom: var(--s5); font-weight: 600; }
h2 {
    font-size: 1.95rem; margin-top: var(--s8); margin-bottom: var(--s4);
    padding-top: var(--s5); border-top: 1px solid var(--line);
}
h3 { font-size: 1.45rem; margin-top: var(--s6); margin-bottom: var(--s3); }
h4 { font-size: 1.15rem; margin-top: var(--s5); margin-bottom: var(--s2); color: var(--ink-dim); }

p { margin: var(--s4) 0; color: var(--ink-dim); }
strong { color: var(--ink); font-weight: 700; }
em { font-style: italic; }

a {
    color: var(--accent); text-decoration: none;
    border-bottom: 1px solid color-mix(in srgb, var(--accent) 35%, transparent);
    transition: all 0.15s;
}
a:hover { border-bottom-color: var(--accent); background: var(--accent-soft); }

/* === LISTS === */
ul, ol { margin: var(--s4) 0 var(--s4) var(--s5); color: var(--ink-dim); }
li { margin: var(--s2) 0; line-height: 1.6; padding-left: var(--s1); }
ul li::marker { color: var(--accent); }
ol li::marker { color: var(--ink-mute); font-family: 'JetBrains Mono', monospace; font-size: 0.85em; }
ul ul, ol ol, ul ol, ol ul { margin-top: var(--s2); margin-bottom: var(--s2); }
li input[type="checkbox"] { margin-right: var(--s2); accent-color: var(--accent); width: 15px; height: 15px; vertical-align: -2px; }

/* === CODE === */
code {
    font-family: 'JetBrains Mono', monospace;
    background: var(--bg-sunk); color: var(--accent);
    padding: 0.12em 0.4em; border-radius: 5px; font-size: 0.86em;
    border: 1px solid var(--line);
}
pre {
    background: var(--bg-sunk); border: 1px solid var(--line);
    border-radius: var(--radius-sm); padding: var(--s4) var(--s5);
    overflow-x: auto; margin: var(--s5) 0; font-size: 0.84rem; line-height: 1.6;
}
pre code { background: transparent; border: none; padding: 0; color: var(--ink-dim); font-size: inherit; }

/* === BLOCKQUOTES === */
blockquote {
    margin: var(--s5) 0; padding: var(--s4) var(--s5);
    border-left: 3px solid var(--accent); background: var(--bg-elev);
    color: var(--ink); font-family: 'Newsreader', Georgia, serif;
    font-style: italic; font-size: 1.12rem; line-height: 1.5;
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0; box-shadow: var(--shadow);
}
blockquote p { color: var(--ink); margin: var(--s2) 0; }
blockquote strong { color: var(--accent); font-style: normal; }

/* === TABLES === */
.table-wrap { overflow-x: auto; margin: var(--s5) 0; border-radius: var(--radius-sm); border: 1px solid var(--line); box-shadow: var(--shadow); }
table { width: 100%; border-collapse: collapse; font-size: 0.92rem; font-variant-numeric: tabular-nums; background: var(--bg-elev); }
thead { background: var(--bg-sunk); }
th {
    padding: var(--s3) var(--s4); text-align: left;
    font-family: 'JetBrains Mono', monospace; font-size: 0.68rem;
    text-transform: uppercase; letter-spacing: 0.08em; color: var(--ink-dim);
    border-bottom: 2px solid var(--line-strong); white-space: nowrap;
}
td { padding: var(--s3) var(--s4); border-bottom: 1px solid var(--line); color: var(--ink-dim); vertical-align: top; }
tbody tr:nth-child(even) { background: color-mix(in srgb, var(--bg-sunk) 50%, transparent); }
tr:last-child td { border-bottom: none; }
tbody tr:hover { background: var(--accent-soft); }
tbody tr:hover td { color: var(--ink); }

/* === HR === */
hr { margin: var(--s7) 0; border: none; height: 1px; background: var(--line); }

/* === CALLOUT BOXES === */
.box {
    margin: var(--s5) 0; padding: var(--s4) var(--s5);
    border-radius: var(--radius-sm); border: 1px solid var(--line);
    border-left: 4px solid var(--accent); background: var(--bg-elev);
    box-shadow: var(--shadow); position: relative;
}
.box p:first-of-type { margin-top: 0; } .box p:last-child { margin-bottom: 0; }
.box-tldr { border-left-color: var(--accent); background: var(--accent-soft); }
.box-veredicto { border-left-color: var(--romi); background: var(--accent-soft); }
.box-critico, .box-stop { border-left-color: var(--red); background: var(--red-soft); }
.box-recomendado, .box-tip { border-left-color: var(--green); background: var(--green-soft); }
.box-warning, .box-alerta { border-left-color: var(--amber); background: var(--amber-soft); }
.box-info, .box-note { border-left-color: var(--blue); background: var(--blue-soft); }
.box-label {
    display: inline-flex; align-items: center; gap: var(--s2);
    font-family: 'JetBrains Mono', monospace; font-size: 0.66rem;
    letter-spacing: 0.12em; text-transform: uppercase; font-weight: 700;
    margin-bottom: var(--s3); color: var(--accent);
}
.box-critico .box-label, .box-stop .box-label { color: var(--red); }
.box-recomendado .box-label, .box-tip .box-label { color: var(--green); }
.box-warning .box-label, .box-alerta .box-label { color: var(--amber); }
.box-info .box-label, .box-note .box-label { color: var(--blue); }
.box-veredicto .box-label { color: var(--romi); }

/* === BADGES === */
.badge {
    display: inline-block; padding: 0.1em 0.5em; border-radius: 5px;
    font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.04em; margin: 0 0.1em; vertical-align: middle;
    border: 1px solid;
}
.badge-ok { background: var(--green-soft); color: var(--green); border-color: var(--green); }
.badge-no { background: var(--red-soft); color: var(--red); border-color: var(--red); }
.badge-warn { background: var(--amber-soft); color: var(--amber); border-color: var(--amber); }
.badge-alert { background: var(--red-soft); color: var(--red); border-color: var(--red); }
.badge-info { background: var(--blue-soft); color: var(--blue); border-color: var(--blue); }
.badge-romi { background: var(--accent-soft); color: var(--romi); border-color: var(--romi); }
.badge-cris { background: var(--green-soft); color: var(--cris); border-color: var(--cris); }
.badge-dali { background: rgba(156,63,134,0.12); color: var(--dali); border-color: var(--dali); }

/* === DATA VIZ: STAT CARDS / KPI STRIP === */
.kpi-strip { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: var(--s4); margin: var(--s6) 0; }
.stat {
    background: var(--bg-elev); border: 1px solid var(--line);
    border-radius: var(--radius); padding: var(--s5); box-shadow: var(--shadow);
    display: flex; flex-direction: column; gap: var(--s2);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.stat:hover { transform: translateY(-3px); box-shadow: var(--shadow-lift); }
.stat-value { font-family: 'Newsreader', serif; font-size: 2.3rem; line-height: 1; color: var(--ink); font-weight: 600; font-variant-numeric: tabular-nums; }
.stat.lg .stat-value { font-size: 3rem; }
.stat-label { font-family: 'JetBrains Mono', monospace; font-size: 0.66rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-mute); }
.stat-delta { font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; font-weight: 700; display: inline-flex; align-items: center; gap: 3px; }
.stat-delta.up { color: var(--green); } .stat-delta.down { color: var(--red); } .stat-delta.flat { color: var(--ink-mute); }
.stat-spark { margin-top: var(--s1); }
.stat-spark svg { width: 100%; height: 32px; display: block; overflow: visible; }

/* === DATA VIZ: BARS === */
.bars { margin: var(--s6) 0; display: flex; flex-direction: column; gap: var(--s3); }
.bar-row { display: grid; grid-template-columns: minmax(90px, 28%) 1fr auto; align-items: center; gap: var(--s4); }
.bar-label { font-size: 0.86rem; color: var(--ink-dim); font-weight: 600; }
.bar-track { background: var(--bg-sunk); border-radius: 999px; height: 18px; overflow: hidden; border: 1px solid var(--line); }
.bar-fill { height: 100%; border-radius: 999px; background: linear-gradient(90deg, color-mix(in srgb, var(--accent) 70%, var(--bg)), var(--accent)); min-width: 2px; transition: width 0.8s cubic-bezier(.2,.8,.2,1); }
.bar-fill.c-green { background: linear-gradient(90deg, color-mix(in srgb, var(--green) 65%, var(--bg)), var(--green)); }
.bar-fill.c-red { background: linear-gradient(90deg, color-mix(in srgb, var(--red) 65%, var(--bg)), var(--red)); }
.bar-fill.c-blue { background: linear-gradient(90deg, color-mix(in srgb, var(--blue) 65%, var(--bg)), var(--blue)); }
.bar-value { font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; color: var(--ink); font-weight: 700; font-variant-numeric: tabular-nums; min-width: 48px; text-align: right; }

/* === DATA VIZ: DONUT === */
.donut-wrap { display: flex; align-items: center; gap: var(--s5); margin: var(--s6) 0; flex-wrap: wrap; }
.donut {
    --pct: 50; --col: var(--accent);
    width: 132px; height: 132px; border-radius: 50%; flex-shrink: 0;
    background: conic-gradient(var(--col) calc(var(--pct) * 1%), var(--bg-sunk) 0);
    display: grid; place-items: center; position: relative;
}
.donut::before { content: ''; position: absolute; inset: 16px; border-radius: 50%; background: var(--bg-elev); box-shadow: var(--shadow); }
.donut-num { position: relative; font-family: 'Newsreader', serif; font-size: 1.9rem; font-weight: 600; color: var(--ink); font-variant-numeric: tabular-nums; }
.donut-info .donut-label { font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-mute); margin-bottom: var(--s2); }
.donut-info .donut-desc { color: var(--ink-dim); font-size: 0.92rem; max-width: 36ch; }

/* === EXAMPLE BOX === */
.example {
    margin: var(--s6) 0; border: 1px solid var(--line-strong); border-radius: var(--radius);
    background: var(--bg-elev); overflow: hidden; box-shadow: var(--shadow);
}
.example-head {
    display: flex; align-items: center; gap: var(--s2);
    padding: var(--s3) var(--s5); background: var(--bg-sunk);
    border-bottom: 1px dashed var(--line-strong);
    font-family: 'JetBrains Mono', monospace; font-size: 0.68rem;
    text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); font-weight: 700;
}
.example-head svg { width: 14px; height: 14px; }
.example-body { padding: var(--s5); }
.example-body > *:first-child { margin-top: 0; } .example-body > *:last-child { margin-bottom: 0; }

/* === BEFORE / AFTER === */
.ba { display: grid; grid-template-columns: 1fr 1fr; gap: var(--s4); margin: var(--s6) 0; }
.ba-col { border: 1px solid var(--line); border-radius: var(--radius-sm); padding: var(--s5); background: var(--bg-elev); box-shadow: var(--shadow); }
.ba-col.before { border-top: 3px solid var(--red); }
.ba-col.after { border-top: 3px solid var(--green); }
.ba-tag { font-family: 'JetBrains Mono', monospace; font-size: 0.66rem; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: var(--s3); font-weight: 700; }
.ba-col.before .ba-tag { color: var(--red); } .ba-col.after .ba-tag { color: var(--green); }

/* === DATA VIZ: FUNNEL === */
.funnel { margin: var(--s6) 0; display: flex; flex-direction: column; gap: var(--s2); }
.funnel-row { display: flex; align-items: center; gap: var(--s4); }
.funnel-bar-wrap { flex: 1; display: flex; justify-content: center; }
.funnel-bar {
    background: linear-gradient(180deg, color-mix(in srgb, var(--accent) 78%, var(--bg)), var(--accent));
    color: #fff; padding: var(--s3) var(--s4); border-radius: var(--radius-sm);
    text-align: center; min-width: 60px; font-weight: 600; font-size: 0.95rem;
    box-shadow: var(--shadow); transition: width 0.7s cubic-bezier(.2,.8,.2,1);
}
.funnel-bar .fn-val { font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; opacity: 0.9; display: block; margin-top: 2px; }
.funnel-meta { font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: var(--ink-mute); min-width: 110px; }
.funnel-drop { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: var(--red); min-width: 56px; text-align: right; }

/* === DATA VIZ: COMPARE (multi-metric cards) === */
.compare { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: var(--s4); margin: var(--s6) 0; }
.compare-card { background: var(--bg-elev); border: 1px solid var(--line); border-radius: var(--radius); padding: var(--s5); box-shadow: var(--shadow); }
.compare-card.win { border-color: var(--green); border-top: 3px solid var(--green); }
.compare-name { font-family: 'Newsreader', serif; font-size: 1.2rem; color: var(--ink); font-weight: 600; margin-bottom: var(--s4); display: flex; align-items: center; justify-content: space-between; gap: var(--s2); }
.compare-name .pill { font-family: 'JetBrains Mono', monospace; font-size: 0.6rem; padding: 2px 7px; border-radius: 999px; background: var(--green-soft); color: var(--green); letter-spacing: 0.08em; text-transform: uppercase; }
.compare-metric { margin: var(--s3) 0; }
.compare-metric .cm-top { display: flex; justify-content: space-between; font-size: 0.78rem; margin-bottom: 3px; }
.compare-metric .cm-label { color: var(--ink-mute); font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.05em; }
.compare-metric .cm-val { color: var(--ink); font-weight: 700; font-variant-numeric: tabular-nums; }
.compare-metric .cm-track { background: var(--bg-sunk); border-radius: 999px; height: 6px; overflow: hidden; }
.compare-metric .cm-fill { height: 100%; border-radius: 999px; background: var(--accent); }

/* === DATA VIZ: TIMELINE === */
.timeline { margin: var(--s6) 0; position: relative; padding-left: var(--s6); }
.timeline::before { content: ''; position: absolute; left: 9px; top: 6px; bottom: 6px; width: 2px; background: var(--line-strong); }
.tl-item { position: relative; margin-bottom: var(--s5); }
.tl-item::before { content: ''; position: absolute; left: calc(-1 * var(--s6) + 4px); top: 4px; width: 12px; height: 12px; border-radius: 50%; background: var(--accent); border: 2px solid var(--bg); box-shadow: 0 0 0 2px var(--accent-soft); }
.tl-when { font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--accent); font-weight: 700; margin-bottom: 2px; }
.tl-what { color: var(--ink-dim); font-size: 0.95rem; }
.tl-what strong { color: var(--ink); }

/* === TABLE SEMAPHORE CELLS === */
td.sg-green { background: var(--green-soft); color: var(--green); font-weight: 700; }
td.sg-amber { background: var(--amber-soft); color: var(--amber); font-weight: 700; }
td.sg-red { background: var(--red-soft); color: var(--red); font-weight: 700; }
tbody tr:hover td.sg-green, tbody tr:hover td.sg-amber, tbody tr:hover td.sg-red { color: var(--ink); }

/* === DETAILS === */
details { margin: var(--s5) 0; border: 1px solid var(--line); border-radius: var(--radius-sm); background: var(--bg-elev); overflow: hidden; }
summary { padding: var(--s4) var(--s5); cursor: pointer; font-weight: 600; color: var(--ink); list-style: none; display: flex; justify-content: space-between; align-items: center; }
summary::-webkit-details-marker { display: none; }
summary::after { content: '+'; font-family: 'JetBrains Mono', monospace; color: var(--accent); font-size: 1.2rem; }
details[open] summary::after { content: '−'; }
details[open] summary { border-bottom: 1px solid var(--line); }
.details-body { padding: var(--s5); }

/* === HEADING ANCHORS === */
h2 .anchor, h3 .anchor, h4 .anchor { opacity: 0; margin-left: var(--s2); color: var(--ink-mute); font-size: 0.8em; text-decoration: none; border: none; transition: opacity 0.15s; }
h2:hover .anchor, h3:hover .anchor, h4:hover .anchor { opacity: 1; }

/* === FOOTER === */
.footer { margin-top: var(--s8); padding-top: var(--s5); border-top: 1px solid var(--line); font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: var(--ink-mute); letter-spacing: 0.06em; text-align: center; }

/* === REVEAL ANIMATION === */
@media (prefers-reduced-motion: no-preference) {
    .reveal { opacity: 0; transform: translateY(14px); transition: opacity 0.5s ease, transform 0.5s ease; }
    .reveal.in { opacity: 1; transform: none; }
}

/* === RESPONSIVE === */
@media (max-width: 920px) {
    .layout { grid-template-columns: 1fr; padding: var(--s5) var(--s4); gap: var(--s5); }
    .sidebar { position: static; max-height: none; border-bottom: 1px solid var(--line); padding-bottom: var(--s4); margin-bottom: var(--s2); }
    h1 { font-size: 2.1rem; } h2 { font-size: 1.6rem; }
    .ba { grid-template-columns: 1fr; }
    .topbar { padding: var(--s3) var(--s4); }
}

@media print {
    .progress, .topbar, .sidebar, .theme-toggle { display: none; }
    .layout { grid-template-columns: 1fr; padding: 0; max-width: 100%; }
    body { background: #fff; color: #000; font-size: 11pt; }
    .stat, .box, .example, table { box-shadow: none; break-inside: avoid; }
    .reveal { opacity: 1 !important; transform: none !important; }
}
"""

# === JS ===
JS = """
// theme toggle
(function(){
    const btn = document.querySelector('.theme-toggle');
    if (btn) btn.addEventListener('click', () => {
        const cur = document.documentElement.getAttribute('data-theme');
        const next = cur === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        try { localStorage.setItem('ab-theme', next); } catch(e){}
    });
})();

// reading progress
window.addEventListener('scroll', () => {
    const h = document.documentElement;
    const sc = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
    const p = document.querySelector('.progress');
    if (p) p.style.width = sc + '%';
}, { passive: true });

// TOC scroll-spy + smooth scroll
const heads = document.querySelectorAll('h2[id], h3[id], h4[id]');
const links = document.querySelectorAll('.toc-list a');
function spy(){
    let active = null; const off = window.scrollY + 110;
    heads.forEach(h => { if (h.offsetTop <= off) active = h.id; });
    links.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + active));
}
window.addEventListener('scroll', spy, { passive: true }); spy();
links.forEach(l => l.addEventListener('click', e => {
    e.preventDefault();
    const t = document.querySelector(l.getAttribute('href'));
    if (t) { window.scrollTo({ top: t.getBoundingClientRect().top + window.scrollY - 80, behavior: 'smooth' }); history.pushState(null, '', l.getAttribute('href')); }
}));

// staggered reveal (con seguro: nunca dejar contenido oculto)
if (window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
    const els = document.querySelectorAll('.content h2, .kpi-strip, .bars, .funnel, .timeline, .compare, .donut-wrap, .example, .ba, .table-wrap, blockquote, .box');
    const io = new IntersectionObserver((es) => {
        es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.05 });
    els.forEach(el => { el.classList.add('reveal'); io.observe(el); });
    setTimeout(() => els.forEach(el => el.classList.add('in')), 1200);
}
"""

THEME_INIT = "<script>(function(){try{var t=localStorage.getItem('ab-theme')||'light';document.documentElement.setAttribute('data-theme',t);}catch(e){document.documentElement.setAttribute('data-theme','light');}})();</script>"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400&family=Public+Sans:ital,wght@0,300..800;1,400..600&family=JetBrains+Mono:wght@400..700&display=swap" rel="stylesheet">'

SUN_MOON = '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'

# === MARKDOWN PARSER ===

def slugify(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[\s_-]+', '-', text).strip('-')
    return text or 'section'

def escape_html(text):
    return html_lib.escape(text, quote=False)

def render_inline(text):
    text = re.sub(r'`([^`]+)`', lambda m: f'<code>{escape_html(m.group(1))}</code>', text)
    def link_repl(m):
        label, url = m.group(1), m.group(2)
        target = ' target="_blank" rel="noopener"' if url.startswith('http') else ''
        return f'<a href="{url}"{target}>{label}</a>'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link_repl, text)
    text = re.sub(r'\*\*([^\*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^\*\n]+)\*(?!\*)', r'<em>\1</em>', text)
    badges = {
        '✅': '<span class="badge badge-ok">OK</span>', '❌': '<span class="badge badge-no">NO</span>',
        '⚠️': '<span class="badge badge-warn">!</span>', '🚨': '<span class="badge badge-alert">CRÍTICO</span>',
        '⏳': '<span class="badge badge-info">PENDIENTE</span>', '🔄': '<span class="badge badge-info">EN CURSO</span>',
        '⛔': '<span class="badge badge-no">BLOQUEADO</span>', '🟢': '<span class="badge badge-ok">●</span>',
        '🟡': '<span class="badge badge-warn">●</span>', '🔴': '<span class="badge badge-no">●</span>',
        '🎯': '<span class="badge badge-info">META</span>', '⭐': '<span class="badge badge-warn">★</span>',
        '💰': '<span class="badge badge-warn">$</span>', '📊': '<span class="badge badge-info">DATA</span>',
        '📈': '<span class="badge badge-cris">↑</span>', '📉': '<span class="badge badge-no">↓</span>',
        '🏆': '<span class="badge badge-warn">WIN</span>',
    }
    for emo, bdg in badges.items():
        text = text.replace(emo, bdg)
    return text

def sparkline_svg(nums, color='var(--accent)'):
    if len(nums) < 2: return ''
    w, h, pad = 100, 30, 3
    lo, hi = min(nums), max(nums)
    rng = (hi - lo) or 1
    pts = []
    for i, n in enumerate(nums):
        x = pad + (w - 2*pad) * i / (len(nums) - 1)
        y = h - pad - (h - 2*pad) * (n - lo) / rng
        pts.append(f'{x:.1f},{y:.1f}')
    poly = ' '.join(pts)
    last = pts[-1].split(',')
    return (f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="none">'
            f'<polyline points="{poly}" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="{last[0]}" cy="{last[1]}" r="2.5" fill="{color}"/></svg>')

def _kv_block(raw):
    """Parse 'key: value' lines + free body. Returns (dict, body_lines)."""
    kv, body = {}, []
    for ln in raw.split('\n'):
        m = re.match(r'^([a-zA-Z_-]+):\s*(.*)$', ln)
        if m and m.group(1).lower() in ('value','label','delta','spark','color','title','pct','desc','before','after'):
            kv[m.group(1).lower()] = m.group(2).strip()
        else:
            body.append(ln)
    return kv, body

def render_stat_card(kv, large=False):
    val = escape_html(kv.get('value', ''))
    label = escape_html(kv.get('label', ''))
    delta = kv.get('delta', '')
    cls = 'stat lg' if large else 'stat'
    delta_html = ''
    if delta:
        d = delta.strip()
        dir_cls = 'up' if d.startswith('+') else ('down' if d.startswith('-') else 'flat')
        arrow = '▲' if dir_cls == 'up' else ('▼' if dir_cls == 'down' else '■')
        delta_html = f'<span class="stat-delta {dir_cls}">{arrow} {escape_html(d.lstrip("+"))}</span>'
    spark_html = ''
    if kv.get('spark'):
        try:
            nums = [float(x) for x in re.split(r'[,\s]+', kv['spark'].strip()) if x]
            spark_html = f'<div class="stat-spark">{sparkline_svg(nums)}</div>'
        except ValueError:
            pass
    return (f'<div class="{cls}"><div class="stat-value">{val}</div>'
            f'<div class="stat-label">{label}</div>{delta_html}{spark_html}</div>')

def render_kpi_strip(raw):
    """Multiple stat cards separated by blank lines or '---'."""
    blocks = re.split(r'\n\s*\n|\n---\n', raw.strip())
    cards = []
    for b in blocks:
        kv, _ = _kv_block(b)
        if kv.get('value'):
            cards.append(render_stat_card(kv))
    return f'<div class="kpi-strip">{"".join(cards)}</div>' if cards else ''

def render_bars(raw):
    rows = []
    items = []
    for ln in raw.strip().split('\n'):
        if '|' not in ln: continue
        parts = [p.strip() for p in ln.split('|')]
        label = parts[0]
        try:
            val = float(re.sub(r'[^\d.]', '', parts[1]))
        except (ValueError, IndexError):
            continue
        color = parts[2].strip() if len(parts) > 2 else ''
        raw_val = parts[1]
        items.append((label, val, raw_val, color))
    if not items: return ''
    mx = max(v for _, v, _, _ in items) or 1
    for label, val, raw_val, color in items:
        pct = max(2, val / mx * 100)
        ccls = f' c-{color}' if color in ('green','red','blue') else ''
        rows.append(f'<div class="bar-row"><div class="bar-label">{render_inline(label)}</div>'
                    f'<div class="bar-track"><div class="bar-fill{ccls}" style="width:{pct:.1f}%"></div></div>'
                    f'<div class="bar-value">{escape_html(raw_val)}</div></div>')
    return f'<div class="bars">{"".join(rows)}</div>'

def render_donut(kv):
    try:
        pct = float(re.sub(r'[^\d.]', '', kv.get('value', kv.get('pct', '0'))))
    except ValueError:
        pct = 0
    label = escape_html(kv.get('label', ''))
    desc = render_inline(kv.get('desc', ''))
    num = escape_html(kv.get('value', f'{pct:.0f}%'))
    color_map = {'green': 'var(--green)', 'red': 'var(--red)', 'blue': 'var(--blue)', 'amber': 'var(--amber)'}
    col = color_map.get(kv.get('color', ''), 'var(--accent)')
    info = ''
    if label or desc:
        info = f'<div class="donut-info"><div class="donut-label">{label}</div><div class="donut-desc">{desc}</div></div>'
    return (f'<div class="donut-wrap"><div class="donut" style="--pct:{pct};--col:{col}">'
            f'<span class="donut-num">{num}</span></div>{info}</div>')

def render_example(kv, body_lines):
    title = escape_html(kv.get('title', 'En la práctica'))
    body_md = '\n'.join(body_lines).strip()
    inner, _ = md_to_html(body_md)
    icon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.3h6c0-1 .4-1.8 1-2.3A7 7 0 0 0 12 2z"/></svg>'
    return f'<div class="example"><div class="example-head">{icon}{title}</div><div class="example-body">{inner}</div></div>'

def render_before_after(kv, body_lines):
    before = kv.get('before', '')
    after = kv.get('after', '')
    # also support 'before:' / 'after:' multiline via body markers
    body = '\n'.join(body_lines)
    bm = re.search(r'(?is)before:\s*(.*?)(?:\nafter:|\Z)', body)
    am = re.search(r'(?is)after:\s*(.*)', body)
    if bm: before = bm.group(1).strip()
    if am: after = am.group(1).strip()
    b_html, _ = md_to_html(before)
    a_html, _ = md_to_html(after)
    return (f'<div class="ba"><div class="ba-col before"><div class="ba-tag">Antes</div>{b_html}</div>'
            f'<div class="ba-col after"><div class="ba-tag">Después</div>{a_html}</div></div>')

def render_funnel(raw):
    items = []
    for ln in raw.strip().split('\n'):
        if '|' not in ln: continue
        parts = [p.strip() for p in ln.split('|')]
        try:
            val = float(re.sub(r'[^\d.]', '', parts[1]))
        except (ValueError, IndexError):
            continue
        items.append((parts[0], val, parts[1]))
    if not items: return ''
    mx = max(v for _, v, _ in items) or 1
    rows, prev = [], None
    for label, val, raw_val in items:
        pct = max(12, val / mx * 100)
        drop = ''
        if prev and prev > 0:
            d = (prev - val) / prev * 100
            drop = f'<div class="funnel-drop">-{d:.0f}%</div>' if d > 0.5 else '<div class="funnel-drop"></div>'
        else:
            drop = '<div class="funnel-drop"></div>'
        rows.append(f'<div class="funnel-row"><div class="funnel-meta">{render_inline(label)}</div>'
                    f'<div class="funnel-bar-wrap"><div class="funnel-bar" style="width:{pct:.0f}%">{escape_html(raw_val)}</div></div>{drop}</div>')
        prev = val
    return f'<div class="funnel">{"".join(rows)}</div>'

def render_compare(raw):
    blocks = re.split(r'\n\s*\n', raw.strip())
    cards = []
    for b in blocks:
        lines = [l for l in b.split('\n') if l.strip()]
        if not lines: continue
        name = lines[0].strip()
        win = False
        m = re.search(r'\((?:win|ganador|recomendado|top)\)', name, re.I)
        if m: win = True; name = name.replace(m.group(0), '').strip()
        mh = []
        for ln in lines[1:]:
            if '|' not in ln: continue
            parts = [p.strip() for p in ln.split('|')]
            if len(parts) < 2: continue
            label, val = parts[0], parts[1]
            try:
                pct = float(re.sub(r'[^\d.]', '', parts[2])) if len(parts) > 2 else float(re.sub(r'[^\d.]', '', val))
            except ValueError:
                pct = 0
            pct = max(0, min(100, pct))
            mh.append(f'<div class="compare-metric"><div class="cm-top"><span class="cm-label">{escape_html(label)}</span>'
                      f'<span class="cm-val">{escape_html(val)}</span></div>'
                      f'<div class="cm-track"><div class="cm-fill" style="width:{pct:.0f}%"></div></div></div>')
        pill = '<span class="pill">Top</span>' if win else ''
        cls = 'compare-card win' if win else 'compare-card'
        cards.append(f'<div class="{cls}"><div class="compare-name">{render_inline(name)}{pill}</div>{"".join(mh)}</div>')
    return f'<div class="compare">{"".join(cards)}</div>' if cards else ''

def render_timeline(raw):
    rows = []
    for ln in raw.strip().split('\n'):
        if '|' not in ln: continue
        parts = [p.strip() for p in ln.split('|', 1)]
        if len(parts) < 2: continue
        rows.append(f'<div class="tl-item"><div class="tl-when">{render_inline(parts[0])}</div>'
                    f'<div class="tl-what">{render_inline(parts[1])}</div></div>')
    return f'<div class="timeline">{"".join(rows)}</div>' if rows else ''

VIZ_LANGS = {'stat', 'kpi', 'bars', 'donut', 'example', 'before-after', 'beforeafter', 'funnel', 'compare', 'timeline'}

def parse_code_block(lines, idx):
    if not lines[idx].startswith('```'): return None, idx
    lang = lines[idx][3:].strip().lower()
    j = idx + 1
    code_lines = []
    while j < len(lines) and not lines[j].startswith('```'):
        code_lines.append(lines[j]); j += 1
    raw = '\n'.join(code_lines)
    end = j + 1
    if lang in VIZ_LANGS:
        kv, body = _kv_block(raw)
        if lang == 'stat': return render_stat_card(kv, large=('lg' in code_lines[0] if code_lines else False)), end
        if lang == 'kpi': return render_kpi_strip(raw), end
        if lang == 'bars': return render_bars(raw), end
        if lang == 'funnel': return render_funnel(raw), end
        if lang == 'compare': return render_compare(raw), end
        if lang == 'timeline': return render_timeline(raw), end
        if lang == 'donut': return render_donut(kv), end
        if lang == 'example': return render_example(kv, body), end
        if lang in ('before-after', 'beforeafter'): return render_before_after(kv, body), end
    code_html = escape_html(raw)
    lang_attr = f' class="language-{lang}"' if lang else ''
    return f'<pre><code{lang_attr}>{code_html}</code></pre>', end

def parse_table(lines, idx):
    if idx + 1 >= len(lines): return None, idx
    if not re.match(r'^\s*\|?\s*[-:]+\s*\|', lines[idx + 1]): return None, idx
    header = [c.strip() for c in lines[idx].strip('|').split('|')]
    rows = []
    j = idx + 2
    while j < len(lines) and '|' in lines[j] and lines[j].strip():
        rows.append([c.strip() for c in lines[j].strip('|').split('|')]); j += 1
    out = ['<div class="table-wrap"><table><thead><tr>']
    for h in header: out.append(f'<th>{render_inline(h)}</th>')
    out.append('</tr></thead><tbody>')
    sg = {'{g}': 'sg-green', '{a}': 'sg-amber', '{r}': 'sg-red'}
    for row in rows:
        out.append('<tr>')
        for cell in row:
            cls = ''
            for mark, c in sg.items():
                if cell.startswith(mark):
                    cls = f' class="{c}"'; cell = cell[len(mark):].strip(); break
            out.append(f'<td{cls}>{render_inline(cell)}</td>')
        out.append('</tr>')
    out.append('</tbody></table></div>')
    return '\n'.join(out), j

def detect_box_type(content):
    lower = content.lower()
    # explicit GitHub/Obsidian style [!TYPE]
    m = re.match(r'^\s*\[!(\w+)\]', content)
    if m:
        t = m.group(1).lower()
        names = {'note':('note','Nota'),'tip':('tip','Tip'),'important':('recomendado','Importante'),
                 'warning':('warning','Atención'),'caution':('critico','Cuidado'),'danger':('critico','Peligro')}
        if t in names: return names[t]
    if any(x in lower for x in ['tl;dr', 'tldr', 'resumen ejecutivo']): return 'tldr', 'TL;DR'
    if 'veredicto' in lower: return 'veredicto', 'Veredicto'
    if any(x in lower for x in ['stop-loss', 'stop loss', 'critico', 'crítico', 'crítica', 'critica', 'no recomendado', 'no negociable']): return 'critico', 'Crítico'
    if any(x in lower for x in ['recomendado', 'recomendación principal']): return 'recomendado', 'Recomendado'
    if any(x in lower for x in ['alerta', 'warning', '⚠']): return 'warning', 'Atención'
    return None, None

def parse_blockquote(lines, idx):
    content_lines = []
    j = idx
    while j < len(lines) and lines[j].lstrip().startswith('>'):
        content_lines.append(lines[j].lstrip()[1:].strip()); j += 1
    content = '\n'.join(content_lines).strip()
    box_type, label = detect_box_type(content)
    content = re.sub(r'^\s*\[!\w+\]\s*', '', content)
    paragraphs = re.split(r'\n\s*\n', content)
    parts = []
    for para in paragraphs:
        para = para.replace('\n', ' ').strip()
        if para: parts.append(f'<p>{render_inline(para)}</p>')
    inner = '\n'.join(parts)
    if box_type:
        return f'<div class="box box-{box_type}"><div class="box-label">{label}</div>{inner}</div>', j
    return f'<blockquote>{inner}</blockquote>', j

def parse_list(lines, idx, indent=0):
    items = []
    j = idx
    list_type = None
    while j < len(lines):
        line = lines[j]
        m_ul = re.match(r'^(\s*)[-*+]\s+(.*)$', line)
        m_ol = re.match(r'^(\s*)\d+\.\s+(.*)$', line)
        m = m_ul or m_ol
        if not m:
            if line.strip() == '' and j + 1 < len(lines):
                nl = lines[j + 1]
                if re.match(r'^(\s*)[-*+]\s+', nl) or re.match(r'^(\s*)\d+\.\s+', nl):
                    j += 1; continue
            break
        line_indent = len(m.group(1))
        if line_indent < indent: break
        current_type = 'ol' if m_ol else 'ul'
        if list_type is None: list_type = current_type
        content = m.group(2)
        cb = re.match(r'^\[([ xX])\]\s+(.*)$', content)
        if cb:
            checked = 'checked' if cb.group(1).lower() == 'x' else ''
            content = f'<input type="checkbox" {checked} disabled>{cb.group(2)}'
        items.append(render_inline(content)); j += 1
    if not items: return None, idx
    out = [f'<{list_type}>'] + [f'<li>{it}</li>' for it in items] + [f'</{list_type}>']
    return '\n'.join(out), j

def parse_heading(line):
    m = re.match(r'^(#{1,6})\s+(.*)$', line)
    if not m: return None
    level = len(m.group(1)); text = m.group(2).strip()
    return level, text, render_inline(text), slugify(text)

def md_to_html(md_text):
    lines = md_text.split('\n')
    parts = []
    headings = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip(): i += 1; continue
        if line.startswith('```'):
            html, i = parse_code_block(lines, i); parts.append(html); continue
        h = parse_heading(line)
        if h:
            level, text, text_inline, slug = h
            headings.append((level, text, slug))
            if level == 1:
                parts.append(f'<h1 id="{slug}">{text_inline}</h1>')
            else:
                parts.append(f'<h{level} id="{slug}">{text_inline}<a class="anchor" href="#{slug}">#</a></h{level}>')
            i += 1; continue
        if re.match(r'^[\s]*[-*_]{3,}[\s]*$', line): parts.append('<hr>'); i += 1; continue
        if '|' in line and i + 1 < len(lines) and re.match(r'^\s*\|?\s*[-:]+\s*\|', lines[i+1]):
            tbl, i = parse_table(lines, i)
            if tbl: parts.append(tbl); continue
        if line.lstrip().startswith('>'):
            bq, i = parse_blockquote(lines, i); parts.append(bq); continue
        if re.match(r'^\s*[-*+]\s+', line) or re.match(r'^\s*\d+\.\s+', line):
            ls, new_i = parse_list(lines, i)
            if ls and new_i > i: parts.append(ls); i = new_i; continue
        para_lines = [line]; j = i + 1
        while j < len(lines):
            nl = lines[j]
            if (not nl.strip() or nl.startswith('#') or nl.startswith('```') or nl.lstrip().startswith('>') or
                re.match(r'^\s*[-*+]\s+', nl) or re.match(r'^\s*\d+\.\s+', nl) or
                re.match(r'^[\s]*[-*_]{3,}[\s]*$', nl) or
                ('|' in nl and j + 1 < len(lines) and re.match(r'^\s*\|?\s*[-:]+\s*\|', lines[j+1]))):
                break
            para_lines.append(nl); j += 1
        para = ' '.join(l.strip() for l in para_lines).strip()
        if para: parts.append(f'<p>{render_inline(para)}</p>')
        i = j
    return '\n'.join(parts), headings

def estimate_reading_time(text):
    return max(1, round(len(text.split()) / 200))

def build_toc(headings):
    if not headings: return ''
    items = []
    for level, text, slug in headings:
        if level == 1 or level > 4: continue
        css_class = f'h{level}' if level > 2 else ''
        text_clean = re.sub(r'<[^>]+>', '', text)
        items.append(f'<li><a href="#{slug}" class="{css_class}">{text_clean}</a></li>')
    return f'<ul class="toc-list">{"".join(items)}</ul>'

def get_breadcrumb(md_path):
    rel = md_path.relative_to(REPO_ROOT)
    parts = list(rel.parts[:-1])
    return ' / '.join(parts) if parts else 'raíz'

def render_html(md_path, output_path):
    md_text = md_path.read_text(encoding='utf-8')
    body_html, headings = md_to_html(md_text)
    toc = build_toc(headings)
    title = md_path.stem
    for level, text, _ in headings:
        if level == 1:
            title = re.sub(r'<[^>]+>', '', text); break
    reading_time = estimate_reading_time(md_text)
    breadcrumb = get_breadcrumb(md_path)
    word_count = len(md_text.split())
    depth = len(md_path.relative_to(REPO_ROOT).parts) - 1
    index_path = '../' * depth + 'index.html' if depth > 0 else 'index.html'

    sidebar = f'<aside class="sidebar"><div class="sidebar-title">Contenido</div>{toc}</aside>' if toc else '<aside class="sidebar"></aside>'

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape_html(title)} · Affiliate Business</title>
{THEME_INIT}
{FONTS}
<style>{CSS}</style>
</head>
<body>
<div class="progress"></div>
<nav class="topbar">
<a class="home" href="{index_path}">← Affiliate Business</a>
<div class="right">
<span class="meta">{breadcrumb} · {reading_time} min · {word_count:,} palabras</span>
<button class="theme-toggle" aria-label="Cambiar tema">{SUN_MOON}</button>
</div>
</nav>
<div class="layout">
{sidebar}
<main class="content">
<div class="content-meta"><span><span class="dot"></span>{md_path.name}</span><span>{word_count:,} palabras</span><span>~{reading_time} min</span></div>
{body_html}
<div class="footer">Affiliate Business · Generado {datetime.now().strftime('%Y-%m-%d')} · Fuente: {md_path.name}</div>
</main>
</div>
<script>{JS}</script>
</body>
</html>"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding='utf-8')
    return reading_time, word_count

def find_md_files():
    md_files = []
    for path in REPO_ROOT.rglob('*.md'):
        if any(part in EXCLUDE_DIRS for part in path.parts): continue
        md_files.append(path)
    return sorted(md_files)

def build_index(md_files, stats):
    groups = {}
    for md in md_files:
        parts = md.relative_to(REPO_ROOT).parts
        if len(parts) == 1:
            group = '01-Raíz · Documentos principales'
        else:
            group_map = {'00-meta': '02-Meta · Charter, decisiones', '00-viabilidad': '03-Viabilidad · Estudio crítico',
                         '01-ejecucion-2026': '04-Ejecución 2026 · ClickBank', '06-ops': '05-Operaciones · SOPs y prompts',
                         '07-learning': '06-Learning · Cruce de cursos', 'knowledge': '07-Knowledge · Skills'}
            group = group_map.get(parts[0], parts[0])
        groups.setdefault(group, []).append(md)

    total_min = total_words = 0
    sections = []
    for group_name in sorted(groups.keys()):
        files = sorted(groups[group_name])
        cards = []
        for md in files:
            rel = md.relative_to(REPO_ROOT)
            html_rel = str(rel).replace('.md', '.html')
            mins, words = stats[md]
            total_min += mins; total_words += words
            md_text = md.read_text(encoding='utf-8')
            title = md.stem
            for line in md_text.split('\n'):
                m = re.match(r'^#\s+(.*)$', line)
                if m: title = re.sub(r'\*\*|`', '', m.group(1)).strip(); break
            desc = ''
            for line in md_text.split('\n'):
                line = line.strip()
                if not line or line.startswith('#') or line.startswith('---') or line.startswith('>') or line.startswith('-') or line.startswith('*') or line.startswith('|') or line.startswith('```'): continue
                desc = line; break
            desc = re.sub(r'\*\*|`|\[([^\]]+)\]\([^)]+\)', r'\1', desc)[:150]
            cards.append(f'<a href="{html_rel}" class="card"><div class="card-name">{escape_html(title)}</div>'
                         f'<div class="card-desc">{escape_html(desc)}</div>'
                         f'<div class="card-meta"><span>{words:,} palabras</span><span>~{mins} min</span><span class="card-path">{rel.name}</span></div></a>')
        label = group_name[3:] if len(group_name) > 2 and group_name[2] == '-' else group_name
        sections.append(f'<section class="group"><h2 class="group-title">{label}</h2><div class="cards">{"".join(cards)}</div></section>')

    index_css = CSS + """
.hero { max-width: 1100px; margin: 0 auto; padding: var(--s9) var(--s6) var(--s7); text-align: center; }
.hero-eyebrow { font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; letter-spacing: 0.25em; color: var(--accent); text-transform: uppercase; margin-bottom: var(--s5); }
.hero h1 { font-size: 4rem; margin-bottom: var(--s4); }
.hero p { font-size: 1.15rem; color: var(--ink-dim); max-width: 60ch; margin: 0 auto; }
.hero-stats { display: flex; gap: var(--s7); justify-content: center; margin-top: var(--s7); flex-wrap: wrap; }
.hero-stats span { display: flex; flex-direction: column; align-items: center; gap: var(--s1); font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: var(--ink-mute); text-transform: uppercase; letter-spacing: 0.08em; }
.hero-stats strong { font-size: 2rem; color: var(--accent); font-family: 'Newsreader', serif; font-weight: 600; }
.groups-wrap { max-width: 1100px; margin: 0 auto; padding: var(--s6) var(--s6) var(--s9); }
.group { margin-bottom: var(--s8); }
.group-title { font-size: 1.5rem; margin-bottom: var(--s5); padding-bottom: var(--s3); border-bottom: 1px solid var(--line); color: var(--ink); }
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: var(--s4); }
.card { background: var(--bg-elev); border: 1px solid var(--line); border-radius: var(--radius); padding: var(--s5); text-decoration: none; color: inherit; box-shadow: var(--shadow); display: flex; flex-direction: column; gap: var(--s3); transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s; }
.card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lift); border-color: var(--line-strong); }
.card-name { font-family: 'Newsreader', serif; font-size: 1.2rem; color: var(--ink); line-height: 1.25; font-weight: 600; }
.card-desc { font-size: 0.9rem; color: var(--ink-dim); line-height: 1.5; flex: 1; }
.card-meta { display: flex; gap: var(--s3); font-family: 'JetBrains Mono', monospace; font-size: 0.66rem; color: var(--ink-mute); text-transform: uppercase; letter-spacing: 0.05em; padding-top: var(--s3); border-top: 1px solid var(--line); flex-wrap: wrap; }
.card-path { color: var(--accent); margin-left: auto; }
"""
    index_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Affiliate Business · Index</title>
{THEME_INIT}
{FONTS}
<style>{index_css}</style>
</head>
<body>
<nav class="topbar"><a class="home" href="index.html">Affiliate Business</a><div class="right"><span class="meta">Equipo Romi · Cris · Dali</span><button class="theme-toggle" aria-label="Cambiar tema">{SUN_MOON}</button></div></nav>
<header class="hero">
<div class="hero-eyebrow">Confidencial · Sistema operativo del proyecto</div>
<h1>Affiliate Business</h1>
<p>Playbook, viabilidad, SOPs, plan comercial e investigaciones data-driven. Click en cualquier card para abrirla.</p>
<div class="hero-stats"><span><strong>{len(md_files)}</strong>documentos</span><span><strong>{total_words:,}</strong>palabras</span><span><strong>~{total_min}</strong>min lectura</span></div>
</header>
<main class="groups-wrap">{"".join(sections)}</main>
<script>{JS}</script>
</body>
</html>"""
    (REPO_ROOT / 'index.html').write_text(index_html, encoding='utf-8')

def main():
    # single-file mode (prototype)
    if len(sys.argv) > 1:
        target = Path(sys.argv[1]).resolve()
        if not target.exists():
            print(f"No existe: {target}"); return
        out = target.with_suffix('.html')
        mins, words = render_html(target, out)
        print(f"✓ {target.name} → {out.name} ({words:,} palabras, ~{mins} min) [single-file, index intacto]")
        return
    md_files = find_md_files()
    print(f"Encontrados {len(md_files)} archivos .md")
    stats = {}
    for md in md_files:
        try:
            stats[md] = render_html(md, md.with_suffix('.html'))
            print(f"  ✓ {md.relative_to(REPO_ROOT)}")
        except Exception as e:
            print(f"  ✗ ERROR {md}: {e}")
            import traceback; traceback.print_exc()
            stats[md] = (1, 0)
    build_index(md_files, stats)
    print(f"\n✓ index.html + {len(md_files)} HTMLs generados")

if __name__ == "__main__":
    main()
