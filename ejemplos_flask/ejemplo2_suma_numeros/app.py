from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/suma')
def suma():
    return render_template('suma.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    total = num1 + num2
    return render_template('resultado.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)