from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/seleccion')
def seleccion():
    return render_template('seleccion.html')

@app.route('/lenguaje', methods=['POST'])
def lenguaje():
    lenguaje = request.form['lenguaje']
    return render_template('lenguaje.html', lenguaje=lenguaje)

if __name__ == '__main__':
    app.run(debug=True)