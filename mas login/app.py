from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Usuario simulado
usuario_guardado = {
    "username": "admin",
    "password_hash": generate_password_hash("1234")
}

@app.route('/')
def inicio():
    if 'usuario' in session:
        return f"Bienvenido, {session['usuario']} <br><a href='/logout'>Cerrar sesión</a>"
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    mensaje = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == usuario_guardado['username'] and check_password_hash(usuario_guardado['password_hash'], password):
            session['usuario'] = username
            return redirect(url_for('inicio'))
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('login.html', mensaje=mensaje)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
