# Dokumentation: 09_Bezugsdauer.ipynb

## Zweck

Letztes (nachrangiges) Themenfeld aus [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md):
wie lange und in welcher Haushaltskonstellation Menschen im SGB-II-Bezug stehen —
Haushaltsstruktur, Langzeitleistungsbezug (LZB) und Bewegungsdynamik ("Drehtür-Effekt").

## Input

- `Data/RegensburgJCData/*.xlsx`, Tabellenblätter **"3.1 Bedarfsgemeinschaften"**,
  **"3.4 Langzeitleistungsbezug"** und **"3.5 Bewegungen Personen"** — **neu eingelesen**,
  direkt aus den Excel-Rohdaten (wie schon Kapitel 6–8), nicht aus `eckwerte_long.csv`.

⚠️ **Wartezeit:** wie bei den Blättern 3.3/3.6/4.1/4.2 nur ein Datenblock mit **3 Monaten
Wartezeit** → Zeitreihe für **Oktober 2024 – Juni 2026**. Der Berichtsmonat steht hier
direkt als Datum in Zelle B32 (nicht als Text wie bei den anderen Blättern).

## Output

- `Docs/Abbildungen/` abb25–abb28 (BG-Größe, BG-Typ, LZB vs. LZA, Drehtür-Effekt) — für Projektdokumentation und -präsentation, erzeugt über
  `export_abbildung()` (Kopie im weißen Layout, gleiche Pixelmaße wie bisher).
- `Data/processed/bezugsdauer_sgb2.csv` — Wide-Format-Zeitreihe mit BG-Struktur (Größe,
  Typ), LZB/LZA sowie Bewegungskennzahlen. Grundlage für den Dashboard-Tab "⏳ Bezugsdauer".

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, Erklärung der drei kombinierten Blätter.
2. **Setup & Parsing** — `parse_bezugsdauer(path)`: kombiniert feste Zellen aus allen drei
   Blättern (jeweils Spalte B, Berichtsmonat aus Zelle B32).
3. **1. Datenüberblick und Plausibilitätsprüfung**
   - **Befund:** 21 lückenlose Monate, Haushaltsgrößen-Klassen summieren sich exakt zur
     BG-Gesamtzahl.
4. **2. Struktur der Bedarfsgemeinschaften: Größe und Typ**
   - Gestapelte Fläche (Größe) + Liniendiagramm (Typ).
   - **Befund:** Single-BG nehmen relativ zu (Anteil 57,0 % → 59,4 %), Alleinerziehende-
     und Partner-BG gehen zurück — zunehmend von Einpersonenhaushalten geprägter Bezug.
5. **3. Langzeitleistungsbezug (LZB) vs. Langzeitarbeitslosigkeit (LZA)**
   - Zwei-Achsen-Chart: LZB absolut + Anteil an ELB, plus LZA zum Vergleich.
   - **Befund:** LZB-Anteil steigt von 48,9 % auf 56,3 % — über die Hälfte aller ELB im
     Langzeitbezug; LZA (aus diesem Blatt) steigt parallel von 461 auf 709.
6. **4. Bewegungsdynamik: der „Drehtür-Effekt“**
   - Liniendiagramm: Anteil Zugang mit Vorbezug + Drehtür-Quote.
   - **Befund:** Anteil der Zugänge mit Vorbezug steigt deutlich (56,1 % → 70,9 %) — echte
     Erstzugänge werden seltener. Drehtür-Quote schwankt stark (Ø 25,4 %) ohne klaren Trend.
7. **5. Export** — Schreibt `bezugsdauer_sgb2.csv`.
8. **6. Zusammenfassung (Markdown)** — fasst alle Befunde zusammen, ordnet sie in den
   Gesamtkontext der Verschärfung der Langzeitarbeitslosigkeit ein.

## Enthaltene Diagramme (4 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Gestapelte Fläche | ✅ Plotly | BG nach Haushaltsgröße |
| 2 | Liniendiagramm (4 Linien) | ✅ Plotly | BG nach Typ |
| 3 | Zwei-Achsen-Liniendiagramm | ✅ Plotly | LZB (absolut + Anteil) vs. LZA |
| 4 | Liniendiagramm | ✅ Plotly | Zugang mit Vorbezug + Drehtür-Quote |

## Voraussetzungen

- Python-Pakete: `openpyxl`, `pandas`, `plotly`
- Rohdaten unter `Data/RegensburgJCData/*.xlsx` müssen vorhanden sein

## Verwandte Dateien

- Priorisierung offener Themen: [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
- Anknüpfungspunkt Langzeitarbeitslosigkeit: [`03_Statistik.ipynb`](../Notebooks/03_Statistik.ipynb) /
  [`03_Statistik.md`](03_Statistik.md)
- Vergleichbare Vorgehensweise: [`06_Erwerbstaetigkeit.ipynb`](../Notebooks/06_Erwerbstaetigkeit.ipynb),
  [`07_Finanzen.ipynb`](../Notebooks/07_Finanzen.ipynb), [`08_Foerderung.ipynb`](../Notebooks/08_Foerderung.ipynb)
- Dashboard-Umsetzung: [`../Dashboard/app.py`](../Dashboard/app.py), Tab "⏳ Bezugsdauer"
