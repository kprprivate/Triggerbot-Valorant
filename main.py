import ctypes
 
from modules import *
 
import win32api
import time
 
# Global variables
 
class ucPasteTrigger:
    def __init__(self):
        self.loadConfig()
 
        ucPasteTrigger.trigger()
 
 
    def loadConfig(self):
        self.config = configManager.loadConfig()
 
    @staticmethod
    def trigger():
        clicked = False
        global current_mode
        current_mode = "auto"
        global available_modes
        available_modes = ["auto", "pistol", "sniper"]
        global mode_index
        mode_index = 0
        while True:
            try:
                key = varManager.getVar("key", "TRIGGER")
                fovX = varManager.getVar("fovx", "TRIGGER")
                fovY = varManager.getVar("fovy", "TRIGGER")
                mode = varManager.getVar("mode", "TRIGGER")
                delay = int(varManager.getVar("shootdelay", "TRIGGER"))
 
                if win32api.GetAsyncKeyState(ord('I')) < 0:
                        if mode_index < 2:
                            mode_index = mode_index + 1
                        else:
                            mode_index = 0
                        current_mode = available_modese_index]
                        beepSound(440, 75)
                        print(available_modese_index])
                        time.sleep(0.2)
 
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
        if current_mode == "auto":
            win32api.keybd_event(72, 0, 0, 0)
            time.sleep(0.3)
            win32api.keybd_event(72, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.25)
        elif current_mode == "pistol":
            win32api.keybd_event(72, 0, 0, 0)
            time.sleep(0.5)
            win32api.keybd_event(72, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.25)
        elif current_mode == "marshal":
            win32api.keybd_event(72, 0, 0, 0)
            time.sleep(0.4)
            win32api.keybd_event(72, 0, win32con.KEYEVENTF_KEYUP, 0)
 
if __name__ == "__main__":
    trigger = ucPasteTrigger()

#edited by tsu so vanguard dont ban me :3