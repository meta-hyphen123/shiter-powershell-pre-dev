import os
import subprocess
import re
import urllib
from urllib.parse import urlparse
import socket
import sys
import os
import time
import random
import urllib.parse



pathdog = os.path.dirname(os.path.abspath(__file__))
pathopen = os.path.join(pathdog, '')
shitermaininput=pathdog+">"
text = r'''welcome to Shiter XSS Tools
'''
def about_url(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        host = parsed_url.hostname
        ip = socket.gethostbyname(host)

        if parsed_url.scheme == 'http':
            port = 80
        elif parsed_url.scheme == 'https':
            port = 443
        else:
            print("Unsupported URL scheme.")
            return

        print(f"URL: {url}\nIP Address: {ip}\nPort: {port}")

    except Exception as e:
        print(f"Error fetching information: {str(e)}")

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        output = result.stdout if result.stdout else result.stderr
        return output
    except Exception as e:
        return f"Error running command: {str(e)}"

def run_python_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")

def main():
    tools_folder = "tools"
    target_path = os.path.join(pathdog, tools_folder)

    print(text)
    while True:
        user_input = input(shitermaininput)
        if not user_input:
            continue
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'xsstrike':
            xss_folder_path = os.path.join(pathdog,"XSStrike-master")
            os.chdir(xss_folder_path)
            run_python_script("xsstrike.py")
        elif user_input.lower() == 'xssxan':
            xss_folder_path = os.path.join(pathdog,"XanXSS-master")
            os.chdir(xss_folder_path)
            run_python_script("xan.py")
        elif user_input.lower() == 'xssxcon':
            xss_folder_path = os.path.join(pathdog,"XSSCon-master")
            os.chdir(xss_folder_path)
            run_python_script("xsscon.py")
        elif user_input.lower() == 'xssfreak':
            run_python_script("XSS-Freak.py")
        elif user_input.lower() == 'xssloader':
            xss_folder_path = os.path.join(pathdog,"xss")
            os.chdir(xss_folder_path)
            run_python_script("payloader.py")
        else:
            result = run_command(user_input)
            print(result)

if __name__ == "__main__":
    main()
