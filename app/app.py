#App de monitoramento de exercicio
from flask import Flask, render_template, redirect, url_for, session, request
import mysql.connector
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.secret_key = 'Quemmandaaquisoueu'

def conectar_db():
    return mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'projetos'
)
conexao = conectar_db()
cursor = conexao.cursor()
data = datetime.now()
dias_semana = {
    "Monday": "segunda",
    "Tuesday": "terca",
    "Wednesday": "quarta",
    "Thursday": "quinta",
    "Friday": "sexta",
    "Saturday": "sabado",
    "Sunday": "domingo"
}


@app.route('/')
def redirecionamento():
    return redirect(url_for('login'))
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        query = 'SELECT * FROM users WHERE usuario = %s'
        cursor.execute(query,(usuario,))
        consulta = cursor.fetchone()
        if consulta:
            if check_password_hash(consulta[2],senha):
                session['usuario'] = usuario
                session['usuario_id'] = consulta[0]
                session.modified = True
                return redirect(url_for('home'))
            else:
                return render_template('login.html', erro= 'Usuario ou senha incorreto.')
    return render_template('login.html')

@app.route('/novo_usuario', methods = ['GET','POST'])
def novo_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        confirm_senha = request.form['confirm_senha']
        if confirm_senha == senha:
            senha_hash = generate_password_hash(senha)
            query = 'SELECT * FROM Users WHERE usuario = %s'
            cursor.execute(query,(usuario,))
            resultado = cursor.fetchone()
            if resultado is None:
                query = 'INSERT INTO users (usuario, senha) VALUES (%s,%s)'
                valores = (usuario,senha_hash)
                cursor.execute(query,valores,)
                conexao.commit()
                print('\n\n\n',usuario,senha,senha_hash)       
                return redirect(url_for('login'))
            else:
                return render_template('novo_usuario.html', erro='Usuario Existente')
        else:
            return render_template('novo_usuario.html', erro= 'Erro! As senhas não compativeis.')
        
    return render_template('novo_usuario.html')
    

@app.route('/logout')
def logout():
    session.pop('usuario',None)
    return redirect (url_for('login'))

@app.route('/inicio', methods=['GET','POST'])
def home():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    if session['usuario'] == 'admin':
        SNLenda = 'ADM, Tu é uma lenda.'
    else:
        SNLenda = session['usuario']
    cursor = conexao.cursor(dictionary=True)

    usuario_id = session['usuario_id']
    dia = dias_semana[data.strftime('%A')]
    print('\n\n\n',usuario_id)
    cursor.execute("SELECT * FROM exercicios WHERE usuario_id = %s and dia = %s",(usuario_id,dia,))
    exercicios = cursor.fetchall()
    print(exercicios)


    return render_template('index.html',lenda = SNLenda, exercicios=exercicios)

@app.route('/novo_exercicio', methods = ['GET','POST'])
def novo():
    if request.method == 'POST':
        nome = request.form['nome']
        series = request.form['series']
        repeticoes = request.form['repeticoes']
        dia = request.form['dia']
        usuario_id = session.get('usuario_id')
        try:
            query = "INSERT INTO exercicios(nome, series, repeticoes, dia, usuario_id)VALUES(%s,%s,%s,%s,%s)"
            valores = (nome,series,repeticoes,dia,usuario_id)
            cursor.execute(query,valores,)
            conexao.commit()
            return redirect(url_for('home'))
        except mysql.connector.Error as e:
            print(f"\nerro\n\n{e}\n\n")
            return render_template('novo.html', erro = 'ocorreu algum erro ao registrar o exercicio. Por favor tente novamente mais tarde.')
    
    return render_template('novo.html')



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,    
        debug=True)
