from model.State import State
from constants import *


class Idle(State):
    def __init__(self, FSM, simpleName):
        super(Idle, self).__init__(FSM, simpleName)

    def enter(self):
        super(Idle, self).enter()

    def execute(self):
        super(Idle, self).execute()

        if self.rodIsPresent():
            self.FSM.toTransition(TRANSITION_FISHING)
        else:
            self.FSM.toTransition(TRANSITION_CASTING_ROD)

    def exit(self):
        super(Idle, self).exit()

    def rodIsPresent(self):
        return self.FSM.bot.capture.checkAreaForColor(self.FSM.bot.settings.rodPresentViewArea)
