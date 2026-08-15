# Arbeitsmarkt Regensburg

Analyse öffentlich zugänglicher Arbeitsmarktdaten für Regensburg mit Python — Fokus auf die
monatlichen "Eckwerte für Jobcenter"-Berichte der Bundesagentur für Arbeit (Rechtskreis SGB II,
Statistik-Nr. t73906-0).

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://daelwve9mj8pxz32vshq7u.streamlit.app/)

**[Live-Dashboard](https://daelwve9mj8pxz32vshq7u.streamlit.app/)**

## Datengrundlage

15 monatliche Excel-Berichte (April 2025 – Juni 2026) für das Jobcenter Regensburg, jeweils mit
dem aktuellen Monatswert je Merkmal, getrennt nach *"Insgesamt (SGB II und SGB III)"* und
*"Rechtskreis SGB II"* (= Jobcenter-Zuständigkeit). Die Rohdaten liegen lokal unter
`Data/RegensburgJCData/` und sind nicht Teil des Repositories (siehe `.gitignore`).

## Projektstruktur

```
Data/
  RegensburgJCData/     Rohdaten (.xlsx, nicht versioniert)
  processed/             aufbereitete CSVs, versioniert fürs Dashboard-Deployment
Notebooks/
  01_Exploration.ipynb      Einlesen, Bereinigen, Aufbereiten, Export nach Data/processed/
  02_Analyse_SGBII.ipynb    Visualisierung und inhaltliche Auswertung (Rechtskreis SGB II)
Dashboard/
  app.py                    interaktives Streamlit-Dashboard
MD/
  ArbeitslosenAnalyse.md    inhaltliche Themenübersicht (behandelt / offen)
  ThemenCheck.md             Abgleich gegen den Lernplan (DatenanalysePython.md)
  01_Exploration.md          Dokumentation zu 01_Exploration.ipynb
  02_Analyse_SGBII.md        Dokumentation zu 02_Analyse_SGBII.ipynb
```

## Lokal ausführen

1. `Notebooks/01_Exploration.ipynb` einmal komplett ausführen (erzeugt `Data/processed/*.csv`
   aus den Rohdaten).
2. `Notebooks/02_Analyse_SGBII.ipynb` für Visualisierung und Auswertung.
3. Dashboard starten:
   ```
   pip install -r Dashboard/requirements.txt
   streamlit run Dashboard/app.py
   ```

Details zum Dashboard: [`Dashboard/README.md`](Dashboard/README.md).
