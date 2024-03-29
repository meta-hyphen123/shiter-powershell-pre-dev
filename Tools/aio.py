import os
import subprocess
import re
import socket  # 用于获取IP地址

# 颜色定义
red = "\033[1;31m"
yellow = "\033[38;2;255;253;85m"  # 使用 RGB 颜色值定义黄色
green = "\033[38;2;255;253;85m"   # 使用 RGB 颜色值定义绿色
blue = "\033[38;2;255;253;85m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
violate = "\033[1;37m"
nc = "\033[00m"
white = "\033[1;37m"

# 获取当前 Python 文件的路径
pathdog = os.path.dirname(os.path.abspath(__file__))


def logo_print(total):
    print(f'''\007
{yellow}
     _    _ _   _                             _                _    
    / \  | | | (_)_ __     ___  _ __   ___   | |__   __ _  ___| | __
   / _ \ | | | | | '_ \   / _ \| '_ \ / _ \  | '_ \ / _` |/ __| |/ /
  / ___ \| | | | | | | | | (_) | | | |  __/  | | | | (_| | (__|   < 
 /_/   \_\_|_| |_|_| |_|  \___/|_| |_|\___|  |_| |_|\__,_|\___|_|\_\\
                                                                    {purple}v4.5

{cyan} ========================================================
{yellow}|              Install Best Hacking Tool                 |
{cyan} ========================================================{nc}



{blue}  [ {white}1 {blue}] {green}Wifi-hacking
{blue}  [ {white}2 {blue}] {green}Big-Tool
{blue}  [ {white}3 {blue}] {green}fsociety
{blue}  [ {white}4 {blue}] {green}Hacked
{blue}  [ {white}5 {blue}] {green}hacknix
{blue}  [ {white}6 {blue}] {green}PhoneSploit-Pro
{blue}  [ {white}7 {blue}] {green}Tool SS
{blue}  [ {white}x {blue}] {green}exit

{white} ________________________________________________________
 ========================================================
''')



shitermaininput = """
┌──(shiter@main)-[~]
└─$"""


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

def rshell():
    try:
        subprocess.run(["./alhack.sh"], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")


def main():
    # Automatically switch to the "Tools" folder
    os.chdir(pathdog)
    
    total_tools = 8  # 工具总数
    logo_print(total_tools)

    while True:
        user_input = input("\033[1;37m┌──(shiter@main)-[~]\n\033[1;37m└─$")

        if not user_input:
            continue
        if user_input.lower() == 'x':
            break
        elif user_input.lower() == '1':
            xss_folder_path = os.path.join(pathdog,"Wifi-Hacking")
            os.system('cls' if os.name == 'nt' else 'clear')
            os.chdir(xss_folder_path)
            run_python_script("Wifi-Hacking.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        elif user_input.lower() == '2':
            xss_folder_path = os.path.join(pathdog,"Big-Tool")
            os.system('cls' if os.name == 'nt' else 'clear')
            os.chdir(xss_folder_path)
            run_python_script("tools")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        elif user_input.lower() == '3':
            xss_folder_path = os.path.join(pathdog,"fsociety")
            os.system('cls' if os.name == 'nt' else 'clear')
            os.chdir(xss_folder_path)
            run_python_script("fsociety.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        elif user_input.lower() == '4':
            xss_folder_path = os.path.join(pathdog,"hacked")
            os.system('cls' if os.name == 'nt' else 'clear')
            os.chdir(xss_folder_path)
            run_python_script("hacked.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == '5':
            xss_folder_path = os.path.join(pathdog,"hacknix")
            os.system('cls' if os.name == 'nt' else 'clear')
            os.chdir(xss_folder_path)
            run_python_script("hacknix.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == '6':
            xss_folder_path = os.path.join(pathdog,"PhoneSploit-Pro-main")
            os.system('cls' if os.name == 'nt' else 'clear')
            os.chdir(xss_folder_path)
            run_python_script("phonesploitpro.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
            
        elif user_input.lower() == '7':
            os.system('cls' if os.name == 'nt' else 'clear')

            run_python_script("toolss.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
            
        else:
            result = run_command(user_input)
            print(result)

if __name__ == "__main__":
    main()

