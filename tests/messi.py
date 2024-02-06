
from ctypes import WinDLL
import mss
import time
from PIL import Image
from mss import mss as mss_module
import dxcam

cam = dxcam.create(output_color='BGRA')

user32, kernel32, shcore = (
    WinDLL("user32", use_last_error=True),
    WinDLL("kernel32", use_last_error=True),
    WinDLL("shcore", use_last_error=True),
)

shcore.SetProcessDpiAwareness(2)
WIDTH, HEIGHT = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

ZONE = 5
GRAB_ZONE = (
    int(WIDTH / 2 - ZONE),
    int(HEIGHT / 2 - ZONE),
    int(WIDTH / 2 + ZONE),
    int(HEIGHT / 2 + ZONE),
)

print(GRAB_ZONE)


sct = mss_module()

# Sct grab zone and show file


# time.sleep(2)
import numpy as np
# img = sct.grab(GRAB_ZONE)
# mss.tools.to_png(img.rgb, img.size, output='sct.png')

# print(np.array(sct.grab(GRAB_ZONE)))

time.sleep(2)

frame = cam.grab(GRAB_ZONE)

print(np.array(frame))
