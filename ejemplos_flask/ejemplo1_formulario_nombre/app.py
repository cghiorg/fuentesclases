from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/saludo', methods=['POST'])
def saludo():
    nombre = request.form['nombre']
    return render_template('saludo.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)