from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'clave_secreta'
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Usuario simulado
usuario_db = {
    'admin': generate_password_hash('1234')
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['usuario']
        clave = request.form['clave']
        if user in usuario_db and check_password_hash(usuario_db[user], clave):
            session['usuario'] = user
            flash('Sesión iniciada correctamente.')
            return redirect(url_for('index'))
        else:
            flash('Credenciales incorrectas.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Sesión finalizada.')
    return redirect(url_for('index'))

def login_requerido(func):
    def decorado(*args, **kwargs):
        if 'usuario' not in session:
            flash('Debes iniciar sesión primero.')
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    decorado.__name__ = func.__name__
    return decorado

@app.route('/formulario')
@login_requerido
def formulario():
    return render_template('formulario.html')

@app.route('/grillas')
@login_requerido
def grillas():
    return render_template('grillas.html')

@app.route('/subida', methods=['GET', 'POST'])
@login_requerido
def subida():
    imagen = None
    if request.method == 'POST':
        archivo = request.files['archivo']
        if archivo:
            nombre = secure_filename(archivo.filename)
            archivo.save(os.path.join(UPLOAD_FOLDER, nombre))
            imagen = nombre
    return render_template('subida.html', imagen=imagen)

if __name__ == '__main__':
    app.run(debug=True)
