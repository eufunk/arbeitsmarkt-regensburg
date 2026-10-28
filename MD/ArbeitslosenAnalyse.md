# Arbeitslosenanalyse Regensburg — Inhaltliche Themenübersicht

Überblick, welche Aspekte der Arbeitslosigkeit im Jobcenter Regensburg (Rechtskreis SGB II,
Januar 2025 – September 2026) wir aus den Rohdaten bereits ausgewertet haben, und was in den
Rohdaten noch steckt, aber bislang nicht analysiert wurde.

Rohdaten: `Data/RegensburgJCData/*.xlsx` (21 Monatsberichte "Eckwerte für Jobcenter").
Kernanalyse basiert auf dem Tabellenblatt **"1.1 Eckwerte"** (Spalte B = Insgesamt
SGB II+SGB III, Spalte G = Rechtskreis SGB II je Berichtsmonat); ergänzend werden die
Blätter **"3.1 Bedarfsgemeinschaften"**, **"3.3 Erwerbstätigkeit"**, **"3.4
Langzeitleistungsbezug"**, **"3.5 Bewegungen Personen"**, **"3.6 Zahlungsansprüche"**,
**"4.1 Förderung"** und **"4.2 Förderung Strukturen"** ausgewertet (jeweils direkt aus den
Excel-Rohdaten, ⚠️ mit 3 Monaten Wartezeit).

## ✅ Bereits analysiert

- **Bestand der Arbeitslosen** (SGB II) über die Zeit — leicht gestiegen (1.470 → 1.523),
  Spanne 1.382–1.587
- **Arbeitslosenquote** über die Zeit — stabil zwischen 1,2 % und 1,4 %
- **Langzeitarbeitslosigkeit** — absolute Zahl und Anteil am Bestand; deutlichster Trend
  (502 → 698 Personen, Anteil 34 % → 46 %); Höchststand 714 im Mai 2026, seither Plateau —
  die lineare Prognose für Juli–September 2026 lag dadurch um 5–7 % zu hoch (siehe Abschnitt
  „Prognose vs. Ist“ in [`03_Statistik.ipynb`](../Notebooks/03_Statistik.ipynb))
- **Unterbeschäftigungsquote** im Vergleich zur Arbeitslosenquote
- **Bedarfsgemeinschaften** und **Personen im Leistungsbezug** über die Zeit — beide
  rückläufig (ca. −8 % bzw. −11 %)
- **Altersstruktur** der Arbeitslosen (15–25 / 25–50 / 50+) — nur letzter Berichtsmonat,
  keine Zeitreihe
- **Geschlechterverteilung** (Männer/Frauen) — nur letzter Berichtsmonat, keine Zeitreihe
- **Veränderung zum Vormonat / Vorjahresmonat** für die vier Kernkennzahlen (Bestand,
  Langzeitarbeitslose, Bedarfsgemeinschaften, Personen in BG)
- **Fluktuation** (Zugang/Abgang aus Arbeitslosigkeit, im Monat und als 12-Monatssumme) —
  Zugang Ø 270/Monat, Abgang Ø 283/Monat, Netto-Fluktuation überwiegend negativ; Abgleich mit
  der Bestandsänderung zeigt eine systematische Differenz von rund 20 Personen/Monat, plausibel
  durch Rechtskreiswechsel SGB II ↔ SGB III erklärbar (siehe
  [`04_Fluktuation.ipynb`](../Notebooks/04_Fluktuation.ipynb))
- **Altersstruktur und Geschlecht als Zeitreihe** (statt nur Momentaufnahme), plus **55+ als
  Teilmenge von 50+** — sehr stabile Verteilung, aber Anteil der 55-Jährigen und Älteren an
  der Gruppe 50+ steigt von 64,8 % auf 71,4 %; Männeranteil weitgehend stabil (53,1 % → 53,6 %)
- **Schwerbehinderte Menschen** unter den Arbeitslosen — kleiner, leicht steigender Anteil
  (7,9 % → 8,8 %)
- **Ausländische Arbeitslose** — überraschend hoher, deutlich rückläufiger Anteil (51,7 % →
  45,0 % des Bestands); bislang auffälligste neue Erkenntnis abseits der
  Langzeitarbeitslosigkeit (siehe [`05_Demografie.ipynb`](../Notebooks/05_Demografie.ipynb))
- **Erwerbstätigkeit trotz Bürgergeld-Bezug ("Aufstocker")** — erstmals Blatt „3.3
  Erwerbstätigkeit“ ausgewertet (⚠️ 3 Monate Wartezeit, Zeitreihe daher Okt 2024 – Jun 2026):
  Aufstockerquote stabil bei Ø 21,2 % (rund jede fünfte erwerbsfähige leistungsberechtigte
  Person ist erwerbstätig), klar dominiert von abhängiger Beschäftigung (93–95 %), leichte
  Verschiebung zu höheren Einkommen innerhalb der Aufstocker (siehe
  [`06_Erwerbstaetigkeit.ipynb`](../Notebooks/06_Erwerbstaetigkeit.ipynb))
- **Zahlungsansprüche (Finanzen)** — erstmals Blatt „3.6 Zahlungsansprüche“ ausgewertet, die
  einzige Quelle für tatsächliche Euro-Beträge (⚠️ 3 Monate Wartezeit, Zeitreihe daher Okt
  2024 – Jun 2026): Gesamtvolumen praktisch stabil (3.451,5 → 3.443,1 Tsd. Euro), aber Ø je
  Bedarfsgemeinschaft spürbar gestiegen (1.251 € → 1.299 €); Sozialversicherungsbeiträge
  steigen deutlich (15,6 % → 18,0 % Anteil), Regelbedarf NEF sinkt (siehe
  [`07_Finanzen.ipynb`](../Notebooks/07_Finanzen.ipynb))
- **Förderung der aktiven Arbeitsmarktpolitik** — erstmals Blätter „4.1 Förderung“ und „4.2
  Förderung Strukturen“ ausgewertet (⚠️ 3 Monate Wartezeit, Zeitreihe daher Okt 2024 – Jun
  2026): Bestand an Teilnehmenden stieg bis Höchststand 313 (April 2025), sank bis März 2026
  auf 250 und steigt seither wieder (Juni 2026: 291); Aktivierungsquoten AQ1/AQ2a bis
  Frühjahr 2026 rückläufig, seither wieder steigend; Anteil zuvor langzeitarbeitsloser
  Teilnehmender steigt deutlich (16,2 % → 25,1 %) — passt zur steigenden
  Langzeitarbeitslosigkeit (siehe [`08_Foerderung.ipynb`](../Notebooks/08_Foerderung.ipynb))
- **Bezugsdauer** (Haushaltsstruktur, Langzeitleistungsbezug, Drehtür-Effekt) — erstmals
  Blätter „3.1 Bedarfsgemeinschaften“, „3.4 Langzeitleistungsbezug“ und „3.5 Bewegungen
  Personen“ kombiniert ausgewertet (⚠️ 3 Monate Wartezeit, Zeitreihe daher Okt 2024 – Jun
  2026): Single-Bedarfsgemeinschaften nehmen relativ zu (57,0 % → 59,4 %); über die Hälfte
  aller ELB ist inzwischen langzeitleistungsbeziehend (LZB-Anteil 48,9 % → 56,3 %); Anteil
  der Zugänge mit Vorbezug steigt deutlich (56,1 % → 70,9 %) — echte Erstzugänge werden
  seltener (siehe [`09_Bezugsdauer.ipynb`](../Notebooks/09_Bezugsdauer.ipynb))
- **Vergleich "Insgesamt (SGB II+SGB III)" vs. "SGB II"** (Rechtskreisvergleich) — der
  Jobcenter-Anteil an allen Arbeitslosen liegt stabil bei nur Ø 39,7 % (Mehrheit ≈ 60 %
  fällt in die Zuständigkeit der Agentur für Arbeit); bei Langzeitarbeitslosen liegt der
  Jobcenter-Anteil dagegen bei Ø 72,2 % — plausibel durch die zeitliche Befristung von
  Arbeitslosengeld I (SGB III); SGB-III-Langzeitarbeitslosigkeit wächst sogar noch stärker
  (+ 58 %) als die SGB-II-Zahl (+ 39 %) (siehe
  [`10_Rechtskreisvergleich.ipynb`](../Notebooks/10_Rechtskreisvergleich.ipynb))
- **Gemeldete Arbeitsstellen** (Nachfrageseite des Arbeitsmarkts) — erstmals den Block
  „gemeldete Arbeitsstellen“ aus „1.1 Eckwerte“ direkt ausgewertet (⚠️ nicht nach Rechtskreis
  differenziert, nur „Insgesamt“-Wert): Bestand sinkt deutlich von 1.571 auf 1.208 (−23 %);
  Relation „Arbeitsstellen je 100 Arbeitslose“ fällt von 106,9 auf 79,3 — ein von den
  Arbeitslosenzahlen unabhängiger Beleg für eine sich eintrübende Arbeitsmarktlage (siehe
  [`11_Arbeitsstellen.ipynb`](../Notebooks/11_Arbeitsstellen.ipynb))
- **Unterbeschäftigung im engeren Sinne / ohne Kurzarbeit** — erstmals als eigene Zeitreihe
  ausgewertet (bisher nur die Quote genutzt): Kurzarbeiter-Komponente im SGB-II-Kontext
  verschwindend gering (Ø 2,4 Personen), Maßnahmen-Komponente deutlich substanzieller (Ø 388
  Personen); SGB-II-Anteil an der Unterbeschäftigung (41–50 %) liegt zwischen dem Anteil am
  Arbeitslosenbestand (≈ 40 %) und dem an der Langzeitarbeitslosigkeit (≈ 72 %) (siehe
  [`12_Unterbeschaeftigung.ipynb`](../Notebooks/12_Unterbeschaeftigung.ipynb))
- **Regelleistungsberechtigte (RLB), erwerbsfähige (ELB) vs. nicht erwerbsfähige (NEF)** —
  Struktur innerhalb der Bedarfsgemeinschaften erstmals als eigene Zeitreihe statt nur
  Momentaufnahme ausgewertet: alle drei Kennzahlen rückläufig (RLB −11,8 %, ELB −10,1 %, NEF
  −16,0 %), aber gegenläufiger Trend bei den nicht leistungsberechtigten
  Haushaltsmitgliedern (PERS − RLB): steigt von 286 auf 295 Personen, Anteil an PERS von
  5,2 % auf 6,0 % (siehe [`13_RLB_ELB_NEF.ipynb`](../Notebooks/13_RLB_ELB_NEF.ipynb))
- **Sozialversicherungspflichtige und geringfügig entlohnte Beschäftigung** (nach Arbeits-
  und Wohnort) — Gegenstück zur Arbeitslosigkeit, erstmals ausgewertet (⚠️ quartalsweise statt
  monatlich, 6 Monate Wartezeit, Zeitreihe daher Jun 2024 – Mär 2026): beide Beschäftigungsarten
  bemerkenswert stabil; auffälligster Befund ist der fast unveränderte Pendlersaldo von rund
  34.000 Personen (Auspendlerüberschuss) über alle 8 verfügbaren Quartale (siehe
  [`14_Beschaeftigung.ipynb`](../Notebooks/14_Beschaeftigung.ipynb))

Damit ist die priorisierte Themenliste aus diesem Dokument **vollständig abgearbeitet**.

## 🔲 In den Rohdaten vorhanden, aber noch nicht analysiert

Keine offenen Punkte mehr aus der ursprünglichen Priorisierung. Verbleibend nur noch
Erweiterungsideen ohne konkrete Priorisierung (siehe unten).

### Noch ungenutzte Tabellenblätter

Jede der 21 Dateien hat 21 Tabellenblätter, nicht nur "1.1 Eckwerte". Alle wurden mittlerweile
systematisch gesichtet — Abschnitt "1. Tabellenblätter der Rohdaten untersuchen" in
[`01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) gibt für jedes Blatt per Print-Ausgabe
eine Einschätzung (Daten + Diagramm-Ideen). Kurzfassung hier:

**⚠️ Wichtige Einschränkung:** Die Blätter **3.1–3.6** und **4.1–4.2** melden nicht den
Berichtsmonat des Dateinamens, sondern Daten mit **3 bzw. 6 Monaten Wartezeit** (z. B. meldet
die September-2026-Datei dort Stand "Juni 2026" bzw. "März 2026"). Beim Aufbau einer Zeitreihe
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
- **3.2 Personen in BG** — Aufschlüsselung nach Geschlecht plus Teilmenge ELB.

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

**Damit ist die ursprüngliche Priorisierungsliste vollständig abgearbeitet.** Auch die
beiden nachrangigen, nicht priorisierten Themen wurden inzwischen ergänzt: Bezugsdauer
(Langzeitleistungsbezug, Drehtür-Effekt, Haushaltsgrößenstruktur; Blätter 3.1, 3.4, 3.5,
siehe [`09_Bezugsdauer.ipynb`](../Notebooks/09_Bezugsdauer.ipynb)) und der Vergleich
"Insgesamt (SGB II+SGB III)" vs. "SGB II" (siehe
[`10_Rechtskreisvergleich.ipynb`](../Notebooks/10_Rechtskreisvergleich.ipynb)). Alle in
diesem Dokument gelisteten Auswertungswünsche sind damit abgedeckt — offen bleiben nur
noch die in "Noch ungenutzte Zeilen"/"Noch ungenutzte Tabellenblätter" gelisteten,
bislang nicht nachgefragten Erweiterungsideen.

## 📊 Dashboard

Ist bereits gebaut und deployed: **Streamlit**, mit Kopfzeilen-Tabs (`st.tabs()`) als
Navigation. [Live-Dashboard](https://daelwve9mj8pxz32vshq7u.streamlit.app/),
Details: [`Dashboard/README.md`](../Dashboard/README.md).

- Tab **"SGB II Übersicht"** enthält alle bisher fertigen Charts (entspricht inhaltlich
  `02_Analyse_SGBII.ipynb`, plus Trichter-Grafik und formatierte Kennzahlen-Tabelle)
- Tab **"SGB II vs. SGB III"** ist fertig (entspricht `10_Rechtskreisvergleich.ipynb`):
  Jobcenter-Anteil an Arbeitslosen-Bestand, Langzeitarbeitslosen und Quoten — nutzt die
  volle 21-Monats-Zeitreihe (Jan 2025 – Sep 2026), reagiert auf den Sidebar-Zeitraum-Filter
- Tab **"Fluktuation"** ist fertig (entspricht `04_Fluktuation.ipynb`): Zugang/Abgang im
  Monatsverlauf, Netto-Fluktuation vs. Bestandsänderung, 12-Monatssummen
- Tab **"Demografie"** ist fertig (entspricht `05_Demografie.ipynb`): Altersstruktur und
  Geschlecht als Zeitreihe, plus Ausländer und Schwerbehinderte als Zeitreihe
- Tab **"Erwerbstätigkeit"** ist fertig (entspricht `06_Erwerbstaetigkeit.ipynb`):
  Aufstockerquote, abhängig vs. selbständig, Einkommensstruktur — mit eigenem
  Zeitfenster (Okt 2024 – Jun 2026), unabhängig vom Sidebar-Zeitraum-Filter
- Tab **"Finanzen"** ist fertig (entspricht `07_Finanzen.ipynb`): Gesamtvolumen der
  Zahlungsansprüche + Ø je BG, Struktur nach Regelbedarf/KdU/Sozialversicherung — ebenfalls
  mit eigenem Zeitfenster (Okt 2024 – Jun 2026)
- Tab **"Förderung"** ist fertig (entspricht `08_Foerderung.ipynb`): Eintritte + Bestand an
  Fördermaßnahmen, Aktivierungsquote AQ1/AQ2a, Struktur nach Geschlecht/LZA-Vorgeschichte —
  ebenfalls mit eigenem Zeitfenster (Okt 2024 – Jun 2026)
- Tab **"Bezugsdauer"** ist fertig (entspricht `09_Bezugsdauer.ipynb`): BG-Struktur nach
  Größe/Typ, LZB vs. LZA, Drehtür-Effekt — ebenfalls mit eigenem Zeitfenster (Okt 2024 –
  Jun 2026)
- Tab **"Glossar"** erklärt alle im Dashboard verwendeten Fachbegriffe (Grundbegriffe,
  Personengruppen wie ELB/RLB/NEF, Kennzahlen, Aufstocker-Einkommen, Zahlungsansprüche,
  Datenbesonderheiten wie die Wartezeit-Problematik) — gruppiert in aufklappbaren
  Abschnitten
- Zeitraum-Filter (Slider) und Berichtsmonat-Auswahl in der Sidebar, wirken auf alle
  Zeitreihen-Charts bzw. Momentaufnahmen mit gemeinsamem Zeitfenster (nicht auf die Tabs
  Erwerbstätigkeit, Finanzen, Förderung, Bezugsdauer und Beschäftigung, siehe oben)
- Datenbasis: die aufbereiteten CSVs aus `Data/processed/`
  (`eckwerte_long.csv`, `kennzahlen_sgb2.csv`, `fluktuation_sgb2.csv`,
  `demografie_sgb2.csv`, `erwerbstaetigkeit_sgb2.csv`, `finanzen_sgb2.csv`,
  `foerderung_sgb2.csv`, `bezugsdauer_sgb2.csv`, `rechtskreisvergleich_sgb2.csv`) — kein
  erneutes Excel-Parsing nötig
- Alle Charts interaktiv (Plotly, `hovermode="x unified"`)

**Alle acht inhaltlichen Tabs sind jetzt vollständig befüllt** — nur der Tab "Glossar" ist
naturgemäß kein Chart-Tab. Damit ist die Themenliste aus diesem Dokument vollständig im
Dashboard umgesetzt.
