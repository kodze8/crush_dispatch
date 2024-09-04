import smtplib
from app.model import app_exceptions

sender = "crushdispatch@gmail.com"
password = "pars fkya yjqf sozd"

SUBJECT_DEFAULT_TEXT = "Letter from your crush"

def __generate_msg(body, subject):
    if subject is None:
        subject = SUBJECT_DEFAULT_TEXT

    with open("../templates/email_layout.html", "r") as file:
        html_content = file.read()

    html_content = html_content.replace("{{subject}}", subject)
    html_content = html_content.replace("{{body}}", body)

    msg = f"Content-Type: text/html\nSubject: {subject}\n\n{html_content}"
    return msg


def send_email(receiver, body, subject=None):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, msg=__generate_msg(body, subject))
        return True
    except smtplib.SMTPException:
        raise app_exceptions.Mail_not_send()


def __generate_inquiry_message(client_mail, body):
    return f"\nuser mail:{client_mail}\n{body}"


def receive_email(client_mail, body):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.sendmail(sender, sender, msg=__generate_inquiry_message(client_mail, body))
    except smtplib.SMTPException:
        raise app_exceptions.Inquiry_not_received()


if __name__ == '__main__':
    print("Sending...")
    rec = "barbaresaikodze@gmail.com"
    bod = "Lorem ipsum dolor sit amet,  Ut enim ad minim veniam, quis nostrud exercitation "
    send_email(rec, bod)
