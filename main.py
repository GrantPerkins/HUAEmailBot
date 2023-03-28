import smtplib
from email.mime.text import MIMEText
import pandas as pd


def send_email(subject, body, sender, recipients, password):
    """
    Build email and send it
    :param subject: text subject
    :param body: email body (html)
    :param sender: who i am i
    :param recipients: who are you?
    :param password: my password
    :return: None
    """
    msg = MIMEText(body, "html")
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

# build email template, load meta data
subject = "hex speculative literary journal is open for submissions—help spread the word?"
with open("body.html", 'r', encoding="utf8") as f:
    body_template = ''.join(f.readlines())
sender = "gcperk20@gmail.com"
recipients = ["gcperkins@wpi.edu"]
with open("creds.txt", 'r') as f:
    password = f.readline().strip()

# loop through sheet, spam emails
df = pd.read_csv("mfa_emails.csv")
df = df[df["2023 student name"] == "Sapphire"]
for index, row in df.iterrows():
    recipients = [row["head"]]
    school = row["school"]
    body = body_template.replace("[xyz]", school)
    send_email(subject, body, sender, recipients, password)
    print(school)
