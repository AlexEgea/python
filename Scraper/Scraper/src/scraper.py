import csv
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.config import CSV_SCRAPER_PATH, SCRAPER_URL


def ejecutar_scraper() -> int:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    productos = []

    try:
        driver.get(SCRAPER_URL)
        time.sleep(2)

        items = driver.find_elements(By.CLASS_NAME, "product_pod")

        for item in items:
            try:
                # Nombre del producto
                nombre = item.find_element(By.TAG_NAME, "h3").text

                # Precio
                precio = item.find_element(By.CLASS_NAME, "price_color").text

                # Rating (corregido)
                rating_element = item.find_element(By.CLASS_NAME, "star-rating")
                clases = rating_element.get_attribute("class") or ""
                rating = clases.split()[-1] if clases else ""

                productos.append([nombre, precio, rating])

            except Exception:
                # Si falla un producto, seguimos con el siguiente
                pass

        # Crear carpeta si no existe
        os.makedirs(CSV_SCRAPER_PATH.parent, exist_ok=True)

        # Guardar CSV
        with open(CSV_SCRAPER_PATH, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Precio", "Rating"])
            writer.writerows(productos)

        return len(productos)

    finally:
        driver.quit()