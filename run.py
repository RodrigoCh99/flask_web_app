# importando as bibliotecas
from flask import Flask, render_template, request

# importando o banco de dados
from bd import *



# Atribuindo a favariavel app o Flask
app = Flask(__name__)

# rota para '/' e '/login'
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        if validar_login(login, senha):
            return render_template('tabela.html', nome=login, disciplinas=get_diciplinas(login))
        else:
            return render_template('index.html', erro='Login/senha incorretos!')
    else:
        return render_template('index.html', erro='Método incorreto. Use POST!')








@app.route('/detalhar/<disciplina>')
def detalhes(disciplina):
    return render_template('disciplina.html', disciplina=disciplina, detalhes=get_detalhes(disciplina))







# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)