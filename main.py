import ctypes

from modules import *

import time


class ucPasteTrigger:
    def __init__(self):
        self.loadConfig()

        ucPasteTrigger.trigger()

    def loadConfig(self):
        self.config = configManager.loadConfig()


    @staticmethod
    def trigger():
        clicked = False
        while True:
            try:
                key = varManager.getVar("key", "TRIGGER")
                fovX = varManager.getVar("fovx", "TRIGGER")
                fovY = varManager.getVar("fovy", "TRIGGER")
                mode = varManager.getVar("mode", "TRIGGER")
                delay = int(varManager.getVar("shootdelay", "TRIGGER"))

                if mode == "Toggle" and keyPressed(key):
                    clicked = not clicked

                    if clicked:
                        beepSound(440, 75)
                        beepSound(700, 100)
                        print("ON")
                    else:
                        beepSound(440, 75)
                        beepSound(200, 100)
                        print("OFF")

                    while keyPressed(key):
                        pass

                elif ((mode == "Toggle" and clicked) or mode == "Holding" and keyPressed(key)) and not any([keyPressed("W"), keyPressed("A"), keyPressed("S"), keyPressed("D")]):
                    enemy = uiPasteFunctions.findEnemyTrigger(int(fovX), int(fovY))
                    if enemy:
                        ucPasteTrigger.shoot()
                        time.sleep(200 * delay / 1000)

                time.sleep(0.005)
            except Exception as e:
                print(e)
                pass

    @staticmethod
    def shoot():
        ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)  # L DOWN
        time.sleep(0.01)
        ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)  # L UP


# BRAZILIAN PASTERS ON TOP. 
# JOINUS - MY3
if __name__ == "__main__":
    trigger = ucPasteTrigger()
