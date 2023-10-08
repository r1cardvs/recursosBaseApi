import json
from modulos import alunos

def buscaDadosTurmas():
    with open('dadosJson/baseTurmas.json', 'r') as arquivo:
        retorno = json.load(arquivo)
    return retorno

def buscaQuantidadeTurmas():
    return len(buscaDadosTurmas())

def buscaListaTurmas( listaTurmas ):
    dadosTurmas = buscaDadosTurmas()
    turmasMatriculado = []
    turmasNaoMatriculado =[]
    for dadosTurma in dadosTurmas:
        retornoTurma = {
                'identificador': dadosTurma['identificador'],
                'nome': dadosTurma['nome']
            }
        if dadosTurma['identificador'] in listaTurmas:
            turmasMatriculado.append(retornoTurma)
        else:
            turmasNaoMatriculado.append(retornoTurma)

    retorno = {
        "matriculado":turmasMatriculado,
        "naoMatriculado":turmasNaoMatriculado
    }
    return retorno

def buscaAlunos( identificador ):
    dadosAlunos = alunos.buscaDadosAlunos()
    
    alunosMatriculados = []
    alunosNaoMatriculados = []

    for dadosAluno in dadosAlunos:
        if identificador in dadosAluno['turma']:
            alunosMatriculados.append( dadosAluno )
        else:
            alunosNaoMatriculados.append( dadosAluno )

    retorno = {
        "matriculado":alunosMatriculados,
        "naoMatriculado":alunosNaoMatriculados
    }

    return retorno

def buscaQuantidadeTurmasAluno(): 
    dadosAlunos = alunos.buscaDadosAlunos()
    dadosTurmas = buscaDadosTurmas()
    retorno = []
    for dadosTurma in dadosTurmas:
        quantidadeAlunos = 0
        for dadosAluno in dadosAlunos:
            if dadosTurma['identificador'] in dadosAluno['turma']:
                quantidadeAlunos = quantidadeAlunos + 1
        retornoTurma = {
            'nome':dadosTurma['nome'],
            'identificador':dadosTurma['identificador'],
            'quantidade':quantidadeAlunos
        }
        retorno.append( retornoTurma )

    return retorno