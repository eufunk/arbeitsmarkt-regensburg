# Dokumentation: 02_Analyse.ipynb

## Zweck

Baut auf den von [`01_Exploration.ipynb`](01_Exploration.md) exportierten CSV-Dateien auf und
enthält die **gesamte Visualisierung und inhaltliche Auswertung** der Arbeitsmarktdaten des
Jobcenters Regensburg (Rechtskreis SGB II, April 2025 – Juni 2026). Alle Grafiken des Projekts
liegen in diesem Notebook.

## Input

- `Data/processed/eckwerte_long.csv` (Long-Format, siehe 01_Exploration.md)
- `Data/processed/kennzahlen_sgb2.csv` (Wide-Format-Zeitreihe, siehe 01_Exploration.md)

Beide werden per `pd.read_csv()` geladen; `period` wird als `PeriodIndex` (long-Format) bzw.
als geparstes Datum (`parse_dates`, wide-Format) wiederhergestellt.

⚠️ Voraussetzung: `01_Exploration.ipynb` muss vorher mindestens einmal komplett gelaufen sein,
sonst fehlen die CSVs.

## Output

Keine Datei-Exporte — das Notebook dient der visuellen/inhaltlichen Auswertung innerhalb von
Jupyter (Diagramme + Tabellen als Zell-Output).

## Ablauf (Zellen)

1. **Intro (Markdown)** — Verweis auf `01_Exploration.ipynb` als Datenquelle.
2. **Setup & Laden** — Imports (`matplotlib`, `pandas`), `matplotlib`-Defaults (Grid, Figurgröße),
   Laden der beiden CSVs, Rekonstruktion der sechs Kennzahl-Serien
   (`bestand`, `quote`, `lza`, `uq`, `bg`, `pers`) aus der Wide-Tabelle `kennzahlen`.
3. **1. Entwicklung der Arbeitslosigkeit (SGB II)**
   - Lineplot: Bestand Arbeitslose über die Zeit.
   - Lineplot: Arbeitslosenquote vs. Unterbeschäftigungsquote (zwei Linien, gemeinsame Achse).
4. **2. Langzeitarbeitslosigkeit**
   - Zwei nebeneinanderliegende Lineplots: absolute Zahl der Langzeitarbeitslosen sowie ihr
     Anteil am gesamten Arbeitslosenbestand (`lza / bestand * 100`).
   - Textausgabe: Start- vs. Endwert (absolut und Anteil).
5. **3. Grundsicherung: Bedarfsgemeinschaften und Personen im Leistungsbezug**
   - Lineplot mit zwei Y-Achsen (`twinx`): Bedarfsgemeinschaften (links) und Personen in BG
     (rechts) in einem Diagramm.
6. **4. Altersstruktur und Geschlecht (letzter Berichtsmonat)**
   - Zwei Balkendiagramme für den jeweils aktuellsten Berichtsmonat: Altersgruppen
     (15–25 / 25–50 / 50+) und Geschlecht (Männer/Frauen) der SGB-II-Arbeitslosen.
7. **5. Veränderung zum Vormonat und zum Vorjahresmonat**
   - Tabelle (`changes`): absolute und prozentuale Veränderung von Bestand, Langzeitarbeitslosen,
     Bedarfsgemeinschaften und Personen in BG gegenüber Vormonat (`.iloc[-2]`) und
     Vorjahresmonat (`.iloc[-13]`).
8. **6. Zusammenfassung (Markdown)**
   - Textliche Einordnung der wichtigsten Befunde:
     - Arbeitslose (Bestand): 1.457 (Apr 2025) → 1.500 (Jun 2026), Spanne 1.438–1.587
     - Arbeitslosenquote: stabil zwischen 1,2 % und 1,4 %
     - Langzeitarbeitslose: 526 → 709 (+ ca. 35 %), deutlichster Trend im Datensatz
     - Bedarfsgemeinschaften / Personen in BG: beide rückläufig (je ca. −5 %)

## Enthaltene Diagramme (5 insgesamt)

| # | Diagrammtyp | Inhalt |
|---|---|---|
| 1 | Lineplot | Arbeitslose (Bestand) über die Zeit |
| 2 | Lineplot (2 Linien) | Arbeitslosen- vs. Unterbeschäftigungsquote |
| 3 | Lineplot (2 Subplots) | Langzeitarbeitslose absolut + Anteil |
| 4 | Lineplot (Dual-Achse) | Bedarfsgemeinschaften + Personen in BG |
| 5 | Barplot (2 Subplots) | Altersstruktur + Geschlecht (letzter Monat) |

Noch nicht enthalten (siehe [`ThemenCheck.md`](ThemenCheck.md)): Scatterplot, Histogram,
Boxplot, Heatmap, interaktive Plotly-Diagramme.

## Voraussetzungen

- Python-Pakete: `pandas`, `matplotlib`
- CSVs aus `01_Exploration.ipynb` müssen vorhanden sein

## Verwandte Dateien

- Datengrundlage: [`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
  [`01_Exploration.md`](01_Exploration.md)
- Themenabgleich gegen den Lernplan: [`ThemenCheck.md`](ThemenCheck.md)
