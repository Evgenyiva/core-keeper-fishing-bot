from model.ViewArea import ViewArea
from model.Coordinate import Coordinate


class Settings(object):
    def __init__(self,
                 rodPresentViewArea: ViewArea,
                 baitViewArea: ViewArea,
                 fishFightingViewArea: ViewArea,
                 catchingBoxPresentViewArea: ViewArea,
                 castRodClickPosition: Coordinate):
        self.rodPresentViewArea: ViewArea = rodPresentViewArea
        self.baitViewArea: ViewArea = baitViewArea
        self.fishFightingViewArea: ViewArea = fishFightingViewArea
        self.catchingBoxPresentViewArea: ViewArea = catchingBoxPresentViewArea
        self.castRodClickPosition: Coordinate = castRodClickPosition

