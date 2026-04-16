import pandas as pd

from src.analisis import limpiar_datos, obtener_estadisticas
from src.config import CSV_SCRAPER_PATH, PDF_REPORT_PATH
from src.pdf_report import generar_pdf_informe
from src.scraper import ejecutar_scraper


def main() -> None:
    try:
        print("Iniciando scraper...")
        total = ejecutar_scraper()
        print(f"Scraping completado: {total} productos")

        print("Leyendo datos...")
        df = pd.read_csv(CSV_SCRAPER_PATH)

        print("Limpiando datos...")
        df = limpiar_datos(df)

        print("Calculando estadísticas...")
        stats = obtener_estadisticas(df)

        print("\nResumen:")
        print(f"Total registros: {stats['total']}")
        print(f"Precio medio: {stats['media']:.2f}")
        print(f"Precio máximo: {stats['max']:.2f}")
        print(f"Precio mínimo: {stats['min']:.2f}")
        print(f"Valores nulos detectados: {stats['nulos']}")

        pdf = generar_pdf_informe(stats)
        PDF_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

        with open(PDF_REPORT_PATH, "wb") as file:
            file.write(pdf)

        print(f"Informe PDF generado en: {PDF_REPORT_PATH}")

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


if __name__ == "__main__":
    main()