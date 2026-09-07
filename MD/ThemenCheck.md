# Themen-Check: Arbeitsmarkt-Regensburg-Notebooks vs. DatenanalysePython.md

Abgleich der Notebooks `Notebooks/01_Exploration.ipynb`, `Notebooks/02_Analyse_SGBII.ipynb`,
`Notebooks/03_Statistik.ipynb`, `Notebooks/04_Fluktuation.ipynb`,
`Notebooks/05_Demografie.ipynb`, `Notebooks/06_Erwerbstaetigkeit.ipynb`,
`Notebooks/07_Finanzen.ipynb`, `Notebooks/08_Foerderung.ipynb`,
`Notebooks/09_Bezugsdauer.ipynb`, `Notebooks/10_Rechtskreisvergleich.ipynb`,
`Notebooks/11_Arbeitsstellen.ipynb` und `Notebooks/12_Unterbeschaeftigung.ipynb` gegen
Abschnitt 2 „Datenanalyse mit Pandas & NumPy“ aus
[`DatenanalysePython.md`](../DatenanalysePython.md).

Stand: nach Aufteilung in Exploration (Einlesen/Bereinigen/Aufbereiten/Export), Analyse
(Visualisierung/Auswertung), Statistik (deskriptive Statistik, Korrelation,
Inferenzstatistik, Regression), Fluktuation (Zugang/Abgang, Netto-Fluktuation,
12-Monatssummen), Demografie (Altersstruktur, Geschlecht, Ausländer, Schwerbehinderte als
Zeitreihe), Erwerbstätigkeit (Aufstockerquote, Erwerbsform, Einkommensstruktur), Finanzen
(Zahlungsansprüche in Euro, Ø je Bedarfsgemeinschaft, Struktur), Förderung
(Eintritte/Bestand an Fördermaßnahmen, Aktivierungsquote AQ1/AQ2a), Bezugsdauer
(BG-Struktur, Langzeitleistungsbezug, Drehtür-Effekt), Rechtskreisvergleich
(Jobcenter-Anteil SGB II vs. SGB III), gemeldete Arbeitsstellen (Nachfrageseite,
Angebot-Nachfrage-Relation) und Unterbeschäftigung (Kurzarbeiter-/Maßnahmen-Komponente,
SGB-II-Anteil im Vergleich) — inkl. Streamlit-Dashboard (`Dashboard/app.py`) als weiterem
Baustein für Abschnitt 4 „Datenvisualisierung“. Weiterhin offen aus `ArbeitslosenAnalyse.md`:
RLB/ELB/NEF-Struktur, sozialversicherungspflichtige/geringfügige Beschäftigung (siehe dort).

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
| Duplikate (`duplicated()`, `drop_duplicates()`) | ✅ `duplicated()` zur Pruefung, `drop_duplicates()` als expliziter Qualitätscheck vor dem Pivotieren | 01_Exploration, 12_Unterbeschaeftigung |
| NumPy Arrays / Funktionen (`mean`, `std`) | ✅ | 01_Exploration |
| Zeitreihen: Monat/Jahr extrahieren | ✅ (`.dt.year`, `.dt.month`) | 01_Exploration |
| Regex-Grundlagen | ✅ (in `normalize_label`) | 01_Exploration |
| `query()` | ✅ Filter auf überdurchschnittlichen Stellenbestand | 11_Arbeitsstellen |
| `astype()`, `pd.to_numeric()`, `pd.to_datetime()` | ✅ `astype("Int64")` für Personenzahlen, `pd.to_datetime()` als Alternative zu `pd.Period` | 12_Unterbeschaeftigung |
| `concat()`, `merge()`, `join()` | ✅ `concat()` beim Zusammenführen der 18 Monatsberichte, `merge()` beim Verknüpfen mit `kennzahlen_sgb2`; `join()` funktional äquivalent über `merge(left_index=True, right_index=True)` abgedeckt | 11_Arbeitsstellen |
| Resample & Rolling | ✅ `resample("QE")` für Quartalsdurchschnitte, `rolling(12).sum()`/`rolling(3).mean()` für Cross-Check und Glättung | 11_Arbeitsstellen |
| `str.contains()`, `.replace()`, `str.extract()` | ✅ `str.replace()` bei der Spaltenumbenennung, `str.extract()` und `str.contains()` bei der Dateinamens-Verarbeitung | 11_Arbeitsstellen |

**Bilanz:** 18 von 18 Themen abgedeckt.

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
| Boxplot / Violinplot | ✅ (03_Statistik, Boxplot; Violinplot in 11_Arbeitsstellen, Verteilung des monatlichen Zugangs) |
| Pieplot / Donut | ✅ (11_Arbeitsstellen, Donut-Chart Struktur des Stellenbestands) |
| Funnel-Chart | ✅ (Dashboard, Trichter-Grafik RLB/ELB) |
| Heatmap | ✅ (03_Statistik, Korrelationsmatrix) |
| Plotly (interaktiv) | ✅ (02_Analyse_SGBII: 4 von 5 Charts; 03_Statistik: alle 5 Charts; 04_Fluktuation: alle 3 Charts; 05_Demografie: alle 4 Charts; 06_Erwerbstaetigkeit: alle 3 Charts; 07_Finanzen: alle 2 Charts; 08_Foerderung: alle 3 Charts; 09_Bezugsdauer: alle 4 Charts; 10_Rechtskreisvergleich: alle 3 Charts; 11_Arbeitsstellen: alle 6 Charts; Dashboard: alle Charts, `hovermode="x unified"`) |

## Offene Punkte für spätere Ergänzung

Abschnitt 2 (Pandas & NumPy) sowie Abschnitt 4 (Datenvisualisierung) sind vollständig
abgedeckt. Aus Abschnitt 3 (Statistik) bleibt offen:

- ANOVA (Mehrgruppen-Varianzanalyse), multiple Regression (mehrere Prädiktoren)
