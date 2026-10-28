# Dokumentation: 07_Finanzen.ipynb

## Zweck

Erschließt die **einzige Quelle für tatsächliche Euro-Beträge** im gesamten Datensatz:
Höhe und Struktur der Zahlungsansprüche für Bedarfsgemeinschaften (BG) nach SGB II.
Bearbeitet Priorität 4 aus dem Priorisierungsvorschlag in
[`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md).

## Input

- `Data/RegensburgJCData/*.xlsx`, Tabellenblatt **"3.6 Zahlungsansprüche"** — **neu
  eingelesen**, wie schon [`06_Erwerbstaetigkeit.ipynb`](06_Erwerbstaetigkeit.md) direkt aus
  den Excel-Rohdaten, nicht aus `eckwerte_long.csv`.
- `Data/processed/kennzahlen_sgb2.csv` (für den Cross-Check des BG-Bestands)

⚠️ **Wartezeit:** Anders als Blatt „3.3 Erwerbstätigkeit“ (zwei Blöcke) liefert dieses Blatt
nur **einen** Datenblock pro Datei mit **3 Monaten Wartezeit**. Da jede der 21 Dateien einen
neuen Monat liefert, ergibt sich eine lückenlose Zeitreihe für **Oktober 2024 – Juni 2026**
(3 Monate vor dem jeweiligen Berichtsmonat der Datei).

## Output

- `Docs/Abbildungen/` abb20–abb21 (Volumen und Ø je BG, Struktur der Zahlungsansprüche) — für Projektdokumentation und -präsentation, erzeugt über
  `export_abbildung()` (Kopie im weißen Layout, gleiche Pixelmaße wie bisher).
- `Data/processed/finanzen_sgb2.csv` — Wide-Format-Zeitreihe mit Gesamtvolumen, Ø je BG,
  BG-Bestand sowie den sechs Einzelposten der Zahlungsansprüche. Grundlage für den
  Dashboard-Tab "💶 Finanzen".

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, Erklärung der (einfacheren) Wartezeit-Struktur
   gegenüber Kapitel 6.
2. **Setup & Parsing** — `parse_zahlungsansprueche(path)`: liest Monat per Regex aus Zelle
   A5 (z. B. "Juni 2026 - Daten nach einer Wartezeit von 3 Monaten"), Werte aus den festen Zeilen
   36 (Insgesamt, Ø je BG, Bestand BG) und 38–47 (Einzelposten) der Spalte B.
3. **1. Datenüberblick und Cross-Check gegen die eigene BG-Zeitreihe**
   - Summen-Check: sechs Einzelposten (Regelbedarf ELB/NEF, Mehrbedarfe, Kosten der
     Unterkunft, Sozialversicherungsbeiträge, weitere Zahlungsansprüche) summieren sich
     exakt zu "Insgesamt". "Gesamtregelleistung (Bürgergeld)" ist eine Teilsumme aus den
     ersten vier Posten und wird separat mitgeführt, aber nicht mitgestapelt (sonst
     Doppelzählung).
   - Cross-Check "Bestand BG" (aus diesem Blatt) gegen die eigene
     Bedarfsgemeinschaften-Zeitreihe für die 18 Überlapp-Monate (Jan 2025 – Jun 2026).
   - **Befund:** Summen-Check exakt (Differenz < 0,001), Cross-Check zeigt kleine,
     unsystematische Abweichung (Ø −12,5, Spanne −47 bis +49 BG) — Daten konsistent.
4. **2. Gesamtvolumen der Zahlungsansprüche im Zeitverlauf**
   - Zwei-Achsen-Chart: Insgesamt (Tsd. Euro) + Ø je BG (Euro).
   - **Befund:** Gesamtvolumen praktisch stabil (3.451,5 → 3.443,1 Tsd. Euro), aber Ø je BG
     spürbar gestiegen (1.251 € → 1.299 €) — sinkende BG-Zahl bei stabilem Gesamtvolumen.
5. **3. Struktur der Zahlungsansprüche**
   - Gestapelte Fläche der sechs Einzelposten.
   - **Befund:** Regelbedarf ELB (größter Posten, 41,6 % → 39,4 %) und Kosten der
     Unterkunft (~36 %) dominieren. Sozialversicherungsbeiträge steigen deutlich
     (15,6 % → 18,0 %), Regelbedarf NEF sinkt (3,8 % → 2,8 %).
6. **4. Export** — Schreibt `finanzen_sgb2.csv`.
7. **5. Zusammenfassung (Markdown)** — fasst alle Befunde zusammen.

## Enthaltene Diagramme (2 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Zwei-Achsen-Liniendiagramm | ✅ Plotly | Gesamtvolumen + Ø je BG |
| 2 | Gestapelte Fläche | ✅ Plotly | Struktur der Zahlungsansprüche (6 Einzelposten) |

## Voraussetzungen

- Python-Pakete: `openpyxl`, `pandas`, `plotly`
- Rohdaten unter `Data/RegensburgJCData/*.xlsx` müssen vorhanden sein
- `Data/processed/kennzahlen_sgb2.csv` für den Cross-Check (aus `01_Exploration.ipynb`)

## Verwandte Dateien

- Priorisierung offener Themen: [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
- Vergleichbare Vorgehensweise: [`06_Erwerbstaetigkeit.ipynb`](../Notebooks/06_Erwerbstaetigkeit.ipynb) /
  [`06_Erwerbstaetigkeit.md`](06_Erwerbstaetigkeit.md)
- Dashboard-Umsetzung: [`../Dashboard/app.py`](../Dashboard/app.py), Tab "💶 Finanzen"
