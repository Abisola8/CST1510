# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self, percent):
        self.percent = percent

    def status(self):    # this parameter should be self
        return self.percent

r = Record(95)
print(r.status())
