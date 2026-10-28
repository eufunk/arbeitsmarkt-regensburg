# Dokumentation: 12_Unterbeschaeftigung.ipynb

## Zweck

Offener Punkt aus [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md): Das Blatt
"1.1 Eckwerte" enthält neben der bereits genutzten **Unterbeschäftigungsquote** auch die drei
zugrundeliegenden absoluten Kennzahlen — bislang nur für die Quote verwendet, nie als eigene
Zeitreihe betrachtet: **Arbeitslosigkeit im weiteren Sinne**, **Unterbeschäftigung im engeren
Sinne** und **Unterbeschäftigung (ohne Kurzarbeit)**.

Schließt außerdem die letzten beiden offenen Punkte aus [`ThemenCheck.md`](ThemenCheck.md):
`drop_duplicates()` und `astype()`/`pd.to_datetime()`.

## Input

- `Data/processed/eckwerte_long.csv` (Langformat aus `01_Exploration.ipynb`) — enthält für
  alle vier Merkmale (inkl. Quote) bereits sowohl `insgesamt` als auch `sgb2`.

**Keine neuen Rohdaten nötig** — anders als bei `11_Arbeitsstellen.ipynb` liegt hier für alle
Kennzahlen bereits ein vollständiger, eindeutiger SGB-II-Wert vor.

## Output

- `Data/processed/unterbeschaeftigung_sgb2.csv` — Zeitreihe (SGB II) mit den Spalten
  `arbeitslosigkeit_weiterer_sinn`, `unterbeschaeftigung_ohne_kurzarbeit`,
  `unterbeschaeftigung_engerer_sinn`, `unterbeschaeftigungsquote`,
  `unterbeschaeftigung_engerer_sinn_insgesamt`.
- `Docs/Abbildungen/abb36_unterbeschaeftigung_komponenten.png`,
  `abb37_unterbeschaeftigung_anteil.png` — für Kapitel 14 der
  Projektdokumentation/-präsentation.

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, Datenherkunft.
2. **Setup & Laden** — Filtert `eckwerte_long.csv` auf `kategorie == "Unterbeschäftigung"`.
3. **1. Qualitätssicherung mit `drop_duplicates()`**
   - Prüft explizit auf doppelte (Berichtsmonat, Merkmal)-Kombinationen vor dem Pivotieren
     (0 gefunden, 21 Monate × 4 Merkmale = 84 Zeilen bestätigt; die erwartete Zeilenzahl wird
     jetzt aus der Zahl der Monate und Merkmale berechnet statt fest eingetragen).
4. **2. Aufbereitung**
   - `pivot_table()` auf Wide-Format mit "Insgesamt"/"SGB II" je Merkmal.
   - Personenzahlen per `astype("Int64")` auf nullable Integer umgestellt (Quote bleibt float).
   - Alternative Datumsverarbeitung mit `pd.to_datetime()` statt `pd.Period` demonstriert.
5. **3. Zeitreihe der drei Komponenten (SGB II)**
   - Liniendiagramm aller drei Kennzahlen.
   - **Befund:** Die Kurzarbeiter-Komponente ("ohne Kurzarbeit" minus "im engeren Sinne") ist
     verschwindend gering (Ø 2,4 Personen, Spanne 1–4) — Kurzarbeit spielt im SGB-II-Kontext
     praktisch keine Rolle. Die Maßnahmen-Komponente ("im engeren Sinne" minus "im weiteren
     Sinne") ist mit Ø 388 Personen (Spanne 314–559) deutlich substanzieller (zuletzt 315–343).
6. **4. SGB-II-Anteil im Vergleich**
   - Vergleich mit den bereits bekannten Anteilen aus
     [`10_Rechtskreisvergleich.ipynb`](10_Rechtskreisvergleich.md) (Bestand ≈ 40 %, LZA ≈ 72 %).
   - **Befund:** SGB-II-Anteil an der Unterbeschäftigung im engeren Sinne liegt bei 42,7 %
     (September 2026, Spanne 41,1–49,6 %, leicht rückläufig) — zwischen dem Bestands- und dem LZA-Anteil.
7. **5. Zusammenfassung (Markdown)** — fasst beide Befunde zusammen und ordnet die
   verwendeten Pandas-Methoden ein.
8. **Export** — schreibt `unterbeschaeftigung_sgb2.csv`.

## Enthaltene Diagramme (2 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Liniendiagramm (3 Linien) | ✅ Plotly | Arbeitslosigkeit i.w.S. / Unterbeschäftigung i.e.S. / ohne Kurzarbeit (SGB II) |
| 2 | Liniendiagramm + Referenzlinien | ✅ Plotly | SGB-II-Anteil an der Unterbeschäftigung im Vergleich zu Bestand/LZA |

## Voraussetzungen

- Python-Pakete: `pandas`, `plotly`
- CSV aus `01_Exploration.ipynb` muss vorhanden sein

## Verwandte Dateien

- Datengrundlage: [`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
  [`01_Exploration.md`](01_Exploration.md)
- Rechtskreisvergleich (Referenzwerte Bestand/LZA): [`10_Rechtskreisvergleich.ipynb`](../Notebooks/10_Rechtskreisvergleich.ipynb) /
  [`10_Rechtskreisvergleich.md`](10_Rechtskreisvergleich.md)
- Priorisierung offener Themen: [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
- Methodischer Abgleich gegen den Lernplan: [`ThemenCheck.md`](ThemenCheck.md)
