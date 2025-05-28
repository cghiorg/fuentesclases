# app.py - CRUD completo con Flask, SQLAlchemy y formularios HTML

from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos_crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo Producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)

# Ruta para mostrar productos y formulario
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = float(request.form["precio"])
        nuevo = Producto(nombre=nombre, precio=precio)
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for("index"))

    productos = Producto.query.all()
    return render_template_string(template_index, productos=productos)

# Ruta para eliminar
@app.route("/eliminar/<int:id>")
def eliminar(id):
    producto = Producto.query.get(id)
    if producto:
        db.session.delete(producto)
        db.session.commit()
    return redirect(url_for("index"))

# Ruta para editar
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    producto = Producto.query.get(id)
    if request.method == "POST":
        producto.nombre = request.form["nombre"]
        producto.precio = float(request.form["precio"])
        db.session.commit()
        return redirect(url_for("index"))
    return render_template_string(template_editar, producto=producto)

# Plantillas HTML embebidas
template_index = """
<!DOCTYPE html>
<html>
<head><title>Productos</title></head>
<body>
<h1>CRUD de Productos</h1>
<form method="post">
  Nombre: <input type="text" name="nombre" required>
  Precio: <input type="number" step="0.01" name="precio" required>
  <button type="submit">Agregar</button>
</form>
<ul>
  {% for prod in productos %}
    <li>{{ prod.nombre }} - ${{ prod.
    [<a href="{{ url_for('editar', id=prod.id) }}">Editar</a>]
    [<a href="{{ url_for('eliminar', id=prod.id) }}">Eliminar</a>]
    </li>
  {% endfor %}
</ul>
</body>
</html>
"""

template_editar = """
<!DOCTYPE html>
<html>
<head><title>Editar Producto</title></head>
<body>
<h1>Editar Producto</h1>
<form method="post">
  Nombre: <input type="text" name="nombre" value="{{ producto.nombre }}" required>
  Precio: <input type="number" step="0.01" name="precio" value="{{ producto.precio }}" required>
  <button type="submit">Guardar Cambios</button>
</form>
<a href="{{ url_for('index') }}">Volver</a>
</body>
</html>
"""

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
