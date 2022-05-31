from constants import *
from model.State import State


class Bite(State):
    def __init__(self, FSM, simpleName):
        super(Bite, self).__init__(FSM, simpleName)

    def enter(self):
        super(Bite, self).enter()

    def execute(self):
        super(Bite, self).execute()

        self.FSM.bot.inputController.pressButton("f")

        self.FSM.toTransition(TRANSITION_CATCHING)

    def exit(self):
        super(Bite, self).exit()
