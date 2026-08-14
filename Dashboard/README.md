# Dashboard: Arbeitsmarkt Regensburg (SGB II)

Interaktives Streamlit-Dashboard zu den bisher analysierten Kennzahlen aus
[`Notebooks/01_Exploration.ipynb`](../Notebooks/01_Exploration.ipynb) /
[`Notebooks/02_Analyse.ipynb`](../Notebooks/02_Analyse.ipynb).

## Voraussetzung

`Data/processed/eckwerte_long.csv` und `Data/processed/kennzahlen_sgb2.csv` müssen vorhanden
sein. Falls nicht: einmal `Notebooks/01_Exploration.ipynb` komplett ausführen.

## Starten

```
pip install -r Dashboard/requirements.txt
streamlit run Dashboard/app.py
```

## Inhalt

- Zeitraum-Filter (Slider) für alle Zeitreihen-Charts
- Kennzahlen-Kacheln für den letzten Monat im gewählten Zeitraum inkl. Veränderung zum Vormonat
- Zeitreihen: Arbeitslose (Bestand), Arbeitslosen- vs. Unterbeschäftigungsquote,
  Langzeitarbeitslose (absolut + Anteil), Bedarfsgemeinschaften & Personen in BG
- Alters- und Geschlechterstruktur für einen frei wählbaren Berichtsmonat
- Aufklappbare Kennzahlen-Tabelle

## Offene Erweiterungen

Siehe [`MD/ArbeitslosenAnalyse.md`](../MD/ArbeitslosenAnalyse.md) für inhaltliche Themen, die
noch nicht ins Dashboard eingeflossen sind (z. B. Zugang/Abgang, Erwerbstätigkeit/Aufstocker,
Förderung).
