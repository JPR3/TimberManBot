import pyautogui
from pynput import keyboard
BG_COLOR = (176,142,51)
#This program is for this game:
# https://fertiz.itch.io/timberman
print("Tab into Timberman and press space to begin")
# Wait to begin
def on_release(key):
    if key == keyboard.Key.space:
        print("Space pressed!")
        return False
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()
#Start
current = "left"
alt = "right"
man_pos = pyautogui.locateCenterOnScreen("Images/Lumberjack.png", confidence=.9)
global check_r
check_l = man_pos[0]
check_r = pyautogui.size()[0]/2 + (pyautogui.size()[0]/2 - man_pos[0])
check_height = man_pos[1] - 175
check_x = check_l
while(True):
    matches = pyautogui.pixelMatchesColor(int(check_x), int(check_height), BG_COLOR)
    if matches:
        pyautogui.press(current)
    else:
        pyautogui.press(alt)
        current, alt = alt, current
        check_x = check_l if current == "left" else check_r


