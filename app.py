from flask import Flask, request, jsonify, abort

app = Flask(__name__)

tareas = []
next_id = 1

def crear_tarea(title, done=False):
    global next_id
    tarea = {"id": next_id, "title": title, "done": bool(done)}
    tareas.append(tarea)
    next_id += 1
    return tarea

# Semillas de ejemplo
crear_tarea("Aprender Flask")
crear_tarea("Hacer el TP", done=False)

# ---- Endpoints CRUD ----

# Endpoint para el index
@app.get("/")
def index():
    return "En la barra de navegación agregar '/tareas' al final de la URL.", 200

# 1) Listar todas

@app.get("/tareas")
def listar_tareas():
    return jsonify(tareas), 200

# 2) Obtener una por ID
@app.get("/tareas/<int:tarea_id>")
def obtener_tarea(tarea_id):
    tarea = next((t for t in tareas if t["id"] == tarea_id), None)
    if not tarea:
        abort(404, description="Tarea no encontrada")
    return jsonify(tarea), 200

# 3) Crear
@app.post("/tareas")
def crear():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        abort(400, description="Falta 'title'")
    nueva = crear_tarea(title, data.get("done", False))
    return jsonify(nueva), 201

# 4) Actualizar
@app.put("/tareas/<int:tarea_id>")
def actualizar(tarea_id):
    tarea = next((t for t in tareas if t["id"] == tarea_id), None)
    if not tarea:
        abort(404, description="Tarea no encontrada")
    data = request.get_json(silent=True) or {}
    if "title" in data:
        tarea["title"] = data["title"]
    if "done" in data:
        tarea["done"] = bool(data["done"])
    return jsonify(tarea), 200

# 5) Borrar
@app.delete("/tareas/<int:tarea_id>")
def borrar(tarea_id):
    idx = next((i for i, t in enumerate(tareas) if t["id"] == tarea_id), None)
    if idx is None:
        abort(404, description="Tarea no encontrada")
    tareas.pop(idx)
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
