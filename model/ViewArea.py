from model.ColorTrigger import ColorTrigger
from model.Coordinate import Coordinate


class ViewArea(object):

    def __init__(self, startPosition: Coordinate, endPosition: Coordinate, windowTag: str, viewWidth: int,
                 viewHeight: int,
                 colorTrigger: ColorTrigger = None):

        self.startPosition: Coordinate = startPosition
        self.endPosition: Coordinate = endPosition
        self.windowTag: str = windowTag
        self.viewWidth: int = viewWidth
        self.viewHeight: int = viewHeight
        self.triggerColor: ColorTrigger = colorTrigger

    @property
    def width(self):
        return self._calculateSize(self.startPosition.x, self.endPosition.x)

    @property
    def height(self):
        return self._calculateSize(self.startPosition.y, self.endPosition.y)

    @property
    def widthIteration(self):
        if self.width > self.height:
            return self._getIteration(self.viewWidth, self.width)
        else:
            return self._getIteration(self.viewWidth, self.height)

    @property
    def heightIteration(self):
        if self.width > self.height:
            return self._getIteration(self.viewHeight, self.height)
        else:
            return self._getIteration(self.viewHeight, self.width)

    @staticmethod
    def _calculateSize(startPosition, endPosition):
        return endPosition - startPosition

    @staticmethod
    def _getIteration(a, b):
        c = int(a / b)
        if c == 0:
            return 1

        return c
