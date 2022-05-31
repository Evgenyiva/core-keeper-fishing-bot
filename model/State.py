class State(object):
    def __init__(self, FSM, fullName):
        self.FSM = FSM
        self.timer = 0
        self.startTime = 0
        self.simpleName = fullName.replace(" ", "_")
        self.fullName: str = fullName

    def enter(self):
        self.FSM.bot.view.getByKey(self.fullName).update(button_color=("#FFFFFF", "#283B5B"))
        pass

    def execute(self):
        text = "Execute: {name}".format(name=self.fullName)
        self.FSM.bot.view.logMessage(text)
        pass

    def exit(self):
        self.FSM.bot.view.getByKey(self.fullName).update(button_color=("#000000", "#FFFFFF"))
        pass
