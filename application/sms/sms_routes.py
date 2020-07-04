from flask import Flask, jsonify, request
from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse
from pprint import pprint
import uuid

from . import sms_bp
from application.util.Parser import Parser
from application.services.Scheduler import SMSScheduler
from application.services.Messager import Messager

@sms_bp.route("/", methods=["GET", "POST"])
def home():
    #people = [{"name":"John", "id":"12333", "color":"Blue"}, {"name":"Brett", "id":"12345", "color":"Green"}]

    # apiResp = {
    #     "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    #     "api_version": "2010-04-01",
    #     "body": "McAvoy or Stewart? These timelines can get so confusing.",
    #     "date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
    #     "date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
    #     "date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
    #     "direction": "outbound-api",
    #     "error_code": "",
    #     "error_message": "",
    #     "from": "+15017122661",
    #     "messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    #     "num_media": "0",
    #     "num_segments": "1",
    #     "price": "",
    #     "price_unit": "",
    #     "sid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    #     "status": "sent",
    #     "subresource_uris": {
    #         "media": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json"
    #     },
    #     "to": "+15558675310",
    #     "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json"
    # }

    resp = MessagingResponse()

    resp.message("HI :)")

    # this is the whole of the data that is sent in the request
    #pprint(request.form)

    pprint(request.form)


    #return jsonify(apiResp)
    s = SMSScheduler()
    s.addJob(datetime(2020, 7, 2, 22, 39, 0), 'job_1', 3)
    print('first added.')
    s.addJob(datetime(2020, 7, 2, 22, 40, 0), 'job_2', 3)
    print('second added.')

    return str(resp)

@sms_bp.route("/t", methods=["GET", "POST"])
def test():
    #app.post('/rq', data=dict(body='+ @12:00 "Get coffee" #1234567899'))
    pass

@sms_bp.route('/rq')
def schedule():
    rq = request.form['body']
    #rq = '+ @21:18 "Get coffee" #3216549879'
    p = Parser(rq)
    if p.requestIsValid():
        if p.getType() == 'add':
            s = SMSScheduler()
            msg = p.getMessage()
            rcp = p.getRecipients()
            times = p.getTimes()
            #m = Messager().sendMessage(receiver=rcp, msg=msg)        

            for t in times:
                print('added...')
                j_id = str(uuid.uuid4())[:8]
                s.addJob(t, j_id, 1, {'msg':msg, 'rcp':rcp})
            # store the missive in the DB
            # schedule the times for the missive
            #s.addJob()
            return 'add'
        elif Parser.getType(rq) == 'remove':
            return 'remove'
        elif Parser.getType(rq) == 'info':
            return 'info'
        elif Parser.getType(rq) == 'help':
            return 'help'
        else:
            return 'none'
        # handle the task based on type from Parser.getType()
            # if 'add': schedule add (build this in the scheduler) and send message.
    else:
        return 'invalid request received'
    # Handler picks up the *valid* request
    print(rq)
    print('finished request ops')
