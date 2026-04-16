# 🕷️ Web Scraper - CSV & Excel Processor

Aplicación desarrollada en **Python** que permite extraer, procesar y visualizar datos desde páginas web o archivos estructurados (CSV/Excel).

El proyecto está orientado a la automatización de tareas de scraping y análisis de datos de forma sencilla y reutilizable.

---

## 🚀 Tecnologías utilizadas

* Python
* Selenium (automatización web)
* Pandas (procesamiento de datos)
* OpenPyXL (Excel)
* Matplotlib (visualización)
* Streamlit (interfaz web opcional)
* BeautifulSoup + lxml (scraping HTML)

---

## 📌 Funcionalidades principales

* 🌐 Extracción de datos mediante scraping web
* 📄 Lectura de archivos CSV y Excel
* 🔄 Limpieza y transformación de datos
* 📊 Visualización de datos (gráficas)
* 📁 Exportación a CSV y Excel
* 🔢 Formateo de datos (ej: precios con 2 decimales)
* 🧠 Procesamiento automático de información

---

## ⚙️ Requisitos

Antes de ejecutar el proyecto necesitas:

* Python 3.10 o superior
* pip
* Google Chrome instalado

---

## 🛠️ Instalación paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/web-scraper.git
cd web-scraper
```

---

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución del proyecto

### Ejecutar el script principal

```bash
python main.py
```

---

### (Opcional) Ejecutar interfaz con Streamlit

```bash
streamlit run app.py
```

---

## 📁 Estructura del proyecto

```
project/
│
├── main.py             → Punto de entrada
├── config.py           → Configuración general
├── scraper/            → Lógica de scraping
├── data/               → Archivos CSV / Excel
├── output/             → Resultados generados
├── utils/              → Funciones auxiliares
├── app.py              → Interfaz con Streamlit
└── requirements.txt    → Dependencias
```

---

## 📊 Ejemplo de uso

El proyecto permite:

1. Cargar un archivo CSV o Excel
2. Procesar los datos automáticamente
3. Limpiar columnas y ordenar información
4. Exportar resultados en formato estructurado

---

## ⚠️ Consideraciones importantes

* Algunas webs pueden bloquear scraping → usar delays si es necesario
* Selenium requiere navegador compatible
* Verificar selectores HTML si cambian las páginas
* No abusar del scraping (respetar términos de uso)

---

## 🔧 Configuración

Puedes modificar parámetros en:

```
config.py
```

Ejemplos:

* URL objetivo
* Rutas de archivos
* Columnas a procesar
* Formato de salida

---

## 📈 Posibles mejoras

* Soporte multi-web
* Scraping paralelo
* API REST
* Dashboard avanzado
* Automatización programada (cron)

---

## 👨‍💻 Autor

**Alejandro Aguilera**

* GitHub: https://github.com/AlexEgea
* Portfolio: https://alejandroaguilera.alwaysdata.net/

---

## 📄 Licencia

Proyecto desarrollado con fines educativos y de portfolio.
