from . import *

import PIL.ImageGrab
import PIL.Image
import mss
import cv2
import numpy as np

class uiPasteFunctions:
    @staticmethod
    def getScreen(width, height, fovX, fovY, numpy=True):
        with mss.mss() as sct:
            bbox = (
                int((width / 2) - fovX),
                int(((height) / 2) - fovY),
                int((width / 2) + fovX),
                int(((height) / 2) + fovY)
            )
            img = sct.grab(bbox)

            if numpy:
                return np.array(img)
            else:
                PIL.Image.frombytes('RGB', img.size, img.bgra, 'raw', 'BGRX')

    @staticmethod
    def findEnemyTrigger(fovx, fovy):
        width, height = getScreenResolution()

        image = uiPasteFunctions.getScreen(width, height, fovx, fovy)

        try:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            lower = np.array([130, 60, 200])
            upper = np.array([150, 255, 255])

            mask = cv2.inRange(hsv, lower, upper)

            if np.any(mask):
                return True
        except Exception as e:
            print(e)
            pass

        return None