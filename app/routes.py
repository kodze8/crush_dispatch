from flask import Flask, render_template, request
from app.model import mail_processor, app_exceptions


def register_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            client_mail = request.form["client_mail"]
            inquiry = request.form["inquiry"]
            try:
                mail_processor.receive_email(client_mail, inquiry)
            except Exception:
                # error
                return render_template("letter_response.html")
            else:
                # success
                return render_template("letter_response.html")
        else:
            return render_template("home.html")

    @app.route("/send_letter", methods=["GET", "POST"])
    def send_letter():
        if request.method == "POST":
            address = request.form["address"]
            letter = request.form["letter"]
            subject = request.form["subject"]
            try:
                if subject == "":
                    mail_processor.send_email(address, letter)
                else:
                    mail_processor.send_email(address, letter, subject)
            except app_exceptions.Mail_not_send:
                # error
                return render_template("letter_response.html")
            except Exception:
                # error
                return render_template("letter_response.html")
            else:
                # success
                return render_template("letter_response.html")
        else:
            return render_template("send_letter.html")

    @app.route("/love_poems")
    def love_poems():
        return render_template("love_poems.html")
