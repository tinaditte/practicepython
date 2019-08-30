class Clock(object):

    def __init__(self, hours, minutes, seconds):
        self.set_Clock(hours, minutes, seconds)

    def set_Clock(self, hours, minutes, seconds):
        if type(hours) == int and 0 <= hours and hours < 24:
            self._hours = hours
        else:
            raise TypeError("Hours have to be integers between 0 and 23")

        if type(minutes) == int and 0 <= minutes and minutes < 60:
            self.__minutes = minutes
        else:
            raise TypeError("Minutes have to be integers between 0 and 59")

        if type(seconds) == int and 0 <= seconds and seconds < 60:
            self.__seconds = seconds
        else:
            raise TypeError("Seconds have to be integers between 0 and 59")

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self._hours, self.__minutes, self.__seconds)

    def tick(self):
        """
        Lets the clock 'tick' --> internal time will be advanced by 1 sec.
            Example:
            x = Clock(12,59,59)
            print(x)
            -12:59:59
            x.tick()
            print(x)
            13:00:00
        """

        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self._hours == 23:
                    self.hours = 0
                else:
                    self._hours += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1
