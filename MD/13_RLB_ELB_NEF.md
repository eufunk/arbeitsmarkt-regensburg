# Dokumentation: 13_RLB_ELB_NEF.ipynb

## Zweck

Offener Punkt aus [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md): Das Blatt
"1.1 Eckwerte" enthält im Block "Grundsicherung für Arbeitsuchende" neben den bereits seit
Kapitel 1 genutzten Kennzahlen **Bedarfsgemeinschaften (BG)** und **Personen in
Bedarfsgemeinschaften (PERS)** auch die Aufschlüsselung in **Regelleistungsberechtigte
(RLB)**, davon **erwerbsfähige Leistungsberechtigte (ELB)** und **nicht erwerbsfähige
Leistungsberechtigte (NEF)** — bislang nur als Momentaufnahme im Funnel-Chart des Dashboards
sichtbar, nie als eigene Zeitreihe betrachtet.

**Zusammenhang der Kennzahlen:** RLB = ELB + NEF. PERS ist größer als RLB — die Differenz
sind Haushaltsmitglieder, die zur Bedarfsgemeinschaft zählen, aber selbst nicht
leistungsberechtigt sind.

## Input

- `Data/processed/eckwerte_long.csv` (Langformat aus `01_Exploration.ipynb`) — enthält alle
  fünf Kennzahlen bereits vollständig, nur als SGB-II-Wert (kein "Insgesamt"-Gegenstück, da
  die Bedarfsgemeinschaft ein SGB-II-spezifisches Konzept ist).

**Keine neuen Rohdaten nötig.**

⚠️ **Hinweis zur Datenaktualität:** Ein Abgleich der jüngsten Rohdateien (April–Juni 2026) mit
den bereits aufbereiteten Werten aus `eckwerte_long.csv` zeigte Abweichungen in diesen drei
Monaten — plausibel durch nachträglich revidierte Werte in den Rohdateien selbst (ältere
Monate stimmen exakt überein). Um konsistent mit allen bisherigen Kapiteln zu bleiben, nutzt
dieses Notebook bewusst die bereits aufbereiteten (unveränderten) Werte statt neu einzulesen.

## Output

- `Data/processed/rlb_elb_nef_sgb2.csv` — Zeitreihe (SGB II) mit den Spalten `bg`, `pers`,
  `rlb`, `elb`, `nef`.
- `Docs/Abbildungen/abb38_rlb_elb_nef_zeitreihe.png`, `abb39_rlb_elb_nef_differenz.png`,
  `abb40_rlb_elb_nef_struktur.png` — für Kapitel 14 der Projektdokumentation/-präsentation.

## Ablauf (Zellen) und Kernbefunde

1. **Intro (Markdown)** — Einordnung, Kennzahlen-Zusammenhang, Hinweis zur Datenaktualität.
2. **Setup & Laden** — Filtert `eckwerte_long.csv` auf `kategorie == "Grundsicherung für
   Arbeitsuchende"`, pivotiert auf Wide-Format.
3. **1. Zeitreihe: RLB, ELB und NEF im Vergleich**
   - **Befund:** Alle drei Kennzahlen rückläufig — RLB −6,9 %, ELB −5,5 %, NEF −10,5 %. NEF
     (überwiegend Kinder) geht damit relativ am stärksten zurück.
4. **2. NEF-Anteil an den Regelleistungsberechtigten**
   - **Befund:** NEF-Anteil sinkt leicht von 28,3 % auf 27,2 % (Spanne 27,1–28,3 %).
5. **3. Nicht leistungsberechtigte Haushaltsmitglieder: PERS minus RLB**
   - **Befund:** Gegenläufiger Trend — die Zahl der nicht leistungsberechtigten
     Haushaltsmitglieder steigt von 286 auf 309 Personen (Anteil an PERS: 5,2 % → 6,0 %),
     obwohl BG, PERS und RLB insgesamt rückläufig sind.
6. **4. Struktur der Bedarfsgemeinschaften im letzten Berichtsmonat**
   - Donut-Chart: ELB / NEF / nicht leistungsberechtigt.
   - **Befund:** Rund 68 % ELB, 26 % NEF, 6 % nicht leistungsberechtigt.
7. **5. Zusammenfassung (Markdown)** — fasst den gegenläufigen Trend ein und ordnet ihn als
   neue, bislang unsichtbare Struktur-Information ein.
8. **Export** — schreibt `rlb_elb_nef_sgb2.csv`.

## Enthaltene Diagramme (3 insgesamt)

| # | Diagrammtyp | Interaktiv? | Inhalt |
|---|---|---|---|
| 1 | Liniendiagramm (3 Linien) | ✅ Plotly | RLB, ELB, NEF im Zeitverlauf |
| 2 | Liniendiagramm | ✅ Plotly | NEF-Anteil an RLB |
| 3 | Balken + Linie (2 Achsen) | ✅ Plotly | Nicht leistungsberechtigte Haushaltsmitglieder (absolut + Anteil) |
| 4 | Donut-Chart | ✅ Plotly | Struktur der Personen in Bedarfsgemeinschaften (letzter Monat) |

## Voraussetzungen

- Python-Pakete: `pandas`, `plotly`
- CSV aus `01_Exploration.ipynb` muss vorhanden sein

## Verwandte Dateien

- Datengrundlage: [`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
  [`01_Exploration.md`](01_Exploration.md)
- Bereits genutzte Kennzahlen BG/PERS: [`02_Analyse_SGBII.ipynb`](../Notebooks/02_Analyse_SGBII.ipynb)
- Aufstockerquote (nutzt ELB als Basis): [`06_Erwerbstaetigkeit.ipynb`](../Notebooks/06_Erwerbstaetigkeit.ipynb)
- Priorisierung offener Themen: [`ArbeitslosenAnalyse.md`](ArbeitslosenAnalyse.md)
