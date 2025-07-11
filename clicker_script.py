import keyboard
import pyautogui
import time

print("Press g to start script, then press g to stop script")

while True:
    if keyboard.is_pressed("g"):
        break

time.sleep(0.15)

while True:
    pyautogui.mouseDown(button="left")
    if keyboard.is_pressed("g"):
        pyautogui.mouseUp(button="left")
        break