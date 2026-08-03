# Dos de Agosto — Café & Letras
## Club de Lectura

Repositorio oficial de la plataforma web del club de lectura **Dos de Agosto**, diseñada para la gestión de lecturas, propuestas de libros y confirmaciones de asistencia mediante Netlify Forms y Serverless Functions.

---

## Stack Tecnológico

* **Frontend:** HTML5, CSS3 nativo (con diseño responsivo y sistema de pestañas) y JavaScript vainilla (`fetch` API).
* **Backend / Serverless:** Netlify Functions (`Node.js`) para la obtención segura de datos de formularios.
* **Hosting & Forms:** [Netlify](https://www.netlify.com/) (Hosting estático + Netlify Forms API).

---

## Estructura del Repositorio

```text
├── libros/                        # Incluye las imágenes msostradas con la información del libro del mes
├── versiones_previas              # Código utilizado en versiones anteriores de la web
│   └── app.py
├── .gitignore
├── .env
├── logo.png
├── new_tab.png
├── index.html                     # Interfaz web principal (SPA con pestañas)
├── netlify.toml                   # Configuración de despliegue y rutas de Netlify
├── netlify/
│   └── functions/
│       └── get-submissions.js     # Serverless function para consultar Netlify Forms API
└── README.md                      # Documentación del proyecto
```

---

## Arquitectura y Funcionamiento

* **Formularios Estáticos (Netlify Forms):**  
  La interfaz web (`index.html`) incluye formularios HTML nativos para la propuesta de lecturas y la confirmación de asistencia (RSVP) procesados automáticamente por Netlify.

* **Función Serverless (`get-submissions.js`):**  
  Dado que las claves de la API de Netlify no deben exponerse en el cliente, la aplicación utiliza una Netlify Function que actúa como intermediario seguro. Esta función realiza lo siguiente:
  * Consulta los formularios activos del sitio mediante la API v1 de Netlify.
  * Recupera las *submissions* (respuestas) asociadas a cada formulario.
  * Ordena los resultados cronológicamente y los devuelve en formato JSON al frontend para poblar las tablas dinámicamente.

---

## Configuración y Despliegue Local

### 1. Variables de Entorno
Para que la Netlify Function pueda comunicarse con la API de Netlify, es necesario configurar las siguientes variables de entorno en el panel de Netlify (*Site settings > Environment variables*):

* `NETLIFY_API_TOKEN`: Personal Access Token generado en Netlify (*User settings > Applications*).
* `NETLIFY_SITE_ID`: API ID único del sitio (*Site settings > General*).

### 2. Despliegue en Netlify
El repositorio incluye un archivo `netlify.toml` que define la configuración automática del proyecto:

```toml
[build]
  functions = "netlify/functions"
  publish = "."
```
Con esto, al conectar el repositorio a Netlify, el despliegue tanto de la web estática como de las funciones serverless se realiza de forma automática.