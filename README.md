# Dos de Agosto — Café & Letras

## Club de Lectura

Repositorio oficial de la plataforma web del club de lectura **Dos de Agosto**, una aplicación web estática para gestionar las lecturas del club, recibir propuestas de libros y confirmar la asistencia a las reuniones utilizando **Google Apps Script** y **Google Sheets** como backend.

---

# Características

- Libro del mes destacado.
- Biblioteca con histórico de lecturas.
- Envío de propuestas de nuevos libros.
- Confirmación de asistencia a reuniones.
- Sincronización automática con Google Sheets.
- Diseño responsive compatible con móviles y escritorio.
- Interfaz sencilla basada en HTML, CSS y JavaScript puro.

---

# Stack Tecnológico

## Frontend

- HTML5
- CSS3 nativo
- JavaScript (Vanilla)
- Fetch API

## Backend

- Google Apps Script (Web App)

## Base de datos

- Google Sheets

---

# Estructura del proyecto

```text
├── libros/                             # Incluye las imágenes msostradas con la información del libro del mes
├── versiones_previas/                  # Código utilizado en versiones anteriores de la web
│   └── app.py
│   └── forms_netlify/
│       └── index.html
│       └── netlify.toml                # Configuración de despliegue y rutas de Netlify
│       └── netflify/
│           └── functions/
│               └── get-submissions.js  # Serverless function para consultar Netlify Forms API
├── .gitignore
├── .env
├── logo.png
├── new_tab.png
├── index.html                           # Interfaz web principal (SPA con pestañas)    
└── README.md                            # Documentación del proyecto
```

---

# Funcionamiento

La aplicación es completamente estática.

Los datos no se almacenan localmente ni existe un servidor propio.

Toda la información se gestiona mediante una **Web App de Google Apps Script**, que actúa como intermediaria entre la página web y una hoja de cálculo de Google Sheets.

## Lectura de datos

Al cargar la página se realizan dos peticiones GET:

- Propuestas
- Confirmaciones

El Apps Script devuelve un JSON que contiene las filas almacenadas en la hoja correspondiente.

Ese JSON se utiliza para rellenar dinámicamente las tablas.

## Envío de formularios

Los formularios envían la información mediante `fetch()` usando `FormData`.

Después del envío:

1. Se limpia el formulario.
2. Se muestra un mensaje de éxito.
3. Tras unos segundos se vuelven a solicitar los datos para actualizar las tablas automáticamente.

---

# Google Apps Script

La aplicación utiliza una única URL pública del Web App. Este servicio se encarga de:

- Recibir nuevas propuestas.
- Guardar confirmaciones.
- Devolver los datos almacenados en Google Sheets en formato JSON.

---

# Pestañas de la aplicación

## Libro del mes

Muestra la lectura actual con:

- Portada.
- Autor.
- Género.
- Número de páginas.
- Descripción.
- Cita destacada.

## Biblioteca

Histórico de libros leídos por el club.

## Propuestas

Permite enviar nuevas recomendaciones de lectura y visualizar todas las propuestas registradas.

## Reuniones

Incluye la información de la próxima reunión y permite confirmar la asistencia.

---

# Personalización

Para actualizar la lectura del mes basta con modificar en `index.html`:

- Portada.
- Autor.
- Género.
- Número de páginas.
- Descripción.
- Cita destacada.

Las tablas se actualizan automáticamente desde Google Sheets sin necesidad de modificar el código.

---

# Despliegue

Al tratarse de una página completamente estática, puede alojarse en cualquier servicio de hosting, por ejemplo:

- GitHub Pages
- Netlify
- Vercel
- Firebase Hosting

Solo es necesario que la URL del Google Apps Script permanezca publicada y accesible.

---

# Licencia

Proyecto desarrollado para uso interno del club de lectura **Dos de Agosto – Café & Letras**.