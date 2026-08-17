# Dashboard: Arbeitsmarkt Regensburg (SGB II)

Interaktives Streamlit-Dashboard zu den analysierten Kennzahlen aus
[`Notebooks/01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
[`Notebooks/02_Analyse_SGBII.ipynb`](../Notebooks/02_Analyse_SGBII.ipynb).

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://daelwve9mj8pxz32vshq7u.streamlit.app/)

**[Live-Dashboard](https://daelwve9mj8pxz32vshq7u.streamlit.app/)**

## Voraussetzung

`Data/processed/eckwerte_long.csv` und `Data/processed/kennzahlen_sgb2.csv` müssen vorhanden
sein. Falls nicht: einmal `Notebooks/01_Exploration.ipynb` komplett ausführen.

## Starten

```
pip install -r Dashboard/requirements.txt
streamlit run Dashboard/app.py
```

## Navigation

Das Dashboard hat sieben Tabs als Kopfzeilen-Navigation (`st.tabs()`):

| Tab | Inhalt | Status |
|---|---|---|
| 📊 SGB II Übersicht | Alle aktuell fertigen Charts (siehe unten) | ✅ fertig |
| 🔄 Fluktuation | Zugang & Abgang aus Arbeitslosigkeit | 🚧 Platzhalter, Priorität 1 |
| 👥 Demografie | Alter/Geschlecht als Zeitreihe, Schwerbehinderte, Ausländer | 🚧 Platzhalter, Priorität 2 |
| 💼 Erwerbstätigkeit | "Aufstocker" (erwerbstätige ELB) | 🚧 Platzhalter, Priorität 3 |
| ⏳ Bezugsdauer | Langzeitleistungsbezug, Drehtür-Effekt, Haushaltsgröße | 🚧 Platzhalter, nachrangig |
| 💶 Finanzen | Zahlungsansprüche in Euro | 🚧 Platzhalter, Priorität 4 |
| 🎯 Förderung | Aktive Arbeitsmarktpolitik, Aktivierungsquote | 🚧 Platzhalter, Priorität 5 |

Jeder Platzhalter-Tab zeigt einheitlich: Kurzbeschreibung des Themas, konkrete Rohdaten-Quelle
(Tabellenblatt), geplante Diagramm-Ideen und ggf. den Hinweis auf die 3–6 Monate Wartezeit bei
den Blättern 3.1–4.2. Priorisierung und Details: [`MD/ArbeitslosenAnalyse.md`](../MD/ArbeitslosenAnalyse.md).

## Inhalt Tab "SGB II Übersicht"

- Sidebar-Filter: Zeitraum-Slider (wirkt auf alle Zeitreihen-Charts) und Berichtsmonat-Auswahl
  (wirkt auf Kennzahlen-Kacheln, Trichter-Grafik und Altersstruktur)
- Kennzahlen-Kacheln für den gewählten Berichtsmonat inkl. Veränderung zum Vormonat, mit
  Hinweis, wenn die gerundete Arbeitslosenquote sich nicht ändert, obwohl der Bestand es tut
- **Übersicht:** kombinierter Chart aller vier Kernkennzahlen (Fläche "Personen in BG" im
  Hintergrund, überlappende Balken für Bedarfsgemeinschaften, Arbeitslose, Langzeitarbeitslose)
  mit Hover-Tooltip für alle Werte gleichzeitig
- Arbeitslosen- vs. Unterbeschäftigungsquote (mit Erklärung der Bezugsgröße)
- Langzeitarbeitslose: Anteil am Arbeitslosenbestand
- Kennzahlen im Vergleich (indexiert auf den ersten Monat im gewählten Zeitraum = 100 %,
  mit Lese-Erklärung)
- Trichter-Grafik: vom Haushalt (Personen in BG) zur gemeldeten Arbeitslosigkeit
  (RLB → ELB → Arbeitslose), gerundete Werte
- Alters- und Geschlechterstruktur für den gewählten Berichtsmonat
- Aufklappbare, formatierte Kennzahlen-Tabelle: Monat statt Roh-Timestamp, ganzzahlige Werte
  außer bei Prozent-Spalten, zweizeilige Header mit korrekter Silbentrennung, scrollbarer
  Container mit sticky Header

Alle Charts sind interaktives Plotly mit `hovermode="x unified"` (eine gemeinsame Tooltip-Box
pro Monat statt Werte einzeln pro Linie).

## Offene Erweiterungen

Die sechs Platzhalter-Tabs oben decken bereits die geplanten Themen ab. Volle inhaltliche
Übersicht (was ist analysiert, was noch offen, mit Priorisierung):
[`MD/ArbeitslosenAnalyse.md`](../MD/ArbeitslosenAnalyse.md).
