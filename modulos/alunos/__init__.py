import json
from flask import jsonify
import random
from modulos import turmas,usuarios

def buscaDadosAlunos():
    with open('dadosJson/baseAlunos.json', 'r') as arquivo:
        dadosAlunos = json.load(arquivo)
        dadosAlunos = sorted(dadosAlunos, key=lambda x: x["nome"])

    return dadosAlunos

def buscaQuantidadeAlunos():
    return len(buscaDadosAlunos())

def cadastrarAluno( dadosAluno ):
    nomeAluno = dadosAluno['nome']
    emailAluno = dadosAluno['email']

    with open('dadosJson/baseAlunos.json') as f:
        dadosAluno = json.load(f)

    raAluno = "ALUNO" + str( len(dadosAluno) ) + str(random.randint(100, 999))
    turmaAluno = []
    novoAluno = {
        'nome': nomeAluno,
        'turma': turmaAluno,
        'RA': raAluno,
        'email':emailAluno
    }

    dadosAluno.append(novoAluno)

    with open('dadosJson/baseAlunos.json', 'w') as arquivoAlunos:
        json.dump(dadosAluno, arquivoAlunos, indent=2)

    senha = usuarios.cadastrarUsuario( raAluno, "aluno")

    return jsonify({'result': '1', 'senhaAluno': senha, 'raAlunos':raAluno})

def excluirAlunos( ra ):
    dadosAlunos = buscaDadosAlunos()

    novosDados = []
    for dadosAluno in dadosAlunos:
        if dadosAluno['RA'] != ra:
            novosDados.append(dadosAluno)

    with open('dadosJson/baseAlunos.json', 'w') as arquivo:
        json.dump(novosDados, arquivo, indent=2)

def pesquisaAluno( ra ):
    dadosAlunos = buscaDadosAlunos()

    retorno = []
    for dadosAluno in dadosAlunos:
        if dadosAluno['RA'] == ra:
            retornoAlunos = {
                "nome": dadosAluno['nome'],
                "turma":dadosAluno['turma'],
                "RA": ra,
                "email": dadosAluno['email']
            }

            retorno = retornoAlunos

    return retorno

def editarAluno( ra ):
    dadosAlunos = buscaDadosAlunos()

    novosDados = []
    for dadosAluno in dadosAlunos:
        if dadosAluno['RA'] != ra:
            novosDados.append(dadosAluno)
        else:
            novosDados.append(dadosAluno)

    with open('dadosJson/baseAlunos.json', 'w') as arquivo:
        json.dump(novosDados, arquivo, indent=2)

def buscaTurmasAlunos( ra ):
    dadosAluno = pesquisaAluno( ra )

    listaTurmas = dadosAluno['turma']
    retorno = turmas.buscaListaTurmas(listaTurmas)

    return retorno

def inserirTurmas( ra, listaTurmas ):
    dadosAlunos = buscaDadosAlunos()

    novosDados = []
    for dadosAluno in dadosAlunos:
        if dadosAluno['RA'] == ra:
            dadosAluno['turma'] = listaTurmas

        novosDados.append(dadosAluno)

    with open('dadosJson/baseAlunos.json', 'w') as arquivo:
        json.dump(novosDados, arquivo, indent=2)