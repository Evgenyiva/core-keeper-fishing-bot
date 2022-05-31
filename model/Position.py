class Position:
    color = [0, 0, 0]

    def r(self):
        return self.color[0]

    def g(self):
        return self.color[1]

    def b(self):
        return self.color[2]

    def __init__(self, coordinate):
        self.coordinate = coordinate

    def colorHex(self):
        return '#%02x%02x%02x' % (self.color[0], self.color[1], self.color[2])
