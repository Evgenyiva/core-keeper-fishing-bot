from PIL import Image, ImageTk
import numpy as np


class ColorPreview:
    @staticmethod
    def getImage(r, g, b, w, h):
        viewData = np.zeros((h, w, 3), dtype=np.uint8)
        for posX in range(w):
            for posY in range(h):
                try:
                    viewData[posY, posX] = [r, g, b]
                except IndexError:
                    pass

        image = Image.fromarray(viewData)
        image = ImageTk.PhotoImage(image)
        return image
