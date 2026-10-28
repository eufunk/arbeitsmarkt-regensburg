# Dokumentation: 14_Beschaeftigung.ipynb

## Zweck

Letzter offener Punkt aus [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md): Das Blatt
"1.1 Eckwerte" enthält — unterhalb der bisher genutzten Zeilen 9–47 — noch einen weiteren,
eigenständigen Block: eine **quartalsweise Beschäftigtenstatistik** (sozialversicherungspflichtig
und ausschließlich geringfügig entlohnte Beschäftigung, jeweils nach **Arbeitsort (AO)** und
**Wohnort (WO)**) — das Gegenstück zur Arbeitslosigkeit.

**Arbeitsort vs. Wohnort:** AO zählt Beschäftigungsverhältnisse, deren Arbeitsplatz in
Regensburg liegt; WO zählt Personen, die in Regensburg wohnen, unabhängig vom Arbeitsort. Die
Differenz WO − AO ist der **Pendlersaldo**.

## Input

- `Data/RegensburgJCData/*.xlsx` (21 Monatsberichte), Blatt "1.1 Eckwerte", **Zeilen 49–58**
  (bislang ungenutzter Bereich unterhalb der Hauptkennzahlen) — direkt neu eingelesen.

⚠️ **Wichtige Einschränkung — abweichender Rhythmus und Zeitraum:** Dieser Block ist
**quartalsweise** (nicht monatlich) und hat laut Fußnote im Bericht eine **Wartezeit von 6
Monaten**. In den 21 Monatsberichten tauchen dadurch nur **8 unterschiedliche Quartale** auf,
jeweils identisch über bis zu 3 aufeinanderfolgende Monatsberichte gemeldet — das abgedeckte
Zeitfenster liegt entsprechend früher: **Juni 2024 – März 2026**, statt Januar 2025 – September
2026 wie in den übrigen Kapiteln.

## Output

- `Data/processed/beschaeftigung_quartal.csv` — Quartals-Zeitreihe (8 Zeilen) mit den Spalten
  `ao_svp`, `wo_svp`, `ao_geringfuegig`, `wo_geringfuegig`.
- `Docs/Abbildungen/abb41_beschaeftigung_ao_wo.png`, `abb42_beschaeftigung_pendlersaldo.png`,
  `abb43_beschaeftigung_anteil_geringfuegig.png` — für Kapitel 15 der
  Projektdokumentation/-präsentation.

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, AO/WO-Begriffe, Hinweis zu Rhythmus und Zeitraum.
2. **Setup & Extraktion** — `parse_beschaeftigung()` liest Zeile 49 (Quartalsdatum) und Zeilen
   55–58 (vier Kennzahlen, jeweils Spalte B) aus jedem der 21 Berichte; `drop_duplicates()`
   reduziert auf die 8 tatsächlich eindeutigen Quartale.
3. **1. Sozialversicherungspflichtige Beschäftigung: Arbeitsort vs. Wohnort**
   - **Befund:** Beide Werte bemerkenswert stabil (AO 54.214–55.331, WO 88.011–89.259),
     WO durchgehend rund 34.000 über AO.
4. **2. Pendlersaldo**
   - **Befund:** Außergewöhnlich stabiler Auspendlerüberschuss von 33.557–34.069 Personen
     (Ø ≈ 33.882) über alle 8 Quartale — kaum Schwankung; Tiefstwert im jüngsten Quartal
     (März 2026), weil die AO-Beschäftigung etwas stärker steigt als die WO-Beschäftigung.
5. **3. Geringfügig entlohnte Beschäftigung: Arbeitsort vs. Wohnort**
   - **Befund:** Leicht rückläufig in beiden Perspektiven (AO −2,6 %, WO −2,4 %).
6. **4. Anteil geringfügiger Beschäftigung an der Gesamtbeschäftigung**
   - **Befund:** Anteil sinkt leicht (AO 13,3 % → 12,9 %, WO 10,8 % → 10,5 %) — passend zur in
     Kapitel 7 beobachteten Verschiebung zu höheren Einkommen bei den Aufstockern.
7. **5. Zusammenfassung (Markdown)** — fasst den stabilen Pendlersaldo als zentralen neuen
   Befund zusammen und markiert den Abschluss der priorisierten Themenliste aus
   `ArbeitslosenAnalyse.md`.
8. **Export** — schreibt `beschaeftigung_quartal.csv`.

## Enthaltene Diagramme (4 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Liniendiagramm (2 Linien) | ✅ Plotly | Sozialversicherungspflichtig Beschäftigte: AO vs. WO |
| 2 | Balkendiagramm | ✅ Plotly | Pendlersaldo (WO − AO) |
| 3 | Liniendiagramm (2 Linien) | ✅ Plotly | Geringfügig entlohnte Beschäftigung: AO vs. WO |
| 4 | Liniendiagramm (2 Linien) | ✅ Plotly | Anteil geringfügiger Beschäftigung an der Gesamtbeschäftigung |

## Voraussetzungen

- Python-Pakete: `pandas`, `openpyxl`, `plotly`

## Verwandte Dateien

- Datengrundlage: [`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
  [`01_Exploration.md`](01_Exploration.md)
- Aufstockerquote (Vergleich zur Einkommensverschiebung): [`06_Erwerbstaetigkeit.ipynb`](../Notebooks/06_Erwerbstaetigkeit.ipynb)
- Priorisierung offener Themen: [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
