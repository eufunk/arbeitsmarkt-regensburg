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
    fluktuation_path = PROCESSED_DIR / "fluktuation_sgb2.csv"
    demografie_path = PROCESSED_DIR / "demografie_sgb2.csv"
    erwerbstaetigkeit_path = PROCESSED_DIR / "erwerbstaetigkeit_sgb2.csv"
    finanzen_path = PROCESSED_DIR / "finanzen_sgb2.csv"
    foerderung_path = PROCESSED_DIR / "foerderung_sgb2.csv"
    bezugsdauer_path = PROCESSED_DIR / "bezugsdauer_sgb2.csv"
    rechtskreis_path = PROCESSED_DIR / "rechtskreisvergleich_sgb2.csv"
    arbeitsstellen_path = PROCESSED_DIR / "arbeitsstellen.csv"
    unterbeschaeftigung_path = PROCESSED_DIR / "unterbeschaeftigung_sgb2.csv"
    rlb_elb_nef_path = PROCESSED_DIR / "rlb_elb_nef_sgb2.csv"
    beschaeftigung_path = PROCESSED_DIR / "beschaeftigung_quartal.csv"

    if not long_path.exists() or not wide_path.exists():
        return None, None, None, None, None, None, None, None, None, None, None, None, None

    df_long = pd.read_csv(long_path)
    df_long["period"] = pd.PeriodIndex(df_long["period"], freq="M").to_timestamp()

    kennzahlen = pd.read_csv(wide_path, index_col="period", parse_dates=["period"])
    kennzahlen = kennzahlen.sort_index()

    fluktuation = None
    if fluktuation_path.exists():
        fluktuation = pd.read_csv(fluktuation_path, index_col="period", parse_dates=["period"])
        fluktuation = fluktuation.sort_index()

    demografie = None
    if demografie_path.exists():
        demografie = pd.read_csv(demografie_path, index_col="period", parse_dates=["period"])
        demografie = demografie.sort_index()

    erwerbstaetigkeit = None
    if erwerbstaetigkeit_path.exists():
        erwerbstaetigkeit = pd.read_csv(erwerbstaetigkeit_path, index_col="period", parse_dates=["period"])
        erwerbstaetigkeit = erwerbstaetigkeit.sort_index()

    finanzen = None
    if finanzen_path.exists():
        finanzen = pd.read_csv(finanzen_path, index_col="period", parse_dates=["period"])
        finanzen = finanzen.sort_index()

    foerderung = None
    if foerderung_path.exists():
        foerderung = pd.read_csv(foerderung_path, index_col="period", parse_dates=["period"])
        foerderung = foerderung.sort_index()

    bezugsdauer = None
    if bezugsdauer_path.exists():
        bezugsdauer = pd.read_csv(bezugsdauer_path, index_col="period", parse_dates=["period"])
        bezugsdauer = bezugsdauer.sort_index()

    rechtskreis = None
    if rechtskreis_path.exists():
        rechtskreis = pd.read_csv(rechtskreis_path, index_col="period", parse_dates=["period"])
        rechtskreis = rechtskreis.sort_index()

    arbeitsstellen = None
    if arbeitsstellen_path.exists():
        arbeitsstellen = pd.read_csv(arbeitsstellen_path, index_col="period", parse_dates=["period"])
        arbeitsstellen = arbeitsstellen.sort_index()

    unterbeschaeftigung = None
    if unterbeschaeftigung_path.exists():
        unterbeschaeftigung = pd.read_csv(unterbeschaeftigung_path, index_col="period", parse_dates=["period"])
        unterbeschaeftigung = unterbeschaeftigung.sort_index()

    rlb_elb_nef = None
    if rlb_elb_nef_path.exists():
        rlb_elb_nef = pd.read_csv(rlb_elb_nef_path, index_col="period", parse_dates=["period"])
        rlb_elb_nef = rlb_elb_nef.sort_index()

    beschaeftigung = None
    if beschaeftigung_path.exists():
        beschaeftigung = pd.read_csv(beschaeftigung_path, index_col="quartal", parse_dates=["quartal"])
        beschaeftigung = beschaeftigung.sort_index()

    return df_long, kennzahlen, fluktuation, demografie, erwerbstaetigkeit, finanzen, foerderung, bezugsdauer, rechtskreis, arbeitsstellen, unterbeschaeftigung, rlb_elb_nef, beschaeftigung


df_long, kennzahlen, fluktuation, demografie, erwerbstaetigkeit, finanzen, foerderung, bezugsdauer, rechtskreis, arbeitsstellen, unterbeschaeftigung, rlb_elb_nef, beschaeftigung = load_data()

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

flu_view = None
if fluktuation is not None:
    flu_mask = (fluktuation.index >= date_range[0]) & (fluktuation.index <= date_range[1])
    flu_view = fluktuation.loc[flu_mask]

demo_view = None
if demografie is not None:
    demo_mask = (demografie.index >= date_range[0]) & (demografie.index <= date_range[1])
    demo_view = demografie.loc[demo_mask]

rechtskreis_view = None
if rechtskreis is not None:
    rechtskreis_mask = (rechtskreis.index >= date_range[0]) & (rechtskreis.index <= date_range[1])
    rechtskreis_view = rechtskreis.loc[rechtskreis_mask]

arbeitsstellen_view = None
if arbeitsstellen is not None:
    arbeitsstellen_mask = (arbeitsstellen.index >= date_range[0]) & (arbeitsstellen.index <= date_range[1])
    arbeitsstellen_view = arbeitsstellen.loc[arbeitsstellen_mask]

unterbeschaeftigung_view = None
if unterbeschaeftigung is not None:
    unterbeschaeftigung_mask = (unterbeschaeftigung.index >= date_range[0]) & (unterbeschaeftigung.index <= date_range[1])
    unterbeschaeftigung_view = unterbeschaeftigung.loc[unterbeschaeftigung_mask]

rlb_elb_nef_view = None
if rlb_elb_nef is not None:
    rlb_elb_nef_mask = (rlb_elb_nef.index >= date_range[0]) & (rlb_elb_nef.index <= date_range[1])
    rlb_elb_nef_view = rlb_elb_nef.loc[rlb_elb_nef_mask]

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
tab_uebersicht, tab_rechtskreis, tab_fluktuation, tab_demografie, tab_erwerbstaetigkeit, tab_bezugsdauer, tab_finanzen, tab_foerderung, tab_arbeitsstellen, tab_unterbeschaeftigung, tab_rlb_elb_nef, tab_beschaeftigung, tab_glossar = st.tabs(
    [
        "📊 SGB II Übersicht",
        "⚖️ SGB II vs. SGB III",
        "🔄 Fluktuation",
        "👥 Demografie",
        "💼 Erwerbstätigkeit",
        "⏳ Bezugsdauer",
        "💶 Finanzen",
        "🎯 Förderung",
        "📋 Arbeitsstellen",
        "📉 Unterbeschäftigung",
        "🧩 RLB/ELB/NEF",
        "🚗 Beschäftigung",
        "📖 Glossar",
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
            '<div style="overflow-x: auto; overflow-y: auto; width: 100%; max-height: 420px; '
            'padding-right: 20px; box-sizing: border-box;">'
            f'{styler.to_html()}'
            '</div>',
            unsafe_allow_html=True,
        )

# =================================================================================
# Tab 1b: SGB II vs. SGB III (Rechtskreisvergleich)
# =================================================================================
with tab_rechtskreis:
    st.subheader("Jobcenter-Anteil an der Arbeitslosigkeit insgesamt")

    if rechtskreis_view is None or rechtskreis_view.empty:
        st.warning(
            "Keine Rechtskreisvergleich-Daten gefunden. Bitte zuerst "
            "`Notebooks/10_Rechtskreisvergleich.ipynb` einmal komplett ausführen, damit "
            "`Data/processed/rechtskreisvergleich_sgb2.csv` entsteht."
        )
    else:
        st.caption(
            "Alle übrigen Tabs zeigen ausschließlich den **Rechtskreis SGB II** "
            "(Jobcenter-Zuständigkeit). Dieser Tab setzt das ins Verhältnis zur "
            "**gesamten** Arbeitslosigkeit in Regensburg (SGB II + SGB III) — die "
            "Differenz fällt in die Zuständigkeit der **Agentur für Arbeit** (SGB III, "
            "z. B. Arbeitslosengeld I)."
        )

        st.markdown("#### Arbeitslose (Bestand): SGB II vs. SGB III")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=rechtskreis_view.index, y=rechtskreis_view["Arbeitslose (Bestand): SGB II"], name="SGB II (Jobcenter)",
            mode="lines", stackgroup="bestand", line=dict(color="#2563eb", width=0.5),
        ))
        fig.add_trace(go.Scatter(
            x=rechtskreis_view.index, y=rechtskreis_view["Arbeitslose (Bestand): SGB III"], name="SGB III (Agentur für Arbeit)",
            mode="lines", stackgroup="bestand", line=dict(color="#7c3aed", width=0.5),
        ))
        fig.add_trace(go.Scatter(
            x=rechtskreis_view.index, y=rechtskreis_view["Arbeitslose (Bestand): Jobcenter-Anteil (%)"], name="Jobcenter-Anteil (%)",
            mode="lines+markers", line=dict(color="#f59e0b", dash="dot"), marker=dict(size=5), yaxis="y2",
        ))
        fig.update_layout(
            yaxis=dict(title="Personen"),
            yaxis2=dict(title="Jobcenter-Anteil (%)", overlaying="y", side="right", ticksuffix="%"),
            xaxis_title="Monat", hovermode="x unified", legend=dict(orientation="h", y=1.15), height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Der Jobcenter-Anteil an allen Arbeitslosen liegt stabil bei rund 40 % — "
            "die Mehrheit der Arbeitslosen (≈ 60 %) fällt in die Zuständigkeit der "
            "Agentur für Arbeit, nicht des Jobcenters."
        )

        st.markdown("#### Langzeitarbeitslose: SGB II vs. SGB III")
        with st.expander("Warum ist der Jobcenter-Anteil hier so viel höher?"):
            st.markdown(
                "Arbeitslosengeld I (SGB III) ist zeitlich befristet (i. d. R. "
                "12–24 Monate). Wer danach weiterhin arbeitslos ist, wechselt in den "
                "SGB-II-Bezug (Bürgergeld) — Langzeitarbeitslosigkeit konzentriert sich "
                "dadurch strukturell im SGB II."
            )
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=rechtskreis_view.index, y=rechtskreis_view["Langzeitarbeitslose: SGB II"], name="SGB II (Jobcenter)",
            mode="lines", stackgroup="lza", line=dict(color="#2563eb", width=0.5),
        ))
        fig.add_trace(go.Scatter(
            x=rechtskreis_view.index, y=rechtskreis_view["Langzeitarbeitslose: SGB III"], name="SGB III (Agentur für Arbeit)",
            mode="lines", stackgroup="lza", line=dict(color="#7c3aed", width=0.5),
        ))
        fig.add_trace(go.Scatter(
            x=rechtskreis_view.index, y=rechtskreis_view["Langzeitarbeitslose: Jobcenter-Anteil (%)"], name="Jobcenter-Anteil (%)",
            mode="lines+markers", line=dict(color="#f59e0b", dash="dot"), marker=dict(size=5), yaxis="y2",
        ))
        fig.update_layout(
            yaxis=dict(title="Personen"),
            yaxis2=dict(title="Jobcenter-Anteil (%)", overlaying="y", side="right", ticksuffix="%"),
            xaxis_title="Monat", hovermode="x unified", legend=dict(orientation="h", y=1.15), height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Rund 72 % aller Langzeitarbeitslosen in Regensburg fallen in die "
            "Zuständigkeit des Jobcenters — deutlich mehr als beim Bestand insgesamt "
            "(≈ 40 %). Die SGB-III-Langzeitarbeitslosigkeit wächst dabei sogar noch "
            "stärker (+ 55 %) als die SGB-II-Zahl (+ 41 %, siehe Tab „📊 SGB II "
            "Übersicht“)."
        )

        st.markdown("#### Quoten im Vergleich")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=rechtskreis_view.index, y=rechtskreis_view["Arbeitslosenquote (%): Insgesamt"], name="Arbeitslosenquote: Insgesamt", mode="lines+markers", line=dict(color="#374151"), marker=dict(size=5)))
        fig.add_trace(go.Scatter(x=rechtskreis_view.index, y=rechtskreis_view["Arbeitslosenquote (%): SGB II"], name="Arbeitslosenquote: SGB II-Anteil", mode="lines+markers", line=dict(color="#2563eb"), marker=dict(size=5)))
        fig.add_trace(go.Scatter(x=rechtskreis_view.index, y=rechtskreis_view["Unterbeschäftigungsquote (%): Insgesamt"], name="Unterbeschäftigungsquote: Insgesamt", mode="lines+markers", line=dict(color="#6b7280", dash="dash"), marker=dict(size=5)))
        fig.add_trace(go.Scatter(x=rechtskreis_view.index, y=rechtskreis_view["Unterbeschäftigungsquote (%): SGB II"], name="Unterbeschäftigungsquote: SGB II-Anteil", mode="lines+markers", line=dict(color="#7c3aed", dash="dash"), marker=dict(size=5)))
        fig.update_layout(
            yaxis_title="Prozent", yaxis_ticksuffix="%",
            xaxis_title="Monat", hovermode="x unified", legend=dict(orientation="h", y=1.15), height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Arbeitslosen- und Unterbeschäftigungsquote bestätigen dasselbe Bild: "
            "SGB-II-Anteil an der Arbeitslosenquote ≈ 40 %, an der "
            "Unterbeschäftigungsquote ≈ 46 % (leicht rückläufig)."
        )

# =================================================================================
# Tab 2: Fluktuation (Zugang & Abgang)
# =================================================================================
with tab_fluktuation:
    st.subheader("Fluktuation: Zugang & Abgang aus Arbeitslosigkeit")

    if flu_view is None or flu_view.empty:
        st.warning(
            "Keine Fluktuationsdaten gefunden. Bitte zuerst "
            "`Notebooks/04_Fluktuation.ipynb` einmal komplett ausführen, damit "
            "`Data/processed/fluktuation_sgb2.csv` entsteht."
        )
    else:
        st.caption(
            "Der bisherige Fokus (Tab „SGB II Übersicht“) liegt auf dem **Bestand** an "
            "Arbeitslosen. Dieser Tab zeigt die Dynamik dahinter: wie viele Personen werden "
            "monatlich neu arbeitslos (**Zugang**), und wie viele verlassen die "
            "Arbeitslosigkeit wieder (**Abgang**)? Rechtskreis SGB II."
        )

        st.markdown("#### Zugang und Abgang im Monatsverlauf")
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=flu_view.index, y=flu_view["Zugang (im Monat)"], name="Zugang",
            marker_color="#dc2626",
        ))
        fig.add_trace(go.Bar(
            x=flu_view.index, y=-flu_view["Abgang (im Monat)"], name="Abgang",
            marker_color="#16a34a",
        ))
        fig.update_layout(
            title="Zugang und Abgang aus Arbeitslosigkeit im Monatsverlauf (SGB II)",
            yaxis_title="Personen (Abgang als negativer Balken)",
            xaxis_title="Monat",
            barmode="relative",
            hovermode="x unified",
            legend=dict(orientation="h", y=1.12),
            height=420,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Zugang = neu arbeitslos gemeldete Personen im jeweiligen Monat, Abgang = "
            "Personen, die die Arbeitslosigkeit im jeweiligen Monat verlassen haben "
            "(Gründe stehen erst im Blatt „2.3 Arbeitslosigkeit Abgang“, hier nicht enthalten)."
        )

        st.markdown("#### Netto-Fluktuation vs. tatsächliche Bestandsänderung")
        bestand_delta = view["Arbeitslose (Bestand)"].diff().reindex(flu_view.index)
        netto = flu_view["Netto-Fluktuation (im Monat)"]
        netto_positiv = netto.where(netto >= 0)
        netto_negativ = netto.where(netto < 0)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=netto.index, y=netto_positiv, name="Netto-Fluktuation: Zugang > Abgang",
            marker_color="#dc2626",
        ))
        fig.add_trace(go.Bar(
            x=netto.index, y=netto_negativ, name="Netto-Fluktuation: Abgang > Zugang",
            marker_color="#16a34a",
        ))
        fig.add_trace(go.Scatter(
            x=bestand_delta.index, y=bestand_delta, name="Tatsächliche Bestandsänderung",
            mode="lines+markers", line=dict(color="#1e3a8a", width=2), marker=dict(size=6),
        ))
        fig.add_hline(y=0, line_color="grey")
        fig.update_layout(
            title="Netto-Fluktuation vs. tatsächliche Bestandsänderung (SGB II)",
            yaxis_title="Personen",
            xaxis_title="Monat",
            hovermode="x unified",
            legend=dict(orientation="h", y=1.12),
            height=420,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Die Netto-Fluktuation (Zugang − Abgang) erklärt die tatsächliche Bestandsänderung "
            "nicht vollständig — im Schnitt liegt sie rund 21 Personen pro Monat darunter, "
            "plausibel erklärbar durch Rechtskreiswechsel zwischen SGB II und SGB III, die "
            "sich im Bestand niederschlagen, aber nicht als eigene Zugangs-/Abgangskategorie "
            "erscheinen."
        )

        st.markdown("#### 12-Monatssummen: der mittelfristige Trend")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=flu_view.index, y=flu_view["Zugang (12-Monatssumme)"], name="Zugang (12-Monatssumme)",
            mode="lines+markers", line=dict(color="#dc2626"), marker=dict(size=6),
        ))
        fig.add_trace(go.Scatter(
            x=flu_view.index, y=flu_view["Abgang (12-Monatssumme)"], name="Abgang (12-Monatssumme)",
            mode="lines+markers", line=dict(color="#16a34a"), marker=dict(size=6),
        ))
        fig.update_layout(
            title="Zugang und Abgang: 12-Monatssummen im Zeitverlauf (SGB II)",
            yaxis_title="Personen (rollierende 12-Monatssumme)",
            xaxis_title="Monat",
            hovermode="x unified",
            legend=dict(orientation="h", y=1.12),
            height=420,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Glättet saisonale Schwankungen der Monatswerte und zeigt den mittelfristigen "
            "Trend: Der Zugangstrend ist rückläufig, der Abgangstrend leicht steigend — die "
            "rollierende Netto-Fluktuation hat sich über den Beobachtungszeitraum spürbar "
            "verschlechtert, ohne dass sich das bislang deutlich im Bestand zeigt."
        )

# =================================================================================
# Tab 3: Demografie (Alter, Geschlecht als Zeitreihe, Schwerbehinderte, Ausländer)
# =================================================================================
with tab_demografie:
    st.subheader("Demografie im Zeitverlauf")

    if demo_view is None or demo_view.empty:
        st.warning(
            "Keine Demografie-Daten gefunden. Bitte zuerst "
            "`Notebooks/05_Demografie.ipynb` einmal komplett ausführen, damit "
            "`Data/processed/demografie_sgb2.csv` entsteht."
        )
    else:
        st.caption(
            "Altersstruktur und Geschlecht gibt es im Tab „SGB II Übersicht“ bisher nur als "
            "Momentaufnahme für den gewählten Berichtsmonat. Hier als echte Zeitreihe, "
            "ergänzt um zwei bislang unanalysierte Personengruppen: Ausländer und "
            "schwerbehinderte Menschen. Rechtskreis SGB II."
        )

        st.markdown("#### Altersstruktur im Zeitverlauf")
        alter_stapel = ["15 bis unter 25 Jahre", "25 bis unter 50 Jahre", "50 bis unter 55 Jahre", "55 Jahre und älter"]
        farben_alter = {
            "15 bis unter 25 Jahre": "#2563eb", "25 bis unter 50 Jahre": "#7c3aed",
            "50 bis unter 55 Jahre": "#f59e0b", "55 Jahre und älter": "#dc2626",
        }
        fig = go.Figure()
        for gruppe in alter_stapel:
            fig.add_trace(go.Scatter(
                x=demo_view.index, y=demo_view[gruppe], name=gruppe,
                mode="lines", stackgroup="alter", line=dict(color=farben_alter[gruppe], width=0.5),
            ))
        fig.update_layout(
            title="Altersstruktur der Arbeitslosen im Zeitverlauf (SGB II)",
            yaxis_title="Personen",
            xaxis_title="Monat",
            hovermode="x unified",
            legend=dict(orientation="h", y=1.15),
            height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Alle vier Bänder sind überschneidungsfrei und summieren sich zum Gesamtbestand "
            "(Fläche) — die Gruppe „50 Jahre und älter“ ist dafür in „50 bis unter 55“ und "
            "„55 und älter“ aufgeteilt. Ihr gemeinsamer Anteil an „50+“ zeigt: die Gruppe "
            "„55 und älter“ wächst darin von 64,8 % auf 68,8 % — die Alterung innerhalb der "
            "älteren Arbeitslosen nimmt zu."
        )

        st.markdown("#### Geschlechterverteilung im Zeitverlauf")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=demo_view.index, y=demo_view["Männer"], name="Männer",
            mode="lines", stackgroup="geschlecht", line=dict(color="#2563eb", width=0.5),
        ))
        fig.add_trace(go.Scatter(
            x=demo_view.index, y=demo_view["Frauen"], name="Frauen",
            mode="lines", stackgroup="geschlecht", line=dict(color="#db2777", width=0.5),
        ))
        fig.update_layout(
            title="Geschlechterverteilung der Arbeitslosen im Zeitverlauf (SGB II)",
            yaxis_title="Personen",
            xaxis_title="Monat",
            hovermode="x unified",
            legend=dict(orientation="h", y=1.15),
            height=400,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Leichte Verschiebung zu mehr Männern über den Beobachtungszeitraum — der "
            "Männeranteil steigt von 53,1 % auf 54,5 %, der Bestandsanstieg der letzten "
            "Monate geht überproportional auf Männer zurück."
        )

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### Ausländische Arbeitslose")
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=demo_view.index, y=demo_view["Ausländer"], name="absolut",
                mode="lines+markers", line=dict(color="#0d9488"), marker=dict(size=5), yaxis="y1",
            ))
            fig.add_trace(go.Scatter(
                x=demo_view.index, y=demo_view["Anteil Ausländer (%)"], name="Anteil (%)",
                mode="lines+markers", line=dict(color="#f59e0b", dash="dot"), marker=dict(size=5), yaxis="y2",
            ))
            fig.update_layout(
                yaxis=dict(title="Personen"),
                yaxis2=dict(title="Anteil (%)", overlaying="y", side="right", ticksuffix="%"),
                xaxis_title="Monat",
                hovermode="x unified",
                legend=dict(orientation="h", y=1.15),
                height=380,
            )
            st.plotly_chart(fig, width="stretch")
            st.caption(
                "Überraschend hoher, deutlich rückläufiger Anteil: von 51,7 % (Jan 2025) "
                "auf 45,4 % (Jun 2026) — fast die Hälfte des SGB-II-Arbeitslosenbestands."
            )

        with col_b:
            st.markdown("#### Schwerbehinderte Menschen")
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=demo_view.index, y=demo_view["schwerbehinderte Menschen"], name="absolut",
                mode="lines+markers", line=dict(color="#7c3aed"), marker=dict(size=5), yaxis="y1",
            ))
            fig.add_trace(go.Scatter(
                x=demo_view.index, y=demo_view["Anteil Schwerbehinderte (%)"], name="Anteil (%)",
                mode="lines+markers", line=dict(color="#f59e0b", dash="dot"), marker=dict(size=5), yaxis="y2",
            ))
            fig.update_layout(
                yaxis=dict(title="Personen"),
                yaxis2=dict(title="Anteil (%)", overlaying="y", side="right", ticksuffix="%"),
                xaxis_title="Monat",
                hovermode="x unified",
                legend=dict(orientation="h", y=1.15),
                height=380,
            )
            st.plotly_chart(fig, width="stretch")
            st.caption(
                "Kleinerer, leicht steigender Anteil: von 7,9 % (Jan 2025) auf 8,7 % "
                "(Jun 2026)."
            )

# =================================================================================
# Tab 4: Erwerbstätigkeit / Aufstocker
# =================================================================================
with tab_erwerbstaetigkeit:
    st.subheader("Erwerbstätigkeit trotz Bürgergeld-Bezug (\"Aufstocker\")")

    if erwerbstaetigkeit is None or erwerbstaetigkeit.empty:
        st.warning(
            "Keine Erwerbstätigkeits-Daten gefunden. Bitte zuerst "
            "`Notebooks/06_Erwerbstaetigkeit.ipynb` einmal komplett ausführen, damit "
            "`Data/processed/erwerbstaetigkeit_sgb2.csv` entsteht."
        )
    else:
        st.caption(
            "Erwerbstätige erwerbsfähige Leistungsberechtigte (ELB) — in der öffentlichen "
            "Diskussion oft „Aufstocker“ genannt: Personen, die trotz eigenem "
            "Erwerbseinkommen ergänzend Bürgergeld beziehen. Passt inhaltlich an die "
            "Trichter-Grafik im Tab „SGB II Übersicht“ an."
        )
        with st.expander("Was bedeutet ELB?"):
            st.markdown(
                "**Erwerbsfähige Leistungsberechtigte (ELB)** sind Personen innerhalb einer "
                "Bedarfsgemeinschaft (BG), die Bürgergeld beziehen **und** erwerbsfähig sind "
                "(zwischen 15 und 65 Jahren, gesundheitlich in der Lage zu arbeiten). Sie "
                "sind die Kernzielgruppe der Arbeitsvermittlung des Jobcenters. Abzugrenzen "
                "von den **nicht erwerbsfähigen Leistungsberechtigten (NEF)** — v. a. Kinder "
                "unter 15 Jahren und dauerhaft erwerbsunfähige Angehörige innerhalb derselben "
                "BG. **Erwerbstätige ELB** sind ELB, die zusätzlich eigenes Einkommen aus "
                "Beschäftigung oder Selbstständigkeit haben — die „Aufstocker“, um die es in "
                "diesem Tab geht. Weitere Begriffe: siehe Tab „📖 Glossar“."
            )
        st.info(
            "⚠️ Das Tabellenblatt „3.3 Erwerbstätigkeit“ meldet nur Werte mit **3 Monaten "
            "Wartezeit**. Die hier gezeigte Zeitreihe (Oktober 2024 – März 2026) liegt "
            "daher 3 Monate früher als der übrige Berichtszeitraum (Januar 2025 – Juni "
            "2026) und wird **nicht** vom Zeitraum-Filter der Sidebar beeinflusst."
        )

        st.markdown("#### Erwerbstätige ELB im Zeitverlauf: die Aufstocker-Quote")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=erwerbstaetigkeit.index, y=erwerbstaetigkeit["erwerbstätige ELB"], name="erwerbstätige ELB (absolut)",
            mode="lines+markers", line=dict(color="#2563eb"), marker=dict(size=6), yaxis="y1",
        ))
        fig.add_trace(go.Scatter(
            x=erwerbstaetigkeit.index, y=erwerbstaetigkeit["Aufstockerquote (%)"], name="Aufstockerquote (%)",
            mode="lines+markers", line=dict(color="#f59e0b", dash="dot"), marker=dict(size=6), yaxis="y2",
        ))
        fig.update_layout(
            yaxis=dict(title="Personen"),
            yaxis2=dict(title="Anteil an allen ELB (%)", overlaying="y", side="right", ticksuffix="%"),
            xaxis_title="Monat",
            hovermode="x unified",
            legend=dict(orientation="h", y=1.15),
            height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Die Aufstockerquote (erwerbstätige ELB / alle ELB, hier selbst berechnet) ist "
            "mit Ø 21,4 % bemerkenswert stabil — rund jede fünfte erwerbsfähige "
            "leistungsberechtigte Person ist erwerbstätig, verdient aber nicht genug für "
            "den vollständigen Ausstieg aus dem Bürgergeld-Bezug."
        )

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### Abhängig vs. selbständig")
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=erwerbstaetigkeit.index, y=erwerbstaetigkeit["abhängig erwerbstätig"], name="abhängig erwerbstätig",
                mode="lines", stackgroup="erwerb", line=dict(color="#2563eb", width=0.5),
            ))
            fig.add_trace(go.Scatter(
                x=erwerbstaetigkeit.index, y=erwerbstaetigkeit["selbständig erwerbstätig"], name="selbständig erwerbstätig",
                mode="lines", stackgroup="erwerb", line=dict(color="#7c3aed", width=0.5),
            ))
            fig.update_layout(
                yaxis_title="Personen",
                xaxis_title="Monat",
                hovermode="x unified",
                legend=dict(orientation="h", y=1.15),
                height=400,
            )
            st.plotly_chart(fig, width="stretch")
            st.caption(
                "**Abhängig erwerbstätig** = angestellt bei einem Arbeitgeber (Lohn/Gehalt). "
                "**Selbständig erwerbstätig** = eigenes Gewerbe/Freiberuflichkeit "
                "(Betriebsgewinn statt Lohn). Beide Gruppen zusammen ergeben die "
                "„erwerbstätige ELB“ aus der Grafik oben. Klar dominiert von abhängiger "
                "Beschäftigung (93–94 %), selbständig Erwerbstätige bleiben eine stabile "
                "Minderheit von rund 6–7 %."
            )

        with col_b:
            st.markdown("#### Einkommensstruktur (abhängig erwerbstätig)")
            einkommens_stufen = ["bis zur Geringfügigkeitsgrenze", "im Übergangsbereich", "über dem Übergangsbereich"]
            farben_einkommen = {"bis zur Geringfügigkeitsgrenze": "#f59e0b", "im Übergangsbereich": "#2563eb", "über dem Übergangsbereich": "#16a34a"}
            fig = go.Figure()
            for stufe in einkommens_stufen:
                fig.add_trace(go.Scatter(
                    x=erwerbstaetigkeit.index, y=erwerbstaetigkeit[stufe], name=stufe,
                    mode="lines", stackgroup="einkommen", line=dict(color=farben_einkommen[stufe], width=0.5),
                ))
            fig.update_layout(
                yaxis_title="Personen",
                xaxis_title="Monat",
                hovermode="x unified",
                legend=dict(orientation="h", y=1.15),
                height=400,
            )
            st.plotly_chart(fig, width="stretch")
            st.caption(
                "Die drei Stufen sind überschneidungsfrei und summieren sich exakt zu "
                "„abhängig erwerbstätig“ aus der Grafik links — sie zeigen, wie viel die "
                "abhängig erwerbstätigen Aufstocker verdienen:\n\n"
                "- **bis zur Geringfügigkeitsgrenze**: Minijob, aktuell bis 603 € brutto/Monat.\n"
                "- **im Übergangsbereich** (\"Midi-Job\"): 603 € bis 2.000 € brutto/Monat, mit "
                "reduzierten Sozialversicherungsbeiträgen.\n"
                "- **über dem Übergangsbereich**: mehr als 2.000 € brutto/Monat — trotzdem "
                "reicht das Einkommen (z. B. wegen Teilzeit, hoher Miete oder mehrerer "
                "Kinder in der Bedarfsgemeinschaft) nicht aus, um ganz ohne Bürgergeld "
                "auszukommen.\n\n"
                "**Trend:** leichte Verschiebung zu höheren Einkommen — der Anteil „bis "
                "Geringfügigkeitsgrenze“ sinkt von 43,4 % auf 38,1 % (jeweils bezogen auf "
                "alle abhängig Erwerbstätigen), während „im Übergangsbereich“ (48,0 % → "
                "51,0 %) und „über dem Übergangsbereich“ (8,6 % → 10,9 %) steigen."
            )

# =================================================================================
# Tab 5: Bezugsdauer (Langzeitleistungsbezug, Bewegungen, Haushaltsstruktur)
# =================================================================================
with tab_bezugsdauer:
    st.subheader("Wie lange dauert der Leistungsbezug?")

    if bezugsdauer is None or bezugsdauer.empty:
        st.warning(
            "Keine Bezugsdauer-Daten gefunden. Bitte zuerst "
            "`Notebooks/09_Bezugsdauer.ipynb` einmal komplett ausführen, damit "
            "`Data/processed/bezugsdauer_sgb2.csv` entsteht."
        )
    else:
        st.caption(
            "Wie lange und in welcher Haushaltskonstellation Menschen im SGB-II-Bezug "
            "stehen — Haushaltsstruktur, Langzeitleistungsbezug (LZB) und "
            "Bewegungsdynamik (\"Drehtür-Effekt\")."
        )
        st.info(
            "⚠️ Die zugrunde liegenden Tabellenblätter melden nur Werte mit **3 Monaten "
            "Wartezeit**. Die hier gezeigte Zeitreihe (Oktober 2024 – März 2026) liegt "
            "daher 3 Monate früher als der übrige Berichtszeitraum (Januar 2025 – Juni "
            "2026) und wird **nicht** vom Zeitraum-Filter der Sidebar beeinflusst."
        )

        st.markdown("#### Struktur der Bedarfsgemeinschaften: Größe und Typ")
        col_a, col_b = st.columns(2)
        with col_a:
            bg_groessen = ["BG 1 Person", "BG 2 Personen", "BG 3 Personen", "BG 4 Personen", "BG 5+ Personen"]
            fig = go.Figure()
            for spalte in bg_groessen:
                fig.add_trace(go.Scatter(
                    x=bezugsdauer.index, y=bezugsdauer[spalte], name=spalte,
                    mode="lines", stackgroup="groesse", line=dict(width=0.5),
                ))
            fig.update_layout(
                yaxis_title="Anzahl Bedarfsgemeinschaften", xaxis_title="Monat",
                hovermode="x unified", legend=dict(orientation="h", y=1.2), height=400,
            )
            st.plotly_chart(fig, width="stretch")
            st.caption("Nach Haushaltsgröße (gestapelt = Gesamtzahl BG).")
        with col_b:
            bg_typen = ["Single-BG", "Alleinerziehende-BG", "Partner-BG ohne Kinder", "Partner-BG mit Kindern"]
            fig = go.Figure()
            for spalte in bg_typen:
                fig.add_trace(go.Scatter(
                    x=bezugsdauer.index, y=bezugsdauer[spalte], name=spalte,
                    mode="lines+markers", marker=dict(size=5),
                ))
            fig.update_layout(
                yaxis_title="Anzahl Bedarfsgemeinschaften", xaxis_title="Monat",
                hovermode="x unified", legend=dict(orientation="h", y=1.2), height=400,
            )
            st.plotly_chart(fig, width="stretch")
            st.caption("Nach BG-Typ.")
        st.caption(
            "Single-Bedarfsgemeinschaften nehmen relativ zu (Anteil 57,0 % → 59,3 %), "
            "während Alleinerziehende- und Partner-BG zurückgehen — der SGB-II-Bezug "
            "wird zunehmend von Einpersonenhaushalten geprägt."
        )

        st.markdown("#### Langzeitleistungsbezug (LZB) vs. Langzeitarbeitslosigkeit (LZA)")
        with st.expander("Was ist der Unterschied zwischen LZB und LZA?"):
            st.markdown(
                "**Langzeitleistungsbeziehende (LZB)** sind erwerbsfähige "
                "Leistungsberechtigte, die in den vergangenen 24 Monaten mindestens "
                "21 Monate leistungsberechtigt waren. Das ist ein anderes Konzept als "
                "**Langzeitarbeitslose (LZA)**: Bürgergeld kann auch ohne "
                "Arbeitslosigkeit bezogen werden — z. B. bei Erwerbstätigkeit mit zu "
                "geringem Einkommen (siehe Tab „💼 Erwerbstätigkeit“)."
            )
        anteil_lzb = (bezugsdauer["LZB"] / bezugsdauer["ELB Insgesamt"] * 100).round(1)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=bezugsdauer.index, y=bezugsdauer["LZB"], name="LZB (absolut)", mode="lines+markers", line=dict(color="#2563eb"), marker=dict(size=5), yaxis="y1"))
        fig.add_trace(go.Scatter(x=bezugsdauer.index, y=anteil_lzb, name="Anteil LZB an allen ELB (%)", mode="lines+markers", line=dict(color="#f59e0b", dash="dot"), marker=dict(size=5), yaxis="y2"))
        fig.add_trace(go.Scatter(x=bezugsdauer.index, y=bezugsdauer["LZA (3.4)"], name="LZA (zum Vergleich)", mode="lines+markers", line=dict(color="#dc2626"), marker=dict(size=5), yaxis="y1"))
        fig.update_layout(
            yaxis=dict(title="Personen"),
            yaxis2=dict(title="Anteil LZB an ELB (%)", overlaying="y", side="right", ticksuffix="%"),
            xaxis_title="Monat", hovermode="x unified", legend=dict(orientation="h", y=1.15), height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Der LZB-Anteil steigt deutlich von 48,9 % auf 55,1 % — über die Hälfte "
            "aller ELB bezieht mittlerweile seit mindestens 21 der letzten 24 Monate "
            "Leistungen. Die (separat erfasste) Langzeitarbeitslosigkeit steigt im "
            "selben Zeitraum noch deutlicher — beide Kennzahlen zeigen unabhängig "
            "voneinander dieselbe Verfestigungstendenz."
        )

        st.markdown("#### Bewegungsdynamik: der „Drehtür-Effekt“")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=bezugsdauer.index, y=bezugsdauer["Anteil Zugang mit Vorbezug (%)"], name="Zugang mit Vorbezug (%)", mode="lines+markers", line=dict(color="#7c3aed"), marker=dict(size=5)))
        fig.add_trace(go.Scatter(x=bezugsdauer.index, y=bezugsdauer["Drehtür-Quote (%)"], name="Drehtür-Quote: erneuter Bezug binnen 3 Monaten (%)", mode="lines+markers", line=dict(color="#dc2626"), marker=dict(size=5)))
        fig.update_layout(
            yaxis_title="Prozent", yaxis_ticksuffix="%",
            xaxis_title="Monat", hovermode="x unified", legend=dict(orientation="h", y=1.15), height=420,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Der Anteil der Zugänge mit Vorbezug steigt deutlich (56,1 % → 73,4 %) — "
            "echte Erstzugänge werden seltener. Die Drehtür-Quote (Anteil der Abgänge, "
            "die binnen 3 Monaten zurückkehren) schwankt stark (Ø 25,6 %) ohne klaren "
            "Trend — im Schnitt kehrt etwa jede vierte Person innerhalb eines "
            "Vierteljahres zurück."
        )

# =================================================================================
# Tab 6: Finanzen (Zahlungsansprüche)
# =================================================================================
with tab_finanzen:
    st.subheader("Zahlungsansprüche in Euro")

    if finanzen is None or finanzen.empty:
        st.warning(
            "Keine Finanzdaten gefunden. Bitte zuerst `Notebooks/07_Finanzen.ipynb` "
            "einmal komplett ausführen, damit `Data/processed/finanzen_sgb2.csv` entsteht."
        )
    else:
        st.caption(
            "Die einzige Quelle für tatsächliche **Euro-Beträge** im gesamten Datensatz: "
            "Höhe und Struktur der Zahlungsansprüche für Bedarfsgemeinschaften (BG) nach "
            "SGB II — Regelbedarf, Kosten der Unterkunft, Sozialversicherungsbeiträge u. a."
        )
        st.info(
            "⚠️ Das Tabellenblatt „3.6 Zahlungsansprüche“ meldet nur Werte mit **3 Monaten "
            "Wartezeit**. Die hier gezeigte Zeitreihe (Oktober 2024 – März 2026) liegt "
            "daher 3 Monate früher als der übrige Berichtszeitraum (Januar 2025 – Juni "
            "2026) und wird **nicht** vom Zeitraum-Filter der Sidebar beeinflusst."
        )

        st.markdown("#### Gesamtvolumen der Zahlungsansprüche im Zeitverlauf")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=finanzen.index, y=finanzen["Insgesamt (Tsd. Euro)"], name="Insgesamt (Tsd. Euro)",
            mode="lines+markers", line=dict(color="#2563eb"), marker=dict(size=6), yaxis="y1",
        ))
        fig.add_trace(go.Scatter(
            x=finanzen.index, y=finanzen["Ø je BG insgesamt (Euro)"], name="Ø je BG (Euro)",
            mode="lines+markers", line=dict(color="#f59e0b", dash="dot"), marker=dict(size=6), yaxis="y2",
        ))
        fig.update_layout(
            yaxis=dict(title="Insgesamt (Tsd. Euro)"),
            yaxis2=dict(title="Ø je BG (Euro)", overlaying="y", side="right"),
            xaxis_title="Monat",
            hovermode="x unified",
            legend=dict(orientation="h", y=1.15),
            height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Das Gesamtvolumen ist über den Zeitraum praktisch stabil (3.451,5 → 3.473,0 "
            "Tsd. Euro), der Anspruch je Bedarfsgemeinschaft ist dagegen spürbar gestiegen "
            "(1.251 € → 1.288 €) — weil die Zahl der Bedarfsgemeinschaften sinkt, das "
            "Gesamtvolumen aber kaum."
        )

        st.markdown("#### Struktur der Zahlungsansprüche")
        leaf_spalten = ["Regelbedarf ELB", "Regelbedarf NEF", "Mehrbedarfe", "Kosten der Unterkunft", "Sozialversicherungsbeiträge", "weitere Zahlungsansprüche"]
        leaf_farben = {
            "Regelbedarf ELB": "#2563eb", "Regelbedarf NEF": "#7c3aed", "Mehrbedarfe": "#db2777",
            "Kosten der Unterkunft": "#f59e0b", "Sozialversicherungsbeiträge": "#16a34a", "weitere Zahlungsansprüche": "#6b7280",
        }
        fig = go.Figure()
        for spalte in leaf_spalten:
            fig.add_trace(go.Scatter(
                x=finanzen.index, y=finanzen[spalte], name=spalte,
                mode="lines", stackgroup="finanzen", line=dict(color=leaf_farben[spalte], width=0.5),
            ))
        fig.update_layout(
            yaxis_title="Tsd. Euro",
            xaxis_title="Monat",
            hovermode="x unified",
            legend=dict(orientation="h", y=1.15),
            height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Die sechs Posten sind überschneidungsfrei und summieren sich exakt zum "
            "Gesamtvolumen. **Regelbedarf ELB** (Grundsicherung für erwerbsfähige "
            "Leistungsberechtigte) ist mit rund 40 % der größte Posten, gefolgt von "
            "**Kosten der Unterkunft** (~36 %, Miete/Heizung). Auffälligster Trend: "
            "**Sozialversicherungsbeiträge** steigen deutlich (15,6 % → 18,3 % Anteil), "
            "während **Regelbedarf NEF** (v. a. Kinder in der Bedarfsgemeinschaft) sinkt "
            "(3,8 % → 2,8 %)."
        )

# =================================================================================
# Tab 7: Förderung (aktive Arbeitsmarktpolitik)
# =================================================================================
with tab_foerderung:
    st.subheader("Förderung der aktiven Arbeitsmarktpolitik")

    if foerderung is None or foerderung.empty:
        st.warning(
            "Keine Förderungs-Daten gefunden. Bitte zuerst "
            "`Notebooks/08_Foerderung.ipynb` einmal komplett ausführen, damit "
            "`Data/processed/foerderung_sgb2.csv` entsteht."
        )
    else:
        st.caption(
            "Maßnahmen zur Eingliederung in Arbeit (z. B. Weiterbildung, "
            "Vermittlungsbudget, Eingliederungszuschuss), die das Jobcenter finanziert. "
            "Die Förderstatistik zählt Förderfälle, nicht Personen — wer mehrere "
            "Leistungen gleichzeitig erhält, wird mehrfach gezählt."
        )
        st.info(
            "⚠️ Die Tabellenblätter „4.1 Förderung“ und „4.2 Förderung Strukturen“ melden "
            "nur Werte mit **3 Monaten Wartezeit**. Die hier gezeigte Zeitreihe (Oktober "
            "2024 – März 2026) liegt daher 3 Monate früher als der übrige "
            "Berichtszeitraum (Januar 2025 – Juni 2026) und wird **nicht** vom "
            "Zeitraum-Filter der Sidebar beeinflusst."
        )

        st.markdown("#### Eintritte und Bestand an Fördermaßnahmen")
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=foerderung.index, y=foerderung["Eintritte (Summe)"], name="Eintritte (im Monat)",
            marker_color="#f59e0b", yaxis="y1",
        ))
        fig.add_trace(go.Scatter(
            x=foerderung.index, y=foerderung["Bestand (Summe)"], name="Bestand (im Monat)",
            mode="lines+markers", line=dict(color="#2563eb"), marker=dict(size=6), yaxis="y2",
        ))
        fig.update_layout(
            yaxis=dict(title="Eintritte im Monat"),
            yaxis2=dict(title="Bestand im Monat", overlaying="y", side="right"),
            xaxis_title="Monat",
            hovermode="x unified",
            legend=dict(orientation="h", y=1.15),
            height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Eintritte = neu begonnene Förderfälle im Monat. Bestand = Personen, die "
            "aktuell an einer Maßnahme teilnehmen. Der Bestand stieg bis zu einem "
            "Höchststand von 313 im April 2025 und ist seither wieder gesunken."
        )

        st.markdown("#### Aktivierungsquote im Zeitverlauf")
        with st.expander("Was bedeuten AQ1 und AQ2a?"):
            st.markdown(
                "Die **Aktivierungsquote** ist eine von der Bundesagentur direkt "
                "mitgelieferte, bestandsorientierte Kennzahl — der Anteil aktivierter "
                "(in Fördermaßnahmen befindlicher) Personen an:\n"
                "- **AQ1**: allen Teilnehmenden plus Arbeitslosen,\n"
                "- **AQ2a**: allen erwerbsfähigen Leistungsberechtigten (ELB)."
            )
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=foerderung.index, y=foerderung["AQ1 (%)"], name="AQ1", mode="lines+markers", line=dict(color="#2563eb"), marker=dict(size=5)))
        fig.add_trace(go.Scatter(x=foerderung.index, y=foerderung["AQ1 12M-Durchschnitt (%)"], name="AQ1 (12M-Ø)", mode="lines", line=dict(color="#2563eb", dash="dot")))
        fig.add_trace(go.Scatter(x=foerderung.index, y=foerderung["AQ2a (%)"], name="AQ2a", mode="lines+markers", line=dict(color="#7c3aed"), marker=dict(size=5)))
        fig.add_trace(go.Scatter(x=foerderung.index, y=foerderung["AQ2a 12M-Durchschnitt (%)"], name="AQ2a (12M-Ø)", mode="lines", line=dict(color="#7c3aed", dash="dot")))
        fig.update_layout(
            yaxis_title="Prozent", yaxis_ticksuffix="%",
            xaxis_title="Monat",
            hovermode="x unified",
            legend=dict(orientation="h", y=1.15),
            height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Beide Quoten sind in den Rohwerten rückläufig (AQ1: 13,3 % → 9,9 %; AQ2a: "
            "6,0 % → 5,5 %) — nur ein kleiner Teil der SGB-II-Grundgesamtheit nimmt "
            "aktuell an einer Fördermaßnahme teil."
        )

        st.markdown("#### Struktur des Bestands: Geschlecht und Vorgeschichte")
        anteil_frauen = (foerderung["Bestand Frauen"] / foerderung["Bestand (Summe)"] * 100).round(1)
        anteil_lza = (foerderung["Bestand vor Eintritt LZA"] / foerderung["Bestand (Summe)"] * 100).round(1)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=foerderung.index, y=anteil_frauen, name="Anteil Frauen am Bestand (%)", mode="lines+markers", line=dict(color="#db2777"), marker=dict(size=5)))
        fig.add_trace(go.Scatter(x=foerderung.index, y=anteil_lza, name="Anteil vor Eintritt langzeitarbeitslos (%)", mode="lines+markers", line=dict(color="#dc2626"), marker=dict(size=5)))
        fig.update_layout(
            yaxis_title="Prozent", yaxis_ticksuffix="%",
            xaxis_title="Monat",
            hovermode="x unified",
            legend=dict(orientation="h", y=1.15),
            height=420,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Der Frauenanteil bleibt stabil bei rund 44 %. Auffälliger: Der Anteil "
            "zuvor langzeitarbeitsloser Teilnehmender steigt deutlich (16,2 % → 23,6 %) "
            "— passend zur insgesamt steigenden Langzeitarbeitslosigkeit im Datensatz "
            "(siehe Tab „SGB II Übersicht“)."
        )

# =================================================================================
# Tab: Arbeitsstellen (Nachfrageseite)
# =================================================================================
with tab_arbeitsstellen:
    st.subheader("Gemeldete Arbeitsstellen — die Nachfrageseite des Arbeitsmarkts")

    if arbeitsstellen_view is None or arbeitsstellen_view.empty:
        st.warning(
            "Keine Arbeitsstellen-Daten gefunden. Bitte zuerst "
            "`Notebooks/11_Arbeitsstellen.ipynb` einmal komplett ausführen, damit "
            "`Data/processed/arbeitsstellen.csv` entsteht."
        )
    else:
        st.caption(
            "Alle übrigen Tabs zeigen ausschließlich die **Angebotsseite** (Arbeitslose). "
            "Dieser Tab ergänzt die **Nachfrageseite**: gemeldete offene Arbeitsstellen. "
            "⚠️ Diese Zahlen werden von der Bundesagentur **nicht nach Rechtskreis** "
            "differenziert ausgewiesen — nur ein „Insgesamt“-Wert, kein eigener SGB-II-Wert."
        )

        st.markdown("#### Zugang und Bestand gemeldeter Arbeitsstellen")
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=arbeitsstellen_view.index, y=arbeitsstellen_view["zugang_im_monat"],
            name="Zugang (im Monat)", marker_color="#93c5fd", opacity=0.75,
        ))
        fig.add_trace(go.Scatter(
            x=arbeitsstellen_view.index, y=arbeitsstellen_view["bestand"],
            name="Bestand (Monatsende)", mode="lines+markers", line=dict(color="#dc2626", width=2.5),
        ))
        fig.update_layout(
            yaxis_title="Anzahl", xaxis_title="Monat", hovermode="x unified",
            legend=dict(orientation="h", y=1.15), height=420,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Der Bestand gemeldeter Arbeitsstellen sinkt über den Beobachtungszeitraum "
            "deutlich von 1.571 auf 1.192 Stellen (≈ −24 %) — ein zusätzliches, von den "
            "Arbeitslosenzahlen unabhängiges Signal für eine sich eintrübende "
            "Arbeitsmarktlage."
        )

        st.markdown("#### Angebot vs. Nachfrage: Arbeitsstellen je 100 Arbeitslose")
        angebot_nachfrage = arbeitsstellen_view[["bestand"]].rename(
            columns={"bestand": "arbeitsstellen_bestand"}
        ).merge(view[["Arbeitslose (Bestand)"]], left_index=True, right_index=True, how="inner")
        angebot_nachfrage["ratio"] = (
            angebot_nachfrage["arbeitsstellen_bestand"] / angebot_nachfrage["Arbeitslose (Bestand)"] * 100
        )
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=angebot_nachfrage.index, y=angebot_nachfrage["ratio"],
            mode="lines+markers", line=dict(color="#059669", width=2.5), name="Arbeitsstellen je 100 Arbeitslose",
        ))
        fig.add_hline(y=100, line_dash="dot", line_color="#9ca3af", annotation_text="Gleichstand (100)")
        fig.update_layout(
            yaxis_title="Arbeitsstellen je 100 Arbeitslose", xaxis_title="Monat",
            hovermode="x unified", height=420,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Zu Jahresbeginn 2025 kamen auf 100 Arbeitslose noch rund 107 gemeldete "
            "Stellen — mehr offene Stellen als Arbeitslose. Bis Juni 2026 fällt diese "
            "Relation auf rund 80 und damit deutlich unter 100."
        )

        st.markdown(f"#### Struktur des Stellenbestands — {pd.Timestamp(gewaehlter_monat):%B %Y}")
        if gewaehlter_monat in arbeitsstellen.index:
            bestand_gesamt = arbeitsstellen.loc[gewaehlter_monat, "bestand"]
            bestand_svp = arbeitsstellen.loc[gewaehlter_monat, "bestand_sozialversicherungspflichtig"]
            fig = go.Figure(go.Pie(
                labels=["sozialversicherungspflichtig", "sonstige Beschäftigungsform"],
                values=[bestand_svp, bestand_gesamt - bestand_svp],
                hole=0.55, marker=dict(colors=["#2563eb", "#cbd5e1"]),
            ))
            fig.update_layout(height=380)
            st.plotly_chart(fig, width="stretch")
            st.caption(
                f"{bestand_svp / bestand_gesamt * 100:.1f} % des Stellenbestands im gewählten "
                "Berichtsmonat sind sozialversicherungspflichtig — der weit überwiegende Teil."
            )
        else:
            st.info("Für den gewählten Berichtsmonat liegen keine Arbeitsstellen-Daten vor.")

# =================================================================================
# Tab: Unterbeschäftigung
# =================================================================================
with tab_unterbeschaeftigung:
    st.subheader("Unterbeschäftigung — mehr als nur Arbeitslosigkeit")

    if unterbeschaeftigung_view is None or unterbeschaeftigung_view.empty:
        st.warning(
            "Keine Unterbeschäftigungs-Daten gefunden. Bitte zuerst "
            "`Notebooks/12_Unterbeschaeftigung.ipynb` einmal komplett ausführen, damit "
            "`Data/processed/unterbeschaeftigung_sgb2.csv` entsteht."
        )
    else:
        st.caption(
            "Die Unterbeschäftigungsquote (Tab „📊 SGB II Übersicht“) beruht auf drei "
            "absoluten Kennzahlen, die hier erstmals als eigene Zeitreihe gezeigt werden — "
            "alle bereits mit vollständigem SGB-II-Wert (anders als bei den gemeldeten "
            "Arbeitsstellen)."
        )

        st.markdown("#### Drei Abgrenzungen im Vergleich (SGB II)")
        fig = go.Figure()
        farben = {
            "arbeitslosigkeit_weiterer_sinn": ("Arbeitslosigkeit im weiteren Sinne", "#2563eb"),
            "unterbeschaeftigung_engerer_sinn": ("Unterbeschäftigung im engeren Sinne", "#7c3aed"),
            "unterbeschaeftigung_ohne_kurzarbeit": ("Unterbeschäftigung (ohne Kurzarbeit)", "#dc2626"),
        }
        for spalte, (label, farbe) in farben.items():
            fig.add_trace(go.Scatter(
                x=unterbeschaeftigung_view.index, y=unterbeschaeftigung_view[spalte], name=label,
                mode="lines+markers", line=dict(color=farbe, width=2), marker=dict(size=5),
            ))
        fig.update_layout(
            yaxis_title="Personen", xaxis_title="Monat", hovermode="x unified",
            legend=dict(orientation="h", y=1.15), height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Die Kurzarbeiter-Komponente (Differenz zwischen den beiden oberen Linien) ist "
            "verschwindend gering (Ø 2,6 Personen) — Kurzarbeit spielt im SGB-II-Kontext "
            "praktisch keine Rolle. Die Maßnahmen-Komponente (Differenz zur Arbeitslosigkeit "
            "im weiteren Sinne) ist mit Ø 399 Personen deutlich substanzieller."
        )

        st.markdown("#### SGB-II-Anteil im Vergleich")
        anteil = (
            unterbeschaeftigung_view["unterbeschaeftigung_engerer_sinn"]
            / unterbeschaeftigung_view["unterbeschaeftigung_engerer_sinn_insgesamt"] * 100
        )
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=unterbeschaeftigung_view.index, y=anteil, mode="lines+markers",
            name="SGB-II-Anteil: Unterbeschäftigung (engere Sinne)", line=dict(color="#059669", width=2.5),
        ))
        fig.add_hline(y=39.8, line_dash="dot", line_color="#2563eb", annotation_text="Ø Anteil am Bestand (≈ 39,8 %)")
        fig.add_hline(y=72.3, line_dash="dot", line_color="#dc2626", annotation_text="Ø Anteil an LZA (≈ 72,3 %)")
        fig.update_layout(
            yaxis_title="Anteil (%)", yaxis_ticksuffix="%", xaxis_title="Monat", height=420,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Der SGB-II-Anteil an der Unterbeschäftigung im engeren Sinne (41–50 %) liegt "
            "zwischen dem Anteil am Arbeitslosenbestand (≈ 40 %) und dem deutlich höheren "
            "Anteil an der Langzeitarbeitslosigkeit (≈ 72 %, siehe Tab „⚖️ SGB II vs. SGB "
            "III“)."
        )

# =================================================================================
# Tab: RLB/ELB/NEF-Struktur
# =================================================================================
with tab_rlb_elb_nef:
    st.subheader("Regelleistungsberechtigte: Struktur der Bedarfsgemeinschaften")

    if rlb_elb_nef_view is None or rlb_elb_nef_view.empty:
        st.warning(
            "Keine RLB/ELB/NEF-Daten gefunden. Bitte zuerst "
            "`Notebooks/13_RLB_ELB_NEF.ipynb` einmal komplett ausführen, damit "
            "`Data/processed/rlb_elb_nef_sgb2.csv` entsteht."
        )
    else:
        st.caption(
            "Die Trichter-Grafik im Tab „📊 SGB II Übersicht“ zeigt RLB/ELB/NEF nur als "
            "Momentaufnahme des letzten Berichtsmonats. Dieser Tab zeigt dieselbe Struktur "
            "als Zeitreihe über alle 18 Monate."
        )

        st.markdown("#### RLB, ELB und NEF im Vergleich")
        fig = go.Figure()
        for spalte, name, farbe in [
            ("rlb", "Regelleistungsberechtigte (RLB)", "#1e3a8a"),
            ("elb", "davon erwerbsfähig (ELB)", "#2563eb"),
            ("nef", "nicht erwerbsfähig (NEF)", "#dc2626"),
        ]:
            fig.add_trace(go.Scatter(
                x=rlb_elb_nef_view.index, y=rlb_elb_nef_view[spalte], name=name,
                mode="lines+markers", line=dict(width=2.5), marker=dict(size=5),
            ))
        fig.update_layout(
            yaxis_title="Personen", xaxis_title="Monat", hovermode="x unified",
            legend=dict(orientation="h", y=1.15), height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Alle drei Kennzahlen sind rückläufig — RLB um 6,9 %, ELB um 5,5 %, NEF (im "
            "Wesentlichen Kinder in der Bedarfsgemeinschaft) mit 10,5 % am stärksten."
        )

        st.markdown("#### Nicht leistungsberechtigte Haushaltsmitglieder (PERS − RLB)")
        differenz = rlb_elb_nef_view["pers"] - rlb_elb_nef_view["rlb"]
        differenz_anteil = (differenz / rlb_elb_nef_view["pers"] * 100)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=rlb_elb_nef_view.index, y=differenz, name="PERS − RLB",
            marker_color="#f59e0b", opacity=0.75,
        ))
        fig.add_trace(go.Scatter(
            x=rlb_elb_nef_view.index, y=differenz_anteil, name="Anteil an PERS (%)",
            mode="lines+markers", line=dict(color="#b45309", width=2.5), yaxis="y2",
        ))
        fig.update_layout(
            yaxis=dict(title="Personen"),
            yaxis2=dict(title="Anteil an PERS (%)", overlaying="y", side="right", ticksuffix="%"),
            xaxis_title="Monat", hovermode="x unified", legend=dict(orientation="h", y=1.15), height=440,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Gegenläufiger Trend: Während Bedarfsgemeinschaften, Personen in BG und RLB "
            "insgesamt sinken, steigt die Zahl der nicht leistungsberechtigten "
            "Haushaltsmitglieder von 286 auf 309 Personen — ihr Anteil an allen Personen in "
            "BG von 5,2 % auf 6,0 %."
        )

# =================================================================================
# Tab: Beschäftigung (sozialversicherungspflichtig/geringfügig, Pendlersaldo)
# =================================================================================
with tab_beschaeftigung:
    st.subheader("Beschäftigung: das Gegenstück zur Arbeitslosigkeit")

    if beschaeftigung is None or beschaeftigung.empty:
        st.warning(
            "Keine Beschäftigungsdaten gefunden. Bitte zuerst "
            "`Notebooks/14_Beschaeftigung.ipynb` einmal komplett ausführen, damit "
            "`Data/processed/beschaeftigung_quartal.csv` entsteht."
        )
    else:
        st.caption(
            "⚠️ Dieser Tab hat ein eigenes Zeitfenster und reagiert **nicht** auf den "
            "Sidebar-Zeitraum-Filter: Die zugrunde liegenden Daten sind **quartalsweise** "
            "(nicht monatlich) mit 6 Monaten Wartezeit gemeldet und decken daher Juni 2024 – "
            "Dezember 2025 ab, statt Januar 2025 – Juni 2026 wie die übrigen Tabs."
        )

        st.markdown("#### Sozialversicherungspflichtige Beschäftigung: Arbeitsort vs. Wohnort")
        with st.expander("Was bedeutet Arbeitsort (AO) vs. Wohnort (WO)?"):
            st.markdown(
                "**Arbeitsort (AO)** zählt Beschäftigungsverhältnisse, deren Arbeitsplatz in "
                "Regensburg liegt. **Wohnort (WO)** zählt Personen, die in Regensburg wohnen, "
                "unabhängig vom Arbeitsort. Die Differenz WO − AO ist der **Pendlersaldo**."
            )
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=beschaeftigung.index, y=beschaeftigung["ao_svp"], name="Arbeitsort (AO)",
            mode="lines+markers", line=dict(color="#2563eb", width=2.5), marker=dict(size=7),
        ))
        fig.add_trace(go.Scatter(
            x=beschaeftigung.index, y=beschaeftigung["wo_svp"], name="Wohnort (WO)",
            mode="lines+markers", line=dict(color="#7c3aed", width=2.5), marker=dict(size=7),
        ))
        fig.update_layout(
            yaxis_title="Personen", xaxis_title="Quartal", hovermode="x unified",
            legend=dict(orientation="h", y=1.15), height=440,
        )
        st.plotly_chart(fig, width="stretch")

        st.markdown("#### Pendlersaldo (WO − AO)")
        pendlersaldo = beschaeftigung["wo_svp"] - beschaeftigung["ao_svp"]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=beschaeftigung.index, y=pendlersaldo, marker_color="#059669", opacity=0.8,
        ))
        fig.update_layout(
            yaxis_title="Personen", xaxis_title="Quartal", height=400, showlegend=False,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Außergewöhnlich stabiler Auspendlerüberschuss von 33.739 bis 34.069 Personen "
            "(Ø ≈ 33.929) über alle 7 verfügbaren Quartale — es pendeln durchgehend rund "
            "34.000 mehr Regensburger aus, als von auswärts einpendeln."
        )

        st.markdown("#### Anteil geringfügiger Beschäftigung an der Gesamtbeschäftigung")
        anteil_ao = beschaeftigung["ao_geringfuegig"] / (beschaeftigung["ao_geringfuegig"] + beschaeftigung["ao_svp"]) * 100
        anteil_wo = beschaeftigung["wo_geringfuegig"] / (beschaeftigung["wo_geringfuegig"] + beschaeftigung["wo_svp"]) * 100
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=beschaeftigung.index, y=anteil_ao, name="Arbeitsort (AO)", mode="lines+markers", line=dict(color="#f59e0b", width=2.5)))
        fig.add_trace(go.Scatter(x=beschaeftigung.index, y=anteil_wo, name="Wohnort (WO)", mode="lines+markers", line=dict(color="#db2777", width=2.5)))
        fig.update_layout(
            yaxis_title="Anteil (%)", yaxis_ticksuffix="%", xaxis_title="Quartal",
            hovermode="x unified", legend=dict(orientation="h", y=1.15), height=420,
        )
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "Der Anteil geringfügiger Beschäftigung sinkt leicht (AO: 13,3 % → 13,0 %, WO: "
            "10,8 % → 10,5 %) — passend zur in Tab „💼 Erwerbstätigkeit“ beobachteten "
            "leichten Verschiebung zu höheren Einkommen bei den Aufstockern."
        )

# =================================================================================
# Tab 8: Glossar
# =================================================================================
with tab_glossar:
    st.subheader("Glossar: Begriffe rund um SGB II und Bürgergeld")
    st.caption(
        "Alle Fachbegriffe, die in diesem Dashboard verwendet werden, an einem Ort erklärt — "
        "nach Themen gruppiert."
    )

    with st.expander("Grundbegriffe", expanded=True):
        st.markdown(
            "- **SGB II** (Zweites Buch Sozialgesetzbuch): regelt die *Grundsicherung für "
            "Arbeitsuchende*, umgangssprachlich „Bürgergeld“ (bis 2022: „Hartz IV“). Wird von "
            "den **Jobcentern** verwaltet.\n"
            "- **SGB III**: regelt die *Arbeitslosenversicherung* (u. a. Arbeitslosengeld I). "
            "Zuständig ist die **Agentur für Arbeit**, nicht das Jobcenter.\n"
            "- **Rechtskreis**: gibt an, ob eine Person dem SGB II (Jobcenter) oder SGB III "
            "(Agentur für Arbeit) zugeordnet ist. Alle Kennzahlen in diesem Dashboard "
            "beziehen sich — sofern nicht anders angegeben — ausschließlich auf den "
            "**Rechtskreis SGB II** (Ausnahme: Tab „⚖️ SGB II vs. SGB III“, der beide "
            "Rechtskreise vergleicht).\n"
            "- **Arbeitslosengeld I (ALG I)**: Versicherungsleistung nach SGB III, "
            "zeitlich befristet (i. d. R. 12–24 Monate), Voraussetzung ist eine "
            "vorherige sozialversicherungspflichtige Beschäftigung. Abzugrenzen vom "
            "Bürgergeld (SGB II), das bedürftigkeitsabhängig und zeitlich "
            "unbefristet ist.\n"
            "- **Bürgergeld**: umgangssprachlicher Name für die Geldleistung nach SGB II.\n"
            "- **Jobcenter**: die Behörde, die SGB-II-Leistungen verwaltet und in "
            "Arbeit vermittelt — hier: Jobcenter Regensburg."
        )

    with st.expander("Personengruppen im SGB II", expanded=True):
        st.markdown(
            "- **Arbeitslose (Bestand)**: Personen, die zum Stichtag als arbeitslos gemeldet "
            "sind (SGB II).\n"
            "- **Langzeitarbeitslose (LZA)**: Personen, die seit mindestens einem Jahr "
            "ununterbrochen arbeitslos gemeldet sind.\n"
            "- **Bedarfsgemeinschaft (BG)**: der Haushalt bzw. die Personengruppe, die "
            "gemeinsam wirtschaftet und gemeinsam Bürgergeld beantragt (z. B. eine Familie).\n"
            "- **Personen in BG**: alle Mitglieder einer Bedarfsgemeinschaft, inkl. Kinder "
            "und nicht erwerbsfähiger Angehöriger — daher immer größer als die Zahl der "
            "Arbeitslosen.\n"
            "- **Regelleistungsberechtigte (RLB)**: alle laufend anspruchsberechtigten "
            "Personen innerhalb einer BG (Teilmenge von „Personen in BG“).\n"
            "- **Erwerbsfähige Leistungsberechtigte (ELB)**: RLB, die erwerbsfähig sind "
            "(15 bis 65 Jahre, gesundheitlich arbeitsfähig) — die Kernzielgruppe der "
            "Arbeitsvermittlung.\n"
            "- **Nicht erwerbsfähige Leistungsberechtigte (NEF)**: RLB, die nicht "
            "erwerbsfähig sind — vor allem Kinder unter 15 Jahren und dauerhaft "
            "erwerbsunfähige Angehörige.\n"
            "- **Erwerbstätige ELB / „Aufstocker“**: ELB, die zusätzlich zum Bürgergeld "
            "eigenes Einkommen aus abhängiger oder selbständiger Erwerbstätigkeit haben.\n"
            "- **Langzeitleistungsbeziehende (LZB)**: ELB, die in den vergangenen "
            "24 Monaten mindestens 21 Monate leistungsberechtigt waren — ein anderes "
            "Konzept als Langzeitarbeitslose (LZA), da Bürgergeld auch ohne "
            "Arbeitslosigkeit bezogen werden kann.\n"
            "- **Drehtür-Effekt**: wenn Personen den Leistungsbezug verlassen und kurz "
            "danach (in diesem Dashboard: binnen 3 Monaten) erneut Leistungen beziehen."
        )

    with st.expander("Kennzahlen (Quoten)"):
        st.markdown(
            "- **Arbeitslosenquote**: Anteil der Arbeitslosen (SGB II) an allen zivilen "
            "Erwerbspersonen Regensburgs (Beschäftigte + Arbeitslose).\n"
            "- **Unterbeschäftigungsquote**: wie die Arbeitslosenquote, aber mit einer "
            "breiteren Bezugsgröße, die zusätzlich Personen in arbeitsmarktpolitischen "
            "Maßnahmen einschließt — deshalb meist etwas höher.\n"
            "- **Aufstockerquote**: Anteil der erwerbstätigen ELB an allen ELB. Nicht "
            "direkt in den Rohdaten enthalten, sondern im Dashboard selbst berechnet "
            "(erwerbstätige ELB ÷ Insgesamt ELB).\n"
            "- **Netto-Fluktuation**: Zugang minus Abgang aus Arbeitslosigkeit in einem "
            "Monat — positiv bedeutet mehr Zugänge als Abgänge."
        )

    with st.expander("Einkommen der Aufstocker"):
        st.markdown(
            "- **Geringfügigkeitsgrenze**: Verdienstgrenze für einen Minijob, aktuell "
            "603 € brutto im Monat.\n"
            "- **Übergangsbereich** (auch „Midi-Job“-Bereich): Einkommensspanne oberhalb der "
            "Geringfügigkeitsgrenze bis 2.000 € brutto, mit reduzierten "
            "Sozialversicherungsbeiträgen."
        )

    with st.expander("Zahlungsansprüche (Finanzen)"):
        st.markdown(
            "- **Regelbedarf**: der monatliche Grundbetrag zur Sicherung des "
            "Existenzminimums (§ 20 SGB II für erwerbsfähige, § 23 SGB II für nicht "
            "erwerbsfähige Leistungsberechtigte) — deckt u. a. Ernährung, Kleidung, "
            "Haushaltsenergie.\n"
            "- **Kosten der Unterkunft (KdU)**: Zahlungsanspruch für Miete und Heizung "
            "(§ 22 SGB II).\n"
            "- **Mehrbedarfe**: zusätzliche Zahlungsansprüche für besondere Lebenslagen "
            "(§ 21 SGB II), z. B. bei Schwangerschaft, Alleinerziehung oder Behinderung.\n"
            "- **Zahlungsanspruch**: die Summe aus Regelbedarf, Mehrbedarfen, KdU und "
            "ggf. weiteren Leistungen, auf die eine Bedarfsgemeinschaft laut Berechnung "
            "Anspruch hat — nicht zwingend identisch mit dem tatsächlich ausgezahlten "
            "Betrag (z. B. bei anzurechnendem Einkommen)."
        )

    with st.expander("Förderung (aktive Arbeitsmarktpolitik)"):
        st.markdown(
            "- **Fördermaßnahmen / Instrumente**: vom Jobcenter finanzierte Maßnahmen zur "
            "Eingliederung in Arbeit, z. B. Weiterbildung, Vermittlungsbudget, "
            "Eingliederungszuschuss.\n"
            "- **Eintritte**: neu begonnene Förderfälle in einem Monat (Zugang).\n"
            "- **Bestand**: Personen, die aktuell an einer Maßnahme teilnehmen (Stichtag).\n"
            "- **Aktivierungsquote**: bestandsorientierte Kennzahl der Bundesagentur — "
            "**AQ1** = Anteil aktivierter Personen an allen Teilnehmenden plus "
            "Arbeitslosen, **AQ2a** = Anteil an allen erwerbsfähigen "
            "Leistungsberechtigten (ELB).\n"
            "- **„*“ in den Rohdaten**: Anonymisierungs-Symbol für kleine Fallzahlen "
            "(< 3 Personen) — aus Datenschutzgründen nicht ausgewiesen."
        )

    with st.expander("Datenbesonderheiten"):
        st.markdown(
            "- **Wartezeit (3 bzw. 6 Monate)**: Einige Tabellenblätter der Rohdaten (u. a. "
            "„3.3 Erwerbstätigkeit“) melden nicht den aktuellen Berichtsmonat, sondern "
            "Werte mit 3 bzw. 6 Monaten Verzögerung — die Daten müssen von der "
            "Bundesagentur erst noch vervollständigt werden, bevor sie veröffentlicht "
            "werden.\n"
            "- **Statistik-Nr. t73906-0**: die eindeutige Kennung der Bundesagentur für "
            "Arbeit für den Bericht „Eckwerte für Jobcenter“, Jobcenter Regensburg."
        )

    st.caption(
        "Quelle für alle Definitionen: Statistik der Bundesagentur für Arbeit "
        "(methodische Hinweise zum Bericht „Eckwerte für Jobcenter“)."
    )
