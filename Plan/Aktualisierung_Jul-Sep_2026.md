# Plan: Aktualisierung um Juli – September 2026

**Stand:** 28.10.2026
**Anlass:** In `Data/RegensburgJCData/` liegen drei neue Monatsberichte
(`jc-eckwerte-t73906-0-202607/08/09-xlsx.xlsx`). Aufbau und Tabellenblätter sind identisch zu den
bisherigen Dateien (geprüft für 202607 und 202609).

## Was sich ändert

| Bereich | bisher | neu |
|---|---|---|
| Berichtsmonate (aktueller Monatswert) | 18 · Jan 2025 – Jun 2026 | **21 · Jan 2025 – Sep 2026** |
| Blätter mit 3 Monaten Wartezeit (Kap. 6–9) | Okt 2024 – Mär 2026 | **Okt 2024 – Jun 2026** |
| Blätter mit 6 Monaten Wartezeit | bis Dez 2025 | **bis Mär 2026** |
| Beschäftigung (quartalsweise, Kap. 14) | 7 Quartale | voraussichtlich **8 Quartale** (wird beim Lauf geprüft) |
| Vorjahresvergleich (`iloc[-13]`) | 6 Monate mit Vorjahreswert | 9 Monate |
| Rollierende 12-Monats-Werte | 7 Werte | 10 Werte |

Der Code liest die Rohdaten überall per `glob("*.xlsx")` ein, er nimmt die neuen Dateien also
ohne Änderung auf. Anpassen muss ich vor allem die **fest eingetragenen Texte, Zahlen und
Zeiträume** in Markdown-Zellen, Plot-Titeln, MD-Dokus, Dashboard, Word und PowerPoint.
Alle Befunde (Werte, Min/Max, Trends, Prozentangaben) müssen nach dem Neulauf neu gelesen und
die Interpretation gegebenenfalls umformuliert werden.

---

## Phase 0 – Vorbereitung

- [x] Prüfen, ob `nbconvert`/`nbclient` installiert ist → `nbclient 0.11` ist vorhanden und
      reicht zum Ausführen der Notebooks; `nbconvert` wird nicht benötigt.
- [x] Kurzer Plausibilitätscheck der drei neuen Dateien: Berichtsmonat in Zelle „1.1 Eckwerte“,
      Zeilenpositionen der genutzten Blöcke (v. a. Blatt 1.1 Zeilen 9–47 und 49–58, 3.3, 3.6, 4.1, 4.2).
      → Spalte A (Zeilen 1–80) aller acht genutzten Blätter ist in 202607–202609 identisch zu
      202606, abgesehen vom Berichtsmonat. **Einzige inhaltliche Änderung:** ab Bericht 202608
      heißt die Maßnahmenkategorie in Blatt 4.1 (Z. 49, 66) und 4.2 (Z. 47) „Eingliederung von
      Langzeit**leistungsbeziehenden**“ statt „…von Langzeit**arbeitslosen**“. Notebook 08 liest
      diese Zeilen nicht (nur Summenzeilen 39/58 bzw. 39/56–59) → kein Codeeingriff, aber als
      Datenhinweis in Kap. 9 der Doku erwähnen.
- [x] Alte Kennzahlen als Vergleichsbasis sichern (Kopie von `Data/processed/*.csv` im
      Scratchpad), damit ich die Veränderungen gezielt nachverfolgen kann.

## Phase 1 – Datenaufbereitung (`01_Exploration.ipynb`)

- [x] Notebook komplett ausführen → `eckwerte_long.csv`, `kennzahlen_sgb2.csv` neu.
- [x] Prüfen: 21 eindeutige Monate, keine Duplikate/Lücken, gleiche Merkmalsliste wie bisher.
      → 651 Zeilen (vorher 558), 0 Duplikate; historische Werte unverändert (Diff nur Zugänge).
- [x] Markdown anpassen: „Januar 2025 – Juni 2026 (18 Berichtsmonate)“ → „Januar 2025 –
      September 2026 (21 Berichtsmonate)“; Beispiel zur Wartezeit („Bericht Juni 2026 → März 2026“)
      auf den neuesten Bericht umstellen.
- [x] `MD/01_Exploration.md` angleichen.

## Phase 2 – Analyse-Notebooks neu ausführen und Texte aktualisieren

Reihenfolge wie im README, weil 02–05 und 10–13 auf den CSVs aus 01 aufbauen.
Für **jedes** Notebook: ausführen → Ausgaben lesen → Markdown-Befunde, Plot-Titel und
Zeitraumangaben anpassen → zugehörige `MD/xx_*.md` angleichen → exportierte CSV prüfen.

| Nr. | Notebook | Besondere Punkte |
|---|---|---|
| 02 | Analyse_SGBII | Start-/Endwerte LZA, Indexierung, Vormonat/Vorjahr (jetzt Sep 2026 vs. Sep 2025) |
| 03 | Statistik | siehe **Phase 2a** unten |
| 04 | Fluktuation | Zugang/Abgang, Netto-Fluktuation, 12-Monatssummen (mehr Werte) |
| 05 | Demografie | Alters-/Geschlechts-/Ausländer-/Schwerbehindertenanteile, Endwerte |
| 06 | Erwerbstätigkeit | Zeitraum im Titel fest eingetragen (`Oktober 2024 – März 2026`) → bis Juni 2026; „18 Dateien / 18 Monate“ → 21 |
| 07 | Finanzen | Zeitraum + „18 Dateien“, Volumen/Ø je BG neu formulieren |
| 08 | Förderung | Zeitraum, Eintritte-Spanne, Bestandshöchststand, Aktivierungsquote |
| 09 | Bezugsdauer | Zeitraum, LZB-Anteil, Drehtür-Quote, Zugänge mit Vorbezug |
| 10 | Rechtskreisvergleich | viele feste Zeitangaben (43 Treffer) – alle durchgehen |
| 11 | Arbeitsstellen | Befunde zu Zugang/Bestand, Angebot-Nachfrage-Relation; Cross-Check `rolling(12)` jetzt mit 10 Werten. Das `str.contains`-Beispiel (2. Halbjahr 2025) bleibt, ist nur Syntaxdemo |
| 12 | Unterbeschäftigung | Komponenten und SGB-II-Anteil |
| 13 | RLB/ELB/NEF | „letzter Berichtsmonat“ ist jetzt September 2026 |
| 14 | Beschäftigung | Anzahl Quartale („7 Quartale“ an mehreren Stellen), Spannen AO/WO, Pendlersaldo; y-Achse ist fest auf `[33000, 34500]` gesetzt, prüfen ob neuer Wert hineinpasst |

### Phase 2a – Sonderfall `03_Statistik.ipynb`

Das Notebook enthält eine **Prognose für Juli–September 2026** (≈ 727, 740, 754
Langzeitarbeitslose). Diese Monate liegen jetzt als Istwerte vor.

Vorschlag:
- [ ] Regression wie bisher auf allen nun 21 Monaten neu rechnen (Monatsindex 0–20), R² und
      Steigung neu interpretieren; Hypothesentest (1. vs. 2. Hälfte) läuft auf 10/11 Monaten.
- [ ] **Neuer kurzer Abschnitt „Prognose vs. Ist“:** alte Prognose (Modell nur auf Jan 2025 –
      Jun 2026) gegen die tatsächlichen Werte Jul–Sep 2026 stellen (Tabelle + Abweichung in
      Personen und %). Das ist ein echter Out-of-Sample-Test und eine gute Ergänzung für die
      Präsentation.
- [ ] Neue Prognose für **Oktober – Dezember 2026**.
- [ ] Die Texte „18 Datenpunkte“, „Monatsindex 0 = Januar 2025 bis 17 = Juni 2026“ anpassen.

*→ Bitte bestätigen, ob der Abschnitt „Prognose vs. Ist“ gewünscht ist (auch als neue Abbildung
und Folie in Word/PowerPoint), oder ob nur stillschweigend aktualisiert werden soll.*

## Phase 3 – Abbildungen `Docs/Abbildungen/` neu erzeugen

- Aktuell exportieren nur die Notebooks 03 (abb32) und 11–14 (abb33–43) ihre Grafiken per
  `write_image`. **abb1–abb31 haben keinen Export-Code** im Notebook.
- [ ] In den Notebooks 02–10 den Export ergänzen, im gleichen Stil wie in 11–14
      (gleicher Dateiname, gleiche Größe/Skalierung wie die vorhandenen PNGs), damit die
      Abbildungen künftig reproduzierbar sind.
- [ ] Alle 43 Abbildungen neu schreiben; ggf. neue Abbildung „Prognose vs. Ist“ (abb44).
- [ ] Stichprobenartig ansehen, ob Achsen, Beschriftungen und Legenden mit 21 Monaten noch
      sauber aussehen.

## Phase 4 – Dashboard (`Dashboard/app.py`)

- Das Dashboard liest die CSVs dynamisch, Grafiken aktualisieren sich automatisch.
- [ ] Feste Texte anpassen: „Januar 2025 – Juni 2026“, „18 Monate“, „bis Juni 2026 …“,
      Wartezeit-Hinweis „bis Dezember 2025“ (Z. ~1196, 1336, 1441, 1507) sowie alle weiteren
      Befundtexte mit Zahlen.
- [ ] Lokal mit `streamlit run Dashboard/app.py` starten und alle Tabs kurz prüfen.
- [ ] `Dashboard/README.md` prüfen.

## Phase 5 – Markdown-Dokumentation

- [ ] `README.md`: „18 monatliche Excel-Berichte (Januar 2025 – Juni 2026)“ → 21 / September 2026.
- [ ] `MD/01–14_*.md`: parallel zu Phase 1–2 jeweils mitziehen (Zahlen, Zeiträume, Befunde).
- [ ] `MD/ArbeitslosenAnalyse.md`, `MD/ThemenCheck.md`: Zeitraumangaben anpassen.
- [ ] Zum Schluss Suche nach Restfundstellen: `18 Monat`, `Juni 2026`, `März 2026`
      (als Wartezeit-Ende), `Dezember 2025` (als 6-Monats-Ende), `7 Quartale`, `17 =`.

## Phase 6 – Word-Dokumentation (`Docs/Projektdokumentation.docx`)

16 Kapitel, 42 eingebettete Bilder, 1 Tabelle.
- [ ] Per Skript (python-docx) alle eingebetteten Abbildungen durch die neuen PNGs ersetzen
      (Zuordnung über die Reihenfolge/Bildunterschrift „Abbildung n“), Formatierung bleibt erhalten.
- [ ] Texte kapitelweise aktualisieren: 1.3 Datengrundlage (Zeitraum, Anzahl Berichte),
      alle Befundabsätze mit Zahlen in Kap. 3–15, 16 Fazit und Ausblick.
- [ ] Kap. 4.5 um „Prognose vs. Ist“ ergänzen (falls bestätigt).
- [ ] Tabelle (deskriptive Statistik) mit neuen Werten füllen.
- [ ] Inhaltsverzeichnis: Hinweis, dass es in Word mit F9 aktualisiert werden muss
      (python-docx kann das Feld nicht neu berechnen).

## Phase 7 – Präsentation (`Docs/Projektpraesentation.pptx`)

84 Folien, ~40 Bilder, Sprechernotizen vorhanden.
- [ ] Bilder auf den Folien per Skript (python-pptx) durch die neuen PNGs ersetzen,
      Position und Größe bleiben gleich.
- [ ] Folientexte und **Sprechernotizen** mit Zahlen/Zeiträumen aktualisieren
      (Titel-, Datengrundlage-, Befund- und Fazitfolien).
- [ ] Ggf. neue Folie „Prognose vs. Ist“ nach Folie 4.5 einfügen (falls bestätigt).
- [ ] Folien als Bilder rendern und visuell prüfen (Textüberlauf durch längere Zahlen).

## Phase 8 – Abschluss

- [ ] Gesamtsuche nach veralteten Angaben (siehe Phase 5, letzter Punkt) über Notebooks, MD,
      Dashboard, Word, PowerPoint.
- [ ] Notebooks mit Ausgaben gespeichert lassen (wie bisher im Repo).
- [ ] `git status` prüfen: Rohdaten bleiben unversioniert (`.gitignore`).
- [ ] Ein Commit mit allen Änderungen, z. B.
      „Daten um Juli–September 2026 erweitern: Notebooks, Abbildungen, Dashboard und
      Dokumentation aktualisiert“, danach `git push` auf `main`.
      Das Streamlit-Dashboard zieht die neuen CSVs nach dem Push automatisch.

---

## Entscheidungen (28.10.2026)

1. **Prognose vs. Ist** in Notebook 03 sowie in Word/PowerPoint ergänzen: **ja**.
2. **Export-Code für abb1–31** in die Notebooks 02–10 einbauen: **ja**.
3. **Ein Commit pro Phase**, Push erst am Ende.
