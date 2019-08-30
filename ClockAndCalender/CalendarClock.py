from .Clock import Clock
from .Calendar import Calendar


class CalendarClock (Clock, Calendar):

    def __init__(self, day, month, year, hour, minute, second):
        Clock.__init__(self, hour, minute, second)
        Calendar.__init__(self, day, month, year)

    def tick(self):
        previous_hour = self._hour
        Clock.tick(self)
        if (self._hour < previous_hour):
            self.advance()

    def __str__(self):
        return Calendar.__str__(self) + ", " + Clock.__str__(self)



x = CalendarClock(31, 12, 2013, 23, 59, 59)
print("One tick from ", x, end=" ")
x.tick()
print("to ", x)