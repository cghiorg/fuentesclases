# app.py - Definición del modelo Producto

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definimos el modelo Producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Producto {self.nombre} - ${self.precio}>"

# Crear la base de datos y la tabla
with app.app_context():
    db.create_all()  # Se ejecuta una sola vez para crear la tabla

@app.route("/")
def home():
    return "Modelo Producto definido y base creada."

if __name__ == "__main__":
    app.run(debug=True)
