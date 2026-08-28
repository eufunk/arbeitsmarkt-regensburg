# Dokumentation: 08_Foerderung.ipynb

## Zweck

Letzter Punkt aus dem Priorisierungsvorschlag in
[`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md): aktive Arbeitsmarktpolitik — Eintritte
und Bestand an Teilnehmenden in Fördermaßnahmen sowie die Aktivierungsquote (AQ1/AQ2a).

## Input

- `Data/RegensburgJCData/*.xlsx`, Tabellenblätter **"4.1 Förderung"** und **"4.2 Förderung
  Strukturen"** — **neu eingelesen**, direkt aus den Excel-Rohdaten (wie schon Kapitel 6
  und 7), nicht aus `eckwerte_long.csv`.

⚠️ **Wartezeit:** wie bei den Blättern 3.3/3.6 nur ein Datenblock mit **3 Monaten
Wartezeit** → Zeitreihe für **Oktober 2024 – März 2026**.

⚠️ **Anonymisierung:** Kleine Fallzahlen (< 3) werden von der Bundesagentur als „*“
unterdrückt — betrifft vor allem die feineren Instrumenten-Unterkategorien. Dieses Notebook
beschränkt sich bewusst auf **Summenzeilen**, die über alle 18 Dateien hinweg durchgehend
als Zahl vorliegen.

## Output

- `Data/processed/foerderung_sgb2.csv` — Wide-Format-Zeitreihe mit Eintritten, Bestand
  (inkl. 12-Monatswerten), Struktur nach Geschlecht/Alter/LZA-Vorgeschichte sowie AQ1/AQ2a
  (inkl. 12-Monatsdurchschnitt). Grundlage für den Dashboard-Tab "🎯 Förderung".

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, Erklärung von Wartezeit und Anonymisierung.
2. **Setup & Parsing** — `parse_foerderung(path)`: liest Monat per Regex aus Zelle A6,
   kombiniert feste Zellen aus beiden Blättern (4.1: B39/F39/B40/B58/F58, 4.2:
   C39/D39/E39/F39/G39/H39/B56/B57/B58/B59).
3. **1. Datenüberblick und Plausibilitätsprüfung**
   - **Befund:** 18 lückenlose Monate. Bestand aus 4.1 und 4.2 stimmt exakt überein
     (Cross-Sheet-Konsistenz). Geschlechter-Summe exakt, Alters-Summe weicht bis zu 11
     Personen ab (vermutlich Gruppe mit unbekanntem Alter).
4. **2. Eintritte und Bestand an Fördermaßnahmen im Zeitverlauf**
   - Kombi-Chart: Eintritte (Balken) + Bestand (Linie), zwei Achsen.
   - **Befund:** Eintritte volatil, leicht rückläufig (Ø 87,2/Monat, 119 → 91). Bestand
     stieg bis Höchststand 313 (April 2025), seither wieder auf 250 (März 2026); geglätteter
     12-Monatsdurchschnitt zeigt klaren Anstieg gegenüber 2024 (203,0 → 268,7).
5. **3. Aktivierungsquote im Zeitverlauf**
   - AQ1 (bezogen auf Teilnehmende + Arbeitslose) und AQ2a (bezogen auf alle ELB), je mit
     12-Monatsdurchschnitt.
   - **Befund:** beide Rohwerte rückläufig (AQ1: 13,3 % → 9,9 %; AQ2a: 6,0 % → 5,5 %); die
     12M-Durchschnitte zeigen ein differenzierteres Bild (AQ1-Ø leicht rückläufig, AQ2a-Ø
     sogar steigend).
6. **4. Struktur des Bestands: Geschlecht und Vorgeschichte**
   - **Befund:** Frauenanteil stabil (~44 %). Anteil zuvor langzeitarbeitsloser
     Teilnehmender steigt deutlich (16,2 % → 23,6 %) — passt zur steigenden
     Langzeitarbeitslosigkeit aus [`03_Statistik.ipynb`](03_Statistik.md).
7. **5. Export** — Schreibt `foerderung_sgb2.csv`.
8. **6. Zusammenfassung (Markdown)** — fasst alle Befunde zusammen, schließt die
   priorisierte Themenliste ab.

## Enthaltene Diagramme (3 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Kombi (Balken + Linie, 2 Achsen) | ✅ Plotly | Eintritte + Bestand |
| 2 | Liniendiagramm (4 Linien) | ✅ Plotly | AQ1/AQ2a + 12M-Durchschnitte |
| 3 | Liniendiagramm | ✅ Plotly | Anteil Frauen + Anteil vor Eintritt LZA |

## Voraussetzungen

- Python-Pakete: `openpyxl`, `pandas`, `plotly`
- Rohdaten unter `Data/RegensburgJCData/*.xlsx` müssen vorhanden sein

## Verwandte Dateien

- Priorisierung offener Themen: [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
- Anknüpfungspunkt Langzeitarbeitslosigkeit: [`03_Statistik.ipynb`](../Notebooks/03_Statistik.ipynb) /
  [`03_Statistik.md`](03_Statistik.md)
- Vergleichbare Vorgehensweise: [`06_Erwerbstaetigkeit.ipynb`](../Notebooks/06_Erwerbstaetigkeit.ipynb),
  [`07_Finanzen.ipynb`](../Notebooks/07_Finanzen.ipynb)
- Dashboard-Umsetzung: [`../Dashboard/app.py`](../Dashboard/app.py), Tab "🎯 Förderung"
