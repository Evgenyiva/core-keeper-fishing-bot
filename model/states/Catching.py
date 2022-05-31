from datetime import datetime, timedelta

from constants import *
from controller.InputController import InputController
from model.State import State


class Catching(State):
    _triggerTimeStamp = None
    _delay = 1  # Seconds

    def __init__(self, FSM, simpleName):
        super(Catching, self).__init__(FSM, simpleName)
        self._clickController = InputController()

    def enter(self):
        super(Catching, self).enter()
        self._triggerTimeStamp = datetime.now().utcnow() + timedelta(seconds=self._delay)

    def execute(self):
        super(Catching, self).execute()
        currentTime = datetime.now().utcnow()

        if self._triggerTimeStamp > currentTime:
            return

        if self.checkForFishBox():
            self.FSM.toTransition(TRANSITION_FISH_FIGHTING)
            return
        else:
            self.FSM.bot.itemCounter += 1
            self.FSM.bot.view.getByKey(VIEW_CATCHED_ITEMS_KEY).update(self.FSM.bot.itemCounter)
            self.FSM.toTransition(TRANSITION_PULL_IN)

    def exit(self):
        super(Catching, self).exit()

    def checkForFishBox(self):
        return self.FSM.bot.capture.checkAreaForColor(self.FSM.bot.settings.catchingBoxPresentViewArea)
