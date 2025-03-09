import keyboard
import os
import threading
import time

ac = False

def on_space():
    open("myfile.txt", "x")

def on_insert():
    os.system("taskkill /F /IM pythonw.exe")
    os._exit(0)

def auto_type():
    global ac
    while True: 
        if ac:
            keyboard.write("a", delay=0.05)
            time.sleep(0.05)
        else:
            time.sleep(0.1)

typing_thread = threading.Thread(target=auto_type, daemon=True)
typing_thread.start()

while True:
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
        on_space()

    elif event.event_type == keyboard.KEY_DOWN and event.name == 'insert':
        on_insert()

    elif event.event_type == keyboard.KEY_DOWN and event.name == '²':
        ac = not ac
