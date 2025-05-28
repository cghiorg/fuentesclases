from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secreto"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Usuario.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['usuario'] = user.username
            return redirect(url_for('index'))
        return render_template('login.html', error="Usuario o contraseña incorrecta")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

@app.route('/productos')
def productos():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        db.session.add(Producto(nombre=nombre, precio=precio))
        db.session.commit()
        return redirect(url_for('productos'))
    return render_template('formulario.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    producto = Producto.query.get(id)
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.precio = float(request.form['precio'])
        db.session.commit()
        return redirect(url_for('productos'))
    return render_template('formulario.html', producto=producto)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    producto = Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('productos'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not Usuario.query.filter_by(username="admin").first():
            db.session.add(Usuario(username="admin", password=generate_password_hash("admin123")))
            db.session.commit()
    app.run(debug=True)
