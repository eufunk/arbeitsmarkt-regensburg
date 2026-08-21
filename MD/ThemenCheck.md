# Themen-Check: Arbeitsmarkt-Regensburg-Notebooks vs. DatenanalysePython.md

Abgleich der Notebooks `Notebooks/01_Exploration.ipynb`, `Notebooks/02_Analyse_SGBII.ipynb`
und `Notebooks/03_Statistik.ipynb` gegen Abschnitt 2 „Datenanalyse mit Pandas & NumPy“ aus
[`DatenanalysePython.md`](../DatenanalysePython.md).

Stand: nach Aufteilung in Exploration (Einlesen/Bereinigen/Aufbereiten/Export), Analyse
(Visualisierung/Auswertung) und Statistik (deskriptive Statistik, Korrelation,
Inferenzstatistik, Regression), inkl. Streamlit-Dashboard (`Dashboard/app.py`) als weiterem
Baustein für Abschnitt 4 „Datenvisualisierung“.

## Abschnitt 2: Datenanalyse mit Pandas & NumPy

| Thema | Status | Wo |
|---|---|---|
| Series & DataFrame | ✅ | 01_Exploration |
| Dateien einlesen (Excel) | ✅ (via `openpyxl`, nicht `pd.read_excel`) | 01_Exploration |
| Dateien einlesen (CSV) | ✅ (`pd.read_csv`) | 02_Analyse_SGBII |
| Daten exportieren (`to_csv`) | ✅ | 01_Exploration |
| `[]`, `.loc[]`, `.iloc[]` | ✅ | 01/02 |
| Boolesche Filter (`&`, `\|`) | ✅ | 01_Exploration |
| `groupby()` | ✅ | 01_Exploration |
| `pivot_table()` | ✅ | 01_Exploration |
| Fehlende Werte (`isnull`) | ✅ (nur Zählung, kein `fillna`/`dropna`) | 01_Exploration |
| Duplikate (`duplicated()`) | ⚠️ nur erkannt, kein `drop_duplicates()` | 01_Exploration |
| NumPy Arrays / Funktionen (`mean`, `std`) | ✅ | 01_Exploration |
| Zeitreihen: Monat/Jahr extrahieren | ✅ (`.dt.year`, `.dt.month`) | 01_Exploration |
| Regex-Grundlagen | ✅ (in `normalize_label`) | 01_Exploration |
| `query()` | ❌ fehlt | – |
| `astype()`, `pd.to_numeric()`, `pd.to_datetime()` | ❌ fehlt (nutzt `pd.Period` statt `to_datetime`) | – |
| `concat()`, `merge()`, `join()` | ❌ fehlt | – |
| Resample & Rolling | ❌ fehlt | – |
| `str.contains()`, `.replace()`, `str.extract()` | ❌ fehlt (nur `str.startswith`) | – |

**Bilanz:** 13 von 18 Themen abgedeckt.

## Angrenzend: Abschnitt 3 „Statistik & Datenauswertung“

| Thema | Status |
|---|---|
| Deskriptive Statistik (Mittelwert/Median/Std) | ✅ (03_Statistik, inkl. Median, Varianz, IQR, Variationskoeffizient) |
| Streuungsmaße (Varianz, IQR) | ✅ (03_Statistik) |
| Korrelationskoeffizient | ✅ (03_Statistik, Pearson-Korrelationsmatrix + `pearsonr`) |
| Streudiagramme | ✅ (03_Statistik, Langzeitarbeitslose vs. Bedarfsgemeinschaften) |
| Inferenzstatistik (Konfidenzintervalle, Tests) | ✅ (03_Statistik, Welch-t-Test + 95%-CI) |
| Regressionsanalyse | ✅ (03_Statistik, einfache lineare Regression mit `sklearn`, R² = 0,983) |
| ANOVA | ❌ fehlt (nur Zweistichproben-t-Test, keine Mehrgruppen-Varianzanalyse) |
| Multiple Regression | ❌ fehlt (nur einfache Regression mit einem Prädiktor „Zeit“) |

## Angrenzend: Abschnitt 4 „Datenvisualisierung“

| Thema | Status |
|---|---|
| Lineplot | ✅ (02_Analyse_SGBII, Dashboard) |
| Barplot | ✅ (02_Analyse_SGBII, Dashboard) |
| Scatterplot | ✅ (03_Statistik, inkl. OLS-Trendlinie) |
| Histogram | ✅ (03_Statistik) |
| Boxplot / Violinplot | ✅ (03_Statistik, Boxplot; Violinplot fehlt weiterhin) |
| Pieplot / Donut | ❌ fehlt |
| Funnel-Chart | ✅ (Dashboard, Trichter-Grafik RLB/ELB) |
| Heatmap | ✅ (03_Statistik, Korrelationsmatrix) |
| Plotly (interaktiv) | ✅ (02_Analyse_SGBII: 4 von 5 Charts; 03_Statistik: alle 5 Charts; Dashboard: alle Charts, `hovermode="x unified"`) |

## Offene Punkte für spätere Ergänzung

- `drop_duplicates()`, `query()`, `pd.to_datetime()`/`astype()`, `concat()`/`merge()`/`join()`, Resample/Rolling, `str.contains()`/`.replace()`/`str.extract()`
- Violinplot, Pieplot/Donut
- ANOVA (Mehrgruppen-Varianzanalyse), multiple Regression (mehrere Prädiktoren)
