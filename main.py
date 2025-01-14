from flask import *

app = Flask(__name__) #instanciar

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/teste', methods=["POST"])
def verificar_nome():
    nome = request.form.get('nome')
    if nome == 'adolfo namorador':
        return 'o pegador do peugeot'
    else:
        return 'voce é um reles mortal'


if __name__ == '__main__':
    app.run() #executar