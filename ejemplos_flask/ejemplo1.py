from flask import Flask

app = Flask(__name__)

@app.route('/saludo/<nombre>')
def inicio():
    return 'Hola, esta es mi primera.'

if __name__ == '__main__':
    app.run(debug=True)