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

# --- Übersicht: Kennzahlen im Vergleich (kombinierter Chart) -------------------
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

# --- Weitere Zeitreihen-Charts --------------------------------------------------
st.subheader("Arbeitslosen- und Unterbeschäftigungsquote")

fig = go.Figure()
fig.add_trace(go.Scatter(x=view.index, y=view["Arbeitslosenquote (%)"], mode="lines+markers", name="Arbeitslosenquote"))
fig.add_trace(go.Scatter(x=view.index, y=view["Unterbeschäftigungsquote (%)"], mode="lines+markers", name="Unterbeschäftigungsquote"))
fig.update_layout(
    title="Arbeitslosen- vs. Unterbeschäftigungsquote",
    yaxis_title="Prozent",
    xaxis_title="Monat",
    legend=dict(orientation="h", y=1.1),
    height=420,
)
st.plotly_chart(fig, width="stretch")
st.caption(
    "Arbeitslosenquote: SGB-II-Anteil bezogen auf alle zivilen Erwerbspersonen Regensburgs. "
    "Die Unterbeschäftigungsquote zählt zusätzlich z. B. Personen in arbeitsmarktpolitischen "
    "Maßnahmen mit und liegt deshalb meist etwas höher."
)

st.subheader("Langzeitarbeitslosigkeit")

anteil = (view["Langzeitarbeitslose"] / view["Arbeitslose (Bestand)"] * 100).round(1)
fig = px.line(x=view.index, y=anteil, markers=True)
fig.update_layout(
    title="Anteil Langzeitarbeitslose an allen Arbeitslosen (SGB II)",
    yaxis_title="Prozent",
    xaxis_title="Monat",
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
indexiert = view[vergleich_spalten] / view[vergleich_spalten].iloc[0] * 100

fig = go.Figure()
for spalte in vergleich_spalten:
    fig.add_trace(go.Scatter(x=indexiert.index, y=indexiert[spalte], mode="lines+markers", name=spalte))
fig.add_hline(y=100, line_dash="dash", line_color="grey")
fig.update_layout(
    title=f"Kennzahlen im Vergleich (indexiert, {indexiert.index[0]:%b %Y} = 100)",
    yaxis_title="Index (Startmonat = 100)",
    xaxis_title="Monat",
    legend=dict(orientation="h", y=1.1),
    height=420,
)
st.plotly_chart(fig, width="stretch")
st.caption(
    "Die vier Kernkennzahlen haben sehr unterschiedliche Größenordnungen (500 bis 5.000+ "
    "Personen) und werden hier auf den ersten Monat im gewählten Zeitraum indexiert (= 100 "
    "gesetzt), damit ihre relative Entwicklung in einem Diagramm vergleichbar ist."
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
funnel_werte = [letzter[s] for s in funnel_stufen]

fig = go.Figure(go.Funnel(y=funnel_labels, x=funnel_werte, textinfo="value+percent initial"))
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

# --- Altersstruktur & Geschlecht (Momentaufnahme) -----------------------------
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
    st.dataframe(view, width="stretch")
