# Dokumentation: 10_Rechtskreisvergleich.ipynb

## Zweck

Letzter offener Punkt aus [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md): Vergleich
"Insgesamt (SGB II+SGB III)" vs. "SGB II" — wie hoch ist der Jobcenter-Anteil an der
gesamten Arbeitslosigkeit, und verändert er sich über die Zeit? Leitet dafür den
**SGB-III-Anteil** (Agentur für Arbeit) als Differenz her: SGB III = Insgesamt − SGB II.

## Input

- `Data/processed/eckwerte_long.csv` (Langformat aus `01_Exploration.ipynb`) — enthält die
  Spalten `insgesamt` und `sgb2` bereits für jede Zeile.

**Keine neuen Rohdaten nötig** — anders als die Kapitel 6–9 liest dieses Notebook nur die
bereits aufbereitete CSV, keine Excel-Dateien. Keine Wartezeit-Problematik, volle 21 Monate
Januar 2025 – September 2026 (wie [`02_Analyse_SGBII.ipynb`](02_Analyse_SGBII.md)).

## Output

- `Docs/Abbildungen/` abb29–abb31 (Bestand, Langzeitarbeitslose, Quoten im Rechtskreisvergleich) — für Projektdokumentation und -präsentation, erzeugt über
  `export_abbildung()` (Kopie im weißen Layout, gleiche Pixelmaße wie bisher).
- `Data/processed/rechtskreisvergleich_sgb2.csv` — Wide-Format-Zeitreihe mit
  Insgesamt/SGB II/SGB III/Jobcenter-Anteil (%) für vier Kennzahlen: Arbeitslose (Bestand),
  Arbeitslosenquote, Langzeitarbeitslose, Unterbeschäftigungsquote.

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, Erklärung der Herleitung SGB III = Insgesamt − SGB II.
2. **Setup & Laden** — Filtert `eckwerte_long.csv` auf vier Merkmale, berechnet je Merkmal
   Insgesamt/SGB II/SGB III/Jobcenter-Anteil.
3. **1. Jobcenter-Anteil am Arbeitslosenbestand insgesamt**
   - Gestapelte Fläche (SGB II + SGB III) + Anteil-Linie.
   - **Befund:** Jobcenter-Anteil stabil bei Ø 39,7 % (36,3–42,2 %; zuletzt seit Mai 2026
     sinkend auf 38,6 %) — die Mehrheit der Arbeitslosen (≈ 60 %) fällt in die Zuständigkeit
     der Agentur für Arbeit (SGB III).
4. **2. Langzeitarbeitslosigkeit: konzentriert sich das stärker im SGB II?**
   - Gleiche Darstellung für Langzeitarbeitslose.
   - **Befund:** Jobcenter-Anteil hier deutlich höher, Ø 72,2 % (69,1–75,9 %) — plausibel
     durch die zeitliche Befristung von Arbeitslosengeld I (SGB III). SGB-III-LZA wächst
     sogar noch stärker (+ 58 %, 185 → 292) als SGB-II-LZA (+ 39 %, 502 → 698).
5. **3. Quoten im Vergleich: Arbeitslosenquote und Unterbeschäftigungsquote**
   - Vier Linien: Insgesamt/SGB II je Quote.
   - **Befund:** SGB-II-Anteil an der Arbeitslosenquote ≈ 40 % (analog zum Bestand),
     an der Unterbeschäftigungsquote Ø 45,2 % (rückläufig, 47,5 % → 42,5 %).
6. **4. Export** — Schreibt `rechtskreisvergleich_sgb2.csv`.
7. **5. Zusammenfassung (Markdown)** — fasst alle Befunde zusammen: der Jobcenter-Fokus
   dieses Projekts bildet nur ~40 % der Gesamtarbeitslosigkeit ab, aber überproportional
   den Teil mit konzentrierter Langzeitarbeitslosigkeit.

## Enthaltene Diagramme (3 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Gestapelte Fläche + Linie (2 Achsen) | ✅ Plotly | Arbeitslose: SGB II vs. SGB III + Anteil |
| 2 | Gestapelte Fläche + Linie (2 Achsen) | ✅ Plotly | Langzeitarbeitslose: SGB II vs. SGB III + Anteil |
| 3 | Liniendiagramm (4 Linien) | ✅ Plotly | Arbeitslosen-/Unterbeschäftigungsquote: Insgesamt vs. SGB II |

## Voraussetzungen

- Python-Pakete: `pandas`, `plotly`
- CSV aus `01_Exploration.ipynb` muss vorhanden sein

## Verwandte Dateien

- Datengrundlage: [`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
  [`01_Exploration.md`](01_Exploration.md)
- SGB-II-Bestandsanalyse: [`02_Analyse_SGBII.ipynb`](../Notebooks/02_Analyse_SGBII.ipynb) /
  [`02_Analyse_SGBII.md`](02_Analyse_SGBII.md)
- Langzeitarbeitslosigkeits-Trend: [`03_Statistik.ipynb`](../Notebooks/03_Statistik.ipynb) /
  [`03_Statistik.md`](03_Statistik.md)
- Priorisierung offener Themen: [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
