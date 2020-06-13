from flask import Flask, jsonify, request
from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse
from pprint import pprint

from . import sms_bp
from .functions.Scheduler import Scheduler

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
    return str(resp)

@sms_bp.route('/rq')
def schedule():
    # probably do some stuff here to make sure it's a valid request.
    print(request.form['body'])
    print('finished request ops')