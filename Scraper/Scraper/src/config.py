from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

CSV_SCRAPER_PATH = DATA_DIR / "productos.csv"
PDF_REPORT_PATH = DATA_DIR / "informe.pdf"

SCRAPER_URL = "https://books.toscrape.com/"