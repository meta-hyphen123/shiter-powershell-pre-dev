import os
import subprocess
import re
import tkinter as tk
from tkinter import filedialog
from rich import print
import urllib
from urllib.parse import urlparse
import time
import socket  # Add this import for the socket module
import sys
import os
import time
from tqdm import tqdm
import socket
import random
from rich import print
from colorama import Fore, Style  
from rich.console import Console
import urllib.parse  # Add this import

console = Console()

# 获取当前脚本所在文件夹的路径
pathdog = os.path.dirname(os.path.abspath(__file__))

# 使用 os.path.join 构建路径
pathopen = os.path.join(pathdog, '')

text =r'''welcome to ddos tools
'''



def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        output = result.stdout if result.stdout else result.stderr
        return output
    except Exception as e:
        return f"Error running command: {str(e)}"


def run_python_script(script_name):
    script_path = os.path.join(pathopen, script_name)
    try:
        subprocess.run(["python", script_path], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")

def run_sqlmap():
    script_path = os.path.join(tools_folder, "sqlmap.py")
    try:
        subprocess.run(["python", script_path, "--wizard"], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")

# 获取本机IP地址
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        print(f"Error getting local IP address: {e}")
        return None

def main():
    # Automatically switch to the "Tools" folder
    os.chdir(pathopen)
    
    print(text)

    while True:
        user_input = input(pathopen+">")

        if not user_input:
            continue
        
        if user_input.lower() == 'exit':
            break




        elif user_input.lower() == 'ddos-ripper':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("DRipper.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == 'ddos':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("ddos-attack.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()


            
        elif user_input.lower() == 'hulk':

            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("hulk.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == 'hulk-gui':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("hulk-gui.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()




        else:
            result = run_command(user_input)
            print(result)


if __name__ == "__main__":
    main()
