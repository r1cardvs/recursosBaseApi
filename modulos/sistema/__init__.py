import json
from modulos import alunos, professores, turmas

def relacaoTiposUsuario():
    quantidadeAlunos = alunos.buscaQuantidadeAlunos()
    quantidadeTurmas = turmas.buscaQuantidadeTurmas()
    quantidadeProfessores = professores.buscaQuantidadeProfessores()

    retorno =[
        {
            'entidade':'Alunos',
            'quantidade': quantidadeAlunos
        },
        {
            'entidade':'Professores',
            'quantidade': quantidadeProfessores
        },
        {
            'entidade':'Turmas',
            'quantidade': quantidadeTurmas 
        }
    ]

    return retorno