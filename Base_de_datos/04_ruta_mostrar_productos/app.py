# app.py - Mostrar productos con Flask y Jinja2

from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo Producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)

@app.route("/productos")
def mostrar_productos():
    productos = Producto.query.all()
    # Plantilla HTML embebida
    plantilla = """
    <!DOCTYPE html>
    <html>
    <head><title>Productos</title></head>
    <body>
    <h1>Lista de Productos</h1>
    <ul>
    {% for prod in productos %}
        <li>{{ prod.nombre }} - ${{ prod.precio }}</li>
    {% endfor %}
    </ul>
    </body>
    </html>
    """
    return render_template_string(plantilla, productos=productos)

if __name__ == "__main__":
    app.run(debug=True)
