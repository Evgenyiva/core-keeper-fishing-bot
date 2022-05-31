from constants import *
from controller.ScreenCaptureController import ViewArea
from model.ColorTrigger import ColorTrigger
from model.Coordinate import Coordinate
from model.Settings import Settings

defaultSettings = Settings(
    rodPresentViewArea=ViewArea(
        Coordinate(1949, 655),
        Coordinate(1954, 700),
        VIEW_SETTINGS_ROD_IMAGE,
        350,
        10,
        ColorTrigger(190, 50, 30, 5)),
    baitViewArea=ViewArea(
        Coordinate(1955, 733),
        Coordinate(1985, 736),
        VIEW_SETTINGS_BAIT_IMAGE,
        350,
        10,
        ColorTrigger(130, 90, 120, 5)),
    fishFightingViewArea=ViewArea(
        Coordinate(1788, 920),
        Coordinate(2055, 933),
        VIEW_SETTINGS_FISH_FIGHTING_IMAGE,
        360,
        10,
        ColorTrigger(178, 28, 22, 3)),
    catchingBoxPresentViewArea=ViewArea(
        Coordinate(1786, 911),
        Coordinate(1787, 912),
        VIEW_SETTINGS_CATCHING_BOX_IMAGE,
        20,
        20,
        ColorTrigger(210, 154, 124, 3)),
    castRodClickPosition=Coordinate(2120, 704)
)
