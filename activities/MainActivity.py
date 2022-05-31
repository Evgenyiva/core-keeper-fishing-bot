import threading

from constants import *
from controller.Bot import Bot
from controller.InputController import InputController
from controller.ScreenCaptureController import ScreenCaptureController
from controller.SettingsController import SettingsController


class MainActivity(object):
    _execute = True
    _pause = True
    _viewPause = False
    _cursorValueVisible = False

    def __init__(self, view):
        self.view = view
        self.capture = ScreenCaptureController(self.view)
        self.settingsController = SettingsController(self.view)
        self.inputController = InputController()
        self.bot = Bot()

        self.bot.setView(self.view)
        self.bot.setCapture(self.capture)
        self.bot.setInputController(self.inputController)

        self.settingsController.loadData()
        self.bot.setSettings(self.settingsController.settings)

    def runBot(self):
        botThread = threading.Thread(target=self._runner, daemon=True)
        self.view.getByKey(VIEW_BUTTON_GO_KEY).update(button_color=("#CCCCCC", "#CCCCCC"), disabled=True)

        botThread.start()

    def _runner(self):
        """
            bot thread runner
        """
        self.capture.addViewArea(self.settingsController.settings.rodPresentViewArea)
        self.capture.addViewArea(self.settingsController.settings.baitViewArea)
        self.capture.addViewArea(self.settingsController.settings.catchingBoxPresentViewArea)
        self.capture.addViewArea(self.settingsController.settings.fishFightingViewArea)

        self.bot.initializeStates()

        while self._execute:
            if self._cursorValueVisible:
                self.capture.captureCursor()

            if self._viewPause:
                continue

            self.bot.execute()

    def onSaveClick(self, values):
        """
            onSaveClick(values)

            save settings and update areas
        """
        self.settingsController.updateData(values)
        self.settingsController.saveData()
        self.capture.updateArea(self.settingsController.settings.rodPresentViewArea)
        self.capture.updateArea(self.settingsController.settings.baitViewArea)
        self.capture.updateArea(self.settingsController.settings.catchingBoxPresentViewArea)
        self.capture.updateArea(self.settingsController.settings.fishFightingViewArea)

    def onCursorValueClick(self):
        """
            toggle cursor capture
        """
        if self._cursorValueVisible:
            self.view.logMessage("Cursor value pause", "#FF0000")
        else:
            self.view.logMessage("Cursor value play", "#FF0000")

        self._cursorValueVisible ^= True

    def onBotPauseClick(self):
        """
            toggle Bot state transition
        """
        if self._pause:
            self.view.logMessage("play", "#FF0000")
        else:
            self.view.logMessage("pause", "#FF0000")

        self._pause ^= True
        self.bot.setPause(self._pause)

    def onViewPauseClick(self):
        """
            toggle View capture preview
        """
        if self._viewPause:
            self.view.logMessage("View pause", "#FF0000")
        else:
            self.view.logMessage("View play", "#FF0000")

        self._viewPause ^= True
