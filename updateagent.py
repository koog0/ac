import requests
import os
import os.path
import json
import base64

endpoint = "https://raw.githubusercontent.com/koog0/ac/refs/heads/main/"

def remove_trailing_empty_lines(text):
    lines = text.splitlines()
    
    while lines and not lines[-1].strip():
        lines.pop()
    
    return '\n'.join(lines)

def update_launcher():
    try:
        response = requests.get(endpoint + "ezacf.py")
        
        gitCode = response.text
        gitCode = remove_trailing_empty_lines(gitCode)

        with open("ezacf.py", "r") as f:
            userCode = f.read()
            f.close()

            userCode = remove_trailing_empty_lines(userCode)
        
        if userCode != gitCode:
            with open("ezacf.py", "w") as f:
                f.write(gitCode)
                f.close()
    except:
        None

def update_program():
    try:
        response = requests.get(endpoint + "newezacf.pyw")
        
        gitCode = response.text
        gitCode = remove_trailing_empty_lines(gitCode)

        with open("newezacf.pyw", "r") as f:
            userCode = f.read()
            f.close()

            userCode = remove_trailing_empty_lines(userCode)
        
        if userCode != gitCode:
            with open("newezacf.pyw", "w") as f:
                f.write(gitCode)
                f.close()
    except:
        None
