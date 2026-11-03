import pyautogui
import time
times = 5
type_text = input("enter your text :")

print("Click where you want the typing to start...")
time.sleep(3)

for i in range(times) :
    pyautogui.write(type_text,interval=0.05)
    pyautogui.press("enter")
    pyautogui.press("_")

print("printing is compleated!")





