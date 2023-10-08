import json
from modulos import turmas

def buscaDadosProfessores():
    with open('dadosJson/baseProfessores.json', 'r') as arquivo:

        dados_json = json.load(arquivo)
    return dados_json

def buscaQuantidadeProfessores():
    return len(buscaDadosProfessores())

def buscaDadosTurmas( identificador ):
    dadosTurmas = turmas.buscaDadosTurmas()
    retorno = []

    for dadosTurma in dadosTurmas:
        print(identificador)
        print(dadosTurma['professor'])
        if identificador == dadosTurma['professor']:
            retorno.append( dadosTurma )
    print(retorno)
    return retorno

