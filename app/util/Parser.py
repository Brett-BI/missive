from abc import ABC, abstractmethod
import re
from datetime import datetime

class Parser():
    def __init__(self):
        pass

    def getElements(msg_body):
        pass

    def getMessage(msg_body):
        messages = []
        split_messages = re.findall(r'(\"[^\"]*\")', msg_body)

        for r in split_messages:
            messages.append(r.strip())

        return messages

    def getRecipients(msg_body):
        recipients = []
        split_recipients = re.findall(r'(#\d+)', msg_body)

        for r in split_recipients:
            recipients.append(r.strip(' #'))
        
        return recipients

    # make sure that this returns a datetime object (all calculations go here for now)
    def getTimes(msg_body: str) -> [datetime]:
        times = []
        # parse time elements
        split_times = re.findall(r'(@\d+:\d+\s*\w*)', msg_body)

        # get datetimes from time elements
        for t in split_times:
            try:
                Parser.convertStringToDateTime(t)
            except CouldNotConvertToDateTimeError as e:
                print(e.message)
        # add to times

        for t in split_times:
            times.append(t.strip(' @'))

        return times
    
    def convertStringToDateTime(dt: str) -> datetime:
        # regex match dt to a format string
        rg = findRegexMatch(dt)
        # apply format string to strftime (or may strptime, whichever one)
        # calculate that DateTime within the next 24 hours
        # return a DateTime
        raise CouldNotConvertToDateTimeError('dt_string_here')

    def findRegexMatch(dt: str) -> str:
        # dict where the key is the regex and value is the format string
        rg_dict = {'^0?(1|2|3|4|5|6|7|8|9|10|11|12)(:\d\d)\s?(a|p|am|pm|AM|PM|a.m.|p.m.|A.M.|P.M.)$':''}

    def parseMissiveID(msg_body):
        message = re.findall(r'(\d+)', msg_body)

        return message
    
    def getType(msg_body):
        if msg_body[0] == '+':
            return 'add'
        if msg_body[0] == '-':
            return 'remove'
        if msg_body[0] == '!':
            return 'info'
        if msg_body[0] == '?':
            return 'help'
        else:
            return 'none'
    
    def requestIsValid(msg_body):
        if Parser.getType(msg_body) == 'add':
            if len(Parser.getMessage(msg_body)) > 0 and len(Parser.getRecipients(msg_body)) > 0 and len(Parser.getTimes(msg_body)) > 0:
                return True
            else: 
                return False
        elif Parser.getType(msg_body) == 'remove':
            return True
        elif Parser.getType(msg_body) == 'info':
            return True
        elif Parser.getType(msg_body) == 'help':
            return True
        else:
            return False
    
    
class CouldNotConvertToDateTimeError(Exception):
    def __init__(self, dt_string, message="Could not convert value to DateTime."):
        self.dt_string = dt_string
        self.message = f'Could not convert {type(self.dt_string).__name__}:"{self.dt_string}" to DateTime.'
    
    def __str__(self):
        return f'Could not convert "{self.dt_string}" to DateTime.'

p = Parser.getTimes('+ @12:00 "do something" #1231231234')
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
