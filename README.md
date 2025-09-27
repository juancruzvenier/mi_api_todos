
# API de Tareas – ToDo List

Una API REST sencilla desarrollada con **Python + Flask**, que permite gestionar una lista de tareas.  
Este proyecto es parte de un trabajo práctico para aprender sobre **APIs, CRUD y JSON**.

---

## 📌 Características
- Listar todas las tareas.
- Crear nuevas tareas.
- Actualizar tareas existentes.
- Eliminar tareas.
- Estructura RESTful utilizando métodos HTTP (`GET`, `POST`, `PUT`, `DELETE`).

---

## 🗂️ Estructura del proyecto
mi_api_todos/
│
├── venv/                # Entorno virtual (NO modificar)
│
├── app.py                # Código principal de la API
└── README.md             # Este archivo

---

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio (opcional si ya tienes los archivos)
git clone https://github.com/juancruzvenier/mi_api_todos
cd mi_api_todos

### 2. Crear un entorno virtual
python -m venv venv

### 3. Activar el entorno virtual
| Sistema | Comando |
|---------|---------|
| Windows (PowerShell) | .\venv\Scripts\Activate.ps1 |
| Windows (CMD) | venv\Scripts\activate.bat |
| Git Bash / Linux / macOS | source venv/Scripts/activate |

> Si PowerShell bloquea el script, ejecuta:
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

### 4. Instalar dependencias
pip install flask

> Opcional (para evitar problemas de CORS):
> pip install flask-cors

---

## 🚀 Ejecutar la API
En la carpeta raíz del proyecto:
python app.py

La API se ejecutará en:
http://127.0.0.1:5000

---

## 📚 Endpoints disponibles

| Acción | Método | URL | Body (JSON) |
|--------|--------|-----|-------------|
| Listar todas las tareas | GET | /tareas | ❌ |
| Obtener tarea por ID | GET | /tareas/<id> | ❌ |
| Crear una nueva tarea | POST | /tareas | {"title": "Comprar pan"} |
| Actualizar tarea existente | PUT | /tareas/<id> | {"done": true} |
| Eliminar tarea | DELETE | /tareas/<id> | ❌ |

---

## 🧪 Ejemplos de uso con Postman

### 1. Crear una tarea
Método: POST  
URL: http://127.0.0.1:5000/tareas  
Body → raw → JSON:
{
  "title": "Pasear al perro"
}

Respuesta:
{
  "id": 3,
  "title": "Pasear al perro",
  "done": false
}

### 2. Listar tareas
Método: GET  
URL: http://127.0.0.1:5000/tareas

Respuesta:
[
  { "id": 1, "title": "Aprender Flask", "done": false },
  { "id": 2, "title": "Hacer el TP", "done": false },
  { "id": 3, "title": "Pasear al perro", "done": false }
]

### 3. Actualizar una tarea
Método: PUT  
URL: http://127.0.0.1:5000/tareas/3
Body → raw → JSON:
{
  "done": true
}

Respuesta:
{
  "id": 3,
  "title": "Pasear al perro",
  "done": true
}

### 4. Eliminar una tarea
Método: DELETE  
URL: http://127.0.0.1:5000/tareas/3

Respuesta:  
Código HTTP: 204 No Content (sin cuerpo)

---

## 🔧 Buenas prácticas incluidas
- Validaciones básicas: no se puede crear una tarea sin 'title'.
- Manejo de errores con códigos HTTP adecuados:
  - 400 Bad Request → Datos inválidos.
  - 404 Not Found → Tarea no encontrada.
- Respuestas en formato JSON.

---

## 📄 Próximos pasos (mejoras sugeridas)
- Persistencia de datos en archivo data.json o base de datos SQLite.
- Autenticación de usuarios.
- Tests automáticos con pytest.
- Documentación de endpoints con Swagger.

---

##Trabajo práctico para **Programación VI – Tecnicatura Superior en Desarrollo de Software**.
### 🧑‍💻 Autores
Banegas Paez, Julian - 46491016
Ibañez, Juan Ignacio - 45958733
Perez Ledesma, Mariano – 46488889
Schuldt Ger, Máximo Agustín - 45955049
Venier Rojas, Juan Cruz - 42216020 