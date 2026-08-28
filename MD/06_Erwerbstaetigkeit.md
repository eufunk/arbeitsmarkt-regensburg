# Dokumentation: 06_Erwerbstaetigkeit.ipynb

## Zweck

Erschließt ein komplett neues Themenfeld: **erwerbstätige erwerbsfähige
Leistungsberechtigte (ELB)**, in der öffentlichen Diskussion oft „Aufstocker“ genannt —
Personen, die trotz eigenem Erwerbseinkommen ergänzend Bürgergeld beziehen. Bearbeitet
Priorität 3 aus dem Priorisierungsvorschlag in
[`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md), direkt anschlussfähig an die
Trichter-Grafik im Dashboard.

## Input

- `Data/RegensburgJCData/*.xlsx`, Tabellenblatt **"3.3 Erwerbstätigkeit"** — **neu
  eingelesen**, nicht Teil von `eckwerte_long.csv` (das nur "1.1 Eckwerte" abdeckt).

⚠️ **Wartezeit-Besonderheit:** Das Blatt liefert pro Datei zwei Datenblöcke: einen mit
**3 Monaten Wartezeit** (Einkommens-Unterteilung: Geringfügigkeitsgrenze/Übergangsbereich)
und einen mit **6 Monaten Wartezeit** (Unterteilung: Vollzeit/Teilzeit). Dieses Notebook
nutzt ausschließlich den 3-Monate-Block (feste Zeilen 35–43 je Datei). Da jede der 18
Dateien einen neuen Monat liefert, ergibt sich eine lückenlose Zeitreihe — jedoch
**3 Monate früher** als der Berichtsmonat der Datei: aus Januar 2025 – Juni 2026 wird
**Oktober 2024 – März 2026**.

## Output

- `Data/processed/erwerbstaetigkeit_sgb2.csv` — Wide-Format-Zeitreihe mit Insgesamt-ELB,
  erwerbstätigen ELB, abhängig/selbständig erwerbstätig, den drei Einkommensstufen sowie
  der berechneten Aufstockerquote. Grundlage für den Dashboard-Tab "💼 Erwerbstätigkeit".

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, ausführliche Erklärung der Wartezeit-Besonderheit.
2. **Setup & Parsing** — `parse_erwerbstaetigkeit(path)`: liest Monat aus Zelle B35, Werte
   aus den festen Zeilen 36–43 (Zeile 41 ist leer und wird übersprungen) der Spalte B.
3. **1. Datenüberblick und Plausibilitätsprüfung**
   - **Befund:** 18 lückenlose, eindeutige Monate (Okt 2024 – Mär 2026). Einkommensstufen
     summieren sich exakt zu "abhängig erwerbstätig" (Differenz = 0). "abhängig +
     selbständig" weicht dagegen um 4–12 Personen pro Monat von "erwerbstätige ELB" ab —
     ein kleiner, durchgängiger Erhebungseffekt der Bundesagentur, kein eigener Fehler.
4. **2. Erwerbstätige ELB im Zeitverlauf: die Aufstocker-Quote**
   - Zwei-Achsen-Chart: absolute Zahl + selbst berechnete Aufstockerquote
     (erwerbstätige ELB / Insgesamt ELB).
   - **Befund:** erwerbstätige ELB 795 → 721 Personen; Aufstockerquote stabil bei Ø 21,4 %
     (20,2–22,3 %), leicht rückläufig von 21,8 % auf 20,2 % — rund jede fünfte
     leistungsberechtigte Person ist erwerbstätig.
5. **3. Struktur: abhängig vs. selbständig erwerbstätig**
   - Gestapelte Fläche.
   - **Befund:** abhängig dominiert klar (93,3–94,2 %), selbständig bleibt stabile
     Minderheit (~6–7 %).
6. **4. Einkommensstruktur der abhängig Erwerbstätigen**
   - Gestapelte Fläche der drei Einkommensstufen.
   - **Befund:** leichte Verschiebung zu höheren Einkommen — "bis Geringfügigkeitsgrenze"
     sinkt (43,4 % → 38,1 % relativ zu "abhängig erwerbstätig"), "im Übergangsbereich"
     (48,0 % → 51,0 %) und "über dem Übergangsbereich" (8,6 % → 10,9 %) steigen.
7. **5. Export** — Schreibt `erwerbstaetigkeit_sgb2.csv`.
8. **6. Zusammenfassung (Markdown)** — fasst alle Befunde zusammen.

## Enthaltene Diagramme (3 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Zwei-Achsen-Liniendiagramm | ✅ Plotly | erwerbstätige ELB: absolut + Aufstockerquote |
| 2 | Gestapelte Fläche | ✅ Plotly | abhängig vs. selbständig erwerbstätig |
| 3 | Gestapelte Fläche | ✅ Plotly | Einkommensstufen der abhängig Erwerbstätigen |

## Voraussetzungen

- Python-Pakete: `openpyxl`, `pandas`, `plotly`
- Rohdaten unter `Data/RegensburgJCData/*.xlsx` müssen vorhanden sein (dieses Notebook
  liest — anders als 02–05 — direkt aus den Excel-Dateien, nicht aus `eckwerte_long.csv`)

## Verwandte Dateien

- Trichter-Grafik (Anschlusspunkt): [`Dashboard/app.py`](../Dashboard/app.py), Tab
  "SGB II Übersicht"
- Priorisierung offener Themen: [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
- Dashboard-Umsetzung: [`../Dashboard/app.py`](../Dashboard/app.py), Tab "💼 Erwerbstätigkeit"
