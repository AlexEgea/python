# 🚀 API REST Python – Ejemplo de tienda

<p align="center">
  <strong>Aplicación full stack para gestión de productos</strong><br>
  FastAPI · SQLAlchemy · SQLite · HTML · CSS · JavaScript
</p>

---

## 📌 Descripción

**cCommerce** es una aplicación web que combina un **backend en FastAPI** con un **frontend visual moderno** para gestionar un catálogo de productos.

Permite realizar todas las operaciones básicas sobre productos desde una API REST y también desde una interfaz web intuitiva.

Este proyecto está pensado como práctica de desarrollo **full stack** y como pieza de portfolio.

---

## ✨ Características principales

* Crear productos
* Listar productos
* Buscar por nombre
* Filtrar por categoría
* Ordenar por precio
* Eliminar productos
* Interfaz visual moderna conectada a la API
* Documentación automática con Swagger

---

## 🛠️ Tecnologías utilizadas

### 🔧 Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

### 🎨 Frontend

* HTML
* CSS
* JavaScript (Fetch API)

---

## 📂 Estructura del proyecto

```bash
api-rest-python/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── config.py
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── app.js
│
├── templates/
│   └── index.html
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/api-rest-python.git
cd api-rest-python
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
.\.venv\Scripts\Activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

```bash
uvicorn app.main:app --reload
```

---

## 🌐 Acceso a la aplicación

| Servicio              | URL                            |
| --------------------- | ------------------------------ |
| Interfaz web          | http://127.0.0.1:8000/         |
| API REST              | http://127.0.0.1:8000/products |
| Documentación Swagger | http://127.0.0.1:8000/docs     |

---

## 🔍 Uso de la aplicación

### Desde la interfaz web

Puedes:

* Añadir productos desde el formulario
* Ver el catálogo completo
* Buscar por nombre
* Filtrar por categoría
* Ordenar por precio
* Eliminar productos

---

### Desde la API

#### Obtener productos

```bash
GET /products
```

#### Crear producto

```json
POST /products

{
  "name": "Mechanical Keyboard",
  "description": "RGB keyboard with red switches",
  "price": 59.99,
  "stock": 12,
  "category": "Peripherals"
}
```

---

### Parámetros disponibles

```bash
/products?search=teclado
/products?category=Periféricos
/products?sort=price_asc
/products?sort=price_desc
```

---

## 🗄️ Base de datos

Se utiliza **SQLite**, por lo que no requiere instalación adicional.

El archivo se genera automáticamente:

```bash
products.db
```

---

## 🧠 Aprendizajes clave

Este proyecto permite trabajar y entender:

* APIs REST con FastAPI
* Arquitectura backend en Python
* CRUD con SQLAlchemy
* Validación con Pydantic
* Consumo de API desde JavaScript
* Separación frontend/backend
* Estructuración de proyectos reales

---

## 🚀 Posibles mejoras

* Edición de productos desde la interfaz
* Autenticación de usuarios
* Paginación de resultados
* Dashboard con estadísticas
* Deploy en servidor (Render, Railway, etc.)
* Uso de PostgreSQL o MySQL

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica de desarrollo web full stack y API REST en Python.

---

## ⭐ Si te gusta el proyecto

Puedes darle una estrella ⭐ en GitHub o usarlo como base para tus propios proyectos.
