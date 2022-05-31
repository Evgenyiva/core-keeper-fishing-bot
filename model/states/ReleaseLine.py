from constants import *
from controller.InputController import InputController
from model.State import State


class ReleaseLine(State):
    def __init__(self, FSM, simpleName):
        super(ReleaseLine, self).__init__(FSM, simpleName)
        self._clickController = InputController()

    def enter(self):
        super(ReleaseLine, self).enter()

    def execute(self):
        super(ReleaseLine, self).execute()

        if self._isCatchingBoxPresent():
            if self._isFishFighting():
                self._releaseLine()
                return
            else:
                self.FSM.toTransition(TRANSITION_PULL_IN)
                return
        else:
            self.FSM.toTransition(TRANSITION_IDLE)

    def exit(self):
        super(ReleaseLine, self).exit()

    def _isFishFighting(self):
        return self.FSM.capture.checkAreaForColor(self.FSM.bot.settings.fishFightingViewArea)

    def _isCatchingBoxPresent(self):
        return self.FSM.capture.checkAreaForColor(self.FSM.bot.settings.catchingBoxPresentViewArea)

    def _releaseLine(self):
        print("released F")
        self._clickController.releaseF()
        # self._clickController.rightMouseUp()
