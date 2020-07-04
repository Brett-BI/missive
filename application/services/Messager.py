from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

class Messager():
    def sendMessage(self, receiver: str, msg: str):
        account = ''
        auth = ''
        _from = ''
        client = Client(account, auth)

        client.messages.create(body=msg, from_=_from, to=receiver)