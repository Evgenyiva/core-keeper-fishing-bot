class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def enter(self):
        pass

    def execute(self):
        # print("Transitioning....")
        pass

    def exit(self):
        pass