import os.path

import jsonpickle

from constants import *
from model.ColorPreview import ColorPreview
from resources.assets.DefaultSettings import defaultSettings


class SettingsController:
    def __init__(self, view):
        self.viewController = view
        self.view = view.root
        self.settings = None

    def saveData(self):
        """
            Tries to save settings to json file
        """
        try:
            with open(SETTINGS_FILE_NAME, "w") as outfile:
                settingsJson = jsonpickle.encode(self.settings)
                outfile.write(settingsJson)
                print("Settings file saved successfully")

        except Exception as e:
            print(e)

    def loadData(self):
        """
            If file exists tries to open and parse settings.
            If no file found, load default values
        """
        try:
            if os.path.exists(SETTINGS_FILE_NAME):
                with open(SETTINGS_FILE_NAME, "r") as outfile:
                    studentJson = outfile.read()
                    self.settings = jsonpickle.decode(studentJson)
            else:
                self.settings = defaultSettings
                print("No settings file found, default settings restored")

            self.parseWithView()
            self.viewController.logMessage("Data is Valid: {}".format(self.isValid()))
        except Exception as e:
            print(e)

    def parseWithView(self):
        """
            Set values to view input fields
        """
        self.parseRodSettings()
        self.parseCatchAreaSettings()
        self.parseCatchingBoxSettings()
        self.parseFishFightingSettings()
        self.parseClickPositionSettings()

    def parseRodSettings(self):
        """
            See parseWithView()
        """
        self.view[VIEW_SETTINGS_ROD_RED].update(self.settings.rodPresentViewArea.triggerColor.r)
        self.view[VIEW_SETTINGS_ROD_GREEN].update(self.settings.rodPresentViewArea.triggerColor.g)
        self.view[VIEW_SETTINGS_ROD_BLUE].update(self.settings.rodPresentViewArea.triggerColor.b)
        self.view[VIEW_SETTINGS_ROD_PERCENTAGE].update(self.settings.rodPresentViewArea.triggerColor.percentage)

        self.view[VIEW_SETTINGS_ROD_START_X].update(self.settings.rodPresentViewArea.startPosition.x)
        self.view[VIEW_SETTINGS_ROD_START_Y].update(self.settings.rodPresentViewArea.startPosition.y)
        self.view[VIEW_SETTINGS_ROD_END_X].update(self.settings.rodPresentViewArea.endPosition.x)
        self.view[VIEW_SETTINGS_ROD_END_Y].update(self.settings.rodPresentViewArea.endPosition.y)
        self.view[VIEW_SETTINGS_ROD_COLOR].update(data=ColorPreview.getImage(
            self.settings.rodPresentViewArea.triggerColor.r,
            self.settings.rodPresentViewArea.triggerColor.g,
            self.settings.rodPresentViewArea.triggerColor.b,
            20,
            20
        ))

    def parseCatchAreaSettings(self):
        """
            See parseWithView()
        """
        self.view[VIEW_SETTINGS_BAIT_RED].update(self.settings.baitViewArea.triggerColor.r)
        self.view[VIEW_SETTINGS_BAIT_GREEN].update(self.settings.baitViewArea.triggerColor.g)
        self.view[VIEW_SETTINGS_BAIT_BLUE].update(self.settings.baitViewArea.triggerColor.b)
        self.view[VIEW_SETTINGS_BAIT_PERCENTAGE].update(self.settings.baitViewArea.triggerColor.percentage)

        self.view[VIEW_SETTINGS_BAIT_START_X].update(self.settings.baitViewArea.startPosition.x)
        self.view[VIEW_SETTINGS_BAIT_START_Y].update(self.settings.baitViewArea.startPosition.y)
        self.view[VIEW_SETTINGS_BAIT_END_X].update(self.settings.baitViewArea.endPosition.x)
        self.view[VIEW_SETTINGS_BAIT_END_Y].update(self.settings.baitViewArea.endPosition.y)

        self.view[VIEW_SETTINGS_BAIT_COLOR].update(data=ColorPreview.getImage(
            self.settings.baitViewArea.triggerColor.r,
            self.settings.baitViewArea.triggerColor.g,
            self.settings.baitViewArea.triggerColor.b,
            20,
            20
        ))

    def parseCatchingBoxSettings(self):
        """
            See parseWithView()
        """
        self.view[VIEW_SETTINGS_CATCHING_BOX_RED].update(self.settings.catchingBoxPresentViewArea.triggerColor.r)
        self.view[VIEW_SETTINGS_CATCHING_BOX_GREEN].update(self.settings.catchingBoxPresentViewArea.triggerColor.g)
        self.view[VIEW_SETTINGS_CATCHING_BOX_BLUE].update(self.settings.catchingBoxPresentViewArea.triggerColor.b)
        self.view[VIEW_SETTINGS_CATCHING_BOX_PERCENTAGE].update(
            self.settings.catchingBoxPresentViewArea.triggerColor.percentage)

        self.view[VIEW_SETTINGS_CATCHING_BOX_START_X].update(self.settings.catchingBoxPresentViewArea.startPosition.x)
        self.view[VIEW_SETTINGS_CATCHING_BOX_START_Y].update(self.settings.catchingBoxPresentViewArea.startPosition.y)
        self.view[VIEW_SETTINGS_CATCHING_BOX_END_X].update(self.settings.catchingBoxPresentViewArea.endPosition.x)
        self.view[VIEW_SETTINGS_CATCHING_BOX_END_Y].update(self.settings.catchingBoxPresentViewArea.endPosition.y)

        self.view[VIEW_SETTINGS_CATCHING_BOX_COLOR].update(data=ColorPreview.getImage(
            self.settings.catchingBoxPresentViewArea.triggerColor.r,
            self.settings.catchingBoxPresentViewArea.triggerColor.g,
            self.settings.catchingBoxPresentViewArea.triggerColor.b,
            20,
            20
        ))

    def parseFishFightingSettings(self):
        """
            See parseWithView()
        """
        self.view[VIEW_SETTINGS_FISH_FIGHTING_RED].update(self.settings.fishFightingViewArea.triggerColor.r)
        self.view[VIEW_SETTINGS_FISH_FIGHTING_GREEN].update(self.settings.fishFightingViewArea.triggerColor.g)
        self.view[VIEW_SETTINGS_FISH_FIGHTING_BLUE].update(self.settings.fishFightingViewArea.triggerColor.b)
        self.view[VIEW_SETTINGS_FISH_FIGHTING_PERCENTAGE].update(
            self.settings.fishFightingViewArea.triggerColor.percentage)

        self.view[VIEW_SETTINGS_FISH_FIGHTING_START_X].update(self.settings.fishFightingViewArea.startPosition.x)
        self.view[VIEW_SETTINGS_FISH_FIGHTING_START_Y].update(self.settings.fishFightingViewArea.startPosition.y)
        self.view[VIEW_SETTINGS_FISH_FIGHTING_END_X].update(self.settings.fishFightingViewArea.endPosition.x)
        self.view[VIEW_SETTINGS_FISH_FIGHTING_END_Y].update(self.settings.fishFightingViewArea.endPosition.y)

        self.view[VIEW_SETTINGS_FISH_FIGHTING_COLOR].update(data=ColorPreview.getImage(
            self.settings.fishFightingViewArea.triggerColor.r,
            self.settings.fishFightingViewArea.triggerColor.g,
            self.settings.fishFightingViewArea.triggerColor.b,
            20,
            20
        ))

    def parseClickPositionSettings(self):
        """
            See parseWithView()
        """
        self.view[VIEW_SETTINGS_CAST_ROD_CLICK_POSITION_X].update(self.settings.castRodClickPosition.x)
        self.view[VIEW_SETTINGS_CAST_ROD_CLICK_POSITION_Y].update(self.settings.castRodClickPosition.y)

    def updateData(self, values):
        """
            Set settings values
        """
        self.settings.rodPresentViewArea.triggerColor.r = int(values[VIEW_SETTINGS_ROD_RED])
        self.settings.rodPresentViewArea.triggerColor.g = int(values[VIEW_SETTINGS_ROD_GREEN])
        self.settings.rodPresentViewArea.triggerColor.b = int(values[VIEW_SETTINGS_ROD_BLUE])
        self.settings.rodPresentViewArea.triggerColor.percentage = int(values[VIEW_SETTINGS_ROD_PERCENTAGE])

        self.settings.rodPresentViewArea.startPosition.x = int(values[VIEW_SETTINGS_ROD_START_X])
        self.settings.rodPresentViewArea.startPosition.y = int(values[VIEW_SETTINGS_ROD_START_Y])
        self.settings.rodPresentViewArea.endPosition.x = int(values[VIEW_SETTINGS_ROD_END_X])
        self.settings.rodPresentViewArea.endPosition.y = int(values[VIEW_SETTINGS_ROD_END_Y])

        self.settings.baitViewArea.triggerColor.r = int(values[VIEW_SETTINGS_BAIT_RED])
        self.settings.baitViewArea.triggerColor.g = int(values[VIEW_SETTINGS_BAIT_GREEN])
        self.settings.baitViewArea.triggerColor.b = int(values[VIEW_SETTINGS_BAIT_BLUE])
        self.settings.baitViewArea.triggerColor.percentage = int(values[VIEW_SETTINGS_BAIT_PERCENTAGE])

        self.settings.baitViewArea.startPosition.x = int(values[VIEW_SETTINGS_BAIT_START_X])
        self.settings.baitViewArea.startPosition.y = int(values[VIEW_SETTINGS_BAIT_START_Y])
        self.settings.baitViewArea.endPosition.x = int(values[VIEW_SETTINGS_BAIT_END_X])
        self.settings.baitViewArea.endPosition.y = int(values[VIEW_SETTINGS_BAIT_END_Y])

        self.settings.catchingBoxPresentViewArea.triggerColor.r = int(values[VIEW_SETTINGS_CATCHING_BOX_RED])
        self.settings.catchingBoxPresentViewArea.triggerColor.g = int(values[VIEW_SETTINGS_CATCHING_BOX_GREEN])
        self.settings.catchingBoxPresentViewArea.triggerColor.b = int(values[VIEW_SETTINGS_CATCHING_BOX_BLUE])
        self.settings.catchingBoxPresentViewArea.triggerColor.percentage = int(
            values[VIEW_SETTINGS_CATCHING_BOX_PERCENTAGE])

        self.settings.catchingBoxPresentViewArea.startPosition.x = int(values[VIEW_SETTINGS_CATCHING_BOX_START_X])
        self.settings.catchingBoxPresentViewArea.startPosition.y = int(values[VIEW_SETTINGS_CATCHING_BOX_START_Y])
        self.settings.catchingBoxPresentViewArea.endPosition.x = int(values[VIEW_SETTINGS_CATCHING_BOX_END_X])
        self.settings.catchingBoxPresentViewArea.endPosition.y = int(values[VIEW_SETTINGS_CATCHING_BOX_END_Y])

        self.settings.fishFightingViewArea.triggerColor.r = int(values[VIEW_SETTINGS_FISH_FIGHTING_RED])
        self.settings.fishFightingViewArea.triggerColor.g = int(values[VIEW_SETTINGS_FISH_FIGHTING_GREEN])
        self.settings.fishFightingViewArea.triggerColor.b = int(values[VIEW_SETTINGS_FISH_FIGHTING_BLUE])
        self.settings.fishFightingViewArea.triggerColor.percentage = int(values[VIEW_SETTINGS_FISH_FIGHTING_PERCENTAGE])

        self.settings.fishFightingViewArea.startPosition.x = int(values[VIEW_SETTINGS_FISH_FIGHTING_START_X])
        self.settings.fishFightingViewArea.startPosition.y = int(values[VIEW_SETTINGS_FISH_FIGHTING_START_Y])
        self.settings.fishFightingViewArea.endPosition.x = int(values[VIEW_SETTINGS_FISH_FIGHTING_END_X])
        self.settings.fishFightingViewArea.endPosition.y = int(values[VIEW_SETTINGS_FISH_FIGHTING_END_Y])

        self.settings.castRodClickPosition.x = int(values[VIEW_SETTINGS_CAST_ROD_CLICK_POSITION_X])
        self.settings.castRodClickPosition.y = int(values[VIEW_SETTINGS_CAST_ROD_CLICK_POSITION_Y])

        self.parseWithView()
        self.viewController.logMessage("Data is Valid: {}".format(self.isValid()))

    def isValid(self):
        """
            checks if settings values are valid
        """
        if self.settings is None:
            return False

        if self.settings.rodPresentViewArea is None:
            return False
        if self.settings.rodPresentViewArea.startPosition is None:
            return False
        if self.settings.rodPresentViewArea.endPosition is None:
            return False
        if self.settings.rodPresentViewArea.triggerColor is None:
            return False

        if self.settings.baitViewArea is None:
            return False
        if self.settings.baitViewArea.startPosition is None:
            return False
        if self.settings.baitViewArea.endPosition is None:
            return False
        if self.settings.baitViewArea.triggerColor is None:
            return False

        if self.settings.fishFightingViewArea is None:
            return False
        if self.settings.fishFightingViewArea.startPosition is None:
            return False
        if self.settings.fishFightingViewArea.endPosition is None:
            return False
        if self.settings.fishFightingViewArea.triggerColor is None:
            return False

        if self.settings.catchingBoxPresentViewArea is None:
            return False
        if self.settings.catchingBoxPresentViewArea.startPosition is None:
            return False
        if self.settings.catchingBoxPresentViewArea.endPosition is None:
            return False
        if self.settings.catchingBoxPresentViewArea.triggerColor is None:
            return False

        return True
