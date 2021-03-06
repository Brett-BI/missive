from datetime import datetime
import time

class TimeValidator():
    @staticmethod
    def validateTime(time_list: [str]) -> bool:
        for t in time_list:
            try:
                _t = time.strptime(t, '%H:%M')
            except:
                return False
        
        return True

    @staticmethod
    def convertTimeToDateTime(year: int, month: int, day: int, time: time) -> datetime:
        
        # returns an array of datetime elements
        # will validate times first?
        pass
    
    def isFutureDate(self, dt: datetime) -> bool:
        if dt > datetime.today():
            return True
        return False
    
    def convertStringToTime(self, time_list: [str]) -> [time]:
        # check that elements are strings
        # _time_list = []

        # for t in time_list:
        #     if not isinstance(t, str):
        #         print('Item in time_list is not a string. Cannot convert to Time object.')
            
        #     _time_list.append(time.strptime(t, '%H:%M'))
        
        # return _time_list
        pass


v = TimeValidator()
print(v.isFutureDate(datetime(2020, 7, 2, 20, 10, 0)))