import datetime


class Flavors:
    """ Snapshot of flavors at a point time """
    def __init__(self):
        self.timestamp = datetime.timestamp()
        self.flavors = {}

    def flavors(self):
        return self.flavors

    def timestamp(self):
        return self.timestamp
