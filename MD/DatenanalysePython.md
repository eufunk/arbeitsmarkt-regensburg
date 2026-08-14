# 📚 Vorbereitung IHK-Projektarbeit — Themenübersicht

---

## <span style="color:#2980b9">🐍 1. Python Grundlagen</span>
`Quelle: Programmieren_13.04_28.04`

### Datentypen & Datenstrukturen
- [ ] **Listen & Tupel** — Erstellen, Indexierung, Slicing, Methoden
- [ ] **Sets** — Mengenoperationen, Duplikatentfernung
- [ ] **Dictionaries** — Key-Value-Paare, Iteration, verschachtelte Dicts

### Kontrollstrukturen
- [ ] **if / elif / else** — Bedingungslogik
- [ ] **Schleifen** — `for`, `while`, `break`, `continue`, `range()`
- [ ] **Comprehensions** — List, Dict, Set Comprehensions

### Funktionen & Funktionale Programmierung
- [ ] **Funktionen** — Definition, Parameter, Rückgabewerte, Scope
- [ ] **Lambda-Funktionen** — anonyme Funktionen
- [ ] **`map()`, `filter()`, `reduce()`** — funktionale Verarbeitung von Sequenzen
- [ ] **Formatierung** — f-Strings, `.format()`, Ausgabe formatieren

### Fehlerbehandlung & Laufzeit
- [ ] **Try / Except / Finally** — Exception Handling
- [ ] **Laufzeiten** — `time`-Modul, Performance messen

### Dateien & Datum
- [ ] **Dateien lesen & schreiben** — `open()`, `read()`, `write()`, Pfade (`os`, `pathlib`)
- [ ] **datetime-Modul** — Datumsobjekte erstellen, formatieren, rechnen

### Objektorientierung (OOP)
- [ ] **Klassen & Objekte** — `class`, `__init__`, Attribute, Methoden
- [ ] **Vererbung** — `super()`, Überschreiben von Methoden
- [ ] **Kapselung** — private/public Attribute
- [ ] **Praxisbeispiele** — Tierarztpraxis, Fahrzeugvermietung, Vokabeltrainer

### Sonstiges
- [ ] **Algorithmen** — Sortieralgorithmen, Suche
- [ ] **Code Style (PEP 8)** — Namenskonventionen, Lesbarkeit

---

## <span style="color:#27ae60">📊 2. Datenanalyse mit Pandas & NumPy</span>
`Quelle: Datenanalyse_29.04_18.05`

### NumPy
- [ ] **Arrays** — Erstellen, Operationen, Broadcasting
- [ ] **Mathematische Funktionen** — `mean`, `std`, `sum`, `min`, `max`

### Pandas Grundlagen
- [ ] **Series & DataFrame** — Erstellen, Struktur, Datentypen
- [ ] **Dateien einlesen** — CSV (`read_csv`), JSON (`read_json`), Excel (`read_excel`)
- [ ] **Daten exportieren** — `to_csv`, `to_excel`, `to_json`

### Selektieren & Filtern
- [ ] **Spalten & Zeilen auswählen** — `[]`, `.loc[]`, `.iloc[]`
- [ ] **Boolesche Filter** — Bedingungen kombinieren (`&`, `|`, `~`)
- [ ] **`query()`-Methode** — SQL-ähnliches Filtern

### Daten bereinigen & transformieren
- [ ] **Fehlende Werte** — `isnull()`, `fillna()`, `dropna()`
- [ ] **Duplikate** — `drop_duplicates()`
- [ ] **Datentypen umwandeln** — `astype()`, `pd.to_numeric()`, `pd.to_datetime()`
- [ ] **String-Operationen** — `.str.lower()`, `.str.contains()`, `.str.replace()`

### Aggregation & Gruppierung
- [ ] **`groupby()`** — Gruppieren und zusammenfassen
- [ ] **Aggregationsfunktionen** — `sum`, `mean`, `count`, `min`, `max`
- [ ] **`pivot_table()`** — mehrdimensionale Auswertungen

### DataFrames verbinden
- [ ] **`concat()`** — vertikales / horizontales Zusammenfügen
- [ ] **`merge()`** — Inner, Left, Right, Outer Join
- [ ] **`join()`** — Index-basiertes Verbinden

### Datum & Zeit in Pandas
- [ ] **`pd.to_datetime()`** — Datum parsen
- [ ] **Zeitreihenoperationen** — Monat, Jahr, Wochentag extrahieren
- [ ] **Resample & Rolling** — Zeitreihen aggregieren

### Regex in Pandas
- [ ] **`str.match()`, `str.extract()`, `str.findall()`** — Muster erkennen
- [ ] **Regex-Grundlagen** — `.`, `*`, `+`, `?`, `[]`, `^`, `$`, Gruppen

---

## <span style="color:#8e44ad">📐 3. Statistik & Datenauswertung</span>
`Quelle: DataCraft_19.05_09.06`

### Deskriptive Statistik
- [ ] **Skalentypen** — Nominal, Ordinal, Intervall, Verhältnis
- [ ] **Lagemaße** — Mittelwert, Median, Modus
- [ ] **Streuungsmaße** — Varianz, Standardabweichung, IQR

### Kombinatorik & Wahrscheinlichkeit
- [ ] **Permutationen & Kombinationen** — `math.factorial()`, `itertools`
- [ ] **Grundregeln der Wahrscheinlichkeit** — Addition, Multiplikation

### Verteilungen
- [ ] **Normalverteilung** — Gaußkurve, z-Score, 68-95-99,7-Regel
- [ ] **Binomialverteilung** — diskrete Wahrscheinlichkeiten
- [ ] **Chi-Quadrat-Verteilung** — Unabhängigkeitstest

### Bivariate Statistik
- [ ] **Korrelationskoeffizient (r)** — Pearson, Spearman, Interpretation
- [ ] **Streudiagramme & Interpretation**

### Inferenzstatistik
- [ ] **Konfidenzintervalle** — Berechnung, Interpretation, Signifikanzniveau
- [ ] **Hypothesentest** — H0/H1, p-Wert, Signifikanzniveau α
- [ ] **T-Test** — Einstichproben-, Zweistichproben-, Welch-Test
- [ ] **ANOVA** — Einfaktorielle Varianzanalyse, F-Statistik

### Regressionsanalyse
- [ ] **Einfache lineare Regression** — Gleichung, Interpretation, R²
- [ ] **Multiple Regression** — mehrere Prädiktoren, Multikollinearität
- [ ] **Fehlende Werte bei Regression** — Imputation, Strategie

---

## <span style="color:#e67e22">📈 4. Datenvisualisierung</span>
`Quelle: Datenvisualisierung_10.06`

### Grundlegende Diagrammtypen
- [ ] **Scatterplot** — Zusammenhänge darstellen
- [ ] **Barplot** — Kategorienvergleich
- [ ] **Lineplot** — Zeitreihen & Trends
- [ ] **Histogram** — Häufigkeitsverteilung
- [ ] **Boxplot & Violinplot** — Verteilung & Ausreißer
- [ ] **Pieplot / Donut Chart** — Anteile darstellen

### Erweiterte Diagrammtypen
- [ ] **Heatmap** — Korrelationsmatrizen, Kreuztabellen
- [ ] **Pairplot** — mehrdimensionale Verteilungsübersicht
- [ ] **Bubble Chart** — 3 Variablen gleichzeitig
- [ ] **3D-Scatterplot & Surface Plot** — räumliche Daten

### Plotly (Interaktivität)
- [ ] **`plotly.express`** — schnelle interaktive Plots
- [ ] **`plotly.graph_objects`** — individuelle Anpassung
- [ ] **Hover-Effekte, Zoom, Filter** — interaktive Steuerung
- [ ] **Animationen** — `animation_frame`, GIF-Export

### Reporting & Export
- [ ] **PDF-Reports** — automatisierte Berichte erstellen
- [ ] **HTML-Export** — `plotly` Charts als HTML speichern

### Dashboards
- [ ] **Dash (Plotly Dash)** — Layout mit `dcc`, `html`, `Input`/`Output` Callbacks
- [ ] **Streamlit** — einfache Web-Apps, Widgets, Session State, Formulare
- [ ] **Flask** — Routen, Templates (Jinja2), Daten an HTML übergeben

### Python Formatierung
- [ ] **String-Formatierung** — f-Strings, Zahlenformate, Datumsformatierung
- [ ] **Ausgabelayout** — Spalten, Tabs, Einrückung

---

## <span style="color:#e74c3c">🤖 5. Machine Learning</span>
`Quelle: KI_Maschinenlearning`

### Grundkonzepte
- [ ] **Supervised vs. Unsupervised Learning** — Unterschied, Anwendungsfälle
- [ ] **Feature Matrix X & Zielvariable y**
- [ ] **Train-Test-Split** — `train_test_split()`, `random_state`, Overfitting vermeiden

### Regressionsmodelle (Supervised)
- [ ] **Einfache Lineare Regression** — `LinearRegression`, Koeffizienten, Intercept
- [ ] **Multiple Lineare Regression** — mehrere Features, Interpretation
- [ ] **Regularisierung** — Overfitting bei Regression verhindern:
  - **Ridge (L2)** — straft große Koeffizienten, reduziert sie gegen 0
  - **Lasso (L1)** — setzt unwichtige Koeffizienten auf exakt 0 (Feature Selection)
  - **ElasticNet** — Kombination aus L1 + L2
  - `alpha`-Parameter steuert Stärke der Regularisierung
- [ ] **Metriken:** MSE, RMSE, MAE, **R² (Bestimmtheitsmaß)** ← *Prüfungsrelevant!*

### Klassifikationsmodelle (Supervised)
- [ ] **K-Nearest Neighbors (KNN)** — Distanzmaße, k-Wahl, `KNeighborsClassifier`
- [ ] **Decision Tree** — Gini/Entropy, `max_depth`, Visualisierung
- [ ] **Random Forest** — Ensemble-Methode, `n_estimators`, Feature Importance
- [ ] **Metriken:** Accuracy, Precision, Recall, F1-Score, Confusion Matrix

### Clustering (Unsupervised)
- [ ] **K-Means** — Zentroiden, `n_clusters`, Elbow-Methode
- [ ] **Interpretation** — Cluster-Bedeutung, Silhouette Score

### Modelloptimierung
- [ ] **Cross-Validation (CV)** — `cross_val_score`, k-Fold
- [ ] **GridSearchCV** — Hyperparameter-Tuning, `param_grid`
- [ ] **Bias-Varianz-Tradeoff** — Underfitting vs. Overfitting

### Modell speichern & laden
- [ ] **`pickle` / `joblib`** — `.pkl`-Dateien erstellen und laden

---

## <span style="color:#c0392b">⚠️ Kritische Themen (aus Präsentation)</span>

> Diese Themen wurden in der Präsentation hinterfragt – besonders gründlich vorbereiten!

| Thema | Warum wichtig? | Wo wiederholen? |
|-------|---------------|-----------------|
| **R²-Metrik (ML)** | Konnte in Präsentation nicht erklärt werden | `KI_Maschinenlearning` → Lineare Regression |
| **Diagramme lesbar gestalten** | Folien kaum sichtbar | `Datenvisualisierung_10.06` → Formatierung |
| **Flask/Dash Dashboards** | Nicht gezeigt, aber Teil des Projekts | `Datenvisualisierung_10.06` → Dash/Flask |

---

## <span style="color:#16a085">✅ Lernplan — Empfohlene Reihenfolge</span>

```
Woche 1:  Python Grundlagen → OOP → Fehlerbehandlung
Woche 2:  NumPy → Pandas Grundlagen → Selektieren/Filtern
Woche 3:  Statistik (Deskriptiv → Inferenz → Regression)
Woche 4:  Datenvisualisierung → Plotly → Dash/Streamlit
Woche 5:  Machine Learning → Metriken → Modelloptimierung
Woche 6:  Wiederholung kritischer Themen + Präsentation üben
```

---

*Erstellt: 07.07.2026 | Basis: automatische Analyse der Kursordner*
