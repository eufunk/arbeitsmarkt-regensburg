# Arbeitsmarkt Regensburg

Analyse öffentlich zugänglicher Arbeitsmarktdaten für Regensburg mit Python — Fokus auf die
monatlichen "Eckwerte für Jobcenter"-Berichte der Bundesagentur für Arbeit (Rechtskreis SGB II,
Statistik-Nr. t73906-0).

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://daelwve9mj8pxz32vshq7u.streamlit.app/)

**[Live-Dashboard](https://daelwve9mj8pxz32vshq7u.streamlit.app/)**

## Datengrundlage

21 monatliche Excel-Berichte (Januar 2025 – September 2026) für das Jobcenter Regensburg, jeweils mit
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
  03_Statistik.ipynb        Deskriptive Statistik, Korrelation, Hypothesentest, Regression, Prognose vs. Ist
  04_Fluktuation.ipynb      Zugang/Abgang, Netto-Fluktuation, 12-Monatssummen
  05_Demografie.ipynb       Altersstruktur, Geschlecht, Ausländer, Schwerbehinderte (Zeitreihe)
  06_Erwerbstaetigkeit.ipynb Aufstockerquote, Erwerbsform, Einkommensstruktur
  07_Finanzen.ipynb          Zahlungsansprüche in Euro, Ø je Bedarfsgemeinschaft, Struktur
  08_Foerderung.ipynb        Eintritte/Bestand an Fördermaßnahmen, Aktivierungsquote
  09_Bezugsdauer.ipynb       BG-Struktur, Langzeitleistungsbezug, Drehtür-Effekt
  10_Rechtskreisvergleich.ipynb  Jobcenter-Anteil an der Arbeitslosigkeit (SGB II vs. SGB III)
  11_Arbeitsstellen.ipynb   Gemeldete Arbeitsstellen (Nachfrageseite), Angebot-Nachfrage-Relation
  12_Unterbeschaeftigung.ipynb  Unterbeschäftigung im engeren Sinne/ohne Kurzarbeit, SGB-II-Anteil
  13_RLB_ELB_NEF.ipynb      RLB/ELB/NEF-Struktur der Bedarfsgemeinschaften als Zeitreihe
  14_Beschaeftigung.ipynb   Sozialversicherungspflichtige/geringfügige Beschäftigung, Pendlersaldo
Dashboard/
  app.py                    interaktives Streamlit-Dashboard
Docs/
  Abbildungen/              PNG-Abbildungen (abb1–abb44), von den Notebooks exportiert
  Projektdokumentation.docx projektbegleitende Dokumentation (Word)
  Projektpraesentation.pptx Projektpräsentation (PowerPoint)
Plan/
  Aktualisierung_Jul-Sep_2026.md  Plan und Protokoll der Datenerweiterung um Jul–Sep 2026
MD/
  ArbeitslosenAnalyse.md    inhaltliche Themenübersicht (behandelt / offen)
  ThemenCheck.md             Abgleich gegen den Lernplan (DatenanalysePython.md)
  01_Exploration.md          Dokumentation zu 01_Exploration.ipynb
  02_Analyse_SGBII.md        Dokumentation zu 02_Analyse_SGBII.ipynb
  03_Statistik.md            Dokumentation zu 03_Statistik.ipynb
  04_Fluktuation.md          Dokumentation zu 04_Fluktuation.ipynb
  05_Demografie.md           Dokumentation zu 05_Demografie.ipynb
  06_Erwerbstaetigkeit.md    Dokumentation zu 06_Erwerbstaetigkeit.ipynb
  07_Finanzen.md             Dokumentation zu 07_Finanzen.ipynb
  08_Foerderung.md           Dokumentation zu 08_Foerderung.ipynb
  09_Bezugsdauer.md          Dokumentation zu 09_Bezugsdauer.ipynb
  10_Rechtskreisvergleich.md Dokumentation zu 10_Rechtskreisvergleich.ipynb
  11_Arbeitsstellen.md      Dokumentation zu 11_Arbeitsstellen.ipynb
  12_Unterbeschaeftigung.md Dokumentation zu 12_Unterbeschaeftigung.ipynb
  13_RLB_ELB_NEF.md         Dokumentation zu 13_RLB_ELB_NEF.ipynb
  14_Beschaeftigung.md      Dokumentation zu 14_Beschaeftigung.ipynb
```

## Lokal ausführen

1. `Notebooks/01_Exploration.ipynb` einmal komplett ausführen (erzeugt `Data/processed/*.csv`
   aus den Rohdaten).
2. `Notebooks/02_Analyse_SGBII.ipynb` für Visualisierung und Auswertung.
3. `Notebooks/03_Statistik.ipynb` für vertiefte statistische Verfahren (Korrelation,
   Hypothesentest, Regression, Abgleich der Prognose mit den Istwerten).
4. `Notebooks/04_Fluktuation.ipynb` für Zugang/Abgang aus Arbeitslosigkeit (Fluktuation).
5. `Notebooks/05_Demografie.ipynb` für Altersstruktur, Geschlecht, Ausländer und
   Schwerbehinderte als Zeitreihe.
6. `Notebooks/06_Erwerbstaetigkeit.ipynb` für Aufstockerquote und Einkommensstruktur (liest
   direkt aus den Excel-Rohdaten, Blatt „3.3 Erwerbstätigkeit“).
7. `Notebooks/07_Finanzen.ipynb` für Zahlungsansprüche in Euro (liest direkt aus den
   Excel-Rohdaten, Blatt „3.6 Zahlungsansprüche“).
8. `Notebooks/08_Foerderung.ipynb` für Eintritte/Bestand an Fördermaßnahmen und
   Aktivierungsquote (liest direkt aus den Excel-Rohdaten, Blätter „4.1 Förderung“ und
   „4.2 Förderung Strukturen“).
9. `Notebooks/09_Bezugsdauer.ipynb` für Haushaltsstruktur, Langzeitleistungsbezug und
   Drehtür-Effekt (liest direkt aus den Excel-Rohdaten, Blätter „3.1 Bedarfsgemeinschaften“,
   „3.4 Langzeitleistungsbezug“, „3.5 Bewegungen Personen“).
10. `Notebooks/10_Rechtskreisvergleich.ipynb` für den Jobcenter-Anteil an der
    Arbeitslosigkeit (SGB II vs. SGB III) — liest nur `Data/processed/eckwerte_long.csv`,
    keine neuen Rohdaten nötig.
11. `Notebooks/11_Arbeitsstellen.ipynb` für gemeldete Arbeitsstellen (Nachfrageseite) und die
    Angebot-Nachfrage-Relation — liest direkt aus den Excel-Rohdaten, Blatt „1.1 Eckwerte“.
12. `Notebooks/12_Unterbeschaeftigung.ipynb` für Unterbeschäftigung im engeren Sinne/ohne
    Kurzarbeit und den SGB-II-Anteil im Vergleich — liest nur `Data/processed/eckwerte_long.csv`,
    keine neuen Rohdaten nötig.
13. `Notebooks/13_RLB_ELB_NEF.ipynb` für die RLB/ELB/NEF-Struktur der Bedarfsgemeinschaften
    als Zeitreihe — liest nur `Data/processed/eckwerte_long.csv`, keine neuen Rohdaten nötig.
14. `Notebooks/14_Beschaeftigung.ipynb` für sozialversicherungspflichtige/geringfügige
    Beschäftigung und den Pendlersaldo — liest direkt aus den Excel-Rohdaten, Blatt
    „1.1 Eckwerte“ (quartalsweiser Block, Zeilen 49–58).
15. Dashboard starten:
   ```
   pip install -r Dashboard/requirements.txt
   streamlit run Dashboard/app.py
   ```

Die Notebooks 02–14 schreiben ihre Abbildungen beim Ausführen nach `Docs/Abbildungen/`
(Plotly-Bildexport, benötigt das Paket `kaleido`).

Details zum Dashboard: [`Dashboard/README.md`](Dashboard/README.md).
