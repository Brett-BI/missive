from abc import ABC, abstractmethod

class HandlerInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def processRequest(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

class AddHandler(HandlerInterface):
    def __init__(self, times, messages, recipients):
        self.times = times
        self.messages = messages
        self.recipients = recipients

    def processRequest(self):
        # validate elements of the missive
        # db handler to log the request (make sure to update the db if anything fails!)
        # schedule the task
        # send "ok!" message to the user

    def validateElements(self):
        pass

    def __str__(self):
        print({'times':self.times, 'messages':self.messages, 'recipients':self.recipients})

    def __repr__(self):
        return({'times':self.times, 'messages':self.messages, 'recipients':self.recipients})

ah = AddHandler(times=['@12:00', '@14:00'], messages=['Get that bread.'], recipients=['1231231234', '2342342344'])
ah.__str__()
print(ah.__repr__())