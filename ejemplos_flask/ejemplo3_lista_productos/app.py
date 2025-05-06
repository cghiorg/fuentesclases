from flask import Flask, render_template

app = Flask(__name__)

@app.route('/productos')
def productos():
    lista = ["Pan", "Leche", "Queso", "Huevos"]
    return render_template('productos.html', productos=lista)

if __name__ == '__main__':
    app.run(debug=True)