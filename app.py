import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Análisis de México",
    page_icon="📊",
    layout="wide"
)

st.title("Análisis económico, demográfico y empresarial de México")

st.write(
    "Comparación de las 32 entidades federativas "
    "mediante indicadores de población, PIB y establecimientos."
)

@st.cache_data
def cargar_datos():
    df = pd.read_csv("indicadores_estatales_clusters.csv")
    return df

df = cargar_datos()

st.subheader("Datos de las entidades federativas")
st.dataframe(df)

st.divider()

st.subheader("Indicadores por entidad federativa")

estado_seleccionado = st.selectbox(
    "Selecciona un estado:",
    sorted(df["estado"].unique())
)

datos_estado = df.loc[
    df["estado"] == estado_seleccionado
].iloc[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Población (2025)",
        f"{datos_estado['poblacion_total']:,.0f}"
    )

with col2:
    st.metric(
        "Establecimientos económicos",
        f"{datos_estado['Numero_establecimientos']:,.0f}"
    )

with col3:
    st.metric(
        "PIB 2024 (millones MXN)",
        f"${datos_estado['pib_2024_millones_mxn']:,.2f}"
    )
    
st.divider()

st.subheader("Top 10 entidades por PIB (2024)")

top_pib = df.nlargest(
    10,
    "pib_2024_millones_mxn"
)

st.bar_chart(
    top_pib,
    x="estado",
    y="pib_2024_millones_mxn",
    x_label="Entidad federativa",
    y_label="PIB (millones de pesos)"
)

st.divider()

st.subheader("Segmentación de estados mediante K-Means")

st.write(
    "Los estados fueron agrupados en tres clústeres "
    "según su población, número de establecimientos y PIB."
)

col1, col2 = st.columns(2)

with col1:
    st.write("Cantidad de estados por clúster")

    conteo_clusters = df["cluster"].value_counts().sort_index()

    st.bar_chart(conteo_clusters)

with col2:
    st.write("Estados pertenecientes a cada clúster")

    cluster_seleccionado = st.selectbox(
        "Selecciona un clúster:",
        sorted(df["cluster"].unique())
    )

    estados_cluster = df.loc[
        df["cluster"] == cluster_seleccionado,
        ["estado", "cluster"]
    ]

    st.dataframe(estados_cluster, hide_index=True)
    
st.divider()

st.subheader("Relación entre PIB y establecimientos económicos")

st.write(
    "Cada punto representa una entidad federativa. "
    "Los colores identifican los clústeres obtenidos con K-Means."
)

import plotly.express as px

fig = px.scatter(
    df,
    x="Numero_establecimientos",
    y="pib_2024_millones_mxn",
    color="cluster",
    hover_name="estado",
    size="poblacion_total",
    labels={
        "Numero_establecimientos": "Número de establecimientos",
        "pib_2024_millones_mxn": "PIB 2024 (millones de pesos)",
        "cluster": "Clúster"
    },
    title="Distribución económica de las entidades federativas"
)

st.plotly_chart(fig, use_container_width=True)