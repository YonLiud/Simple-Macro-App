import time
import pyautogui
import os
import pygetwindow as gw
os.system('title MacroApp')
print("Press ENTER after every prompt")
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

app = input("App to macro in? ")
if app == "":
    print("Invalid input")
    input("Press enter to exit")
    exit()
elif gw.getWindowsWithTitle(app)[0] == None:
    print("App not found")
    input("Press enter to exit")
    exit()

print("Press Ctrl+C to stop")
counter = 5
while counter > 0:
    print(f"Starting in {counter} seconds")
    time.sleep(1)
    counter -= 1
os.system('cls')
print(f"""Running Macro:
    Delay:  {delay}ms
    Key  :  {key}
    App  :  {app}
Press [CTRL + C] to exit""")
while True:
    try:
        active_app = gw.getActiveWindow()
        print("Active App: "+active_app.title)
        hwnd = gw.getWindowsWithTitle(app)
        if hwnd != []:
            try:
                hwnd[0].activate()
            except:
                hwnd[0].minimize()
                hwnd[0].maximize()
        else:
            print("App not found")
            input("Press enter to exit")
            exit()
        print("App found")
        time.sleep(0.05)
        pyautogui.press(key)
        active_app.activate()
        time.sleep(delay/1000)
    except KeyboardInterrupt:
        print("Keyboard Interruption\nExiting...")
        time.sleep(2)
        exit()
    except Exception as e:
        print(e)
        input("Press enter to exit")
        exit()