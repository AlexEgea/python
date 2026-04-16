import re
import pandas as pd


def limpiar_precio(precio) -> float:
    if pd.isna(precio):
        return 0.0

    texto = str(precio).strip()

    if texto == "":
        return 0.0

    texto = texto.replace("€", "").replace("£", "").replace("$", "")
    texto = texto.replace(" ", "")
    texto = re.sub(r"[^0-9,.\-]", "", texto)

    if texto == "":
        return 0.0

    if "," in texto and "." in texto:
        if texto.rfind(",") > texto.rfind("."):
            texto = texto.replace(".", "")
            texto = texto.replace(",", ".")
        else:
            texto = texto.replace(",", "")
    else:
        if "," in texto:
            texto = texto.replace(",", ".")

    try:
        return round(float(texto), 2)
    except ValueError:
        return 0.0


def convertir_rating(rating) -> float:
    mapa = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    if pd.isna(rating):
        return 0.0

    texto = str(rating).strip()

    if texto in mapa:
        return float(mapa[texto])

    try:
        return float(texto)
    except ValueError:
        return 0.0


def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = [str(col).strip() for col in df.columns]

    if "Precio" in df.columns:
        df["Precio"] = df["Precio"].apply(limpiar_precio)

    if "Rating" in df.columns:
        df["Rating"] = df["Rating"].apply(convertir_rating)

    if "Stock" in df.columns:
        df["Stock"] = pd.to_numeric(df["Stock"], errors="coerce").fillna(0).astype(int)

    if "Fecha" in df.columns:
        df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")

    return df


def obtener_estadisticas(df: pd.DataFrame) -> dict:
    stats = {
        "total": len(df),
        "media": 0.0,
        "max": 0.0,
        "min": 0.0,
        "nulos": int(df.isna().sum().sum())
    }

    if "Precio" in df.columns and not df.empty:
        stats["media"] = round(df["Precio"].mean(), 2)
        stats["max"] = round(df["Precio"].max(), 2)
        stats["min"] = round(df["Precio"].min(), 2)

    return stats