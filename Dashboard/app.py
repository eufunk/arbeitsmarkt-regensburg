"""Streamlit-Dashboard: Arbeitsmarkt Regensburg (Jobcenter, SGB II).

Baut auf den in Notebooks/01_Exploration.ipynb aufbereiteten CSVs auf
(Data/processed/eckwerte_long.csv, Data/processed/kennzahlen_sgb2.csv).
Starten mit: streamlit run Dashboard/app.py
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

PROCESSED_DIR = Path(__file__).resolve().parent.parent / "Data" / "processed"

st.set_page_config(page_title="Arbeitsmarkt Regensburg (SGB II)", layout="wide")


@st.cache_data
def load_data():
    long_path = PROCESSED_DIR / "eckwerte_long.csv"
    wide_path = PROCESSED_DIR / "kennzahlen_sgb2.csv"

    if not long_path.exists() or not wide_path.exists():
        return None, None

    df_long = pd.read_csv(long_path)
    df_long["period"] = pd.PeriodIndex(df_long["period"], freq="M").to_timestamp()

    kennzahlen = pd.read_csv(wide_path, index_col="period", parse_dates=["period"])
    kennzahlen = kennzahlen.sort_index()
    return df_long, kennzahlen


df_long, kennzahlen = load_data()

if kennzahlen is None:
    st.error(
        "Keine aufbereiteten Daten gefunden. Bitte zuerst "
        "`Notebooks/01_Exploration.ipynb` einmal komplett ausführen, "
        "damit `Data/processed/*.csv` entsteht."
    )
    with st.expander("Diagnose"):
        st.write("Gesucht in:", str(PROCESSED_DIR))
        st.write("Verzeichnis existiert:", PROCESSED_DIR.exists())
        if PROCESSED_DIR.exists():
            st.write("Inhalt:", [p.name for p in PROCESSED_DIR.iterdir()])
        data_dir = PROCESSED_DIR.parent
        st.write("Data/-Verzeichnis existiert:", data_dir.exists())
        if data_dir.exists():
            st.write("Inhalt von Data/:", [p.name for p in data_dir.iterdir()])
    st.stop()

st.title("Arbeitsmarkt Regensburg — Jobcenter (SGB II)")
st.caption(
    "Datenquelle: Statistik der Bundesagentur für Arbeit, Bericht "
    "\"Eckwerte für Jobcenter\", Jobcenter Regensburg (Statistik-Nr. t73906-0)."
)

with st.expander("Was ist SGB II?"):
    st.markdown(
        "**SGB II** (Zweites Buch Sozialgesetzbuch) regelt die *Grundsicherung für "
        "Arbeitsuchende* (umgangssprachlich „Bürgergeld\", vormals „Hartz IV\") und wird "
        "von den **Jobcentern** verwaltet — daher der Fokus dieses Dashboards auf den "
        "„Rechtskreis SGB II\". Abzugrenzen ist das vom **SGB III** (Arbeitslosenversicherung), "
        "für das die Agentur für Arbeit zuständig ist und das Menschen mit Anspruch auf "
        "Arbeitslosengeld I betrifft. Alle Kennzahlen hier beziehen sich ausschließlich auf SGB II."
    )

# --- Sidebar: Filter -----------------------------------------------------------
min_month = kennzahlen.index.min().to_pydatetime()
max_month = kennzahlen.index.max().to_pydatetime()

st.sidebar.header("Filter")
date_range = st.sidebar.slider(
    "Zeitraum (Zeitreihen-Charts)",
    min_value=min_month,
    max_value=max_month,
    value=(min_month, max_month),
    format="MMM YYYY",
)

mask = (kennzahlen.index >= date_range[0]) & (kennzahlen.index <= date_range[1])
view = kennzahlen.loc[mask]

if view.empty:
    st.warning("Kein Berichtsmonat im gewählten Zeitraum.")
    st.stop()

gewaehlter_monat = st.sidebar.selectbox(
    "Berichtsmonat (Kennzahlen & Struktur)",
    options=list(kennzahlen.index[::-1]),
    format_func=lambda d: pd.Timestamp(d).strftime("%b %Y"),
)

# --- Kennzahlen-Kacheln (gewählter Berichtsmonat) ------------------------------
monat_position = kennzahlen.index.get_loc(gewaehlter_monat)
letzter = kennzahlen.iloc[monat_position]
vorheriger = kennzahlen.iloc[monat_position - 1] if monat_position > 0 else None


def delta_value(spalte: str) -> float | None:
    if vorheriger is None:
        return None
    return letzter[spalte] - vorheriger[spalte]


def delta_str(spalte: str, decimals: int = 0) -> str | None:
    val = delta_value(spalte)
    return None if val is None else f"{val:+.{decimals}f}"


def geplant(beschreibung: str, datenquelle: str, ideen: list[str], prioritaet: str, wartezeit: bool = False) -> None:
    """Platzhalter-Inhalt für einen noch nicht umgesetzten Tab."""
    st.info(f"🚧 Noch nicht umgesetzt — {prioritaet}")
    st.markdown(beschreibung)
    st.markdown(f"**Datenquelle:** {datenquelle}")
    if wartezeit:
        st.caption(
            "⚠️ Diese Rohdaten melden nicht den aktuellen Berichtsmonat, sondern Stand mit "
            "3–6 Monaten Wartezeit (siehe Abschnitt 1 in `01_Exploration.ipynb`)."
        )
    st.markdown("**Geplante Diagramme:**")
    for idee in ideen:
        st.markdown(f"- {idee}")
    st.caption("Details: [`MD/ArbeitslosenAnalyse.md`](https://github.com/eufunk/arbeitsmarkt-regensburg/blob/main/MD/ArbeitslosenAnalyse.md)")


# --- Navigation: Menü-Tabs ------------------------------------------------------
tab_uebersicht, tab_fluktuation, tab_demografie, tab_erwerbstaetigkeit, tab_bezugsdauer, tab_finanzen, tab_foerderung = st.tabs(
    [
        "📊 SGB II Übersicht",
        "🔄 Fluktuation",
        "👥 Demografie",
        "💼 Erwerbstätigkeit",
        "⏳ Bezugsdauer",
        "💶 Finanzen",
        "🎯 Förderung",
    ]
)

# =================================================================================
# Tab 1: SGB II Übersicht (bisheriger Dashboard-Inhalt, entspricht 02_Analyse_SGBII)
# =================================================================================
with tab_uebersicht:
    st.subheader(f"Kennzahlen — {letzter.name:%B %Y}")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Arbeitslose (Bestand)", f"{letzter['Arbeitslose (Bestand)']:.0f}", delta_str("Arbeitslose (Bestand)"))
    c2.metric(
        "Arbeitslosenquote",
        f"{letzter['Arbeitslosenquote (%)']:.1f} %",
        delta_str("Arbeitslosenquote (%)", decimals=1),
        help=(
            "SGB-II-anteilige Quote: Bestand bezogen auf alle zivilen Erwerbspersonen "
            "Regensburgs, von der Bundesagentur auf eine Nachkommastelle gerundet. "
            "Kleine Bestandsänderungen schlagen sich dadurch oft nicht sichtbar nieder — "
            "siehe Kachel „Arbeitslose (Bestand)“ für die tatsächliche Bewegung."
        ),
    )
    c3.metric("Langzeitarbeitslose", f"{letzter['Langzeitarbeitslose']:.0f}", delta_str("Langzeitarbeitslose"))
    c4.metric("Bedarfsgemeinschaften", f"{letzter['Bedarfsgemeinschaften']:.0f}", delta_str("Bedarfsgemeinschaften"))
    c5.metric("Personen in BG", f"{letzter['Personen in BG']:.0f}", delta_str("Personen in BG"))

    quote_delta = delta_value("Arbeitslosenquote (%)")
    bestand_delta = delta_value("Arbeitslose (Bestand)")
    if quote_delta is not None and bestand_delta is not None and round(quote_delta, 1) == 0 and bestand_delta != 0:
        richtung = "gestiegen" if bestand_delta > 0 else "gesunken"
        st.caption(
            f"ℹ️ Die Arbeitslosenquote ist zum Vormonat unverändert (Rundung auf eine Nachkommastelle) — "
            f"der Bestand ist im selben Zeitraum um {bestand_delta:+.0f} Personen {richtung}."
        )

    st.divider()

    # --- Übersicht: Kennzahlen im Vergleich (kombinierter Chart) ---------------
    st.subheader("Übersicht: Kennzahlen im Vergleich")
    st.caption(
        "Bedarfsgemeinschaften-, Arbeitslosen- und Langzeitarbeitslosen-Balken überlappend vor der "
        "Fläche aller Personen in Bedarfsgemeinschaften im Hintergrund — die Fläche ist immer die "
        "größte Menge, die Balken werden von außen nach innen kleiner (BG → Arbeitslose → "
        "Langzeitarbeitslose). Maus über einen Monat bewegen zeigt alle vier Werte gleichzeitig als "
        "Tooltip an."
    )

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=view.index, y=view["Personen in BG"], name="Personen in BG (gesamt)",
        mode="lines+markers", fill="tozeroy",
        line=dict(color="#1d4ed8", width=1), fillcolor="rgba(147,197,253,0.3)", marker=dict(size=4),
    ))
    fig.add_trace(go.Bar(x=view.index, y=view["Bedarfsgemeinschaften"], marker_color="rgba(245,158,11,0.6)", hoverinfo="skip", showlegend=False))
    fig.add_trace(go.Scatter(
        x=view.index, y=view["Bedarfsgemeinschaften"], name="Bedarfsgemeinschaften",
        mode="lines+markers", line=dict(color="#b45309", width=1), marker=dict(size=4),
    ))
    fig.add_trace(go.Bar(x=view.index, y=view["Arbeitslose (Bestand)"], marker_color="#2563eb", hoverinfo="skip", showlegend=False))
    fig.add_trace(go.Scatter(
        x=view.index, y=view["Arbeitslose (Bestand)"], name="Arbeitslose (Bestand)",
        mode="lines+markers", line=dict(color="#1e3a8a", width=1), marker=dict(size=4),
    ))
    fig.add_trace(go.Bar(x=view.index, y=view["Langzeitarbeitslose"], marker_color="#7c3aed", hoverinfo="skip", showlegend=False))
    fig.add_trace(go.Scatter(
        x=view.index, y=view["Langzeitarbeitslose"], name="Langzeitarbeitslose",
        mode="lines+markers", line=dict(color="#4c1d95", width=1), marker=dict(size=4),
    ))
    fig.update_layout(
        title="Arbeitslose, Langzeitarbeitslose und Bedarfsgemeinschaften im Verhältnis zu allen Personen in BG, Jobcenter Regensburg",
        yaxis_title="Personen / Bedarfsgemeinschaften",
        xaxis_title="Monat",
        barmode="overlay",
        hovermode="x unified",
        height=500,
    )
    st.plotly_chart(fig, width="stretch")

    st.divider()

    # --- Weitere Zeitreihen-Charts ----------------------------------------------
    st.subheader("Arbeitslosen- und Unterbeschäftigungsquote")
    st.caption(
        "Anteilswerte, keine Rohzahlen: Beide Quoten setzen den SGB-II-Bestand ins Verhältnis zu "
        "**allen zivilen Erwerbspersonen** Regensburgs (Beschäftigte + Arbeitslose zusammen, "
        "nicht nur die SGB-II-Fälle)."
    )

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=view.index, y=view["Arbeitslosenquote (%)"], name="Arbeitslosenquote (SGB II-Anteil)",
        mode="lines+markers", line=dict(color="#2563eb"), marker=dict(symbol="circle", size=6),
    ))
    fig.add_trace(go.Scatter(
        x=view.index, y=view["Unterbeschäftigungsquote (%)"], name="Unterbeschäftigungsquote (SGB II-Anteil)",
        mode="lines+markers", line=dict(color="#dc2626"), marker=dict(symbol="square", size=6),
    ))
    fig.update_layout(
        title="Arbeitslosen- vs. Unterbeschäftigungsquote",
        yaxis_title="Anteil an den Erwerbspersonen (%)",
        yaxis_ticksuffix="%",
        xaxis_title="Monat",
        hovermode="x unified",
        legend=dict(orientation="h", y=1.1),
        height=420,
    )
    st.plotly_chart(fig, width="stretch")
    st.caption(
        "Die Unterbeschäftigungsquote nutzt eine etwas breitere Bezugsgröße, die zusätzlich "
        "unterbeschäftigte Personen (z. B. in arbeitsmarktpolitischen Maßnahmen) mit einschließt "
        "— deshalb liegt sie meist etwas über der Arbeitslosenquote, obwohl beide sich auf "
        "denselben Rechtskreis SGB II beziehen."
    )

    st.subheader("Langzeitarbeitslosigkeit")

    anteil = (view["Langzeitarbeitslose"] / view["Arbeitslose (Bestand)"] * 100).round(1)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=view.index, y=anteil, name="Anteil Langzeitarbeitslose",
        mode="lines+markers", line=dict(color="#7c3aed"), marker=dict(symbol="circle", size=6),
        hovertemplate="%{y}<extra></extra>",
    ))
    fig.update_layout(
        title="Anteil Langzeitarbeitslose an allen Arbeitslosen (SGB II)",
        yaxis_title="Prozent",
        yaxis_ticksuffix="%",
        xaxis_title="Monat",
        hovermode="x unified",
        showlegend=False,
        height=420,
    )
    st.plotly_chart(fig, width="stretch")
    st.caption(
        "Anteil der Langzeitarbeitslosen am gesamten Arbeitslosenbestand — ein steigender Anteil "
        "deutet darauf hin, dass sich Arbeitslosigkeit stärker verfestigt. Die absolute Entwicklung "
        "ist bereits in der Übersicht oben enthalten."
    )

    st.subheader("Kennzahlen im Vergleich (indexiert)")

    vergleich_spalten = ["Arbeitslose (Bestand)", "Langzeitarbeitslose", "Bedarfsgemeinschaften", "Personen in BG"]
    indexiert = (view[vergleich_spalten] / view[vergleich_spalten].iloc[0] * 100).round(1)

    fig = go.Figure()
    for spalte in vergleich_spalten:
        fig.add_trace(go.Scatter(
            x=indexiert.index, y=indexiert[spalte], mode="lines+markers", name=spalte,
            hovertemplate="%{y:.1f}<extra></extra>",
        ))
    fig.add_hline(y=100, line_dash="dash", line_color="grey", annotation_text="Startmonat = 100 %")
    fig.update_layout(
        title=f"Kennzahlen im Vergleich (indexiert, {indexiert.index[0]:%b %Y} = 100 %)",
        yaxis_title="Index (Startmonat = 100 %)",
        yaxis_ticksuffix="%",
        xaxis_title="Monat",
        hovermode="x unified",
        legend=dict(orientation="h", y=1.1),
        height=420,
    )
    st.plotly_chart(fig, width="stretch")
    st.caption(
        "Die vier Kernkennzahlen haben sehr unterschiedliche Größenordnungen (500 bis 5.000+ "
        "Personen) und werden hier auf den ersten Monat im gewählten Zeitraum indexiert: "
        "**100 = wie im Startmonat.** Ein Wert von 110 bedeutet +10 % gegenüber dem Startmonat, "
        "90 bedeutet −10 %."
    )

    st.subheader(f"Warum ist die Personenzahl größer als der Arbeitslosen-Bestand? — {letzter.name:%B %Y}")

    funnel_stufen = [
        "Personen in BG",
        "Regelleistungsberechtigte (RLB)",
        "Erwerbsfähige Leistungsberechtigte (ELB)",
        "Arbeitslose (Bestand)",
    ]
    funnel_labels = [
        "Personen in BG (ganzer Haushalt)",
        "davon Regelleistungsberechtigte (RLB)",
        "davon erwerbsfähig (ELB)",
        "davon als arbeitslos gemeldet",
    ]
    funnel_werte = [round(letzter[s]) for s in funnel_stufen]

    fig = go.Figure(go.Funnel(
        y=funnel_labels, x=funnel_werte,
        texttemplate="%{value:.0f} Personen<br>(%{percentInitial} von oben)",
        hovertemplate="%{y}<br>%{value:.0f} Personen<extra></extra>",
    ))
    fig.update_layout(title="Vom Haushalt zur gemeldeten Arbeitslosigkeit", height=420)
    st.plotly_chart(fig, width="stretch")
    st.caption(
        "Jede Stufe ist eine Teilmenge der vorherigen. **Personen in BG** = alle Haushaltsmitglieder "
        "im Bürgergeld-Bezug, inkl. Kinder. **RLB** = laufend anspruchsberechtigt. **ELB** = davon "
        "erwerbsfähig (15–64, arbeitsfähig) — der Rest sind vor allem Kinder und nicht erwerbsfähige "
        "Angehörige (NEF). **Arbeitslose (Bestand)** = davon aktuell als arbeitslos gemeldet — die "
        "übrigen ELB haben bereits einen Job und stocken auf (\"Aufstocker\"), nehmen an einer "
        "Maßnahme teil, oder sind aus anderen Gründen (Kindererziehung, Krankheit, Ausbildung) "
        "nicht sofort verfügbar."
    )

    st.divider()

    # --- Altersstruktur & Geschlecht (Momentaufnahme) ---------------------------
    st.subheader(f"Altersstruktur und Geschlecht — {pd.Timestamp(gewaehlter_monat):%B %Y}")
    st.caption(
        "Momentaufnahme für den im Filter gewählten Berichtsmonat (keine Zeitreihe): Verteilung "
        "der SGB-II-Arbeitslosen nach Altersgruppe und Geschlecht."
    )

    snap = df_long[(df_long["period"] == gewaehlter_monat) & (df_long["kategorie"] == "Arbeitslose")]
    snap = snap.set_index("merkmal")["sgb2"]

    col5, col6 = st.columns(2)

    with col5:
        alter_labels = ["15 bis unter 25 Jahre", "25 bis unter 50 Jahre", "50 Jahre und älter"]
        alter_df = pd.DataFrame({"Altersgruppe": ["15-25", "25-50", "50+"], "Personen": [snap[l] for l in alter_labels]})
        fig = px.bar(alter_df, x="Altersgruppe", y="Personen", title="Altersstruktur")
        st.plotly_chart(fig, width="stretch")

    with col6:
        geschlecht_df = pd.DataFrame({"Geschlecht": ["Männer", "Frauen"], "Personen": [snap["Männer"], snap["Frauen"]]})
        fig = px.bar(geschlecht_df, x="Geschlecht", y="Personen", color="Geschlecht", color_discrete_map={"Männer": "#2563eb", "Frauen": "#dc2626"}, title="Geschlecht")
        st.plotly_chart(fig, width="stretch")

    st.divider()

    with st.expander("Kennzahlen-Tabelle anzeigen"):
        anzeige = view.copy()
        anzeige.index = anzeige.index.strftime("%b %Y")
        anzeige.index.name = "Monat"

        # Genau ein weiches Trennzeichen (\xad) je zusammengesetztem Wort, an einer sinnvollen
        # Silbengrenze. Zwei-Wort-Spalten (mit Leerzeichen) bekommen keine zusätzliche Trennstelle,
        # sonst entstehen durch Leerzeichen + Trennzeichen zusammen zu viele Umbruchpunkte.
        anzeige = anzeige.rename(columns={
            "Arbeitslosenquote (%)": "Arbeitslosen\xadquote (%)",
            "Langzeitarbeitslose": "Langzeit\xadarbeitslose",
            "Unterbeschäftigungsquote (%)": "Unter\xadbeschäftigungs\xadquote (%)",
            "Bedarfsgemeinschaften": "Bedarfs\xadgemeinschaften",
            "Regelleistungsberechtigte (RLB)": "Regelleistungs\xadberechtigte (RLB)",
            "Erwerbsfähige Leistungsberechtigte (ELB)": "Erwerbsfähige Leistungs\xadberechtigte (ELB)",
        })

        format_spalten = {
            spalte: "{:.1f}" if "(%)" in spalte else "{:.0f}" for spalte in anzeige.columns
        }
        styler = anzeige.style.format(format_spalten).set_table_styles([
            {"selector": "th", "props": [
                ("white-space", "normal"),
                ("overflow-wrap", "normal"),
                ("word-break", "keep-all"),
                ("max-width", "120px"),
                ("font-size", "0.8em"),
                ("text-align", "center"),
                ("vertical-align", "bottom"),
                ("padding", "4px"),
                ("position", "sticky"),
                ("top", "0"),
                ("background", "var(--background-color, white)"),
                ("z-index", "1"),
            ]},
            {"selector": "td", "props": [
                ("max-width", "120px"),
                ("font-size", "0.85em"),
                ("text-align", "center"),
                ("padding", "4px"),
            ]},
            # Unterbeschäftigungsquote (%) = Spalte 3: schmal halten, damit der Header auf
            # 3 Zeilen umbricht (Unter- / beschäftigungs- / quote (%)).
            {"selector": ".col3", "props": [("max-width", "100px")]},
            # Erwerbsfähige Leistungsberechtigte (ELB) = Spalte 7: längster Header, braucht mehr
            # Platz als die anderen Spalten.
            {"selector": ".col7", "props": [("max-width", "110px")]},
        ])
        st.markdown(
            '<div style="overflow-y: auto; width: 100%; max-height: 420px; padding-right: 20px; box-sizing: border-box;">'
            '<div style="overflow-x: auto; width: 100%;">'
            f'{styler.to_html()}'
            '</div></div>',
            unsafe_allow_html=True,
        )

# =================================================================================
# Tab 2: Fluktuation (Zugang & Abgang)
# =================================================================================
with tab_fluktuation:
    st.subheader("Fluktuation: Zugang & Abgang aus Arbeitslosigkeit")
    geplant(
        beschreibung=(
            "Der bisherige Fokus liegt auf dem **Bestand** an Arbeitslosen. Dieser Tab ergänzt "
            "die Dynamik: wie viele Personen werden monatlich neu arbeitslos, und wie viele "
            "verlassen die Arbeitslosigkeit wieder?"
        ),
        datenquelle="Blatt „1.1 Eckwerte“, Zeilen „Zugang (im Monat)“, „Zugang (12-Monatssumme)“, "
        "„Abgang (im Monat)“, „Abgang (12-Monatssumme)“ — bereits in `eckwerte_long.csv` "
        "enthalten, nur noch nicht visualisiert.",
        ideen=[
            "Zeitreihe Zugang vs. Abgang (gruppierte Balken oder zwei Linien)",
            "Netto-Veränderung (Zugang − Abgang) pro Monat als Wasserfall- oder Balkendiagramm",
            "Gleitende 12-Monatssumme zur Glättung saisonaler Effekte",
        ],
        prioritaet="Priorität 1 (kein zusätzlicher Wartezeit-Aufwand, Daten direkt verfügbar)",
    )

# =================================================================================
# Tab 3: Demografie (Alter, Geschlecht als Zeitreihe, Schwerbehinderte, Ausländer)
# =================================================================================
with tab_demografie:
    st.subheader("Demografie im Zeitverlauf")
    geplant(
        beschreibung=(
            "Altersstruktur und Geschlecht gibt es im Übersicht-Tab bisher nur als Momentaufnahme "
            "für den letzten Berichtsmonat. Hier sollen diese Merkmale als echte Zeitreihe sowie "
            "weitere Personengruppen (Schwerbehinderte, Ausländer) ergänzt werden."
        ),
        datenquelle="Blatt „1.1 Eckwerte“ (Altersgruppen, Geschlecht, Schwerbehinderte, Ausländer je "
        "Berichtsmonat) sowie Blatt „2.4 Langzeitarbeitslosigkeit“ (Geschlechterverteilung "
        "speziell der Langzeitarbeitslosen).",
        ideen=[
            "Gestapeltes Flächendiagramm der Altersgruppen über die Zeit",
            "Geschlechteranteil als Zeitreihe (statt nur letzter Monat)",
            "Anteil Schwerbehinderte / Ausländer an allen Arbeitslosen als Zeitreihe",
        ],
        prioritaet="Priorität 2",
    )

# =================================================================================
# Tab 4: Erwerbstätigkeit / Aufstocker
# =================================================================================
with tab_erwerbstaetigkeit:
    st.subheader("Erwerbstätigkeit trotz Bürgergeld-Bezug (\"Aufstocker\")")
    geplant(
        beschreibung=(
            "Komplett neues Themenfeld: Personen, die trotz eines Jobs ergänzend Bürgergeld "
            "beziehen, weil ihr Einkommen nicht zum Leben reicht. Passt inhaltlich direkt an die "
            "Trichter-Grafik im Übersicht-Tab an — dort endet die Kette bei „Arbeitslose“, hier "
            "käme die Ergänzung „davon in Arbeit, aber bedürftig“ dazu."
        ),
        datenquelle="Blatt „3.3 Erwerbstätigkeit“ — erwerbstätige erwerbsfähige Leistungsberechtigte "
        "(ELB), aufgeschlüsselt nach abhängig/selbstständig und Einkommenshöhe "
        "(Geringfügigkeitsgrenze vs. Übergangsbereich).",
        ideen=[
            "Zeitreihe der Aufstocker-Zahl (absolut und Anteil an allen ELB)",
            "Aufschlüsselung abhängig vs. selbstständig erwerbstätig",
            "Erweiterte Trichter-Grafik mit zusätzlicher Stufe „erwerbstätige ELB“",
        ],
        prioritaet="Priorität 3",
        wartezeit=True,
    )

# =================================================================================
# Tab 5: Bezugsdauer (Langzeitleistungsbezug, Bewegungen, Haushaltsstruktur)
# =================================================================================
with tab_bezugsdauer:
    st.subheader("Wie lange dauert der Leistungsbezug?")
    geplant(
        beschreibung=(
            "Langzeitarbeitslosigkeit (LZA) und Langzeitleistungsbezug (LZB) sind unterschiedliche "
            "Kennzahlen — Bürgergeld kann auch ohne Arbeitslosigkeit bezogen werden (z. B. bei "
            "Aufstockern). Ergänzt außerdem, wie oft Personen den Leistungsbezug wiederholt "
            "verlassen und erneut beginnen (\"Drehtür-Effekt\"), sowie die Haushaltsgrößenstruktur "
            "der Bedarfsgemeinschaften."
        ),
        datenquelle="Blatt „3.4 Langzeitleistungsbezug“ (LZB: mind. 21 von 24 Monaten im Bezug), "
        "Blatt „3.5 Bewegungen Personen“ (Zu-/Abgänge Regelleistungsbezug inkl. "
        "Vorbezugs-Historie), Blatt „3.1 Bedarfsgemeinschaften“ (Struktur nach Haushaltsgröße).",
        ideen=[
            "LZB vs. LZA im Liniendiagramm vergleichen",
            "Anteil der Wiederholungsfälle (erneuter Bezug innerhalb 12 Monaten) als Zeitreihe",
            "Balkendiagramm der Haushaltsgrößenverteilung (1, 2, 3, 4+ Personen)",
        ],
        prioritaet="nachrangig",
        wartezeit=True,
    )

# =================================================================================
# Tab 6: Finanzen (Zahlungsansprüche)
# =================================================================================
with tab_finanzen:
    st.subheader("Zahlungsansprüche in Euro")
    geplant(
        beschreibung=(
            "Bisher zeigt das Dashboard nur Personen- und Haushaltszahlen. Dieser Tab bringt die "
            "einzige Quelle für tatsächliche **Euro-Beträge**: das Finanzvolumen der "
            "SGB-II-Leistungen."
        ),
        datenquelle="Blatt „3.6 Zahlungsansprüche“ — Summe der Zahlungsansprüche (in Tsd. Euro), "
        "durchschnittlicher Anspruch je Bedarfsgemeinschaft, aufgeschlüsselt nach Regelbedarf "
        "für erwerbsfähige (ELB) und nicht erwerbsfähige (NEF) Leistungsberechtigte.",
        ideen=[
            "Zeitreihe der monatlichen Gesamtsumme in Euro",
            "Durchschnittlicher Zahlungsanspruch je Bedarfsgemeinschaft im Zeitverlauf",
            "Aufteilung Regelbedarf ELB vs. NEF als gestapeltes Balkendiagramm",
        ],
        prioritaet="Priorität 4",
        wartezeit=True,
    )

# =================================================================================
# Tab 7: Förderung (aktive Arbeitsmarktpolitik)
# =================================================================================
with tab_foerderung:
    st.subheader("Förderung der aktiven Arbeitsmarktpolitik")
    geplant(
        beschreibung=(
            "Komplett neues Themenfeld ohne bisherige Berührung: Maßnahmen zur Eingliederung in "
            "Arbeit (z. B. Weiterbildung, Aktivierung), die das Jobcenter finanziert."
        ),
        datenquelle="Blatt „4.1 Förderung“ (Eintritte in Maßnahmen nach Instrumenten-Kategorie, "
        "inkl. gleitender 12-Monatssumme) und Blatt „4.2 Förderung Strukturen“ (Bestand an "
        "Teilnehmenden nach Geschlecht, Alter, LZA-Status, Schwerbehinderung, sowie die fertige "
        "Kennzahl Aktivierungsquote AQ1/AQ2a).",
        ideen=[
            "Balkendiagramm der Maßnahmen-Kategorien nach Teilnehmerzahl",
            "Bestand an Teilnehmenden nach Altersgruppe (gestapeltes Balkendiagramm)",
            "Aktivierungsquote (AQ1/AQ2a) als Zeitreihe",
        ],
        prioritaet="Priorität 5",
        wartezeit=True,
    )
