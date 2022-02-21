# This Python file uses the following encoding: utf-8
from email import policy
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import pandas as pd
import configparser

def sendMail():

    # Von config.ini die SMTP-Auth-Daten einlesen
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")

    account = config["DEFAULT"]["Account"]
    password = config["DEFAULT"]["Password"]
    smtp = config["DEFAULT"]["smtp"]
    port = int(config["DEFAULT"]["port"])

    # error-log as df
    error_df = pd.read_csv("./link_error_log.csv", header=0)
    fb = list(set(error_df["Fachbereich"]))
    #print(fb)

    # Empfänger aus der linkCheckerPerso-Liste
    pers_df = pd.read_csv("./linkCheckPerso.csv", header=0)
    
    for i in fb:
        # error list pro fachbereich
        fb_error = error_df[error_df["Fachbereich"] == i]
        csv_object = fb_error.to_csv()

        fb_tbl = pers_df[pers_df["Fachbereich"] == i]
        fb_inCharge = list(set(fb_tbl["E-Mail"]))



        to_email = ", ".join(fb_inCharge)
        #print(to_email)
        from_email = "Automatischer Linkchecker"
        
        # MIME1 
        subject = "Bitte Links überprüfen"
        message = "Bitte Links überprüfen"
        msg = MIMEMultipart(policy=policy.default)
        
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email
        msg.attach(MIMEText(message))

        part = MIMEBase('text', "csv")
        part.set_payload(csv_object)
        # wegen Umlaut oder sonstige non-ascii-Zeichen
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="link_error.csv"')
        msg.attach(part)
        
        # Mail abschicken
        server = smtplib.SMTP(smtp, port)
        server.starttls()
        server.login(account, password)
        server.send_message(msg)
        server.quit()


if __name__ == "__main__":
    sendMail()