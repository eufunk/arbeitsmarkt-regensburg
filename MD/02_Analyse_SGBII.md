# Dokumentation: 02_Analyse_SGBII.ipynb

## Zweck

Baut auf den von [`01_Exploration.ipynb`](01_Exploration.md) exportierten CSV-Dateien auf und
enthält die **gesamte Visualisierung und inhaltliche Auswertung** der Arbeitsmarktdaten des
Jobcenters Regensburg (Rechtskreis **SGB II**, Januar 2025 – Juni 2026). Alle Grafiken des
Notebook-Teils liegen hier. Ausgewertet wird ausschließlich der SGB-II-Anteil (Jobcenter-
Zuständigkeit) — die parallel vorliegende "Insgesamt (SGB II+SGB III)"-Spalte aus den Rohdaten
wird nicht visualisiert.

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
2. **Setup & Laden** — Imports (`matplotlib`, `pandas`, `plotly.graph_objects`), Laden der
   beiden CSVs, Rekonstruktion der sechs Kennzahl-Serien (`bestand`, `quote`, `lza`, `uq`,
   `bg`, `pers`) aus der Wide-Tabelle `kennzahlen`.
3. **1. Übersicht: Kennzahlen im Vergleich**
   - Kurzerklärung, was SGB II bedeutet (Bürgergeld/Jobcenter) und Abgrenzung zu SGB III
     (Arbeitslosengeld I/Agentur für Arbeit).
   - **Interaktiver Plotly-Kombichart** (`go.Figure`, `barmode="overlay"`, `hovermode="x
     unified"`): Fläche "Personen in BG" im Hintergrund, davor überlappende Balken für
     Bedarfsgemeinschaften, Arbeitslose (Bestand) und Langzeitarbeitslose, jeweils mit einer
     zusätzlichen Linie+Marker-Spur zum genauen Ablesen der Werte per Mouseover. Das ist der
     zentrale Einstiegs-Chart des Notebooks.
4. **2. Arbeitslosen- und Unterbeschäftigungsquote**
   - Erklärtext zur Bezugsgröße: beide Quoten sind Anteilswerte bezogen auf alle zivilen
     Erwerbspersonen Regensburgs, nicht nur die SGB-II-Fälle.
   - Interaktiver Plotly-Lineplot (zwei Linien, `hovermode="x unified"`, `yaxis_ticksuffix="%"`):
     Arbeitslosenquote vs. Unterbeschäftigungsquote.
5. **3. Langzeitarbeitslosigkeit**
   - Interaktiver Plotly-Lineplot: Anteil der Langzeitarbeitslosen am Arbeitslosenbestand in
     Prozent (`lza / bestand * 100`, gerundet, `%`-Achse). Die absolute Entwicklung steckt
     bereits im Übersichtschart.
   - Textausgabe: Start- vs. Endwert (absolut und Anteil).
6. **4. Kennzahlen im Vergleich (indexiert)**
   - Erklärtext, wie der Index zu lesen ist (100 = Startmonat, 110 = +10 %, 90 = −10 %).
   - Interaktiver Plotly-Lineplot: alle vier Kernkennzahlen auf den ersten Berichtsmonat
     indexiert (= 100 % gesetzt, gerundet auf eine Nachkommastelle), um ihre relative
     Entwicklung trotz unterschiedlicher Größenordnungen in einem Diagramm vergleichbar zu
     machen. Gestrichelte Linie bei 100 % als Referenz.
7. **5. Altersstruktur und Geschlecht (letzter Berichtsmonat)**
   - Zwei Matplotlib-Balkendiagramme (ein Figure, zwei Subplots) für den aktuellsten
     Berichtsmonat: Altersgruppen (15–25 / 25–50 / 50+) und Geschlecht (Männer/Frauen) der
     SGB-II-Arbeitslosen. Reine Momentaufnahme, keine Zeitreihe. Einziger noch nicht auf
     Plotly umgestellter Chart im Notebook.
8. **6. Veränderung zum Vormonat und zum Vorjahresmonat**
   - Tabelle (`changes`): absolute und prozentuale Veränderung von Bestand, Langzeitarbeitslosen,
     Bedarfsgemeinschaften und Personen in BG gegenüber Vormonat (`.iloc[-2]`) und
     Vorjahresmonat (`.iloc[-13]`).
9. **7. Zusammenfassung (Markdown)**
   - Textliche Einordnung der wichtigsten Befunde:
     - Arbeitslose (Bestand): 1.470 (Jan 2025) → 1.500 (Jun 2026), Spanne 1.382–1.587
     - Arbeitslosenquote: stabil zwischen 1,2 % und 1,4 %
     - Langzeitarbeitslose: 502 → 709 (+ ca. 41 %), deutlichster Trend im Datensatz
     - Bedarfsgemeinschaften / Personen in BG: beide rückläufig (ca. −4 % bzw. −6 %)

## Enthaltene Diagramme (5 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Fläche + überlappende Balken + Linien (Übersicht) | ✅ Plotly | Personen in BG, Bedarfsgemeinschaften, Arbeitslose, Langzeitarbeitslose in einem Chart |
| 2 | Lineplot (2 Linien) | ✅ Plotly | Arbeitslosen- vs. Unterbeschäftigungsquote |
| 3 | Lineplot | ✅ Plotly | Anteil Langzeitarbeitslose an allen Arbeitslosen |
| 4 | Lineplot (4 Linien, indexiert) | ✅ Plotly | Kernkennzahlen im Vergleich, Basis = 100 % |
| 5 | Barplot (2 Subplots) | ❌ Matplotlib | Altersstruktur + Geschlecht (letzter Monat) |

Alle interaktiven Charts nutzen `hovermode="x unified"`: Maus über einen Monat zeigt alle
Werte an dieser Stelle gemeinsam als eine Tooltip-Box statt einzeln pro Linie.

Bewusst entfernt (redundant zur Übersicht): Bestand-Arbeitslose als eigenständiger
Linien-/Balkenchart, Bedarfsgemeinschaften/Personen-in-BG als eigener Dualachsen-Chart.

Scatterplot, Histogramm, Boxplot und Heatmap sind mittlerweile in
[`03_Statistik.ipynb`](../Notebooks/03_Statistik.ipynb) enthalten (siehe
[`03_Statistik.md`](03_Statistik.md)), nicht hier.

## Voraussetzungen

- Python-Pakete: `pandas`, `matplotlib`, `plotly`
- CSVs aus `01_Exploration.ipynb` müssen vorhanden sein

## Verwandte Dateien

- Datengrundlage: [`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
  [`01_Exploration.md`](01_Exploration.md)
- Vertiefende Statistik (Korrelation, Hypothesentest, Regression):
  [`03_Statistik.ipynb`](../Notebooks/03_Statistik.ipynb) / [`03_Statistik.md`](03_Statistik.md)
- Themenabgleich gegen den Lernplan: [`ThemenCheck.md`](ThemenCheck.md)
- Inhaltliche Themenübersicht (analysiert/offen): [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
- Der Übersichtschart und der Quote-Chart existieren in gleicher Form auch im
  [Dashboard](../Dashboard/README.md) (Tab "SGB II Übersicht"), dort zusätzlich mit
  Trichter-Grafik (RLB/ELB-Aufschlüsselung) und formatierter Kennzahlen-Tabelle, die im
  Notebook (noch) nicht vorhanden sind.
