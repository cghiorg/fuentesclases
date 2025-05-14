from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <h2>Ingresá tu nombre</h2>
        <form method='post' action='/saludo'>
            <input type='text' name='nombre' placeholder='Escribí tu nombre'>
            <input type='submit' value='Saludar'>
        </form>
    """

@app.route('/saludo', methods=['POST'])
def saludo():
    nombre = request.form['nombre']
    return render_template('saludo.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
