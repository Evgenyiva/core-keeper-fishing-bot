from constants import VIEW_LOG_CURRENT_STATE
from model.State import State


# Finite State Machine
class FSM(object):
    def __init__(self, bot):
        self.bot = bot
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.prevState = None
        self.trans = None
        self.pause = True

    def addTransition(self, transName, transition):
        self.transitions[transName] = transition

    def addState(self, state: State):
        self.states[state.simpleName] = state

    def updateState(self, state: State):
        self.states[state.simpleName] = state

    def setState(self, stateName):
        self.prevState = self.curState
        self.curState = self.states[stateName]
        self.bot.view.logMessage(stateName)
        self.bot.view.getByKey(VIEW_LOG_CURRENT_STATE).update(stateName)

    def toTransition(self, toTrans):
        self.trans = self.transitions[toTrans]

    def execute(self):
        if self.pause:
            return

        if self.trans:
            self.trans.enter()
            self.curState.exit()
            self.trans.execute()
            self.setState(self.trans.toState)
            self.curState.enter()
            self.trans.exit()
            self.trans = None

        self.curState.execute()
