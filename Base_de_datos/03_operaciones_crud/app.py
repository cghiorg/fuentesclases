# app.py - Operaciones CRUD básicas con SQLAlchemy

from flask import Flask
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

    def __repr__(self):
        return f"<Producto {self.nombre} - ${self.precio}>"

with app.app_context():
    # Crear tablas
    db.create_all()

    # CREATE - Insertar nuevos productos
    p1 = Producto(nombre="Teclado", precio=4500.0)
    p2 = Producto(nombre="Mouse", precio=2500.0)
    p3 = Producto(nombre="Monitor", precio=80000.0)
    db.session.add_all([p1, p2, p3])
    db.session.commit()
    print("✔ Productos creados")

    # READ - Leer productos
    productos = Producto.query.all()
    print("📦 Productos en la base:")
    for prod in productos:
        print(prod)

    # UPDATE - Actualizar producto
    teclado = Producto.query.filter_by(nombre="Teclado").first()
    if teclado:
        teclado.precio = 5000.0
        db.session.commit()
        print("✏ Precio del Teclado actualizado")

    # DELETE - Eliminar un producto
    monitor = Producto.query.filter_by(nombre="Monitor").first()
    if monitor:
        db.session.delete(monitor)
        db.session.commit()
        print("❌ Monitor eliminado")

    # Mostrar productos finales
    print("📋 Lista final de productos:")
    for prod in Producto.query.all():
        print(prod)
