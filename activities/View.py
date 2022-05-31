from datetime import datetime

from resources.layout.activity_layout import *


class View(object):
    Gui.theme('DarkBlue')  # Add a touch of color

    layout = [[Gui.Column(settings, vertical_alignment='t'), Gui.Column(log, vertical_alignment='top')], buttons]

    root = Gui.Window('Core Keeper - Fishing Bot', layout, finalize=True, keep_on_top=True)

    def __init__(self, ):
        self.activity = None
        self._lastMessage = ""

    def setActivity(self, activity):
        self.activity = activity

    def getByKey(self, viewKey):
        return self.root[viewKey]

    def logMessage(self, value, color="#000000"):
        """
            Output formatted Log 'value' with timestamp.
            Holds 'value' until changes.
            if 'color' is set change line color.
        """
        if not self._lastMessage == value:
            timestamp = datetime.now().strftime('%H:%M:%S')
            outValue = "[{}] - {}".format(timestamp, value)

            if color is not None:
                self.getByKey(VIEW_LOG_OUTPUT).print(outValue, text_color=color)
            else:
                self.getByKey(VIEW_LOG_OUTPUT).print(outValue)

        self._lastMessage = value

    def show(self):
        """
            creates window and listen for events
        """
        while True:
            event, values = self.root.read()

            if event == Gui.WIN_CLOSED or event == VIEW_BUTTON_EXIT_KEY:
                break

            if event == VIEW_BUTTON_CLEAR_LOG_KEY:
                self.getByKey(VIEW_LOG_OUTPUT).update("")
                continue

            if event == VIEW_BUTTON_SAVE_KEY:
                try:
                    self.activity.onSaveClick(values)
                except ValueError:
                    self.logMessage("Can't save")
                continue

            if event == VIEW_BUTTON_GO_KEY:
                self.activity.runBot()
                continue

            if event == VIEW_BUTTON_CURSOR_VALUE_KEY:
                self.activity.onCursorValueClick()
                continue

            if event == VIEW_BUTTON_PAUSE_KEY:
                self.activity.onBotPauseClick()
                continue

            if event == VIEW_BUTTON_VIEW_PAUSE_KEY:
                self.activity.onViewPauseClick()
                continue
