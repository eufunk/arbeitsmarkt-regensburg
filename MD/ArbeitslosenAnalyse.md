# Arbeitslosenanalyse Regensburg — Inhaltliche Themenübersicht

Überblick, welche Aspekte der Arbeitslosigkeit im Jobcenter Regensburg (Rechtskreis SGB II,
April 2025 – Juni 2026) wir aus den Rohdaten bereits ausgewertet haben, und was in den
Rohdaten noch steckt, aber bislang nicht analysiert wurde.

Rohdaten: `Data/RegensburgJCData/*.xlsx` (15 Monatsberichte "Eckwerte für Jobcenter").
Bisher genutzt wurde ausschließlich das Tabellenblatt **"1.1 Eckwerte"**, dort nur der Ausschnitt
Spalte B (Insgesamt SGB II+SGB III) und Spalte G (Rechtskreis SGB II) je Berichtsmonat.

## ✅ Bereits analysiert

- **Bestand der Arbeitslosen** (SGB II) über die Zeit — leicht gestiegen (1.457 → 1.500),
  Spanne 1.438–1.587
- **Arbeitslosenquote** über die Zeit — stabil zwischen 1,2 % und 1,4 %
- **Langzeitarbeitslosigkeit** — absolute Zahl und Anteil am Bestand; deutlichster Trend
  (526 → 709 Personen, Anteil 36 % → 47 %)
- **Unterbeschäftigungsquote** im Vergleich zur Arbeitslosenquote
- **Bedarfsgemeinschaften** und **Personen im Leistungsbezug** über die Zeit — beide
  rückläufig (je ca. −5 %)
- **Altersstruktur** der Arbeitslosen (15–25 / 25–50 / 50+) — nur letzter Berichtsmonat,
  keine Zeitreihe
- **Geschlechterverteilung** (Männer/Frauen) — nur letzter Berichtsmonat, keine Zeitreihe
- **Veränderung zum Vormonat / Vorjahresmonat** für die vier Kernkennzahlen (Bestand,
  Langzeitarbeitslose, Bedarfsgemeinschaften, Personen in BG)

## 🔲 In den Rohdaten vorhanden, aber noch nicht analysiert

### Noch ungenutzte Zeilen in "1.1 Eckwerte" (gleiches Blatt, das wir schon nutzen)
- **Zugang und Abgang** aus Arbeitslosigkeit (im Monat und als 12-Monatssumme) — bisher nur
  der *Bestand* betrachtet, nicht die Dynamik/Fluktuation
- **Altersstruktur und Geschlecht als Zeitreihe** statt nur Momentaufnahme des letzten Monats
  (55+ separat, nicht nur 50+)
- **Schwerbehinderte Menschen** unter den Arbeitslosen
- **Ausländische Arbeitslose**
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

Jede der 15 Dateien hat 21 Tabellenblätter, nicht nur "1.1 Eckwerte". Alle wurden mittlerweile
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
- **3.3 Erwerbstätigkeit** — "Aufstocker" (erwerbstätige ELB), aufgeschlüsselt nach
  abhängig/selbstständig und Einkommenshöhe (Geringfügigkeit vs. Übergangsbereich). Komplett
  neues Themenfeld, direkt anschlussfähig an die Trichter-Grafik im Dashboard (zusätzliche
  Stufe "davon in Arbeit, aber bedürftig").
- **3.4 Langzeitleistungsbezug** — neue Kennzahl **Langzeitleistungsbeziehende (LZB)**: mind.
  21 von 24 Monaten im Bezug — nicht identisch mit Langzeitarbeitslosen, da Bürgergeld auch
  ohne Arbeitslosigkeit bezogen werden kann. Idee: LZB vs. LZA im Vergleich.
- **3.5 Bewegungen Personen** — Zu-/Abgänge im Regelleistungsbezug (ELB-Ebene) inkl.
  Vorbezugs-Historie (Hinweis auf "Drehtür-Effekt": erneuter Bezug innerhalb 12 Monaten).
- **3.6 Zahlungsansprüche** — einzige Quelle für **Euro-Beträge**: Summe der Zahlungsansprüche,
  Ø Anspruch je BG, aufgeschlüsselt nach Regelbedarf ELB/NEF. Bisher komplett unberührtes
  Themenfeld (Kostenvolumen).
- **4.1 Förderung** — Eintritte in arbeitsmarktpolitische Maßnahmen nach Instrumenten-Kategorie.
- **4.2 Förderung Strukturen** — Bestand an Maßnahmenteilnehmenden nach Geschlecht, Alter,
  LZA-Status, Schwerbehinderung; enthält die fertige Kennzahl **Aktivierungsquote (AQ1/AQ2a)**.

Nicht nutzbar (reine Metadaten/Links, keine Zahlen): Deckblatt, Impressum, Inhaltsverzeichnis
(nützlich nur als Zeichenerklärung-Nachschlagewerk), Grafik (nur eingebettete Bilder), Linkliste,
Statistik-Infoseite.

## Priorisierungsvorschlag für die Fortsetzung

1. Zugang/Abgang (Fluktuation) ergänzen — direkt in "1.1 Eckwerte" verfügbar, kleiner Aufwand,
   keine Wartezeit-Problematik
2. Altersstruktur/Geschlecht als Zeitreihe statt Momentaufnahme
3. Erwerbstätigkeit/Aufstocker (3.3) — inhaltlich relevanter neuer Aspekt (⚠️ 3 Monate Wartezeit)
4. Zahlungsansprüche (3.6) — einziger Zugang zu Euro-Beträgen, bisher komplett unbeleuchtet
   (⚠️ 3 Monate Wartezeit)
5. Förderung (4.1/4.2) — falls Fokus auf aktive Arbeitsmarktpolitik gewünscht ist
   (⚠️ 3 Monate Wartezeit)

## 📊 Dashboard

Ist bereits gebaut und deployed: **Streamlit**, mit Kopfzeilen-Tabs (`st.tabs()`) als
Navigation. [Live-Dashboard](https://daelwve9mj8pxz32vshq7u.streamlit.app/),
Details: [`Dashboard/README.md`](../Dashboard/README.md).

- Tab **"SGB II Übersicht"** enthält alle bisher fertigen Charts (entspricht inhaltlich
  `02_Analyse_SGBII.ipynb`, plus Trichter-Grafik und formatierte Kennzahlen-Tabelle)
- Sechs weitere Tabs sind als Platzhalter für genau die oben gelistete Priorisierung
  vorbereitet (Fluktuation, Demografie, Erwerbstätigkeit, Bezugsdauer, Finanzen, Förderung) —
  jeder zeigt bereits Datenquelle, geplante Diagramme und Priorität, nur die eigentlichen
  Charts fehlen noch
- Zeitraum-Filter (Slider) und Berichtsmonat-Auswahl in der Sidebar, wirken auf alle
  Zeitreihen-Charts bzw. Momentaufnahmen
- Datenbasis: die aufbereiteten CSVs aus `Data/processed/`
  (`eckwerte_long.csv`, `kennzahlen_sgb2.csv`) — kein erneutes Excel-Parsing nötig
- Alle Charts interaktiv (Plotly, `hovermode="x unified"`)

Nächster Schritt: die sechs Platzhalter-Tabs nacheinander mit echten Charts befüllen, in der
oben genannten Prioritätsreihenfolge.
