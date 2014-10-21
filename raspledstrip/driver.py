class Driver(object):

    def __init__(self, dev="/dev/null"):
        self.dev = dev

    def update(self, buffer):
        raise RuntimeError('Error: update() function from base class called, shouldn''t happen!')