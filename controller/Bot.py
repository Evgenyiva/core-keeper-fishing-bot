from constants import *
from model.FSM import FSM
from model.Transition import Transition
from model.states.Bite import Bite
from model.states.CastingRod import CastingRod
from model.states.Catching import Catching
from model.states.FishFighting import FishFighting
from model.states.Fishing import Fishing
from model.states.Idle import Idle
from model.states.PullIn import PullIn


class Bot(object):
    def __init__(self):
        self.FSM = FSM(bot=self)
        self.capture = None
        self.view = None
        self.settings = None
        self.inputController = None
        self.fishCounter = 0
        self.itemCounter = 0

    def initializeStates(self):
        idleState = Idle(self.FSM, STATE_IDLE)
        castingRod = CastingRod(self.FSM, STATE_CASTING_ROD)
        fishingState = Fishing(self.FSM, STATE_FISHING)
        biteState = Bite(self.FSM, STATE_BITE)
        catchingState = Catching(self.FSM, STATE_CATCHING)
        fishFightingState = FishFighting(self.FSM, STATE_FISH_FIGHTING)
        pullInState = PullIn(self.FSM, STATE_PULL_IN)

        # STATES
        self.FSM.addState(idleState)
        self.FSM.addState(castingRod)
        self.FSM.addState(fishingState)
        self.FSM.addState(biteState)
        self.FSM.addState(catchingState)
        self.FSM.addState(fishFightingState)
        self.FSM.addState(pullInState)

        # TRANSITIONS
        self.FSM.addTransition(TRANSITION_IDLE, Transition(idleState.simpleName))
        self.FSM.addTransition(TRANSITION_CASTING_ROD, Transition(castingRod.simpleName))
        self.FSM.addTransition(TRANSITION_FISHING, Transition(fishingState.simpleName))
        self.FSM.addTransition(TRANSITION_BITE, Transition(biteState.simpleName))
        self.FSM.addTransition(TRANSITION_CATCHING, Transition(catchingState.simpleName))
        self.FSM.addTransition(TRANSITION_FISH_FIGHTING, Transition(fishFightingState.simpleName))
        self.FSM.addTransition(TRANSITION_PULL_IN, Transition(pullInState.simpleName))

        # DEFAULT
        self.FSM.setState(idleState.simpleName)

    def execute(self):
        self.capture.refreshImages()
        self.FSM.execute()

    def setPause(self, pause):
        self.FSM.pause = pause

    def setInputController(self, controller):
        self.inputController = controller

    def setSettings(self, settings):
        self.settings = settings

    def setView(self, view):
        self.view = view

    def setCapture(self, capture):
        self.capture = capture
