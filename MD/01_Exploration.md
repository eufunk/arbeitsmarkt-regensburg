# Dokumentation: 01_Exploration.ipynb

## Zweck

Liest die 15 monatlichen Excel-Berichte "Eckwerte für Jobcenter" (Jobcenter Regensburg,
Statistik-Nr. t73906-0) aus `Data/RegensburgJCData/` ein, bereinigt und strukturiert sie zu
einer Zeitreihe und exportiert das Ergebnis als CSV für die Weiterverarbeitung in
[`02_Analyse.ipynb`](02_Analyse.md). Enthält **keine Grafiken** — reine Daten-Pipeline
(Einlesen → Bereinigen → Aufbereiten → Export).

## Input

- `Data/RegensburgJCData/*.xlsx` (15 Dateien, April 2025 – Juni 2026, benannt
  `jc-eckwerte-t73906-0-JJJJMM-xlsx.xlsx`)
- Jede Datei enthält u. a. das Tabellenblatt **"1.1 Eckwerte"** mit dem Monatswert je Merkmal,
  getrennt nach Spalte B *"Insgesamt (SGB II und SGB III)"* und Spalte G *"Rechtskreis SGB II"*
  (= Jobcenter-Zuständigkeit).

## Output

- `Data/processed/eckwerte_long.csv` — Long-Format, eine Zeile je (Monat, Kategorie, Merkmal):
  Spalten `period`, `kategorie`, `merkmal`, `insgesamt`, `sgb2`, `jahr`, `monat`, `label`
- `Data/processed/kennzahlen_sgb2.csv` — Wide-Format-Zeitreihe, eine Zeile je Monat, sechs
  SGB-II-Kennzahlen als Spalten (Index: `period`)

Beide Dateien liegen unter `Data/`, das komplett in `.gitignore` steht — sie werden also nicht
versioniert und müssen bei Bedarf per Notebook-Lauf neu erzeugt werden.

## Ablauf (Zellen)

1. **Intro (Markdown)** — Datenquelle, Zeitraum, Verweis auf Teil 2.
2. **Imports & Setup** — `numpy`, `openpyxl`, `pandas`, `re`, `pathlib`; legt
   `Data/processed/` an, falls nicht vorhanden.
3. **Daten einlesen**
   - `normalize_label()`: entfernt Fußnotenmarker (z. B. `" 1)"`, `" 2) 4)"`) aus
     Zeilenbeschriftungen per Regex, damit gleiche Merkmale über alle 15 Dateien hinweg
     identisch benannt sind (Berichte revidieren Fußnoten-Referenzen zwischen Monaten).
   - `parse_eckwerte(path)`: liest Zeilen 9–44 des Blatts "1.1 Eckwerte"; Zeilen ohne
     Zahlenwert sind Kategorie-Überschriften (z. B. "Arbeitslose", "Grundsicherung für
     Arbeitsuchende"), Zeilen mit Zahlenwert werden als Datensatz erfasst. Der Berichtsmonat
     wird aus dem Dateinamen abgeleitet (`pd.Period`), nicht aus dem Blattinhalt.
   - Alle 15 Dateien werden geparst und zu einem DataFrame `df` zusammengeführt; zusätzlich
     werden `jahr`, `monat` (aus `period`) sowie ein kombinierter Schlüssel `label`
     (`kategorie | merkmal`) ergänzt — Letzterer löst Namenskollisionen wie "Bestand" (kommt
     bei "Arbeitsuchende", "Arbeitslose" und "gemeldete Arbeitsstellen" vor).
4. **Datenüberblick und Bereinigung**
   - Shape, abgedeckter Zeitraum, Duplikat-Check (`duplicated()`), Anzahl fehlender
     SGB-II-Werte (`isna()` — betrifft v. a. die Kategorie "gemeldete Arbeitsstellen", die
     nicht nach Rechtskreis differenziert wird), Liste aller Merkmale je Kategorie.
   - `describe()` auf der Spalte `sgb2` für einen groben Verteilungsüberblick.
5. **Kennzahlen-Zeitreihe aufbereiten**
   - Auswahl von sechs zentralen SGB-II-Kennzahlen über ein Label-Mapping-Dict.
   - `pivot_table(index="period", columns="kennzahl", values="sgb2")` erzeugt die
     Wide-Format-Tabelle `kennzahlen`.
   - Mittelwert und Standardabweichung je Kennzahl werden zusätzlich direkt über NumPy
     (`np.mean`, `np.std` auf `.to_numpy()`) ausgegeben.
6. **Export** — `df.to_csv(...)` und `kennzahlen.to_csv(...)` nach `Data/processed/`.
7. **Abschluss (Markdown)** — Verweis auf `02_Analyse.ipynb`.

## Ausgewählte SGB-II-Kennzahlen (Wide-Tabelle)

| Spalte in `kennzahlen` | Quelle (Kategorie \| Merkmal) |
|---|---|
| Arbeitslose (Bestand) | Arbeitslose \| Bestand |
| Arbeitslosenquote (%) | Arbeitslose \| Arbeitslosenquote |
| Langzeitarbeitslose | Arbeitslose \| Langzeitarbeitslose |
| Unterbeschäftigungsquote (%) | Unterbeschäftigung \| Unterbeschäftigungsquote |
| Bedarfsgemeinschaften | Grundsicherung für Arbeitsuchende \| Bedarfsgemeinschaften (BG) |
| Personen in BG | Grundsicherung für Arbeitsuchende \| Personen in Bedarfsgemeinschaften (PERS) |

## Voraussetzungen

- Python-Pakete: `pandas`, `numpy`, `openpyxl`, `matplotlib` (für Setup-Konsistenz, hier nicht
  zwingend genutzt)
- Wird das Notebook nicht ausgeführt, fehlen die CSVs für `02_Analyse.ipynb` — dieses bricht
  dann beim Einlesen ab.

## Verwandte Dateien

- Themenabgleich gegen den Lernplan: [`ThemenCheck.md`](ThemenCheck.md)
- Fortsetzung: [`02_Analyse.ipynb`](../Notebooks/02_Analyse.ipynb) /
  [`02_Analyse.md`](02_Analyse.md)
