import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import app.base.QException as qex
import app.base.Cifra as Cifra

class qMail():
    
    def __init__(self, smtpAddress, port, user, password):
        self.__smtpAddress = smtpAddress
        self.__port = port
        self.__user = user
        self.__password = password

    def enviaInstrucoesNovaSenha(self, emailDestination, ID_USUARIO):
        try:
            message = MIMEMultipart()
            message["From"] = self.__user
            message["To"] = emailDestination
            message["Subject"] = 'Datamigra - Definição de nova senha'

            cifrada = Cifra.cifra(ID_USUARIO)
            link = ''

            html = ''.join(("<br>Clique no link abaixo para acessar a área de <b>reset</b> de sua senha:<br><br>",
                    "<a href='" + link + "?view=" + cifrada + "'>" + link + "</a><br><br>"))

            part = MIMEText(html, "html")
            message.attach(part)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(self.__smtpAddress, self.__port, context=context) as server:
                server.login(self.__user, self.__password)
                server.send_message(self.__user, emailDestination, message.as_string())

        except Exception as ex:
            qex.throw(ex)

        finally:
            server.quit()

    def __del__(self):
        pass