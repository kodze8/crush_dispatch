
class Mail_not_send(Exception):
    def __init__(self):
        msg = "Mail couldn't be send"
        super().__init__(msg)

class Inquiry_not_received(Exception):
    def __init__(self):
        msg = "Client inquiry cannot be received"
        super().__init__(msg)