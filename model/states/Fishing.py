from model.State import State
from constants import *


class Fishing(State):
    def __init__(self, FSM, simpleName):
        super(Fishing, self).__init__(FSM, simpleName)

    def enter(self):
        super(Fishing, self).enter()

    def execute(self):
        super(Fishing, self).execute()

        if not self.checkForRod():
            self.FSM.toTransition(TRANSITION_CASTING_ROD)
            return

        if self.checkForBite():
            self.FSM.toTransition(TRANSITION_BITE)
            return

    def exit(self):
        super(Fishing, self).exit()

    def checkForBite(self):
        return self.FSM.bot.capture.checkAreaForColor(self.FSM.bot.settings.baitViewArea)

    def checkForRod(self):
        return self.FSM.bot.capture.checkAreaForColor(self.FSM.bot.settings.rodPresentViewArea)

