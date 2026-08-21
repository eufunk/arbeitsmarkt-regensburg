# Dokumentation: 03_Statistik.ipynb

## Zweck

Ergänzt [`02_Analyse_SGBII.ipynb`](02_Analyse_SGBII.md) um vertiefte statistische Verfahren,
die dort bisher fehlten (siehe [`ThemenCheck.md`](ThemenCheck.md), Abschnitt "Statistik &
Datenauswertung"): deskriptive Statistik im Detail (Median, Varianz, IQR,
Variationskoeffizient), Korrelationsanalyse mit Heatmap und Streudiagramm, Verteilungen
(Histogramm/Boxplot), ein Hypothesentest (Inferenzstatistik) sowie eine einfache lineare
Regression mit Prognose.

⚠️ **Stichprobengröße:** Die Zeitreihe umfasst nur 18 Monatswerte (Januar 2025 – Juni 2026).
Alle Tests und die Regression sind entsprechend vorsichtig zu interpretieren.

## Input

- `Data/processed/kennzahlen_sgb2.csv` (Wide-Format-Zeitreihe aus `01_Exploration.ipynb`)

⚠️ Voraussetzung: `01_Exploration.ipynb` muss vorher mindestens einmal komplett gelaufen sein.

## Output

Keine Datei-Exporte — reine Auswertung innerhalb von Jupyter (Diagramme, Tabellen und
Text-Ausgaben als Zell-Output).

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, Hinweis zur kleinen Stichprobengröße.
2. **Setup & Laden** — Imports (`numpy`, `scipy.stats`, `sklearn.linear_model.LinearRegression`,
   `plotly`), Laden von `kennzahlen_sgb2.csv`. Betrachtet werden die vier Kernkennzahlen
   Arbeitslose (Bestand), Langzeitarbeitslose, Bedarfsgemeinschaften, Personen in BG.
3. **1. Deskriptive Statistik im Detail**
   - Tabelle mit Mittelwert, Median, Standardabweichung, Varianz, Min/Max, Quartilen, IQR
     und Variationskoeffizient (CV = Std.-Abw./Mittelwert in %) je Kernkennzahl.
   - **Befund:** Langzeitarbeitslose haben mit CV ≈ 11,8 % die mit Abstand höchste relative
     Streuung; Bedarfsgemeinschaften (CV ≈ 2,1 %) und Personen in BG (CV ≈ 2,4 %) sind am
     stabilsten.
4. **2. Korrelationsanalyse**
   - Pearson-Korrelationsmatrix der vier Kernkennzahlen als Plotly-Heatmap.
   - Streudiagramm Langzeitarbeitslose vs. Bedarfsgemeinschaften mit OLS-Trendlinie
     (`px.scatter(..., trendline="ols")`, benötigt `statsmodels`) und `scipy.stats.pearsonr`.
   - **Befund:** Bedarfsgemeinschaften und Personen in BG korrelieren sehr stark (r ≈ 0,95,
     plausibel, da die Personenzahl aus der BG-Zahl hervorgeht). Langzeitarbeitslose und
     Bedarfsgemeinschaften korrelieren **signifikant negativ** (r = −0,49, p = 0,04).
     Langzeitarbeitslose und Arbeitslosenbestand korrelieren deutlich positiv (r = 0,67,
     p = 0,002). Mit den ursprünglichen 15 Monaten waren beide Zusammenhänge noch nicht
     signifikant nachweisbar (r = −0,08/p = 0,78 bzw. r = 0,48/p = 0,07) — ein anschauliches
     Beispiel dafür, wie empfindlich Korrelationstests bei kleinen Stichproben auf
     zusätzliche Datenpunkte reagieren.
5. **3. Verteilungen**
   - Histogramm und Boxplot (`boxmean=True`) des Arbeitslosenbestands über die 18 Monate.
   - **Befund:** keine auffälligen Ausreißer, leicht linksschiefe Verteilung (Median knapp
     über dem Mittelwert).
6. **4. Inferenzstatistik: Hypothesentest**
   - Fragestellung: Unterscheidet sich die durchschnittliche Zahl der Langzeitarbeitslosen
     zwischen erster (n=9) und zweiter (n=9) Hälfte des Beobachtungszeitraums signifikant?
   - Zweiseitiger **Welch-t-Test** (`scipy.stats.ttest_ind(..., equal_var=False)`),
     α = 0,05, plus approximatives 95 %-Konfidenzintervall für die Mittelwertdifferenz.
   - **Ergebnis:** 1. Hälfte Ø 543,3 (± 34,1) vs. 2. Hälfte Ø 661,1 (± 41,2); Differenz 117,8
     Personen, 95 %-CI [82,8; 152,7]; t = 6,61, **p ≈ 0,00001** — hoch signifikant, H₀ wird
     verworfen.
7. **5. Regressionsanalyse: Trend der Langzeitarbeitslosigkeit**
   - Einfache lineare Regression (`sklearn.linear_model.LinearRegression`) der
     Langzeitarbeitslosen-Zahl über den Monatsindex (0 = Januar 2025 … 17 = Juni 2026).
   - Ausgabe von Steigung, Achsenabschnitt, Bestimmtheitsmaß R² sowie einer Prognose für die
     folgenden drei Monate.
   - Plotly-Chart: beobachtete Werte, Regressionsgerade und Prognosepunkte in einem Diagramm.
   - **Ergebnis:** Langzeitarbeitslose ≈ 490,4 + 13,16 × Monatsindex, **R² = 0,983**
     (außergewöhnlich guter linearer Fit, noch etwas besser als mit 15 Monaten [R² = 0,976]).
     Prognose: Jul 2026 ≈ 727, Aug 2026 ≈ 740, Sep 2026 ≈ 754 Personen — mit ausdrücklichem
     Hinweis, dass eine lineare Extrapolation aus 18 Datenpunkten nur eine grobe Orientierung
     ist (keine Saisonalität, keine Strukturbrüche berücksichtigt).
8. **6. Zusammenfassung (Markdown)** — fasst alle vier Befundblöcke zusammen und ordnet sie
   in den Gesamtkontext ein: Die Verschärfung der Langzeitarbeitslosigkeit ist statistisch
   der am stärksten abgesicherte Trend im Datensatz.

## Enthaltene Diagramme (5 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Heatmap | ✅ Plotly | Korrelationsmatrix der vier Kernkennzahlen |
| 2 | Scatterplot + Trendlinie | ✅ Plotly | Langzeitarbeitslose vs. Bedarfsgemeinschaften |
| 3 | Histogramm | ✅ Plotly | Verteilung Arbeitslose (Bestand) |
| 4 | Boxplot | ✅ Plotly | Verteilung Arbeitslose (Bestand) |
| 5 | Scatter + Regressionsgerade + Prognose | ✅ Plotly | Langzeitarbeitslose: linearer Trend |

Damit sind gegenüber `ThemenCheck.md` zusätzlich abgedeckt: Scatterplot, Histogramm, Boxplot,
Heatmap, Korrelationskoeffizient, Konfidenzintervalle, Hypothesentest (t-Test) und einfache
lineare Regression (inkl. R²).

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
