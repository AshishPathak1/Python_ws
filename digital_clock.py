from datetime import date, datetime
import abc
class Calendar(metaclass = abc.ABCMeta):
    def __init__(self):
        today = date.today()
        today = str(today)
        today = today.split('-')
        self.__date = today[-1]
        self.__month = today[1]
        self.__year = today[0]

    @abc.abstractclassmethod
    def get_date(self):
        return date.today()

    @abc.abstractclassmethod
    def set_date(self, d, m, y):
        self.__date = d
        self.__month = m
        self.__year = y
        return "Date has been changed"

    def __str__(self):
        return "Hello, from calendar class"

class Clock(metaclass = abc.ABCMeta):
    def __init__(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_time = current_time.split(':')
        self.__hour = current_time[0]
        self.__min = current_time[1]
        self.__sec = current_time[-1]

    @abc.abstractclassmethod
    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")

    @abc.abstractclassmethod
    def set_time(self, h, m, s):
        self.__hour = h
        self.__min = m
        self.__sec = s
        return "Time has been changed"
      
    def __str__(self):
        return "Hello from clock class"

class DigitalClock(Calendar, Clock):
    def __init__(self):
        Calendar.__init__(self)
        Clock.__init__(self)

    def get_time(self):
        return super().get_time()

    def set_time(self, h, m, s):
        return super().set_time(h, m, s)

    def get_date(self):
        return self.get_date()

    def set_date(self, d, m, y):
        return self.set_date(d, m, y)
 
    def __str__(self):
        return "Hello from digital clock class"

if __name__ == '__main__':
    dc = DigitalClock()
    ans = dc.get_time()
    print(ans)
