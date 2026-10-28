# Dokumentation: 11_Arbeitsstellen.ipynb

## Zweck

Offener Punkt aus [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md), Abschnitt "In den
Rohdaten vorhanden, aber noch nicht analysiert": Das Blatt "1.1 Eckwerte" enthält neben allen
bisher genutzten Arbeitslosen- und Bedarfsgemeinschafts-Kennzahlen auch einen eigenen Block
**"gemeldete Arbeitsstellen"** — die **Nachfrageseite** des Arbeitsmarkts, die in den Kapiteln
1–10 komplett ausgeklammert war.

Gleichzeitig schließt dieses Notebook mehrere methodische Lücken aus
[`ThemenCheck.md`](ThemenCheck.md): die bis dahin fehlenden Pandas-Methoden `concat()`,
`merge()`/`join()`, `query()`, `resample()`, `rolling()` sowie die Stringmethoden
`str.replace()`/`str.extract()`, außerdem die fehlenden Diagrammtypen Violinplot und
Donut-/Pie-Chart.

## Input

- `Data/RegensburgJCData/*.xlsx` (21 Monatsberichte), Blatt "1.1 Eckwerte", **direkt neu
  eingelesen** — nicht aus `eckwerte_long.csv`.
- `Data/processed/kennzahlen_sgb2.csv` (für den Angebot-Nachfrage-Vergleich).

**Warum nicht `eckwerte_long.csv`?** Der Block "gemeldete Arbeitsstellen" enthält die
Zeilenbeschriftung **"sozialversicherungspflichtig" dreimal identisch** (als Teilmenge von
"Zugang (im Monat)", "Zugang (12-Monatssumme)" und "Bestand"). In der bestehenden
Longtable erhalten alle drei denselben `label`-Wert und sind nach dem Sortieren nicht mehr
eindeutig ihrer jeweiligen Hauptzeile zuordenbar. Das Notebook liest den Block deshalb mit
einer eigenen Parser-Funktion (`parse_arbeitsstellen()`) direkt aus den Rohdateien und ordnet
jede "sozialversicherungspflichtig"-Zeile explizit der unmittelbar vorangehenden Hauptzeile zu.

⚠️ **Wichtige Einschränkung:** "gemeldete Arbeitsstellen" wird von der Bundesagentur **nicht
nach Rechtskreis differenziert** ausgewiesen — nur ein "Insgesamt"-Wert, kein eigener
SGB-II-Wert. Das erklärt auch die 126 fehlenden Werte, die in
[`01_Exploration.ipynb`](01_Exploration.ipynb) dokumentiert wurden.

## Output

- `Data/processed/arbeitsstellen.csv` — Zeitreihe mit 6 Kennzahlen je Berichtsmonat
  (`zugang_im_monat`, `zugang_im_monat_sozialversicherungspflichtig`, `zugang_12m`,
  `zugang_12m_sozialversicherungspflichtig`, `bestand`, `bestand_sozialversicherungspflichtig`).
- `Docs/Abbildungen/abb33_arbeitsstellen_zugang_bestand.png`,
  `abb34_arbeitsstellen_angebot_nachfrage.png`, `abb35_arbeitsstellen_struktur.png` — für
  Kapitel 13 der Projektdokumentation/-präsentation.

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, Datenherkunft, Einschränkung (keine Rechtskreis-Aufteilung).
2. **Setup** — Lädt `kennzahlen_sgb2.csv` für den späteren Vergleich.
3. **1. Datenextraktion**
   - `parse_arbeitsstellen()` liest Zeilen 9–47 aus "1.1 Eckwerte", verfolgt beim Durchlaufen
     die zuletzt gesehene Hauptzeile und hängt jede "sozialversicherungspflichtig"-Zeile daran.
   - `pd.concat()` fügt die 21 Monats-Einzeltabellen zusammen; Spaltennamen werden über
     vektorisierte Stringmethoden (`str.lower()`, `str.replace()`, `str.strip()`) in
     einheitliches snake_case überführt.
   - Alternative Demonstration: `str.extract()` zur vektorisierten Berichtsmonat-Extraktion
     aus den Dateinamen (statt Schleife mit `re.search()`), sowie `str.contains()` zum
     Filtern der Dateinamen auf einen Zeitraum (zweites Halbjahr 2025).
4. **2. Zeitreihe: Zugang und Bestand**
   - Balken (Zugang) + Linie (Bestand).
   - **Befund:** Bestand sinkt von 1.571 (Jan 2025) auf 1.208 (Sep 2026), rund −23 %; seit
     dem Tiefstand im Mai 2026 (1.169) Seitwärtsbewegung. Zugang volatil (163–593/Monat),
     Höchststand im August 2025 (593), Sommer 2026 deutlich schwächer (Aug 2026: 289).
5. **3. Cross-Check und Glättung mit `rolling()`**
   - `rolling(12).sum()` auf den eigenen Monatswerten vs. die von der Bundesagentur bereits
     gemeldete 12-Monatssumme; zusätzlich `rolling(3).mean()` zur Glättung.
   - **Befund:** Für alle 10 vergleichbaren Monate exakte Übereinstimmung (Differenz 0) — Beleg
     für korrekte Extraktion. Der August-2025-Ausreißer erweist sich im geglätteten Verlauf als
     Einzelmonat ohne dauerhaften Trendwechsel. Seit er aus dem Fenster gefallen ist, sinkt die
     12-Monatssumme auf ihren Tiefstwert 2.885 (Sep 2026; Höchstwert 3.684 im Nov 2025).
6. **4. Quartalsdurchschnitt mit `resample()`**
   - `PeriodIndex` → `DatetimeIndex` → `resample("QE").mean()`.
   - **Befund:** Q3 2025 sticht heraus (Ø Bestand 1.624,7, Ø Zugang 441,3) — deutlich über allen
     anderen Quartalen. Q2 2026 (Ø 1.207,0) und Q3 2026 (Ø 1.201,7) markieren die niedrigsten
     Quartalsbestände; Q3 2026 hat mit Ø 223,7 Zugängen nur halb so viele wie Q3 2025.
7. **5. Angebot vs. Nachfrage mit `merge()` und `query()`**
   - Verknüpft `arbeitsstellen` mit `kennzahlen_sgb2["Arbeitslose (Bestand)"]` über
     `merge(..., left_index=True, right_index=True)`; berechnet Arbeitsstellen je 100
     Arbeitslose. `query()` filtert Monate mit überdurchschnittlichem Stellenbestand.
   - **Befund:** Relation fällt von 106,9 (Jan 2025, mehr Stellen als Arbeitslose) auf 79,3
     (Sep 2026); Höchstwert 115,0 (Okt 2025), Tiefstwert 75,3 (Mai 2026), seither stabil bei 78–80 — ein von den
     Arbeitslosenkennzahlen unabhängiger Beleg für eine sich eintrübende Arbeitsmarktlage.
8. **6. Struktur und Verteilung**
   - Donut-Chart: Zusammensetzung des Bestands im letzten Berichtsmonat.
   - Violinplot: Verteilung des monatlichen Zugangs über alle 21 Monate.
   - **Befund:** 98,3 % des Bestands (September 2026) ist sozialversicherungspflichtig. Der
     Zugang ist rechtsschief verteilt (Median 245 < Mittelwert 272,0), gezogen durch den
     August-2025-Ausreißer.
9. **7. Zusammenfassung (Markdown)** — fasst den Befund ein und ordnet die verwendeten
   Pandas-Methoden den jeweiligen Analyseschritten zu.
10. **Export** — schreibt `arbeitsstellen.csv`.

## Enthaltene Diagramme (5 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Balken + Linie | ✅ Plotly | Zugang (im Monat) und Bestand gemeldeter Arbeitsstellen |
| 2 | Balken + Linie (geglättet) | ✅ Plotly | Monatlicher Zugang vs. gleitendes 3-Monats-Mittel |
| 3 | Balkendiagramm | ✅ Plotly | Ø Bestand je Quartal |
| 4 | Liniendiagramm | ✅ Plotly | Arbeitsstellen je 100 Arbeitslose |
| 5 | Donut-Chart | ✅ Plotly | Struktur des Bestands (sozialversicherungspflichtig vs. sonstige) |
| 6 | Violinplot | ✅ Plotly | Verteilung des monatlichen Zugangs (21 Monate) |

## Voraussetzungen

- Python-Pakete: `pandas`, `numpy`, `openpyxl`, `plotly`
- `kennzahlen_sgb2.csv` aus `01_Exploration.ipynb` muss vorhanden sein

## Verwandte Dateien

- Datengrundlage: [`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
  [`01_Exploration.md`](01_Exploration.md)
- SGB-II-Bestandsanalyse: [`02_Analyse_SGBII.ipynb`](../Notebooks/02_Analyse_SGBII.ipynb) /
  [`02_Analyse_SGBII.md`](02_Analyse_SGBII.md)
- Priorisierung offener Themen: [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
- Methodischer Abgleich gegen den Lernplan: [`ThemenCheck.md`](ThemenCheck.md)
