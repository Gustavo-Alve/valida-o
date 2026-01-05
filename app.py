from flask import Flask, render_template, request,session, jsonify
from conect import inserir_usuario, buscar_usuario
import os
#from conect import #nomes da função

app = Flask(__name__)
app.secret_key = os.urandom(24)
#rota para pagina inicial
@app.route('/')
def index():
    return render_template('index.html')

#rota para pagina de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/api/usuarios', methods=['POST'])
def receberDados():
    try:
        usuario = request.form.get('user')
        senha = request.form.get('password')

        if not usuario or not senha:
            return jsonify({"erro": "Campos obrigatórios"}), 400

        inserir_usuario(usuario, senha)

        return jsonify({
            "status": "ok",
            "mensagem": "Usuário cadastrado com sucesso"
        }), 200

    except Exception as e:
        print("ERRO NO FLASK:", e)
        return jsonify({
            "status": "erro",
            "mensagem": str(e)
        }), 500
    

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('user')
    senha = request.form.get('password')

    dados_usuario = buscar_usuario(usuario)

    if dados_usuario and dados_usuario['pwrd'] == senha:
        session['usuario'] = usuario
        session['tipo_usuario'] = dados_usuario['tipo_usuario']

        return jsonify({
            "status": "ok",
            "tipo": dados_usuario['tipo_usuario']
        })

    return jsonify({"status": "erro"}), 401


@app.route('/user')
def user():
    if 'usuario' in session and session.get('tipo_usuario') == 'user': #validando se o usuario e user e puxando o html de user
        return render_template('usuario.html')

@app.route('/admin')
def admin():
    if 'usuario' in session and session.get('tipo_usuario') == 'admin':  #validando se o usuario e admin e puxando o html de admin
        return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
