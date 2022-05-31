from model.State import State
from constants import *


class FishFighting(State):
    def __init__(self, FSM, simpleName):
        super(FishFighting, self).__init__(FSM, simpleName)

    def enter(self):
        super(FishFighting, self).enter()

    def execute(self):
        super(FishFighting, self).execute()

        if self.checkForFishBox():
            self._handleCatching()
        else:
            self.FSM.bot.fishCounter += 1
            self.FSM.bot.view.getByKey(VIEW_CATCHED_FISHES_KEY).update(self.FSM.bot.fishCounter)
            self.FSM.toTransition(TRANSITION_PULL_IN)

    def exit(self):
        super(FishFighting, self).exit()

    def _handleCatching(self):
        if self._isFishFighting():
            self._releaseLine()
        else:
            self._pullLine()

    def _isFishFighting(self):
        return self.FSM.bot.capture.checkAreaForColor(self.FSM.bot.settings.fishFightingViewArea)

    def checkForFishBox(self):
        return self.FSM.bot.capture.checkAreaForColor(self.FSM.bot.settings.catchingBoxPresentViewArea)

    def _pullLine(self):
        self.FSM.bot.inputController.pressF()

    def _releaseLine(self):
        self.FSM.bot.inputController.releaseF()
