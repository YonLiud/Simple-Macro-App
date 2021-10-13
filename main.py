import time
import pyautogui
#import pygetwindow as gw
import os
import ctypes


delay = input("How long between itterations? [Milliseconds] default: 10500: ")
if delay == "":
    delay = 10500
else:
    try:
        delay = float(delay)
    except:
        print("Invalid input")
        input("Press enter to exit")
        exit()
key = input("What key do you want to press? ")
if key == "":
    print("Invalid input")
    input("Press enter to exit")
    exit()
print("Press Ctrl+C to stop")
counter = 5
while counter > 0:
    print(f"Starting in {counter} seconds")
    time.sleep(1)
    counter -= 1
os.system('cls')
print("Starting")
while True:
    try:
        pyautogui.press(key)
        time.sleep(delay/1000)
    except KeyboardInterrupt:
        print("Exiting... Bye Bye Lina!")
        time.sleep(2)
        exit()