class ColorTrigger:
    r: int = 0
    g: int = 0
    b: int = 0
    percentage: int = 0

    def __init__(self, red: int = 0, green: int = 0, blue: int = 0, percentage: int = 0):
        self.r: int = red
        self.g: int = green
        self.b: int = blue
        self.percentage: int = percentage

    def getMin(self, color):
        return color - (255 / 100 * self.percentage)

    def getMax(self, color):
        return color + (255 / 100 * self.percentage)

    def _inRange(self, color, checkColor):
        return self.getMin(color) < checkColor < self.getMax(color)

    def isInRange(self, color):
        if self._inRange(color[0], self.r) and self._inRange(color[1], self.g) and self._inRange(color[2], self.b):
            return True

        return False
