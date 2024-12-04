from flask import Flask, g, render_template, request, redirect, url_for, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = '12345678'  
DATABASE = 'neabi.db'

# Função para conectar ao banco de dados
def conexaodb():
    db = getattr(g, 'conexao_db', None)
    if db is None:
        db = g.conexao_db = sqlite3.connect(DATABASE)
    return db

# Função para fechar a conexão com o banco de dados após a requisição
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'conexao_db', None)
    if db is not None:
        db.close()

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('loginU.html')


# Rota para exibir o formulário de cadastro de usuário
@app.route('/formcadastroU')
def form_cadastro():
    return render_template('formcadastroU.html')


# Rota para processar o cadastro de usuário
@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    nome = request.form['nome']
    matricula = request.form['matricula']
    telefone = request.form['telefone']
    email = request.form['email']
    senha = request.form['senha']
    tipo_usuario_id = request.form['tipo_usuario_id'] 

    # Criptografando a senha
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    db = conexaodb()
    cursor = db.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO usuarios (nome, matricula, telefone, senha_hash, tipo_usuario_id) 
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, matricula, telefone, senha_hash, tipo_usuario_id))
        db.commit()

        # Verifica se o tipo de usuário é 'Administrador' (tipo_usuario_id == 1)
        if tipo_usuario_id == '1':  
            return redirect(url_for('admin_page'))  # Redireciona para a página de administração
        else:
            return redirect(url_for('denuncia_form'))  # Caso contrário, redireciona para a página de denúncias
    except sqlite3.IntegrityError as e:
        return f'Erro: {e}'
    finally:
        db.close()



# Rota para exibir o formulário de login
@app.route('/loginU')
def login_form():
    return render_template('loginU.html')

# Rota para processar o login do usuário
@app.route('/login_usuario', methods=['POST'])
def login_usuario():
    matricula = request.form['matricula']
    senha = request.form['senha']

    # Criptografando a senha recebida para comparação
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    db = conexaodb()
    cursor = db.cursor()

    # Verifica se a matrícula e senha correspondem a um usuário no banco de dados
    cursor.execute('''
        SELECT * FROM usuarios WHERE matricula = ? AND senha_hash = ?
    ''', (matricula, senha_hash))
    
    user = cursor.fetchone()
    db.close()
    
    if user:
        session['user_id'] = user[0]  #
        tipo_usuario_id = user[5]  

       
        if tipo_usuario_id == 1:
            return redirect(url_for('admin_page')) 
        else:
            return redirect(url_for('denuncia_form')) 
    else:
        return 'Matrícula ou senha inválidos.'
    


# Rota para logout
@app.route('/logout')
def logout():
    # Encerra a sessão do usuário
    session.pop('user_id', None)
    # Redireciona para a página inicial
    return redirect(url_for('index'))



    
#Rota para tela de denuncia
@app.route('/denuncia')
def denuncia_form():
    return render_template('denuncia.html')

#registrando denuncia
@app.route('/registrar_denuncia', methods=['POST'])
def registrar_denuncia():
    if 'user_id' not in session:
        return redirect(url_for('login_form'))  # Redireciona para o login se não estiver logado

    usuario_id = session['user_id']  # Obtém o ID do usuário logado diretamente da sessão
    tipo_denuncia_id = request.form['tipo_denuncia_id']
    denuncia = request.form['denuncia']
    data_denuncia = request.form['data_denuncia']
    status_denuncia_id = 1  # Status inicial da denúncia como 'Pendente'

    db = conexaodb()
    cursor = db.cursor()

    try:
        # Insere a nova denúncia no banco de dados usando o ID do usuário logado
        cursor.execute('''
            INSERT INTO denuncias (usuario_id, tipo_denuncia_id, status_denuncia_id, denuncia, data_denuncia)
            VALUES (?, ?, ?, ?, ?)
        ''', (usuario_id, tipo_denuncia_id, status_denuncia_id, denuncia, data_denuncia))
        db.commit()
        return '''
            <p>Denúncia registrada com sucesso!</p>
            <a href="/denuncia">Voltar para a página de denúncia</a>
            <a href="/">Ir para a página inicial</a>
        '''
    except sqlite3.IntegrityError as e:
        return f'Erro: {e}'
    finally:
        db.close()




#rota para tela de denuncias feitas
@app.route('/minhas_denuncias')
def minhas_denuncias():
    if 'user_id' not in session:
        return redirect(url_for('login_form'))  

    usuario_id = session['user_id']  
    db = conexaodb()
    cursor = db.cursor()

    cursor.execute('''
        SELECT d.id, td.nome, sd.status, d.denuncia, d.data_denuncia
        FROM denuncias d
        JOIN tipos_denuncias td ON d.tipo_denuncia_id = td.id
        JOIN status_denuncias sd ON d.status_denuncia_id = sd.id
        WHERE d.usuario_id = ?
    ''', (usuario_id,))

    denuncias = cursor.fetchall()
    db.close()

    return render_template('minhas_denuncias.html', denuncias=denuncias)


#rota para tela de adm
@app.route('/admin')
def admin_page():
    # Busca todas as denúncias do banco de dados
    db = conexaodb()
    cursor = db.cursor()
    cursor.execute('''
        SELECT d.id, u.nome, td.nome, sd.status, d.denuncia, d.data_denuncia
        FROM denuncias d
        JOIN usuarios u ON d.usuario_id = u.id
        JOIN tipos_denuncias td ON d.tipo_denuncia_id = td.id
        JOIN status_denuncias sd ON d.status_denuncia_id = sd.id
    ''')
    denuncias = cursor.fetchall()
    db.close()
    
    return render_template('adm.html', denuncias=denuncias)




@app.route('/atualizar_denuncia/<int:denuncia_id>', methods=['POST'])
def atualizar_denuncia(denuncia_id):
    novo_status_id = request.form['status_denuncia_id']
    
    db = conexaodb()
    cursor = db.cursor()

    try:
        cursor.execute('''
            UPDATE denuncias
            SET status_denuncia_id = ?
            WHERE id = ?
        ''', (novo_status_id, denuncia_id))
        db.commit()
        return redirect(url_for('admin_page'))
    except sqlite3.Error as e:
        return f'Erro ao atualizar denúncia: {e}'
    finally:
        db.close()



if __name__ == "__main__":
    app.run(debug=True)
