import keyboard
from pynput import mouse
from pynput.mouse import Button, Controller
import os
import threading
import time
import pickle
import subprocess

uMouse = Controller()

ac = False
ac2 = False
last_toggle_time = 0

targetCPS = None

def getTargetCPS():
    global targetCPS

    subprocess.run(["attrib","-H","ezacf.conf"],check=True)
        
    with open("ezacf.conf", 'rb') as f:
        dataRetrieved = pickle.load(f)

        targetCPS = int(dataRetrieved["targetCPS"])

        f.close()
        subprocess.run(["attrib","+H","ezacf.conf"],check=True)

getTargetCPS()

def on_insert():
    os.system("taskkill /F /IM pythonw.exe")
    os._exit(0)

def auto_click():
    global ac
    global ac2
    while True:
        if ac:
            uMouse.click(Button.left, 1)
        if ac2:
            uMouse.click(Button.right, 1)
        time.sleep(1 / targetCPS)
            
def insert():
    while True:
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN and event.name == 'insert':
            on_insert()

clicking_thread = threading.Thread(target=auto_click, daemon=True)
clicking_thread.start()

insert_thread = threading.Thread(target=insert, daemon=True)
insert_thread.start()

def on_click(x, y, button, pressed):
    global ac
    global ac2
    if button == Button.x2:
        if pressed:
            ac = True
        else:
            ac = False
    elif button == Button.x1:
        if pressed:
            ac2 = True
        else:
            ac2 = False

with mouse.Listener(
        on_click=on_click) as listener:
    listener.join()

listener = mouse.Listener(
    on_click=on_click)
listener.start()
