from flask import Flask, render_template, request
from app.model import mail_processor, app_exceptions

SUCCESS = "Headed to the one who needs to know!"
ERROR = "Something went wrong...\n\nTry later!"


def register_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            client_mail = request.form["client_mail"]
            inquiry = request.form["inquiry"]
            try:
                mail_processor.receive_email(client_mail, inquiry)
            except app_exceptions.Inquiry_not_received:
                return render_template("letter_response.html", response=ERROR)
            else:
                return render_template("letter_response.html", response=SUCCESS)
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
                return render_template("letter_response.html", response="ERROR")
            else:
                return render_template("letter_response.html", response=SUCCESS)
        else:
            return render_template("send_letter.html")

    @app.route("/love_poems")
    def love_poems():
        return render_template("love_poems.html")
