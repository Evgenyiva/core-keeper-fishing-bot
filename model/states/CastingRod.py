from datetime import datetime, timedelta

from constants import *
from controller.InputController import InputController
from model.Coordinate import Coordinate
from model.State import State


class CastingRod(State):
    _viewArea = None
    _fishingClickPosition = Coordinate(0, 0)
    _triggerTimeStamp = None
    _delay = 2  # Seconds

    def __init__(self, FSM, simpleName):
        super(CastingRod, self).__init__(FSM, simpleName)
        self._clickController = InputController()
        self._fishingClickPosition = self.FSM.bot.settings.castRodClickPosition

    def enter(self):
        super(CastingRod, self).enter()
        self._triggerTimeStamp = datetime.now().utcnow() + timedelta(seconds=self._delay)

    def execute(self):
        super(CastingRod, self).execute()
        currentTime = datetime.now().utcnow()

        if self._triggerTimeStamp < currentTime:
            if not self.rodIsPresent():
                self._castFishingRod()
                self._triggerTimeStamp = currentTime + timedelta(seconds=self._delay)
            else:
                self.FSM.toTransition(TRANSITION_FISHING)

    def exit(self):
        super(CastingRod, self).exit()

    def rodIsPresent(self):
        return self.FSM.bot.capture.checkAreaForColor(self.FSM.bot.settings.rodPresentViewArea)

    def _castFishingRod(self):
        self._clickController.pressButton("f", duration=0.13, startDelay=0, endDelay=1.5)
