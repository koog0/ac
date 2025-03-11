import os
import os.path
import subprocess
import sys
import pickle
import requests

RES = '\033[m'
TRED = '\033[31m'
TGREEN = '\033[32m'
TYELLOW = '\033[33m'

try:
    import keyboard
    import pynput
except:
    print(TYELLOW + "[WARNING] Required dependancies were not found, installing dependancies...", RES)
    try:
        subprocess.run(["pip", "install", "keyboard"],check=True)
        subprocess.run(["pip", "install", "pynput"],check=True)

        print(TGREEN + "[OK] Successfully installed dependancies", RES)
    except:
        None

url = "https://raw.githubusercontent.com/koog0/ac/refs/heads/main/"

def getcode(file):
    response = requests.get(f"{url}{file}")
    if response.status_code == 200:
        return response
    else:
        return False

try:
    open("ezacf.conf", "w")
    data = {
        "targetCPS": 10
        }

    with open("ezacf.conf", 'wb') as f:
        pickle.dump(data, f)
        f.close()


    subprocess.run(["attrib","+H","ezacf.conf"],check=True)

except:
    None

banner = """
 /$$$$$$$$ /$$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$$$
| $$_____/|_____ $$  /$$__  $$ /$$__  $$| $$_____/
| $$           /$$/ | $$  \\ $$| $$  \\__/| $$      
| $$$$$       /$$/  | $$$$$$$$| $$      | $$$$$   
| $$__/      /$$/   | $$__  $$| $$      | $$__/   
| $$        /$$/    | $$  | $$| $$    $$| $$      
| $$$$$$$$ /$$$$$$$$| $$  | $$|  $$$$$$/| $$      
|________/|________/|__/  |__/ \\______/ |__/

//@koogo@\\\\
"""

options = """
[[1]] - Launch
[[2]] - Options
[[3]] - Help
"""
print(TGREEN, banner, RES)

def start():
    print(options)

    choice = input("")

    if choice == "1":
        if not os.path.isfile('ezacf.pyw'):
            f = open("ezacf.pyw", "w")
            code = getcode("ac.pyw")
            if code != False:
                f.write(code.text)
                f.close()
                subprocess.run(["attrib","+H","ezacf.pyw"],check=True)
            else:
                print(TRED + "[ERROR] There was an error while trying to retrieve code!", RES)
                sys.exit()
        
        subprocess.Popen(['pythonw', 'ezacf.pyw'])

    elif choice == "2":
        subprocess.run(["attrib","-H","ezacf.conf"],check=True)
        
        with open("ezacf.conf", 'rb') as f:
            dataRetrieved = pickle.load(f)

            print("Current target CPS: " + TGREEN + "[" + str(dataRetrieved["targetCPS"]) + "]", RES)

            choice = input("Desired target CPS: ")

            while not int(choice):
                choice = input("Desired target CPS: ")

            if int(choice) <= 0:
                choice = "1"
            if int(choice) > 500:
                choice = "500"

            print("New target CPS: " + TGREEN + "[" + choice + "]", RES)

            data = {
            "targetCPS": int(choice)
            }

            with open("ezacf.conf", 'wb') as f:
                pickle.dump(data, f)
                f.close()

                subprocess.run(["attrib","+H","ezacf.conf"],check=True)

                f.close()
                start()

    elif choice == "3":
        print(TGREEN + "[NEXT]" + RES + " Auto Left Click")
        print(TGREEN + "[PREVIOUS]" + RES + " Auto Right Click")
        print(TGREEN + "[INSERT]" + RES + " Quit")

        start()

start()

#//@koogo\\#