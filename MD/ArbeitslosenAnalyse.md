# Arbeitslosenanalyse Regensburg — Inhaltliche Themenübersicht

Überblick, welche Aspekte der Arbeitslosigkeit im Jobcenter Regensburg (Rechtskreis SGB II,
Januar 2025 – Juni 2026) wir aus den Rohdaten bereits ausgewertet haben, und was in den
Rohdaten noch steckt, aber bislang nicht analysiert wurde.

Rohdaten: `Data/RegensburgJCData/*.xlsx` (18 Monatsberichte "Eckwerte für Jobcenter").
Kernanalyse basiert auf dem Tabellenblatt **"1.1 Eckwerte"** (Spalte B = Insgesamt
SGB II+SGB III, Spalte G = Rechtskreis SGB II je Berichtsmonat); ergänzend werden die
Blätter **"3.3 Erwerbstätigkeit"**, **"3.6 Zahlungsansprüche"**, **"4.1 Förderung"** und
**"4.2 Förderung Strukturen"** ausgewertet (jeweils direkt aus den Excel-Rohdaten, ⚠️ mit
3 Monaten Wartezeit).

## ✅ Bereits analysiert

- **Bestand der Arbeitslosen** (SGB II) über die Zeit — leicht gestiegen (1.470 → 1.500),
  Spanne 1.382–1.587
- **Arbeitslosenquote** über die Zeit — stabil zwischen 1,2 % und 1,4 %
- **Langzeitarbeitslosigkeit** — absolute Zahl und Anteil am Bestand; deutlichster Trend
  (502 → 709 Personen, Anteil 34 % → 47 %)
- **Unterbeschäftigungsquote** im Vergleich zur Arbeitslosenquote
- **Bedarfsgemeinschaften** und **Personen im Leistungsbezug** über die Zeit — beide
  rückläufig (ca. −4 % bzw. −6 %)
- **Altersstruktur** der Arbeitslosen (15–25 / 25–50 / 50+) — nur letzter Berichtsmonat,
  keine Zeitreihe
- **Geschlechterverteilung** (Männer/Frauen) — nur letzter Berichtsmonat, keine Zeitreihe
- **Veränderung zum Vormonat / Vorjahresmonat** für die vier Kernkennzahlen (Bestand,
  Langzeitarbeitslose, Bedarfsgemeinschaften, Personen in BG)
- **Fluktuation** (Zugang/Abgang aus Arbeitslosigkeit, im Monat und als 12-Monatssumme) —
  Zugang Ø 267/Monat, Abgang Ø 281/Monat, Netto-Fluktuation überwiegend negativ; Abgleich mit
  der Bestandsänderung zeigt eine systematische Differenz von rund 21 Personen/Monat, plausibel
  durch Rechtskreiswechsel SGB II ↔ SGB III erklärbar (siehe
  [`04_Fluktuation.ipynb`](../Notebooks/04_Fluktuation.ipynb))
- **Altersstruktur und Geschlecht als Zeitreihe** (statt nur Momentaufnahme), plus **55+ als
  Teilmenge von 50+** — sehr stabile Verteilung, aber Anteil der 55-Jährigen und Älteren an
  der Gruppe 50+ steigt von 64,8 % auf 68,8 %; Männeranteil steigt leicht (53,1 % → 54,5 %)
- **Schwerbehinderte Menschen** unter den Arbeitslosen — kleiner, leicht steigender Anteil
  (7,9 % → 8,7 %)
- **Ausländische Arbeitslose** — überraschend hoher, deutlich rückläufiger Anteil (51,7 % →
  45,4 % des Bestands); bislang auffälligste neue Erkenntnis abseits der
  Langzeitarbeitslosigkeit (siehe [`05_Demografie.ipynb`](../Notebooks/05_Demografie.ipynb))
- **Erwerbstätigkeit trotz Bürgergeld-Bezug ("Aufstocker")** — erstmals Blatt „3.3
  Erwerbstätigkeit“ ausgewertet (⚠️ 3 Monate Wartezeit, Zeitreihe daher Okt 2024 – Mär 2026):
  Aufstockerquote stabil bei Ø 21,4 % (rund jede fünfte erwerbsfähige leistungsberechtigte
  Person ist erwerbstätig), klar dominiert von abhängiger Beschäftigung (93–94 %), leichte
  Verschiebung zu höheren Einkommen innerhalb der Aufstocker (siehe
  [`06_Erwerbstaetigkeit.ipynb`](../Notebooks/06_Erwerbstaetigkeit.ipynb))
- **Zahlungsansprüche (Finanzen)** — erstmals Blatt „3.6 Zahlungsansprüche“ ausgewertet, die
  einzige Quelle für tatsächliche Euro-Beträge (⚠️ 3 Monate Wartezeit, Zeitreihe daher Okt
  2024 – Mär 2026): Gesamtvolumen praktisch stabil (3.451,5 → 3.473,0 Tsd. Euro), aber Ø je
  Bedarfsgemeinschaft spürbar gestiegen (1.251 € → 1.288 €); Sozialversicherungsbeiträge
  steigen deutlich (15,6 % → 18,3 % Anteil), Regelbedarf NEF sinkt (siehe
  [`07_Finanzen.ipynb`](../Notebooks/07_Finanzen.ipynb))
- **Förderung der aktiven Arbeitsmarktpolitik** — erstmals Blätter „4.1 Förderung“ und „4.2
  Förderung Strukturen“ ausgewertet (⚠️ 3 Monate Wartezeit, Zeitreihe daher Okt 2024 – Mär
  2026): Bestand an Teilnehmenden stieg bis Höchststand 313 (April 2025), seither wieder auf
  250 gesunken; Aktivierungsquoten AQ1/AQ2a rückläufig; Anteil zuvor langzeitarbeitsloser
  Teilnehmender steigt deutlich (16,2 % → 23,6 %) — passt zur steigenden
  Langzeitarbeitslosigkeit (siehe [`08_Foerderung.ipynb`](../Notebooks/08_Foerderung.ipynb))

## 🔲 In den Rohdaten vorhanden, aber noch nicht analysiert

### Noch ungenutzte Zeilen in "1.1 Eckwerte" (gleiches Blatt, das wir schon nutzen)
- **Gemeldete Arbeitsstellen** (Zugang, Bestand, davon sozialversicherungspflichtig) —
  Nachfrageseite des Arbeitsmarkts, bisher komplett ausgeklammert
- **Unterbeschäftigung im engeren Sinne** und **ohne Kurzarbeit** (Detailkomponenten der
  Unterbeschäftigung, wir nutzen bisher nur "im weiteren Sinne" für die Quote)
- **Regelleistungsberechtigte (RLB)**, **erwerbsfähige (ELB)** vs. **nicht erwerbsfähige
  Leistungsberechtigte (NEF)** — Struktur innerhalb der Bedarfsgemeinschaften
- **sozialversicherungspflichtige und geringfügig entlohnte Beschäftigung** (nach Arbeits-
  und Wohnort) — Beschäftigungsentwicklung als Gegenstück zur Arbeitslosigkeit
- **Vergleich "Insgesamt (SGB II+SGB III)" vs. "SGB II"** — wie hoch ist der Jobcenter-Anteil
  an der gesamten Arbeitslosigkeit, und verändert er sich über die Zeit?

### Noch ungenutzte Tabellenblätter

Jede der 18 Dateien hat 21 Tabellenblätter, nicht nur "1.1 Eckwerte". Alle wurden mittlerweile
systematisch gesichtet — Abschnitt "1. Tabellenblätter der Rohdaten untersuchen" in
[`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) gibt für jedes Blatt per Print-Ausgabe
eine Einschätzung (Daten + Diagramm-Ideen). Kurzfassung hier:

**⚠️ Wichtige Einschränkung:** Die Blätter **3.1–3.6** und **4.1–4.2** melden nicht den
Berichtsmonat des Dateinamens, sondern Daten mit **3 bzw. 6 Monaten Wartezeit** (z. B. meldet
die Juni-2026-Datei dort Stand "März 2026" bzw. "Dezember 2025"). Beim Aufbau einer Zeitreihe
aus mehreren Dateien muss der tatsächliche Stichmonat aus dem Blattinhalt gelesen werden, nicht
aus dem Dateinamen abgeleitet werden.

- **1.2 Eckwerte Zeitreihe** — enthält bereits eine rollierende ~13-Monats-Zeitreihe direkt im
  Bericht (gleiche Kennzahlen wie 1.1). Eignet sich als Cross-Check für unsere selbst gebaute
  Zeitreihe, liefert aber keine neuen Kennzahlen.
- **2.1 Arbeitslosigkeit Zugang** — Zugang nach Zugangsgrund (z. B. "aus Erwerbstätigkeit").
  Idee: gestapeltes Balkendiagramm "woher kommen die neuen Arbeitslosen".
- **2.2 Arbeitslosigkeit Bestand** — inhaltlich weitgehend deckungsgleich mit "1.1", kein
  großer Mehrwert.
- **2.3 Arbeitslosigkeit Abgang** — Abgang nach Abgangsgrund (z. B. "in Erwerbstätigkeit").
  Idee: Zugang vs. Abgang nach Grund gegenüberstellen, um zu sehen, wie viele tatsächlich in
  Arbeit abgehen.
- **2.4 Langzeitarbeitslosigkeit** — Langzeitarbeitslose zusätzlich nach Geschlecht (nicht nur
  Alter wie in "1.1"). Idee: Geschlechterverteilung der Langzeitarbeitslosen als Zeitreihe.
- **2.5 Unterbeschäftigung** — feinere Komponenten der Unterbeschäftigungs-Lücke (z. B.
  "Aktivierung und berufliche Eingliederung", "Sonderregelung für Ältere"). Idee: gestapeltes
  Flächendiagramm der Komponenten.
- **3.1 Bedarfsgemeinschaften** — Struktur nach **Haushaltsgröße** (1, 2, 3, 4+ Personen), nicht
  nach BG-Typ wie ursprünglich vermutet. Idee: Balkendiagramm der Haushaltsgrößenverteilung,
  Zeitreihe des Single-Haushalt-Anteils.
- **3.2 Personen in BG** — Aufschlüsselung nach Geschlecht plus Teilmenge ELB.
- **3.4 Langzeitleistungsbezug** — neue Kennzahl **Langzeitleistungsbeziehende (LZB)**: mind.
  21 von 24 Monaten im Bezug — nicht identisch mit Langzeitarbeitslosen, da Bürgergeld auch
  ohne Arbeitslosigkeit bezogen werden kann. Idee: LZB vs. LZA im Vergleich.
- **3.5 Bewegungen Personen** — Zu-/Abgänge im Regelleistungsbezug (ELB-Ebene) inkl.
  Vorbezugs-Historie (Hinweis auf "Drehtür-Effekt": erneuter Bezug innerhalb 12 Monaten).

Nicht nutzbar (reine Metadaten/Links, keine Zahlen): Deckblatt, Impressum, Inhaltsverzeichnis
(nützlich nur als Zeichenerklärung-Nachschlagewerk), Grafik (nur eingebettete Bilder), Linkliste,
Statistik-Infoseite.

## Priorisierungsvorschlag für die Fortsetzung

1. ~~Zugang/Abgang (Fluktuation) ergänzen~~ — ✅ erledigt, siehe
   [`04_Fluktuation.ipynb`](../Notebooks/04_Fluktuation.ipynb)
2. ~~Altersstruktur/Geschlecht als Zeitreihe statt Momentaufnahme~~ — ✅ erledigt (inkl.
   Ausländer, Schwerbehinderte), siehe [`05_Demografie.ipynb`](../Notebooks/05_Demografie.ipynb)
3. ~~Erwerbstätigkeit/Aufstocker (3.3)~~ — ✅ erledigt, siehe
   [`06_Erwerbstaetigkeit.ipynb`](../Notebooks/06_Erwerbstaetigkeit.ipynb)
4. ~~Zahlungsansprüche (3.6)~~ — ✅ erledigt, siehe
   [`07_Finanzen.ipynb`](../Notebooks/07_Finanzen.ipynb)
5. ~~Förderung (4.1/4.2)~~ — ✅ erledigt, siehe
   [`08_Foerderung.ipynb`](../Notebooks/08_Foerderung.ipynb)

**Damit ist die ursprüngliche Priorisierungsliste vollständig abgearbeitet.** Als
nachrangiges, nicht priorisiertes Thema bleibt Bezugsdauer (Langzeitleistungsbezug,
Drehtür-Effekt, Haushaltsgrößenstruktur; Blätter 3.1, 3.4, 3.5) offen — siehe Abschnitt
"Noch ungenutzte Tabellenblätter" oben.

## 📊 Dashboard

Ist bereits gebaut und deployed: **Streamlit**, mit Kopfzeilen-Tabs (`st.tabs()`) als
Navigation. [Live-Dashboard](https://daelwve9mj8pxz32vshq7u.streamlit.app/),
Details: [`Dashboard/README.md`](../Dashboard/README.md).

- Tab **"SGB II Übersicht"** enthält alle bisher fertigen Charts (entspricht inhaltlich
  `02_Analyse_SGBII.ipynb`, plus Trichter-Grafik und formatierte Kennzahlen-Tabelle)
- Tab **"Fluktuation"** ist fertig (entspricht `04_Fluktuation.ipynb`): Zugang/Abgang im
  Monatsverlauf, Netto-Fluktuation vs. Bestandsänderung, 12-Monatssummen
- Tab **"Demografie"** ist fertig (entspricht `05_Demografie.ipynb`): Altersstruktur und
  Geschlecht als Zeitreihe, plus Ausländer und Schwerbehinderte als Zeitreihe
- Tab **"Erwerbstätigkeit"** ist fertig (entspricht `06_Erwerbstaetigkeit.ipynb`):
  Aufstockerquote, abhängig vs. selbständig, Einkommensstruktur — mit eigenem
  Zeitfenster (Okt 2024 – Mär 2026), unabhängig vom Sidebar-Zeitraum-Filter
- Tab **"Finanzen"** ist fertig (entspricht `07_Finanzen.ipynb`): Gesamtvolumen der
  Zahlungsansprüche + Ø je BG, Struktur nach Regelbedarf/KdU/Sozialversicherung — ebenfalls
  mit eigenem Zeitfenster (Okt 2024 – Mär 2026)
- Tab **"Förderung"** ist fertig (entspricht `08_Foerderung.ipynb`): Eintritte + Bestand an
  Fördermaßnahmen, Aktivierungsquote AQ1/AQ2a, Struktur nach Geschlecht/LZA-Vorgeschichte —
  ebenfalls mit eigenem Zeitfenster (Okt 2024 – Mär 2026)
- Nur noch **ein** Tab ist Platzhalter: "Bezugsdauer" (nachrangig, nicht in der
  Priorisierungsliste) — zeigt bereits Datenquelle und geplante Diagramme
- Tab **"Glossar"** erklärt alle im Dashboard verwendeten Fachbegriffe (Grundbegriffe,
  Personengruppen wie ELB/RLB/NEF, Kennzahlen, Aufstocker-Einkommen, Zahlungsansprüche,
  Datenbesonderheiten wie die Wartezeit-Problematik) — gruppiert in aufklappbaren
  Abschnitten
- Zeitraum-Filter (Slider) und Berichtsmonat-Auswahl in der Sidebar, wirken auf alle
  Zeitreihen-Charts bzw. Momentaufnahmen mit gemeinsamem Zeitfenster (nicht auf die Tabs
  Erwerbstätigkeit, Finanzen und Förderung, siehe oben)
- Datenbasis: die aufbereiteten CSVs aus `Data/processed/`
  (`eckwerte_long.csv`, `kennzahlen_sgb2.csv`, `fluktuation_sgb2.csv`,
  `demografie_sgb2.csv`, `erwerbstaetigkeit_sgb2.csv`, `finanzen_sgb2.csv`,
  `foerderung_sgb2.csv`) — kein erneutes Excel-Parsing nötig
- Alle Charts interaktiv (Plotly, `hovermode="x unified"`)

Nächster Schritt: bei Bedarf den verbleibenden Platzhalter-Tab "Bezugsdauer" mit echten
Charts befüllen (nachrangig, siehe oben).
