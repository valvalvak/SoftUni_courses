class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.increace = 0

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        time = {"hours": self.hours, "minutes": self.minutes, "seconds": self.seconds}
        for times, digits in time.items():
            if len(str(digits)) < 2:
                time[times] = "0" + str(digits)
            else:
                time[times] = str(digits)
        return f"{time['hours']}:{time['minutes']}:{time['seconds']}"

    def next_second(self):
        if self.seconds + 1 <= Time.max_seconds:
            self.seconds += 1
            return self.get_time()
        else:
            self.seconds = 0
            self.increace = 1
        if self.increace:
            if self.minutes + self.increace <= Time.max_minutes:
                self.minutes += self.increace
                self.increace = 0
                return self.get_time()
            else:
                self.minutes = 0
        if self.increace:
            if self.hours + self.increace <= Time.max_hours:
                self.hours += self.increace
                return self.get_time()
            else:
                self.hours = 0
        return self.get_time()

# time = Time(99, 58, 67)
# print(time.next_second())
# time = Time(10, 59, 59)
# print(time.next_second())
# time = Time(23, 59, 59)
# print(time.next_second())
