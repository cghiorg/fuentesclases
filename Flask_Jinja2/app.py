from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    lista = ["Notebook", "Teclado", "Mouse", "Monitor"]
    return render_template('productos.html', productos=lista)

@app.route('/encuesta', methods=['GET', 'POST'])
def encuesta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        lenguaje = request.form['lenguaje']
        return render_template('resultado.html', nombre=nombre, lenguaje=lenguaje)
    return render_template('encuesta.html')

if __name__ == '__main__':
    app.run(debug=True)
