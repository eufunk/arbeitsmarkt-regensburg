# Dokumentation: 03_Statistik.ipynb

## Zweck

Ergänzt [`02_Analyse_SGBII.ipynb`](02_Analyse_SGBII.md) um vertiefte statistische Verfahren,
die dort bisher fehlten (siehe [`ThemenCheck.md`](ThemenCheck.md), Abschnitt "Statistik &
Datenauswertung"): deskriptive Statistik im Detail (Median, Varianz, IQR,
Variationskoeffizient), Korrelationsanalyse mit Heatmap und Streudiagramm, Verteilungen
(Histogramm/Boxplot), ein Hypothesentest (Inferenzstatistik) sowie eine einfache lineare
Regression mit Prognose und einem nachträglichen Abgleich der Prognose mit den Istwerten
(Out-of-Sample-Test).

⚠️ **Stichprobengröße:** Die Zeitreihe umfasst nur 21 Monatswerte (Januar 2025 – September 2026).
Alle Tests und die Regression sind entsprechend vorsichtig zu interpretieren.

## Input

- `Data/processed/kennzahlen_sgb2.csv` (Wide-Format-Zeitreihe aus `01_Exploration.ipynb`)

⚠️ Voraussetzung: `01_Exploration.ipynb` muss vorher mindestens einmal komplett gelaufen sein.

## Output

- `Docs/Abbildungen/abb32_verteilung_boxstrip.png` (Boxplot mit Einzelpunkten, für die
  Projektpräsentation)
- `Docs/Abbildungen/abb44_prognose_vs_ist.png` (Prognose vs. Ist, Juli – September 2026)
- Ansonsten keine weiteren Datei-Exporte — reine Auswertung innerhalb von Jupyter
  (Diagramme, Tabellen und Text-Ausgaben als Zell-Output).

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, Hinweis zur kleinen Stichprobengröße.
2. **Setup & Laden** — Imports (`numpy`, `scipy.stats`, `sklearn.linear_model.LinearRegression`,
   `plotly`), Laden von `kennzahlen_sgb2.csv`. Betrachtet werden die vier Kernkennzahlen
   Arbeitslose (Bestand), Langzeitarbeitslose, Bedarfsgemeinschaften, Personen in BG.
3. **1. Deskriptive Statistik im Detail**
   - Tabelle mit Mittelwert, Median, Standardabweichung, Varianz, Min/Max, Quartilen, IQR
     und Variationskoeffizient (CV = Std.-Abw./Mittelwert in %) je Kernkennzahl.
   - **Befund:** Langzeitarbeitslose haben mit CV ≈ 11,9 % die mit Abstand höchste relative
     Streuung; Bedarfsgemeinschaften (CV ≈ 2,2 %) und Personen in BG (CV ≈ 2,9 %) sind am
     stabilsten, der Arbeitslosenbestand liegt mit 3,7 % dazwischen.
4. **2. Korrelationsanalyse**
   - Pearson-Korrelationsmatrix der vier Kernkennzahlen als Plotly-Heatmap.
   - Streudiagramm Langzeitarbeitslose vs. Bedarfsgemeinschaften mit OLS-Trendlinie
     (`px.scatter(..., trendline="ols")`, benötigt `statsmodels`) und `scipy.stats.pearsonr`.
   - **Befund:** Bedarfsgemeinschaften und Personen in BG korrelieren sehr stark (r ≈ 0,96,
     plausibel, da die Personenzahl aus der BG-Zahl hervorgeht). Langzeitarbeitslose und
     Bedarfsgemeinschaften korrelieren **signifikant negativ** (r = −0,58, p = 0,006; bei 18
     Monaten r = −0,49, p = 0,04). Langzeitarbeitslose und Arbeitslosenbestand korrelieren
     deutlich positiv (r = 0,65, p = 0,001). Mit den ursprünglichen 15 Monaten waren beide
     Zusammenhänge noch nicht signifikant nachweisbar (r = −0,08/p = 0,78 bzw. r = 0,48/p = 0,07) — ein anschauliches
     Beispiel dafür, wie empfindlich Korrelationstests bei kleinen Stichproben auf
     zusätzliche Datenpunkte reagieren.
5. **3. Verteilungen**
   - Histogramm und Boxplot (`boxmean=True`) des Arbeitslosenbestands über die 21 Monate.
   - **Befund:** keine auffälligen Ausreißer, leicht linksschiefe Verteilung (Median knapp
     über dem Mittelwert).
   - Zusätzlich eine alternative Darstellung als Boxplot mit allen 21 Einzelpunkten
     (`boxpoints="all"`, Jitter) — vermeidet die bei so kleinen Stichproben leicht
     missverständliche Bin-Häufigkeits-Achse eines Histogramms. Wird exportiert nach
     `Docs/Abbildungen/abb32_verteilung_boxstrip.png` und in der Projektpräsentation
     (Folie 22) verwendet.
6. **4. Inferenzstatistik: Hypothesentest**
   - Fragestellung: Unterscheidet sich die durchschnittliche Zahl der Langzeitarbeitslosen
     zwischen erster (n=10) und zweiter (n=11) Hälfte des Beobachtungszeitraums signifikant?
     Bei ungerader Monatszahl erhält die zweite Hälfte den zusätzlichen Monat (`len(lza) // 2`).
   - Zweiseitiger **Welch-t-Test** (`scipy.stats.ttest_ind(..., equal_var=False)`),
     α = 0,05, plus approximatives 95 %-Konfidenzintervall für die Mittelwertdifferenz.
   - **Ergebnis:** 1. Hälfte Ø 549,6 (± 37,8) vs. 2. Hälfte Ø 674,9 (± 34,0); Differenz 125,3
     Personen, 95 %-CI [94,4; 156,2]; t = 7,95, **p < 0,0001** — hoch signifikant, H₀ wird
     verworfen.
7. **5. Regressionsanalyse: Trend der Langzeitarbeitslosigkeit**
   - Einfache lineare Regression (`sklearn.linear_model.LinearRegression`) der
     Langzeitarbeitslosen-Zahl über den Monatsindex (0 = Januar 2025 … 20 = September 2026).
   - Ausgabe von Steigung, Achsenabschnitt, Bestimmtheitsmaß R² sowie einer Prognose für die
     folgenden drei Monate.
   - Plotly-Chart: beobachtete Werte, Regressionsgerade und Prognosepunkte in einem Diagramm.
   - **Ergebnis:** Langzeitarbeitslose ≈ 500,4 + 11,48 × Monatsindex, **R² = 0,952**
     (weiterhin sehr guter Fit, aber schwächer als mit 18 Monaten [R² = 0,983, Steigung
     +13,16], weil Juni – September 2026 nach dem Höchststand im Mai 2026 unter der Geraden
     liegen). Prognose: Okt 2026 ≈ 742, Nov 2026 ≈ 753, Dez 2026 ≈ 765 Personen — mit
     ausdrücklichem Hinweis, dass eine lineare Extrapolation aus 21 Datenpunkten nur eine grobe
     Orientierung ist (keine Saisonalität, keine Strukturbrüche berücksichtigt).
8. **6. Prognose vs. Ist: Out-of-Sample-Test** *(neu mit der Datenerweiterung Juli –
   September 2026)*
   - Das Modell wird noch einmal nur mit den Daten bis Juni 2026 geschätzt (Stand der
     ursprünglichen Analyse) und seine Prognose den inzwischen gemeldeten Istwerten
     gegenübergestellt. Fehlermaße: MAE (Personen) und MAPE (%).
   - Tabelle `prognose_vs_ist` und Plotly-Chart (beobachtete Werte bis Juni 2026, alte
     Regressionsgerade, damalige Prognose, Istwerte), Export nach
     `Docs/Abbildungen/abb44_prognose_vs_ist.png`.
   - **Ergebnis:** Prognose 727 / 740 / 754 vs. Ist 690 / 692 / 698 — Abweichung −37 / −48 /
     −56 Personen (−5,1 % / −6,5 % / −7,4 %), MAE ≈ 47 Personen, MAPE ≈ 6,3 %. Die Prognose
     lag durchgehend zu hoch, der Fehler wächst mit dem Horizont: Die lineare Gerade kann das
     Plateau nach dem Höchststand im Mai 2026 nicht abbilden. Lehre: Ein hohes R² beschreibt
     den Fit an die Vergangenheit, nicht die Prognosegüte.
9. **7. Zusammenfassung (Markdown)** — fasst alle fünf Befundblöcke zusammen und ordnet sie
   in den Gesamtkontext ein: Die Verschärfung der Langzeitarbeitslosigkeit ist statistisch
   der am stärksten abgesicherte Trend im Datensatz, hat sich aber seit Mai 2026 vorerst
   stabilisiert.

## Enthaltene Diagramme (7 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Heatmap | ✅ Plotly | Korrelationsmatrix der vier Kernkennzahlen |
| 2 | Scatterplot + Trendlinie | ✅ Plotly | Langzeitarbeitslose vs. Bedarfsgemeinschaften |
| 3 | Histogramm | ✅ Plotly | Verteilung Arbeitslose (Bestand) |
| 4 | Boxplot | ✅ Plotly | Verteilung Arbeitslose (Bestand) |
| 5 | Boxplot mit Einzelpunkten | ✅ Plotly | Verteilung Arbeitslose (Bestand) — Export für Präsentation (Folie 22) |
| 6 | Scatter + Regressionsgerade + Prognose | ✅ Plotly | Langzeitarbeitslose: linearer Trend |
| 7 | Scatter + Gerade + Prognose/Ist | ✅ Plotly | Prognose vs. Ist Juli – September 2026 (Export abb44) |

Damit sind gegenüber `ThemenCheck.md` zusätzlich abgedeckt: Scatterplot, Histogramm, Boxplot,
Heatmap, Korrelationskoeffizient, Konfidenzintervalle, Hypothesentest (t-Test), einfache
lineare Regression (inkl. R²) sowie Prognosevalidierung mit Fehlermaßen (MAE, MAPE).

## Voraussetzungen

- Python-Pakete: `pandas`, `numpy`, `scipy`, `scikit-learn`, `statsmodels` (für die
  OLS-Trendlinie in `px.scatter`), `plotly`
- CSV aus `01_Exploration.ipynb` muss vorhanden sein

## Verwandte Dateien

- Datengrundlage: [`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
  [`01_Exploration.md`](01_Exploration.md)
- Visuelle Analyse: [`02_Analyse_SGBII.ipynb`](../Notebooks/02_Analyse_SGBII.ipynb) /
  [`02_Analyse_SGBII.md`](02_Analyse_SGBII.md)
- Themenabgleich gegen den Lernplan: [`ThemenCheck.md`](ThemenCheck.md)
