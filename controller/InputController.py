import time
import win32api
import win32con
import keyboard


class InputController(object):
    def click(self, button='left', x=None, y=None, duration=0.1):
        """
            click(button, x, y, duration)

            - `left`: left mouse button
            - `right`: right mouse button

            If coordinates x and y are set, move cursor to position.
            Press 'button' for 'duration' seconds.
        """
        if x is not None and y is not None:
            win32api.SetCursorPos((x, y))

        if button == 'right':
            self.rightMouseDown()
        elif button == 'left':
            self.leftMouseDown()

        time.sleep(duration)

        if button == 'right':
            self.rightMouseUp()
        elif button == 'left':
            self.leftMouseUp()

    def clickRightButton(self, x=None, y=None, duration=0.1, startDelay=0.0, endDelay=0.0):
        """
            clickRightButton( x, y, duration, startDelay, endDelay)

            If coordinates x and y are set, move cursor to position.
            Waits before and after 'button' is pressed for 'duration' seconds.
        """
        time.sleep(startDelay)
        self.click('right', x, y, duration)
        time.sleep(endDelay)

    @staticmethod
    def rightMouseDown():
        """
            Press right mouse button
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)

    @staticmethod
    def rightMouseUp():
        """
            Release right mouse button
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

    @staticmethod
    def leftMouseDown():
        """
            Press left mouse button
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

    @staticmethod
    def leftMouseUp():
        """
            Release left mouse button
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    @staticmethod
    def pressF():
        """
            Press keyboard button F
        """
        keyboard.press("f")

    @staticmethod
    def releaseF():
        """
            Release keyboard button F
        """
        keyboard.release("f")

    @staticmethod
    def pressButton(button, duration=0.1, startDelay=0.0, endDelay=0.0):
        """
            Waits before and after keyboard 'button' pressed for 'duration'
        """
        time.sleep(startDelay)
        keyboard.press(button)
        time.sleep(duration)
        keyboard.release(button)
        time.sleep(endDelay)

    @staticmethod
    def isKeyPressed(key):
        """
            isKeyPressed(key) -> bool

            Returns True if the key is pressed.

                isKeyPressed('k') #-> True
        """
        return keyboard.is_pressed(key)
