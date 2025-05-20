# app.py - Configuración básica de Flask y SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creamos la app Flask
app = Flask(__name__)

# Configuramos la URI de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mibase.db'

# Desactivamos el seguimiento de modificaciones para evitar advertencias
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creamos la instancia del ORM
db = SQLAlchemy(app)

# Solo para probar que funciona
@app.route("/")
def inicio():
    return "¡Flask y SQLAlchemy configurados correctamente!"

if __name__ == "__main__":
    app.run(debug=True)
