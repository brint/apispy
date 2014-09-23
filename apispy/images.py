import datetime


class Images:
    """ Snapshot of images at a point time """
    def __init__(self):
        self.timestamp = datetime.timestamp()
        self.images = {}

    def images(self):
        return self.images

    def timestamp(self):
        return self.timestamp
