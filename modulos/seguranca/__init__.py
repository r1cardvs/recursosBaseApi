from cryptography.fernet import Fernet
import json
import base64

def encriptar( mensagem ):
    chave = getChave()
    cipher_suite = Fernet(chave)
    retorno = cipher_suite.encrypt(mensagem.encode())
    return retorno

def descriptar( mensagemEncripitada ):
    chave = getChave()
    cipher_suite = Fernet(chave)
    retorno = cipher_suite.decrypt(mensagemEncripitada).decode()
    return retorno

def getChave():
    with open('dadosJson/baseConfiguracoesSistema.json', 'r') as arquivo:
        dadosSeguranca = json.load(arquivo)
        chave = dadosSeguranca['key']
        if( chave == "" ):
            chave = Fernet.generate_key()
            chaveBase64 = base64.b64encode(chave).decode()
            dadosSeguranca = {
                "key":chaveBase64
            }
        else:
            chave = base64.b64decode(chave.encode())

    with open('dadosJson/baseConfiguracoesSistema.json', 'w') as arquivoUsuarios:
        json.dump(dadosSeguranca, arquivoUsuarios, indent=2)
    return chave