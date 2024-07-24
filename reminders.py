import datetime

class Reminders:
    def __init__(self, type, timedate, urgency, description, title):
        self.type = type
        self.timedate = timedate
        self.urgency = urgency
        self.description = description
        self.title = title

    def format_timedate(self):
        # Format timedate
        return self.timedate.strftime("%Y-%m-%d %H:%M")
