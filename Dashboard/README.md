# Dashboard: Arbeitsmarkt Regensburg (SGB II)

Interaktives Streamlit-Dashboard zu den bisher analysierten Kennzahlen aus
[`Notebooks/01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
[`Notebooks/02_Analyse.ipynb`](../Notebooks/02_Analyse.ipynb).

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

## Inhalt

- Zeitraum-Filter (Slider) für alle Zeitreihen-Charts, Berichtsmonat-Filter für Kennzahlen-Kacheln
  und Altersstruktur
- Kennzahlen-Kacheln für den gewählten Berichtsmonat inkl. Veränderung zum Vormonat
- **Übersicht:** kombinierter Chart aller vier Kernkennzahlen (Fläche "Personen in BG" im
  Hintergrund, überlappende Balken für Bedarfsgemeinschaften, Arbeitslose, Langzeitarbeitslose)
  mit Hover-Tooltip für alle Werte gleichzeitig
- Arbeitslosen- vs. Unterbeschäftigungsquote
- Langzeitarbeitslose: Anteil am Arbeitslosenbestand
- Kennzahlen im Vergleich (indexiert auf den ersten Monat = 100)
- Trichter-Grafik: vom Haushalt (Personen in BG) zur gemeldeten Arbeitslosigkeit
  (RLB → ELB → Arbeitslose)
- Alters- und Geschlechterstruktur für den gewählten Berichtsmonat
- Aufklappbare Kennzahlen-Tabelle

## Offene Erweiterungen

Siehe [`MD/ArbeitslosenAnalyse.md`](../MD/ArbeitslosenAnalyse.md) für inhaltliche Themen, die
noch nicht ins Dashboard eingeflossen sind (z. B. Zugang/Abgang, Erwerbstätigkeit/Aufstocker,
Förderung).
