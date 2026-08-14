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

### Noch ungenutzte Tabellenblätter (in jeder der 15 Dateien vorhanden)
- **1.2 Eckwerte Zeitreihe** — Zeitreihe direkt im Bericht, evtl. als Cross-Check oder für
  längere Historie nutzbar
- **2.1 Arbeitslosigkeit Zugang** / **2.2 Bestand** / **2.3 Abgang** — vermutlich feinere
  Aufschlüsselung (z. B. nach Herkunft des Zugangs, Verbleib nach Abgang)
- **2.4 Langzeitarbeitslosigkeit** — Detailtabelle über das hinaus, was wir aus "1.1" ziehen
- **2.5 Unterbeschäftigung** — Detailtabelle
- **3.1 Bedarfsgemeinschaften** / **3.2 Personen in BG** — vermutlich Aufschlüsselung nach
  BG-Typ (Singles, Alleinerziehende, Paare mit/ohne Kinder)
- **3.3 Erwerbstätigkeit** — erwerbstätige Leistungsberechtigte ("Aufstocker": Menschen, die
  trotz Arbeit ergänzend SGB-II-Leistungen beziehen) — komplett neues Themenfeld
- **3.4 Langzeitleistungsbezug** — wie lange bleiben Personen im SGB-II-Bezug?
- **3.5 Bewegungen Personen** — Zu- und Abgänge im Leistungsbezug
- **3.6 Zahlungsansprüche** — finanzielle Kennzahlen (Euro-Beträge), bisher nicht betrachtet
- **4.1 Förderung** / **4.2 Förderung Strukturen** — aktive Arbeitsmarktpolitik,
  Eingliederungsleistungen, Maßnahmen — komplett neues Themenfeld, keine Berührung bisher

## Priorisierungsvorschlag für die Fortsetzung

1. Zugang/Abgang (Fluktuation) ergänzen — direkt in "1.1 Eckwerte" verfügbar, kleiner Aufwand
2. Altersstruktur/Geschlecht als Zeitreihe statt Momentaufnahme
3. Erwerbstätigkeit/Aufstocker (3.3) — inhaltlich relevanter neuer Aspekt
4. Förderung (4.1/4.2) — falls Fokus auf aktive Arbeitsmarktpolitik gewünscht ist

## 📊 Geplant: Dashboard

Sobald der inhaltliche Umfang steht, soll ein interaktives Dashboard entstehen (Streamlit,
Dash oder Flask). Grobe Idee:

- Zeitreihen-Charts mit Zeitraum-Filter für alle erschlossenen Kennzahlen
- Kennzahlen-Kacheln für den aktuellsten Berichtsmonat inkl. Veränderung zum Vormonat/Vorjahr
- Altersstruktur- und Geschlechterverteilung als interaktive Diagramme (sobald als Zeitreihe
  verfügbar, auch im Zeitverlauf filterbar)
- Datenbasis: die aufbereiteten CSVs aus `Data/processed/`
  (`eckwerte_long.csv`, `kennzahlen_sgb2.csv`) — kein erneutes Excel-Parsing nötig

Technologieentscheidung (Streamlit vs. Dash vs. Flask) steht noch aus.
