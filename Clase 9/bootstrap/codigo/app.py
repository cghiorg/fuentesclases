from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/modal')
def modal():
    return render_template('modal.html')

@app.route('/grillas')
def grillas():
    return render_template('grillas.html')

@app.route('/subida', methods=['GET', 'POST'])
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
