from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'morizehenrique@gmail.com'
app.config['MAIL_PASSWORD'] = 'Ohomeméolobodohomem*'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

def enviarEmailSenha( emailAluno,senha ):

    destinatario = emailAluno
    assunto = "Sua senha foi resetada"
    corpo = "Nova senha ="
    
    corpo = '''
        <h6>Nova senha cadastrada</h6>
        <button>Nova senha gerada</button>
    '''

    msg = Message(assunto, sender='rck13campos@gmail.com', recipients=[destinatario])
    msg.body = corpo

    mail.send(msg)
    return "E-mail enviado com sucesso!"


if __name__ == '__main__':
    app.run(debug=True)
