import PySimpleGUI as Gui

from constants import *

settings = [[Gui.Frame(VIEW_SETTINGS_TITLE, [
    # ROD
    [Gui.Text(VIEW_SETTINGS_ROD_TITLE)],
    [
        Gui.Text(VIEW_SETTINGS_ROD_START_X_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_ROD_START_X),
        Gui.Text(VIEW_SETTINGS_ROD_START_Y_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_ROD_START_Y),
        Gui.Text(VIEW_SETTINGS_ROD_END_X_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_ROD_END_X),
        Gui.Text(VIEW_SETTINGS_ROD_END_Y_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_ROD_END_Y)
    ],
    [
        Gui.Text(VIEW_SETTINGS_ROD_RED_LABEL, size=(5, 1)), Gui.Input(size=(5, 1), key=VIEW_SETTINGS_ROD_RED),
        Gui.Text(VIEW_SETTINGS_ROD_GREEN_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_ROD_GREEN),
        Gui.Text(VIEW_SETTINGS_ROD_BLUE_LABEL, size=(5, 1)), Gui.Input(size=(5, 1), key=VIEW_SETTINGS_ROD_BLUE),
        Gui.Text(VIEW_SETTINGS_ROD_PERCENTAGE_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_ROD_PERCENTAGE),
        Gui.Image(size=(20, 20), key=VIEW_SETTINGS_ROD_COLOR)
    ],
    [Gui.Image(size=(360, 20), key=VIEW_SETTINGS_ROD_IMAGE)],

    # BAIT
    [Gui.Text(VIEW_SETTINGS_BAIT_TITLE)],
    [
        Gui.Text(VIEW_SETTINGS_BAIT_START_X_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_BAIT_START_X),
        Gui.Text(VIEW_SETTINGS_BAIT_START_Y_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_BAIT_START_Y),
        Gui.Text(VIEW_SETTINGS_BAIT_END_X_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_BAIT_END_X),
        Gui.Text(VIEW_SETTINGS_BAIT_END_Y_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_BAIT_END_Y)
    ],
    [
        Gui.Text(VIEW_SETTINGS_BAIT_RED_LABEL, size=(5, 1)), Gui.Input(size=(5, 1), key=VIEW_SETTINGS_BAIT_RED),
        Gui.Text(VIEW_SETTINGS_BAIT_GREEN_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_BAIT_GREEN),
        Gui.Text(VIEW_SETTINGS_BAIT_BLUE_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_BAIT_BLUE),
        Gui.Text(VIEW_SETTINGS_BAIT_PERCENTAGE_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_BAIT_PERCENTAGE),
        Gui.Image(size=(20, 20), key=VIEW_SETTINGS_BAIT_COLOR)
    ],
    [Gui.Image(size=(360, 20), key=VIEW_SETTINGS_BAIT_IMAGE)],

    # CATCHING BOX
    [Gui.Text(VIEW_SETTINGS_CATCHING_BOX_TITLE)],
    [
        Gui.Text(VIEW_SETTINGS_CATCHING_BOX_START_X_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_CATCHING_BOX_START_X),
        Gui.Text(VIEW_SETTINGS_CATCHING_BOX_START_Y_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_CATCHING_BOX_START_Y),
        Gui.Text(VIEW_SETTINGS_CATCHING_BOX_END_X_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_CATCHING_BOX_END_X),
        Gui.Text(VIEW_SETTINGS_CATCHING_BOX_END_Y_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_CATCHING_BOX_END_Y)
    ],
    [
        Gui.Text(VIEW_SETTINGS_CATCHING_BOX_RED_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_CATCHING_BOX_RED),
        Gui.Text(VIEW_SETTINGS_CATCHING_BOX_GREEN_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_CATCHING_BOX_GREEN),
        Gui.Text(VIEW_SETTINGS_CATCHING_BOX_BLUE_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_CATCHING_BOX_BLUE),
        Gui.Text(VIEW_SETTINGS_CATCHING_BOX_PERCENTAGE_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_CATCHING_BOX_PERCENTAGE),
        Gui.Image(size=(20, 20), key=VIEW_SETTINGS_CATCHING_BOX_COLOR)
    ],
    [Gui.Image(size=(20, 20), key=VIEW_SETTINGS_CATCHING_BOX_IMAGE)],

    # FISH FIGHTING
    [Gui.Text(VIEW_SETTINGS_FISH_FIGHTING_TITLE)],
    [
        Gui.Text(VIEW_SETTINGS_FISH_FIGHTING_START_X_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_FISH_FIGHTING_START_X),
        Gui.Text(VIEW_SETTINGS_FISH_FIGHTING_START_Y_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_FISH_FIGHTING_START_Y),
        Gui.Text(VIEW_SETTINGS_FISH_FIGHTING_END_X_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_FISH_FIGHTING_END_X),
        Gui.Text(VIEW_SETTINGS_FISH_FIGHTING_END_Y_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_FISH_FIGHTING_END_Y)
    ],
    [
        Gui.Text(VIEW_SETTINGS_FISH_FIGHTING_RED_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_FISH_FIGHTING_RED),
        Gui.Text(VIEW_SETTINGS_FISH_FIGHTING_GREEN_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_FISH_FIGHTING_GREEN),
        Gui.Text(VIEW_SETTINGS_FISH_FIGHTING_BLUE_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_FISH_FIGHTING_BLUE),
        Gui.Text(VIEW_SETTINGS_FISH_FIGHTING_PERCENTAGE_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_FISH_FIGHTING_PERCENTAGE),
        Gui.Image(size=(20, 20), key=VIEW_SETTINGS_FISH_FIGHTING_COLOR)
    ],
    [Gui.Image(size=(360, 20), key=VIEW_SETTINGS_FISH_FIGHTING_IMAGE)],

    # CLICK CAST COORDINATE
    [Gui.Text(VIEW_SETTINGS_CAST_ROD_CLICK_POSITION_TITLE)],
    [
        Gui.Text(VIEW_SETTINGS_CAST_ROD_CLICK_POSITION_X_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_CAST_ROD_CLICK_POSITION_X),
        Gui.Text(VIEW_SETTINGS_CAST_ROD_CLICK_POSITION_Y_LABEL, size=(5, 1)),
        Gui.Input(size=(5, 1), key=VIEW_SETTINGS_CAST_ROD_CLICK_POSITION_Y)
    ],
    [Gui.Button(VIEW_BUTTON_SAVE, key=VIEW_BUTTON_SAVE_KEY)]

], border_width=1)]]

log = [[Gui.Frame(VIEW_TEXT_LOG, [
    [Gui.Text(VIEW_TEXT_CURRENT_STATE), Gui.Text(key=VIEW_LOG_CURRENT_STATE)],
    [
        Gui.Button(STATE_IDLE, size=(6, 2), disabled=True, button_color="#FFFFFF"),
        Gui.Button(STATE_CASTING_ROD, size=(6, 2), disabled=True, button_color="#FFFFFF"),
        Gui.Button(STATE_FISHING, size=(6, 2), disabled=True, button_color="#FFFFFF"),
        Gui.Button(STATE_BITE, size=(6, 2), disabled=True, button_color="#FFFFFF"),
        Gui.Button(STATE_CATCHING, size=(6, 2), disabled=True, button_color="#FFFFFF"),
        Gui.Button(STATE_FISH_FIGHTING, size=(6, 2), disabled=True, button_color="#FFFFFF"),
        Gui.Button(STATE_PULL_IN, size=(6, 2), disabled=True, button_color="#FFFFFF")
    ],
    [Gui.Multiline(size=(65, 10), key=VIEW_LOG_OUTPUT)],
    [Gui.Button(VIEW_BUTTON_CLEAR_LOG, key=VIEW_BUTTON_CLEAR_LOG_KEY)],
    [Gui.Text(VIEW_CATCHED_FISHES_LABEL), Gui.Text(key=VIEW_CATCHED_FISHES_KEY)],
    [Gui.Text(VIEW_CATCHED_ITEMS_LABEL), Gui.Text(key=VIEW_CATCHED_ITEMS_KEY)]
], border_width=1)]]

buttons = [
    [
        [Gui.Text(VIEW_TEXT_CURSOR_VALUE_LABEL, size=(10, 1)),
         Gui.Text('', size=(45, 1), key=VIEW_TEXT_CURSOR_VALUE_KEY),
         Gui.Button('', size=(2, 1), key=VIEW_TEXT_CURSOR_VALUE_IMAGE_KEY)]
    ],
    [Gui.Button(VIEW_BUTTON_GO, key=VIEW_BUTTON_GO_KEY),
     Gui.Button(VIEW_BUTTON_CURSOR_VALUE, key=VIEW_BUTTON_CURSOR_VALUE_KEY),
     Gui.Button(VIEW_BUTTON_PAUSE, key=VIEW_BUTTON_PAUSE_KEY),
     Gui.Button(VIEW_BUTTON_VIEW_PAUSE, key=VIEW_BUTTON_VIEW_PAUSE_KEY),
     Gui.Button(VIEW_BUTTON_EXIT, key=VIEW_BUTTON_EXIT_KEY)]
]
