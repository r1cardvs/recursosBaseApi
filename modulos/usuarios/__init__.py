import json
import secrets
import string
import base64
from modulos import seguranca

def buscaDadosUsuarios():
    with open('dadosJson/baseUsuarios.json', 'r') as arquivo:
        dados_json = json.load(arquivo)
    return dados_json

def cadastrarUsuario(usuario, tipo):
    dadosUsuarios = buscaDadosUsuarios()

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for i in range(20))

    senhaEncriptada = seguranca.encriptar( senha )

    novoUsuario = {
        "usuario": usuario,
        "senha": base64.b64encode(senhaEncriptada).decode(),
        "tipo": tipo,
        "resetSenha": True
    }

    dadosUsuarios.append(novoUsuario)

    with open('dadosJson/baseUsuarios.json', 'w') as arquivoUsuarios:
        json.dump(dadosUsuarios, arquivoUsuarios, indent=2)

    return senha
    
def redefinirSenha( ra, novaSenha ):
    dadosUsuarios = buscaDadosUsuarios()

    novosDados = []
    for dadosUsuario in dadosUsuarios:
        if dadosUsuario['usuario'] != ra:
            novosDados.append(dadosUsuario)
        else:
            elementoAluno = {
                "usuario":dadosUsuario['usuario'],
                "senha":novaSenha,
                "tipo":dadosUsuario['tipo'],
                "resetSenha":True
            }
            novosDados.append(elementoAluno)

    with open('dadosJson/baseUsuarios.json', 'w') as arquivoRedefinirSenha:
        json.dump(novosDados, arquivoRedefinirSenha, indent=2)
