from winsound import Beep, PlaySound, SND_FILENAME


def playSound(soundPath):
    try:
        PlaySound(soundPath, SND_FILENAME)
    except:
        pass


def beepSound(mhz, long):
    try:
        Beep(mhz, long)
    except:
        pass
