import pandas as pd
import streamlit as st

from src.analisis import limpiar_datos, obtener_estadisticas
from src.config import CSV_SCRAPER_PATH
from src.pdf_report import generar_pdf_informe
from src.scraper import ejecutar_scraper


st.set_page_config(
    page_title="Analizador de Datos con Scraper",
    page_icon="📊",
    layout="wide"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3 {
        color: #1e3a8a;
    }

    .stButton > button {
        background-color: #4f46e5;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.6rem 1.2rem;
        font-weight: bold;
    }

    .stDownloadButton > button {
        background-color: #059669;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.6rem 1.2rem;
        font-weight: bold;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        opacity: 0.9;
    }

    .custom-box {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style='text-align: center;'>📊 Analizador de Datos con Scraper</h1>
    <p style='text-align: center; font-size: 18px; color: #555;'>
        Sube un archivo CSV, un Excel o ejecuta el scraper para analizar productos de forma sencilla
    </p>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("⚙️ Opciones")
st.sidebar.write("Selecciona cómo quieres cargar y analizar los datos")

opcion = st.sidebar.radio(
    "Fuente de datos",
    ["CSV", "Excel", "Scraper"]
)

df = None
nombre_origen = ""

if opcion == "CSV":
    archivo = st.file_uploader("📂 Sube un archivo CSV", type=["csv"])
    if archivo is not None:
        try:
            df = pd.read_csv(archivo)
            nombre_origen = archivo.name
            st.success("CSV cargado correctamente")
        except Exception as e:
            st.error(f"Error al leer el CSV: {e}")

elif opcion == "Excel":
    archivo = st.file_uploader("📂 Sube un archivo Excel", type=["xlsx", "xls"])
    if archivo is not None:
        try:
            df = pd.read_excel(archivo)
            nombre_origen = archivo.name
            st.success("Excel cargado correctamente")
        except Exception as e:
            st.error(f"Error al leer el Excel: {e}")

elif opcion == "Scraper":
    st.markdown(
        """
        <div class="custom-box">
            <h3>🌐 Ejecutar scraper</h3>
            <p>Pulsa el botón para obtener productos desde la web y analizarlos automáticamente.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Ejecutar scraper"):
        try:
            total = ejecutar_scraper()
            df = pd.read_csv(CSV_SCRAPER_PATH)
            nombre_origen = CSV_SCRAPER_PATH.name
            st.success(f"Scraping completado. Productos encontrados: {total}")
        except Exception as e:
            st.error(f"Error al ejecutar el scraper: {e}")

if df is not None:
    try:
        df = limpiar_datos(df)
        stats = obtener_estadisticas(df)

        st.markdown("## 📌 Resumen general")

        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("📦 Registros", stats["total"])
        col2.metric("💶 Precio medio", f"{stats['media']:.2f}")
        col3.metric("⬆️ Precio máximo", f"{stats['max']:.2f}")
        col4.metric("⬇️ Precio mínimo", f"{stats['min']:.2f}")
        col5.metric("⚠️ Nulos", stats["nulos"])

        st.markdown(
            f"""
            <div class="custom-box">
                <strong>📁 Origen de los datos:</strong> {nombre_origen}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.sidebar.markdown("### 🔎 Filtros")

        df_filtrado = df.copy()

        if "Precio" in df.columns and not df.empty:
            minimo = float(df["Precio"].min())
            maximo = float(df["Precio"].max())

            if minimo == maximo:
                maximo = minimo + 1.0

            rango_precio = st.sidebar.slider(
                "Filtrar por precio",
                min_value=minimo,
                max_value=maximo,
                value=(minimo, maximo)
            )

            df_filtrado = df_filtrado[
                (df_filtrado["Precio"] >= rango_precio[0]) &
                (df_filtrado["Precio"] <= rango_precio[1])
            ]

        if "Nombre" in df.columns:
            busqueda = st.sidebar.text_input("Buscar por nombre")
            if busqueda:
                df_filtrado = df_filtrado[
                    df_filtrado["Nombre"].astype(str).str.contains(busqueda, case=False, na=False)
                ]

        if "Rating" in df.columns:
            ratings = sorted(df["Rating"].dropna().unique().tolist())
            rating_elegido = st.sidebar.multiselect(
                "Filtrar por rating",
                ratings,
                default=ratings
            )
            if rating_elegido:
                df_filtrado = df_filtrado[df_filtrado["Rating"].isin(rating_elegido)]

        tabs = st.tabs(["📋 Datos", "📈 Gráficos", "🧾 Informe"])

        with tabs[0]:
            st.markdown("### 📋 Datos cargados")
            st.write(f"Registros mostrados: {len(df_filtrado)}")

            df_mostrar = df_filtrado.copy()

            if "Precio" in df_mostrar.columns:
                df_mostrar["Precio"] = df_mostrar["Precio"].map(lambda x: f"{x:.2f}")

            st.dataframe(df_mostrar, use_container_width=True, hide_index=True)

            csv_data = df_filtrado.to_csv(index=False).encode("utf-8")
            st.download_button(
                "⬇️ Descargar CSV filtrado",
                data=csv_data,
                file_name="datos_filtrados.csv",
                mime="text/csv"
            )

        with tabs[1]:
            st.markdown("### 📈 Visualización de datos")

            col_graf1, col_graf2 = st.columns(2)

            with col_graf1:
                st.markdown(
                    """
                    <div class="custom-box">
                        <h4>⭐ Productos por rating</h4>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if "Rating" in df_filtrado.columns and not df_filtrado.empty:
                    st.bar_chart(df_filtrado["Rating"].value_counts().sort_index())
                else:
                    st.info("No hay datos de rating para mostrar")

            with col_graf2:
                st.markdown(
                    """
                    <div class="custom-box">
                        <h4>💰 Top 10 productos más caros</h4>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if "Precio" in df_filtrado.columns and "Nombre" in df_filtrado.columns and not df_filtrado.empty:
                    top_10 = df_filtrado.sort_values(by="Precio", ascending=False).head(10)
                    st.bar_chart(top_10.set_index("Nombre")["Precio"])
                else:
                    st.info("No hay datos suficientes para mostrar el gráfico")

        with tabs[2]:
            st.markdown("### 🧾 Generar informe")
            st.write("Descarga un informe PDF con el resumen de los datos filtrados.")

            pdf = generar_pdf_informe(obtener_estadisticas(df_filtrado))

            st.download_button(
                "⬇️ Descargar informe PDF",
                data=pdf,
                file_name="informe_analisis.pdf",
                mime="application/pdf"
            )

    except Exception as e:
        st.error(f"Error al procesar los datos: {e}")
else:
    st.info("Selecciona una fuente de datos para empezar.")