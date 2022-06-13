import cv2
import numpy as np
from PIL import Image, ImageTk, ImageGrab
from pyautogui import *

from constants import *
from model.ViewArea import ViewArea


class ScreenCaptureController(object):
    def __init__(self, view):
        self._view = view
        self._picture = ImageGrab.grab().load()
        self._viewAreas = {}

    def addViewArea(self, viewArea: ViewArea):
        """
        addViewArea(viewArea)

        Adds an ViewArea to dictionary.

        :param  viewArea:
        """
        self._viewAreas[viewArea.windowTag] = viewArea

    def refreshImages(self):
        """
            Loads screenshot and converts to array[X,Y].

            Iterates through _viewArea dictionary and refreshes preview image
        """
        image = ImageGrab.grab()
        image.convert('RGB')

        self._picture = image.load()

        for key, item in self._viewAreas.items():
            self._refreshViewArray(item)

    def _refreshViewArray(self, viewArea: ViewArea):
        """
            Creates empty Array with precalculated view area size.
            Tries to copy pixel color.
            Rotates image if height is bigger than width.
            Stretches and converts the Array to Image.

            :param viewArea:
        """
        viewData = np.zeros((viewArea.height, viewArea.width, 4), dtype=np.uint8)

        for posX in range(viewArea.width):
            for posY in range(viewArea.height):
                pixelX = viewArea.startPosition.x + posX
                pixelY = viewArea.startPosition.y + posY
                color = self._picture[pixelX, pixelY]
                try:
                    viewData[posY, posX] = color
                except IndexError:
                    pass

        if viewArea.width < viewArea.viewHeight:
            viewData = cv2.rotate(viewData, cv2.ROTATE_90_CLOCKWISE)

        viewData = cv2.resize(viewData, (viewArea.viewWidth, viewArea.viewHeight))
        image = ImageTk.PhotoImage(Image.fromarray(viewData))

        self._view.getByKey(viewArea.windowTag).update(data=image)

    def checkAreaForColor(self, viewArea: ViewArea):
        """
            Goes pixel by pixel through the Area.
            If ´´color´´ matches the ´´triggerColor´´ returns True
        """
        for posX in range(viewArea.width):
            for posY in range(viewArea.height):
                color = self._picture[viewArea.startPosition.x + posX, viewArea.startPosition.y + posY]

                if viewArea.triggerColor.isInRange(color):
                    return True

        return False

    def updateArea(self, viewArea: ViewArea):
        """
            Update dictionary value
        """
        self._viewAreas.update({viewArea.windowTag: viewArea})

    def captureCursor(self, xOffset=0, yOffset=0):
        """
            Get and print the mouse coordinates.
        """

        x, y = position()
        positionStr = "X: {} Y: {} - ".format(str(x - xOffset).rjust(4), str(y - yOffset).rjust(4))

        pixelColor = pyscreeze.screenshot().getpixel((x, y))

        colorStr = "RGB: ({}, {}, {})".format(str(pixelColor[0]).rjust(3),
                                              str(pixelColor[1]).rjust(3),
                                              str(pixelColor[2]).rjust(3))

        retVal = positionStr + colorStr
        self._view.getByKey(VIEW_TEXT_CURSOR_VALUE_KEY).update(retVal)
        colorHex = '#%02x%02x%02x' % (int(pixelColor[0]), int(pixelColor[1]), int(pixelColor[2]))
        self._view.getByKey(VIEW_TEXT_CURSOR_VALUE_IMAGE_KEY).update(button_color=(colorHex, colorHex))
