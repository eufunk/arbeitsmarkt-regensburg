# Themen-Check: Arbeitsmarkt-Regensburg-Notebooks vs. DatenanalysePython.md

Abgleich der Notebooks `Notebooks/01_Exploration.ipynb` und `Notebooks/02_Analyse.ipynb` gegen
Abschnitt 2 „Datenanalyse mit Pandas & NumPy“ aus [`DatenanalysePython.md`](../DatenanalysePython.md).

Stand: nach Aufteilung in Exploration (Einlesen/Bereinigen/Aufbereiten/Export) und Analyse
(Visualisierung/Auswertung).

## Abschnitt 2: Datenanalyse mit Pandas & NumPy

| Thema | Status | Wo |
|---|---|---|
| Series & DataFrame | ✅ | 01_Exploration |
| Dateien einlesen (Excel) | ✅ (via `openpyxl`, nicht `pd.read_excel`) | 01_Exploration |
| Dateien einlesen (CSV) | ✅ (`pd.read_csv`) | 02_Analyse |
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
| Deskriptive Statistik (Mittelwert/Median/Std) | ⚠️ nur `describe()` und `mean`/`std`, kein Median explizit |
| Streuungsmaße (Varianz, IQR) | ❌ fehlt |
| Korrelationskoeffizient | ❌ fehlt |
| Streudiagramme | ❌ fehlt |
| Inferenzstatistik (Konfidenzintervalle, Tests) | ❌ fehlt |
| Regressionsanalyse | ❌ fehlt |

## Angrenzend: Abschnitt 4 „Datenvisualisierung“

| Thema | Status |
|---|---|
| Lineplot | ✅ (02_Analyse) |
| Barplot | ✅ (02_Analyse) |
| Scatterplot | ❌ fehlt |
| Histogram | ❌ fehlt |
| Boxplot / Violinplot | ❌ fehlt |
| Pieplot / Donut | ❌ fehlt |
| Heatmap | ❌ fehlt |
| Plotly (interaktiv) | ❌ fehlt (nur matplotlib) |

## Offene Punkte für spätere Ergänzung

- `drop_duplicates()`, `query()`, `pd.to_datetime()`/`astype()`, `concat()`/`merge()`/`join()`, Resample/Rolling, `str.contains()`/`.replace()`/`str.extract()`
- Korrelation + Scatterplot (z. B. Langzeitarbeitslose vs. Bedarfsgemeinschaften)
- Histogram/Boxplot der Verteilungen
- Heatmap (z. B. Korrelationsmatrix der Kennzahlen)
