# Dokumentation: 05_Demografie.ipynb

## Zweck

Macht aus der bisherigen **Momentaufnahme** von Altersstruktur und Geschlecht in
[`02_Analyse_SGBII.ipynb`](02_Analyse_SGBII.md) echte **Zeitreihen** und ergänzt zwei
bislang komplett unanalysierte Merkmale aus derselben Zeilengruppe: **Ausländer** und
**schwerbehinderte Menschen** unter den Arbeitslosen. Bearbeitet Priorität 2 aus dem
Priorisierungsvorschlag in [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md), erweitert um
die beiden zusätzlichen Merkmale (gleicher Datenzugriff, kein Mehraufwand).

## Input

- `Data/processed/eckwerte_long.csv` (Langformat aus `01_Exploration.ipynb`) — enthält
  Alter/Geschlecht/Ausländer/Schwerbehinderte bereits, da `parse_eckwerte()` alle Zeilen des
  Blatts "1.1 Eckwerte" liest.
- `Data/processed/kennzahlen_sgb2.csv` (für die Anteilsberechnung an `Arbeitslose (Bestand)`)

⚠️ Voraussetzung: `01_Exploration.ipynb` muss vorher mindestens einmal komplett gelaufen sein.
Kein erneutes Einlesen der Excel-Rohdaten nötig.

## Output

- `Data/processed/demografie_sgb2.csv` — Wide-Format-Zeitreihe mit den acht Merkmalen
  (Altersgruppen, Geschlecht, Ausländer, Schwerbehinderte) sowie berechneten Anteilen.
  Grundlage für den Dashboard-Tab "👥 Demografie".

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung gegenüber `02_Analyse_SGBII.ipynb`.
2. **Setup & Laden** — Filtert `eckwerte_long.csv` auf Kategorie "Arbeitslose" und die acht
   Merkmale, pivotiert zu einer Wide-Zeitreihe.
3. **1. Altersstruktur im Zeitverlauf**
   - Gestapelte Fläche aus vier überschneidungsfreien Bändern (15–25, 25–50, 50 bis unter
     55, 55+). Die Gruppe „50 Jahre und älter“ wird dafür in „50 bis unter 55“ und „55 und
     älter“ aufgeteilt (Subtraktion), damit die Teilmenge 55+ als eigenes, korrekt
     positioniertes Band erscheint statt als frei schwebende Linie.
   - **Befund:** sehr stabile Verteilung (25–50 Jahre ~57 %), aber der Anteil der
     55-Jährigen und Älteren an der Gruppe 50+ steigt von 64,8 % auf 68,8 % — die
     Altersstruktur *innerhalb* von 50+ verschiebt sich stärker als die grobe Einteilung
     zeigt.
4. **2. Geschlechterverteilung im Zeitverlauf**
   - Gestapelte Fläche Männer/Frauen.
   - **Befund:** leichte Verschiebung zu mehr Männern (53,1 % → 54,5 %); der
     Bestandsanstieg der letzten Monate geht überproportional auf Männer zurück
     (Männer 780 → 818, Frauen 690 → 682).
5. **3. Ausländische Arbeitslose im Zeitverlauf**
   - Zwei-Achsen-Chart: absolute Zahl + Anteil am Bestand.
   - **Befund:** überraschend hoher Anteil von 45–52 % des gesamten SGB-II-Bestands,
     deutlich rückläufig von 51,7 % (760 Personen, Jan 2025) auf 45,4 % (681 Personen,
     Jun 2026) — die auffälligste neue Erkenntnis dieses Notebooks.
6. **4. Schwerbehinderte Menschen im Zeitverlauf**
   - Gleiche Darstellung wie Ausländer.
   - **Befund:** kleinerer, leicht steigender Anteil (7,9 % → 8,7 %, 116 → 130 Personen).
7. **5. Export** — Schreibt `demografie_sgb2.csv`.
8. **6. Zusammenfassung (Markdown)** — fasst alle Befunde zusammen.

## Enthaltene Diagramme (4 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Gestapelte Fläche | ✅ Plotly | Altersstruktur (4 überschneidungsfreie Bänder) |
| 2 | Gestapelte Fläche | ✅ Plotly | Geschlechterverteilung |
| 3 | Zwei-Achsen-Liniendiagramm | ✅ Plotly | Ausländer: absolut + Anteil |
| 4 | Zwei-Achsen-Liniendiagramm | ✅ Plotly | Schwerbehinderte: absolut + Anteil |

## Voraussetzungen

- Python-Pakete: `pandas`, `plotly`
- CSV aus `01_Exploration.ipynb` muss vorhanden sein

## Verwandte Dateien

- Datengrundlage: [`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
  [`01_Exploration.md`](01_Exploration.md)
- Bisherige Momentaufnahme: [`02_Analyse_SGBII.ipynb`](../Notebooks/02_Analyse_SGBII.ipynb) /
  [`02_Analyse_SGBII.md`](02_Analyse_SGBII.md)
- Priorisierung offener Themen: [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
- Dashboard-Umsetzung: [`../Dashboard/app.py`](../Dashboard/app.py), Tab "👥 Demografie"
