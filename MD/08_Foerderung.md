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
Wartezeit** → Zeitreihe für **Oktober 2024 – Juni 2026**.

⚠️ **Anonymisierung:** Kleine Fallzahlen (< 3) werden von der Bundesagentur als „*“
unterdrückt — betrifft vor allem die feineren Instrumenten-Unterkategorien. Dieses Notebook
beschränkt sich bewusst auf **Summenzeilen**, die über alle 21 Dateien hinweg durchgehend
als Zahl vorliegen. Ab Bericht August 2026 (Datenmonat Mai 2026) hat die Bundesagentur
zudem die Unterkategorie „Eingliederung von Langzeitarbeitslosen“ in „Eingliederung von
Langzeitleistungsbeziehenden“ umbenannt (Blatt 4.1 Z. 49/66, Blatt 4.2 Z. 47) — die
genutzten Summenzeilen sind davon nicht betroffen.

## Output

- `Docs/Abbildungen/` abb22–abb24 (Eintritte/Bestand, Aktivierungsquote, Anteile im Bestand) — für Projektdokumentation und -präsentation, erzeugt über
  `export_abbildung()` (Kopie im weißen Layout, gleiche Pixelmaße wie bisher).
- `Data/processed/foerderung_sgb2.csv` — Wide-Format-Zeitreihe mit Eintritten, Bestand
  (inkl. 12-Monatswerten), Struktur nach Geschlecht/Alter/LZA-Vorgeschichte sowie AQ1/AQ2a
  (inkl. 12-Monatsdurchschnitt). Grundlage für den Dashboard-Tab "🎯 Förderung".

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, Erklärung von Wartezeit und Anonymisierung.
2. **Setup & Parsing** — `parse_foerderung(path)`: liest Monat per Regex aus Zelle A6,
   kombiniert feste Zellen aus beiden Blättern (4.1: B39/F39/B40/B58/F58, 4.2:
   C39/D39/E39/F39/G39/H39/B56/B57/B58/B59).
3. **1. Datenüberblick und Plausibilitätsprüfung**
   - **Befund:** 21 lückenlose Monate. Bestand aus 4.1 und 4.2 stimmt exakt überein
     (Cross-Sheet-Konsistenz). Geschlechter-Summe exakt, Alters-Summe weicht bis zu 11
     Personen ab (vermutlich Gruppe mit unbekanntem Alter).
4. **2. Eintritte und Bestand an Fördermaßnahmen im Zeitverlauf**
   - Kombi-Chart: Eintritte (Balken) + Bestand (Linie), zwei Achsen.
   - **Befund:** Eintritte volatil, rückläufig (Ø 86,7/Monat, 119 → 73). Bestand stieg bis
     Höchststand 313 (April 2025), sank bis März 2026 auf 250 und stieg seither erneut auf
     291 (Juni 2026); geglätteter 12-Monatsdurchschnitt zeigt klaren Anstieg gegenüber 2024
     (203,0 → 263,8).
5. **3. Aktivierungsquote im Zeitverlauf**
   - AQ1 (bezogen auf Teilnehmende + Arbeitslose) und AQ2a (bezogen auf alle ELB), je mit
     12-Monatsdurchschnitt.
   - **Befund:** beide Rohwerte bis März 2026 rückläufig (AQ1: 13,3 % → 9,9 %), seither
     wieder steigend (Juni 2026: AQ1 11,8 %, AQ2a 6,6 % — über dem Startwert 6,0 %); die
     12M-Durchschnitte zeigen ein differenzierteres Bild (AQ1-Ø 12,3 % → 10,9 %, AQ2a-Ø
     5,3 % → 6,1 %).
6. **4. Struktur des Bestands: Geschlecht und Vorgeschichte**
   - **Befund:** Frauenanteil überwiegend stabil (~44 %). Anteil zuvor langzeitarbeitsloser
     Teilnehmender steigt deutlich (16,2 % → 25,1 %, Höchstwert 26,3 % im Mai 2026) — passt zur steigenden
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
