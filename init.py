import json
from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from modulos import alunos, professores, turmas, usuarios, sistema

app = Flask(__name__)
app.secret_key = 'chave_secreta'

def is_logged_in():
    return 'username' in session

@app.route('/')
def index():
    if not is_logged_in():
        return render_template('login.html')
    if session['tipoUsuario'] == 'diretor':
        dadosTurmas = turmas.buscaQuantidadeTurmasAluno()
        dadosEntidades = sistema.relacaoTiposUsuario()
        return render_template('index.html', relacaoTurmaAlunos = dadosTurmas, relacaoEntidades=dadosEntidades )
    if session['tipoUsuario'] == 'professor':
        return render_template('acessoProfessor/index.html')
    if session['tipoUsuario'] == 'aluno':
        return render_template('acessoAluno/index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    dadosUsuarios = usuarios.buscaDadosUsuarios()
    autentica = False
    tipoUsuario = ""
    resetSenha = ""
    for dadosUsuario in dadosUsuarios:
        if dadosUsuario['usuario'] == username and dadosUsuario['senha'] == password:
            autentica = True
            tipoUsuario = dadosUsuario['tipo']
            resetSenha = dadosUsuario['resetSenha']
            break

    if autentica == True:
        session['username'] = username
        session['tipoUsuario'] = tipoUsuario
         
        return jsonify({'result': '1', 'message': '', 'resetSenha':resetSenha})
    else:
        return jsonify({'result': '', 'message': 'Credenciais inválidas. Tente novamente.'})

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login.html')

@app.route('/gerenciarAlunos')
def gerenciarAlunos():
    if not is_logged_in():
        return render_template('login.html')

    dadosAlunos = alunos.buscaDadosAlunos()
    dadosTurmas = turmas.buscaDadosTurmas()

    return render_template('alunos/gerenciarAlunos.html', alunos=dadosAlunos, turmas=dadosTurmas, nomeUsuario=session['username'])

@app.route('/redefinirNovaSenha')
def redirecionaRedefinirSenha():
    if not is_logged_in():
        return render_template('login.html')

    return render_template('redefinirNovaSenha.html')

@app.route('/excluirAluno/<string:ra>', methods=['POST', 'DELETE'])
def excluir(ra):
    alunos.excluirAlunos( ra )

    if request.method == 'DELETE':
        return '', 204

    return '', 200

@app.route('/editarAluno/<string:ra>', methods=['POST', 'DELETE'])
def editarAluno(ra):
    alunos.editarAluno( ra )

@app.route('/cadastrarAluno', methods=['POST'])
def cadastrarAluno():
    return alunos.cadastrarAluno( request.form )    

@app.route('/limparSenha/<string:ra>', methods=['POST', 'DELETE'])
def redefinirSenha(ra):
    usuarios.redefinirSenha( ra, request.form['senha'] )

    return '', 200

@app.route('/turmas')
def carregarTurmas():
    if not is_logged_in():
        return render_template('login.html')

    dadosTurmas = turmas.buscaDadosTurmas()
    dadosProfessores = professores.buscaDadosProfessores()

    return render_template('turmas/gerenciamentoTurmas.html', turmas=dadosTurmas, professores=dadosProfessores)

@app.route('/professores')
def carregarProfessores():
    if not is_logged_in():
        return render_template('login.html')

    dadosProfessores = professores.buscaDadosProfessores()

    return render_template('professores/gerenciamentoProfessores.html', professores=dadosProfessores)


@app.route('/buscaTurmasAluno/<string:ra>', methods=['POST', 'GET'])
def buscaDadosTurma(ra):
    listaNomeTurmas = alunos.buscaTurmasAlunos(ra)
    return jsonify(
        {
            'result': '1',
            'turmasNaoMatriculadas':listaNomeTurmas['naoMatriculado'],
            'turmasMatriculadas':listaNomeTurmas['matriculado']
        } )

@app.route('/buscaDadosAluno/<string:ra>', methods=['POST', 'GET'])
def buscaAluno(ra):
    dadosAluno = alunos.pesquisaAluno(ra)
    return jsonify(
        {
            'result': '1',
            'dadosAluno':dadosAluno
        } )

@app.route('/modificarTurmasAluno', methods=['POST'])
def modificarTurmasAlunos():
    listaTurmasMatriculadas = json.loads(request.form['turmas'])
    ra = request.form['ra']
    alunos.inserirTurmas(ra,listaTurmasMatriculadas)

    return ''

@app.route('/buscaAlunosTurma/<string:identificador>', methods=['POST', 'GET'])
def buscaAlunosTurma(identificador):
    listaAlunos = turmas.buscaAlunos(identificador)
    return jsonify(
        {
            'result': '1',
            'alunosNaoMatriculadas':listaAlunos['naoMatriculado'],
            'alunosMatriculadas':listaAlunos['matriculado']
        } )

@app.route('/minhasturmasprofessor')
def carregaTurmasProfessor():
    if not is_logged_in():
        return render_template('login.html')

    dadosTurmas = professores.buscaDadosTurmas('PF03')
    return render_template('acessoProfessor/gerenciamentoTurmas.html', turmas=dadosTurmas)

if __name__ == '__main__':
    app.run(debug=True)