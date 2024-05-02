from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', resultado='')

@app.route('/verificar', methods=['POST'])
def verificar():
    numero = int(request.form['numero'])
    resultado = "par" if numero % 2 == 0 else "ímpar"
    return render_template('index.html', resultado=f'O número {numero} é {resultado}.')

if __name__ == '__main__':
    app.run(debug=True)
