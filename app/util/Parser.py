from abc import ABC, abstractmethod
import re
from datetime import datetime, timedelta

class Parser():
    def __init__(self, msg_body: str):
        self.msg_body = msg_body

    def getElements(self):
        pass

    def getMessage(self):
        messages = []
        split_messages = re.findall(r'(\"[^\"]*\")', self.msg_body)

        for r in split_messages:
            messages.append(r.strip())

        return messages

    def getRecipients(self):
        recipients = []
        split_recipients = re.findall(r'(#\d+)', self.msg_body)

        for r in split_recipients:
            recipients.append(r.strip(' #'))
        
        return recipients

    # make sure that this returns a datetime object (all calculations go here for now)
    def getTimes(self) -> [datetime]:
        times = []
        # parse time elements
        split_times = re.findall(r'(@\d+:?\d+\s*\w*)', self.msg_body)

        # get datetimes from time elements
        for t in split_times:
            try:
                _time = self.convertStringToDateTime(t.strip().replace('@', ''))
                if _time:
                    times.append(_time)
            except CouldNotConvertToDateTimeError as e:
                print(e.message)
        # add to times

        # for t in split_times:
        #     times.append(t.strip(' @'))

        print('ALL TIMES:')

        return times
    
    def convertStringToDateTime(self, dt: str) -> datetime:
        # regex match dt to a format string
        rg = self.getStrptimeFormatString(dt)
        print(f'dt: {dt}')
        print(f'rg: {rg}')
        # apply format string to strftime (or may strptime, whichever one)
        if rg:
            _time = datetime.strptime(dt, rg)
            print(datetime.strptime(dt, rg))
            if (datetime.today().hour >= _time.hour) and (datetime.today().minute >= _time.minute):
                print('time has past. do it tomorrow.')
                _dt = datetime(datetime.today().year, datetime.today().month, datetime.today().day, _time.hour, _time.minute, 0) + timedelta(days=1)
                return _dt
            else:
                print('there is still time today...')
                _dt = datetime(datetime.today().year, datetime.today().month, datetime.today().day, _time.hour, _time.minute, 0)
                return _dt
            #calc hour/day: current day or next day?
        else:
            raise CouldNotConvertToDateTimeError(dt)
        # return a DateTime
        

    def getStrptimeFormatString(self, dt: str) -> str:
        # dict where the key is the regex and value is the format string
        rg_dict = {
            r'^0?(1|2|3|4|5|6|7|8|9|10|11|12)(:\d\d)\s(a|p|am|pm|AM|PM)$':'%I:%M %p',
            r'^0?(1|2|3|4|5|6|7|8|9|10|11|12)(:\d\d)(a|p|am|pm|AM|PM)$':'%I:%M%p',
            r'^0?(1|2|3|4|5|6|7|8|9|10|11|12)\s(a|p|am|pm|AM|PM)$':'%I:00 %p',
            r'^0?(1|2|3|4|5|6|7|8|9|10|11|12)(a|p|am|pm|AM|PM)$':'%I:00%p',
            r'^[0-9]{1,2}:\d\d$':'%H:%M',
            r'^[0-9]{1,2}$':'%H:%M'
        }

        # return the strftime format string if found, otherwise empty string (since this is 'falsey')
        for r in rg_dict:
            print(f'rematch: {re.findall(r, dt)}')
            print(f'r: {r}')
            if re.findall(r, dt):
                print(f'match found {r}')
                return rg_dict[r]
            else:
                print(f'did not match: {r}')

        print('no match found')
        return ''

    def parseMissiveID(self):
        message = re.findall(r'(\d+)', self.msg_body)

        return message
    
    def getType(self):
        if self.msg_body[0] == '+':
            return 'add'
        if self.msg_body[0] == '-':
            return 'remove'
        if self.msg_body[0] == '!':
            return 'info'
        if self.msg_body[0] == '?':
            return 'help'
        else:
            return 'none'
    
    def requestIsValid(self):
        if self.getType() == 'add':
            if len(self.getMessage()) > 0 and len(self.getRecipients()) > 0 and len(self.getTimes()) > 0:
                return True
            else: 
                return False
        elif self.getType() == 'remove':
            return True
        elif self.getType() == 'info':
            return True
        elif self.getType() == 'help':
            return True
        else:
            return False
    
    
class CouldNotConvertToDateTimeError(Exception):
    def __init__(self, dt_string, message="Could not convert value to DateTime."):
        self.dt_string = dt_string
        self.message = f'Could not convert {type(self.dt_string).__name__}:"{self.dt_string}" to DateTime.'
    
    def __str__(self):
        return f'Could not convert "{self.dt_string}" to DateTime.'

p = Parser('+ @14:41 @21:00 "do something" #1231231234').getTimes()
print(p)

# class ParserInterface(ABC):
#     @staticmethod
#     def __init__(self):
#         pass

#     @staticmethod
#     def getElements(self):
#         pass

#     @staticmethod
#     def isValid(self):
#         pass

#     @staticmethod
#     def __repr__(self):
#         pass

# class AddParser(ParserInterface):
#     def __init__(self, msg_body):
#         self.msg_body = msg_body
#         self.times = self.parseTimes()
#         self.reminder = self.parseReminder()
#         self.receivers = self.parseReceivers()
#         self.elements = []

#     def getElements(self):
#         for t in self.times:
#             self.elements.append(t)

#         for m in self.reminder:
#             self.elements.append(m)

#         for r in self.receivers:
#             self.elements.append(r)

#         return self.elements

#     def parseTimes(self):
#         times = []
#         split_times = re.findall(r'(@\d+:\d+\s*\w*)', self.msg_body)

#         for t in split_times:
#             times.append(t.strip())

#         return times
    
#     def parseReceivers(self):
#         receivers = []
#         split_receivers = re.findall(r'(#\d+)', self.msg_body)

#         for r in split_receivers:
#             receivers.append(r.strip())
        
#         return receivers

#     def parseReminder(self):
#         reminders = []
#         split_reminders = re.findall(r'(\"[^\"]*\")', self.msg_body)

#         for r in split_reminders:
#             reminders.append(r.strip())

#         return reminders
    
#     def isValid(self):
#         if self.times.len() > 0 AND self.receivers.len() > 0 AND self.msg_body.len() > 0:
#             return True
#         else:
#             return False

#     def __repr__(self):
#         return self.msg_body

# class RemoveParser(ParserInterface):
#     def __init__(self, sms_msg):
#         self.sms_msg = sms_msg
#         self.missive_id = self.parseMissiveID()
#         self.elements = []
    
#     def getElements(self):
#         for m in self.missive_id:
#             self.elements.append(m.strip())
        
#         return self.elements

#     def parseMissiveID(self):
#         message = re.findall(r'(\d+)', self.sms_msg)

#         return message
    
#     def isValid(self):
#         if self.missive_id.len() > 0 AND self.msg_body.len() > 0:
#             return True
#         else:
#             return False
    
#     def __repr__(self):
#         return self.sms_msg

# class InfoParser(ParserInterface):
#     def __init__(self, sms_msg):
#         self.sms_msg = sms_msg
#         self.times = self.parseTimes()
#         self.elements = []
    
#     def getElements(self):
#         for t in self.times:
#             self.elements.append(t)

#         return self.elements

#     def parseTimes(self):
#         times = []
#         split_times = re.findall(r'(@\d+:\d+\s*\w*)', self.sms_msg)

#         for t in split_times:
#             times.append(t.strip())

#         return times
    
#     def isValid(self):
#         if self.times.len() > 0 AND self.sms_msg.len() > 0:
#             return True
#         else:
#             return False
    
#     def __repr__(self):
#         return self.sms_msg

# class HelpParser(ParserInterface):
#     pass
