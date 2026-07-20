#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open("/tmp/claude-0/-home-user-CalmCut/14eb46c2-9f54-5929-a895-373ef3f32d20/scratchpad/bible_data.json", encoding="utf-8") as f:
    data = json.load(f)

scenes = data["scenes"]
assets = data["assets"]
BASE_STYLE = data["base_style"]
CONSISTENCY = data["consistency"]
NEGATIVE = data["negative"]

HEAD = '''<title>Illustration Bible v2 — Οι Περιπέτειες των Συναισθημάτων</title>
<style>
  :root {
    --paper: #FBFAFF; --ink: #2E2A47; --ink-soft: #5A5578;
    --card: #FFFFFF; --line: rgba(46,42,71,0.14);
    --coral: #E85D42; --coral-soft: #FDE4DD;
    --yellow: #F4B93C; --yellow-soft: #FDF0D2;
    --sage: #5AA588; --sage-soft: #E1F1EA;
    --purple: #7B6FC4; --purple-soft: #EAE6F9;
    --blue-soft: #E3EEF6;
  }
  :root[data-theme="dark"] {
    --paper: #1B1830; --ink: #EDEAFB; --ink-soft: #B6AFD6;
    --card: #252140; --line: rgba(237,234,251,0.14);
    --coral-soft: #4A2A26; --yellow-soft: #4A3C1E; --sage-soft: #1E3A30; --purple-soft: #322A54; --blue-soft: #223244;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --paper: #1B1830; --ink: #EDEAFB; --ink-soft: #B6AFD6;
      --card: #252140; --line: rgba(237,234,251,0.14);
      --coral-soft: #4A2A26; --yellow-soft: #4A3C1E; --sage-soft: #1E3A30; --purple-soft: #322A54; --blue-soft: #223244;
    }
  }
  * { box-sizing: border-box; }
  body {
    background: var(--paper); color: var(--ink);
    font-family: "Source Sans 3", Verdana, "Segoe UI", Arial, sans-serif;
    max-width: 920px; margin: 0 auto; padding: 56px 24px 100px; line-height: 1.6;
  }
  h1.title {
    font-family: "Comfortaa", "Trebuchet MS", sans-serif; font-weight: 700;
    color: var(--purple); font-size: clamp(1.6rem, 4vw, 2.1rem); text-align: center; text-wrap: balance; margin: 0 0 6px;
  }
  .subtitle { text-align: center; color: var(--ink-soft); font-size: 1rem; margin: 0 0 10px; }
  .lock-note {
    display: block; text-align: center; font-size: 0.8rem; color: var(--sage);
    background: var(--sage-soft); width: fit-content; margin: 0 auto 12px; padding: 6px 16px; border-radius: 20px; font-weight: bold;
  }
  .count-note {
    display: block; text-align: center; font-size: 0.85rem; color: var(--purple);
    background: var(--purple-soft); width: fit-content; margin: 0 auto 36px; padding: 6px 16px; border-radius: 20px; font-weight: bold;
  }

  h2.section-h {
    font-family: "Comfortaa", "Trebuchet MS", sans-serif; font-weight: 700; font-size: 1.3rem; color: var(--ink);
    margin: 56px 0 8px; display: flex; align-items: center; gap: 12px;
  }
  h2.section-h::after { content: ""; flex: 1; height: 2px; background: var(--line); }
  .section-sub { color: var(--ink-soft); font-size: 0.88rem; margin: 0 0 24px; }

  .base-card {
    background: var(--card); border: 1px solid var(--line); border-radius: 14px;
    padding: 22px 26px; margin-bottom: 24px;
  }
  .base-card h3 { font-family: "Comfortaa", "Trebuchet MS", sans-serif; font-size: 1.05rem; margin: 0 0 12px; color: var(--purple); }
  .base-block {
    background: var(--ink); color: #F3F1FB; border-radius: 10px; padding: 14px 18px;
    font-family: monospace; font-size: 0.82rem; line-height: 1.65; margin-bottom: 10px; overflow-x: auto; white-space: pre-wrap;
  }
  .base-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--ink-soft); margin: 14px 0 4px; font-weight: bold; }

  .toc { columns: 3; gap: 20px; margin-bottom: 20px; font-size: 0.8rem; }
  .toc a { color: var(--ink); text-decoration: none; display: block; padding: 2px 0; }
  .toc a:hover { color: var(--purple); }

  .img-card {
    background: var(--card); border: 1px solid var(--line); border-radius: 14px;
    padding: 22px 26px; margin-bottom: 20px; scroll-margin-top: 20px;
  }
  .img-head { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; flex-wrap: wrap; }
  .img-id { font-family: "Comfortaa", "Trebuchet MS", sans-serif; font-weight: 700; font-size: 1.1rem; color: var(--coral); }
  .tag {
    font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.04em;
    padding: 3px 9px; border-radius: 12px; font-weight: bold;
  }
  .tag.size { background: var(--purple-soft); color: var(--purple); }
  .tag.prio-HIGH { background: var(--coral-soft); color: var(--coral); }
  .tag.prio-MEDIUM { background: var(--yellow-soft); color: #8a6d1a; }
  .tag.prio-LOW { background: var(--sage-soft); color: var(--sage); }
  .img-page { font-size: 0.82rem; color: var(--ink-soft); margin-left: auto; }

  .meta-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px,1fr)); gap: 6px 18px; margin-bottom: 12px; font-size: 0.83rem; }
  .meta-grid dt { font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.04em; color: var(--ink-soft); }
  .meta-grid dd { margin: 0; }

  .desc { font-size: 0.88rem; margin-bottom: 12px; }
  .prompt-block {
    background: var(--ink); color: #F3F1FB; border-radius: 10px; padding: 11px 15px;
    font-family: monospace; font-size: 0.78rem; line-height: 1.55; margin-bottom: 8px; overflow-x: auto; white-space: pre-wrap;
  }
  .field-label { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--ink-soft); font-weight: bold; margin: 8px 0 4px; }

  .asset-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px,1fr)); gap: 14px; margin-bottom: 8px; }
  .asset-card {
    background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 14px 16px;
  }
  .asset-head { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
  .asset-id { font-family: monospace; font-weight: bold; color: var(--coral); font-size: 0.85rem; }
  .asset-name { font-weight: bold; font-size: 0.9rem; }
  .asset-prompt {
    font-family: monospace; font-size: 0.72rem; color: var(--ink-soft); line-height: 1.5;
    background: var(--paper); border: 1px dashed var(--line); border-radius: 8px; padding: 8px 10px; margin-top: 6px;
  }
  .cat-group { margin-bottom: 28px; }
  .cat-title { font-weight: bold; font-size: 0.95rem; color: var(--purple); margin-bottom: 10px; }
</style>

<h1 class="title">Illustration Bible v2</h1>
<p class="subtitle">«Οι Περιπέτειες των Συναισθημάτων» — πλήρες πακέτο παραγωγής εικόνων</p>
<span class="lock-note">🔒 Manuscript κλειδωμένο μετά από editorial QA — οι σελίδες εδώ είναι οριστικές</span>
<span class="count-note">26 σκηνές (Full/Half/Spot) + 39 reusable assets = 65 εικόνες συνολικά</span>

<div class="base-card">
  <h3>Base style (μπαίνει σε ΚΑΘΕ prompt)</h3>
  <div class="base-label">Style tag</div>
  <div class="base-block">''' + BASE_STYLE + '''</div>
  <div class="base-label">Consistency clause</div>
  <div class="base-block">''' + CONSISTENCY + '''</div>
  <div class="base-label">Negative prompt (μπαίνει σε ΚΑΘΕ εικόνα)</div>
  <div class="base-block">''' + NEGATIVE + '''</div>
  <p style="font-size:0.85rem; color:var(--ink-soft); margin:10px 0 0;">
    <strong>Μεγέθη:</strong> Full page (3:4, ολοσέλιδη) · Half page (4:3, μοιράζεται με κείμενο) · Spot (4:3, μικρή)<br>
    <strong>Priority:</strong> <span class="tag prio-HIGH">HIGH</span> = απαραίτητη πρώτα · <span class="tag prio-MEDIUM">MEDIUM</span> = σημαντική · <span class="tag prio-LOW">LOW</span> = προαιρετική/διακοσμητική, μπορεί να μπει τελευταία ή να παραλειφθεί αν λείψει χρόνος
  </p>
</div>

<h2 class="section-h">Σκηνές (26)</h2>
<p class="section-sub">Μοναδικές, αφηγηματικές εικόνες δεμένες με συγκεκριμένη σελίδα του βιβλίου.</p>

<div class="toc">
'''

toc_items = "\n".join(f'  <a href="#{s["id"]}">{s["id"]} — σελ.{s["page"]}</a>' for s in scenes)

CARDS = ""
for s in scenes:
    CARDS += f'''
<div class="img-card" id="{s['id']}">
  <div class="img-head">
    <span class="img-id">{s['id']}</span>
    <span class="tag size">{s['size']}</span>
    <span class="tag prio-{s['priority']}">{s['priority']}</span>
    <span class="img-page">Σελίδα {s['page']}</span>
  </div>
  <dl class="meta-grid">
    <div><dt>Χαρακτήρες</dt><dd>{s['chars']}</dd></div>
    <div><dt>Συναίσθημα</dt><dd>{s['emotion']}</dd></div>
    <div><dt>Camera</dt><dd>{s['camera']}</dd></div>
    <div><dt>Aspect ratio</dt><dd>{s['aspect']}</dd></div>
  </dl>
  <div class="desc"><strong>Palette:</strong> {s['palette']}</div>
  <div class="desc"><strong>Περιγραφή:</strong> {s['desc']}</div>
  <div class="field-label">Prompt (πρόσθεσε πριν το base style + consistency clause από πάνω)</div>
  <div class="prompt-block">{s['prompt']}</div>
  <div class="field-label">Safe area</div>
  <div class="desc">{s['safe']}</div>
</div>'''

ASSETS_SECTION = '''
<h2 class="section-h">Reusable Asset Library (39)</h2>
<p class="section-sub">Χαρακτήρες σε πολλαπλές στάσεις/εκφράσεις, επαναλαμβανόμενα σκηνικά, και διακοσμητικά stamps — παράγονται ΜΙΑ φορά το καθένα και ξαναχρησιμοποιούνται σε όλο το βιβλίο (πολύ πιο αποδοτικό από 60+ μοναδικές σκηνές).</p>
'''

# group assets by category preserving order
from collections import OrderedDict
grouped = OrderedDict()
for a in assets:
    grouped.setdefault(a["cat"], []).append(a)

for cat, items in grouped.items():
    ASSETS_SECTION += f'<div class="cat-group"><div class="cat-title">{cat}</div><div class="asset-grid">'
    for a in items:
        ASSETS_SECTION += f'''
    <div class="asset-card">
      <div class="asset-head"><span class="asset-id">{a['id']}</span><span class="asset-name">{a['name']}</span><span class="tag prio-{a['priority']}" style="margin-left:auto;">{a['priority']}</span></div>
      <div class="asset-prompt">{a['prompt']}</div>
    </div>'''
    ASSETS_SECTION += '</div></div>'

full_html = HEAD + toc_items + "\n</div>\n" + CARDS + "\n" + ASSETS_SECTION

with open("/tmp/claude-0/-home-user-CalmCut/14eb46c2-9f54-5929-a895-373ef3f32d20/scratchpad/illustration-bible.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Written. Total scenes:", len(scenes), "Total assets:", len(assets))
