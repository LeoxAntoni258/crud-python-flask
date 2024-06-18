from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

@app.route('/')
def dasboard():
    return render_template('admin_dashboard.html')

@app.route('/consulta')
def add_consulta():
    return render_template('consulta.html')

@app.route('/listar_consultas')
def listar_consultas():
    return render_template('list_consultas.html')

db = mysql.connector.connect(
host="localhost",
user="root",
password="@Chance873433576",
database="bd_diabete"
)
cursor = db.cursor()

@app.route('/add_consult', methods=['POST'])
def add_consult():


# Obtém os dados do formulário
    nome = request.form['nome']
    email = request.form['email']
    numero = request.form['numero']
    genero = request.form['genero']
    data = request.form['data']
    data_c = request.form['data_consulta']
    especialidade = request.form['especialidade']
    observacoes = request.form['observacoes']


    # Insere os dados no banco de dados
    cursor = db.cursor()
    cursor.execute("INSERT INTO consultas (nome, email, numero, genero, data_nascimento, data_consulta, especialidade, observacoes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (nome, email, numero, genero, data, data_c, especialidade, observacoes))
    db.commit()

    return ('Consultas adicionado com sucesso!')

#Listar as consultas
@app.route('/list_consulta')
def list_consultas():
    cursor.execute("SELECT * FROM consultas")
    data = cursor.fetchall()
    return render_template('list_consultas.html',data=data)

#Eliminar As Consultas
@app.route('/delete_c/int:id', methods=['POST'])
def delete_entryy(id):
    cursor.execute("DELETE FROM consultas WHERE id = %s", (id,))
    db.commit()
    return redirect('/list_consulta')

if __name__ == '__main__':
    app.run(debug=True)