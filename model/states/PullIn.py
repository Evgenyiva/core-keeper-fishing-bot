from constants import *
from model.State import State


class PullIn(State):
    def __init__(self, FSM, simpleName):
        super(PullIn, self).__init__(FSM, simpleName)

    def enter(self):
        super(PullIn, self).enter()

    def execute(self):
        super(PullIn, self).execute()

        self._pullLine()

        self.FSM.toTransition(TRANSITION_IDLE)

    def exit(self):
        super(PullIn, self).exit()

    def _isFishFighting(self):
        return self.FSM.bot.capture.checkAreaForColor(self.FSM.bot.settings.fishFightingViewArea)

    def _isCatchingBoxPresent(self):
        return self.FSM.bot.capture.checkAreaForColor(self.FSM.bot.settings.catchingBoxPresentViewArea)

    def _pullLine(self):
        self.FSM.bot.inputController.pressButton("f", duration=0.13, startDelay=0.25, endDelay=0.25)
