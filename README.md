#  API de Gestión de Librería

API RESTful desarrollada con **Python** y **FastAPI**. Este proyecto simula un sistema de gestión de inventario de libros permitiendo realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar).

##  Tecnologías Utilizadas

* **Python 3.12** - Lenguaje principal.
* **FastAPI** - Framework web moderno y rápido.
* **Uvicorn** - Servidor ASGI.
* **Pydantic** - Validación de datos robusta.

##  Instalación y Ejecución Local

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/ivanfm93/api-libreria-portfolio.git
    cd api-libreria-portfolio
    ```

2.  **Crear y activar entorno virtual:**
    ```bash
    python -m venv .venv
    # Windows:
    .\.venv\Scripts\activate
    # Mac/Linux:
    source .venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar el servidor:**
    ```bash
    uvicorn main:app --reload
    ```

5.  **Abrir la documentación:**
    Visita `http://127.0.0.1:8000/docs` en tu navegador.

##  Endpoints Disponibles

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `GET` | `/libros` | Obtiene la lista de todos los libros. |
| `GET` | `/libros/{id}` | Busca un libro por su ID. |
| `POST` | `/libros` | Crea un nuevo libro. |
| `PUT` | `/libros/{id}` | Actualiza un libro existente. |
| `DELETE` | `/libros/{id}` | Elimina un libro. |

---