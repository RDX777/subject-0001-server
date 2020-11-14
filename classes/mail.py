import smtplib
from email.message import EmailMessage

from classes.dadoslocal import Local

class MandarEmails:

    def __init__(self):
        d = Local()
        self.email_de = d.get_dados('email', 'de', 'one')[2]
        #encminha para uma lista de e-mail no campo para
        #cadastrar no banco igualmente somente mudar o endereço de email
        self.email_para = d.get_dados('email', 'para', 'all')
        listadeemails = []
        for emailpara in self.email_para:
            listadeemails.append(emailpara[2])
        self.email_para = listadeemails
        self.servidor_smtp = d.get_dados('email', 'smtp', 'one')[2]
        self.servidor_smpt_porta = d.get_dados('email', 'porta', 'one')[2]
        self.servidor_smtp_senha = d.get_dados('email', 'senha', 'one')[2]

        print(self.email_para)

    def mandar_mensagem(self, texto_mensagem, titulo_mensagem):
        e = EmailMessage()
        e.set_content(texto_mensagem)
        e['Subject'] = titulo_mensagem
        e['From'] = self.email_de
        e['To'] = self.email_para
        s = smtplib.SMTP(self.servidor_smtp, self.servidor_smpt_porta)
        s.starttls()
        s.login(self.email_de, self.servidor_smtp_senha)
        s.send_message(e)
        s.quit()
