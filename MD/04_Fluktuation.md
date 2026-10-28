# Dokumentation: 04_Fluktuation.ipynb

## Zweck

Ergänzt [`02_Analyse_SGBII.ipynb`](02_Analyse_SGBII.md), das nur den *Bestand* an
Arbeitslosen über die Zeit betrachtet, um die Dynamik dahinter: **Zugang** (neu arbeitslos
gemeldet) und **Abgang** (nicht mehr arbeitslos gemeldet) im Rechtskreis SGB II. Bearbeitet
Priorität 1 aus dem Priorisierungsvorschlag in
[`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md) — die Werte stehen bereits im Blatt
"1.1 Eckwerte" (keine zusätzliche Wartezeit-Problematik wie bei den Blättern 2.x–4.x).

## Input

- `Data/processed/eckwerte_long.csv` (Langformat aus `01_Exploration.ipynb`) — enthält
  Zugang/Abgang bereits, da `parse_eckwerte()` alle Zeilen des Blatts "1.1 Eckwerte" liest.
- `Data/processed/kennzahlen_sgb2.csv` (Wide-Format, für den Abgleich mit dem Bestand)

⚠️ Voraussetzung: `01_Exploration.ipynb` muss vorher mindestens einmal komplett gelaufen sein.
Kein erneutes Einlesen der Excel-Rohdaten nötig.

## Output

- `Data/processed/fluktuation_sgb2.csv` — Wide-Format-Zeitreihe mit Zugang/Abgang (im Monat
  und als 12-Monatssumme) sowie der berechneten Netto-Fluktuation, Rechtskreis SGB II.
  Grundlage für den Dashboard-Tab "🔄 Fluktuation".

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung gegenüber `02_Analyse_SGBII.ipynb`.
2. **Setup & Laden** — Filtert `eckwerte_long.csv` auf Kategorie "Arbeitslose" und die vier
   Merkmale Zugang/Abgang (im Monat / 12-Monatssumme), pivotiert zu einer Wide-Zeitreihe.
3. **1. Zugang und Abgang im Monatsverlauf**
   - Plotly-Balkendiagramm: Zugang als positiver, Abgang als negativer Balken.
   - **Befund:** Zugang Ø 270 Personen/Monat (215–346), Abgang Ø 283 (185–369) — im Schnitt
     etwas mehr Abgang als Zugang. Zugang: Tiefstand 215 (Jun 2026), Höchststand 346 (Aug 2026,
     Sommereffekt), zuletzt 252 (Sep 2026; Jan 2025: 271). Abgang steigt von 204 (Jan 2025) auf
     293 (Sep 2026).
4. **2. Netto-Fluktuation und Abgleich mit dem Bestand**
   - Tabelle: Netto-Fluktuation (Zugang − Abgang) vs. tatsächliche Bestandsänderung
     (`.diff()` auf `Arbeitslose (Bestand)`), als Plausibilitätscheck der Daten.
   - Plotly-Chart: Netto-Fluktuation (Balken) vs. tatsächliche Bestandsänderung (Linie).
   - **Befund:** Netto-Fluktuation liegt in 19 von 20 vergleichbaren Monaten unter der
     tatsächlichen Bestandsänderung (Ø Differenz −19,8 Personen, Spanne 0 bis −30; nur im
     September 2026 deckungsgleich). Plausibelster Grund:
     Rechtskreiswechsel SGB II ↔ SGB III schlagen sich im Bestand nieder, ohne als eigene
     Zugangs-/Abgangskategorie zu erscheinen.
5. **3. 12-Monatssummen: der mittelfristige Trend**
   - Plotly-Chart der rollierenden 12-Monatssummen von Zugang und Abgang.
   - **Befund:** Zugangstrend rückläufig (3.260 → 3.182 pro Jahr, Tiefpunkt 3.115 im Juni
     2026), Abgangstrend steigend (3.318 → 3.468) — rollierende Netto-Fluktuation
     verschlechtert sich von −58 auf −286 Personen/Jahr, ohne dass sich das bislang deutlich im
     Bestand zeigt.
6. **4. Export** — Schreibt `fluktuation_sgb2.csv`.
7. **5. Zusammenfassung (Markdown)** — fasst alle Befunde zusammen.

## Enthaltene Diagramme (3 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Balkendiagramm (gegenläufig) | ✅ Plotly | Zugang/Abgang im Monat |
| 2 | Balken + Linie | ✅ Plotly | Netto-Fluktuation vs. tatsächliche Bestandsänderung |
| 3 | Liniendiagramm | ✅ Plotly | Zugang/Abgang als 12-Monatssumme |

## Voraussetzungen

- Python-Pakete: `pandas`, `numpy`, `plotly`
- CSV aus `01_Exploration.ipynb` muss vorhanden sein

## Verwandte Dateien

- Datengrundlage: [`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
  [`01_Exploration.md`](01_Exploration.md)
- Bestands-Analyse: [`02_Analyse_SGBII.ipynb`](../Notebooks/02_Analyse_SGBII.ipynb) /
  [`02_Analyse_SGBII.md`](02_Analyse_SGBII.md)
- Priorisierung offener Themen: [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
- Dashboard-Umsetzung: [`../Dashboard/app.py`](../Dashboard/app.py), Tab "🔄 Fluktuation"
