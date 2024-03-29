import os
import subprocess
import re
import socket  # 用于获取IP地址

# 颜色定义
tool = """
        _   _                 _              _     
   ___ | |_| |__   ___ _ __  | |_ ___   ___ | |___ 
  / _ \| __| '_ \ / _ \ '__| | __/ _ \ / _ \| / __|
 | (_) | |_| | | |  __/ |    | || (_) | (_) | \__ \
  \___/ \__|_| |_|\___|_|     \__\___/ \___/|_|___/
                                                   """
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
current_file_path = os.path.dirname(os.path.abspath(__file__))
tools_folder = os.path.join(current_file_path,)


def logo_print(total):
    print(f'''\007
{yellow}{tool}{purple}v4.5

{cyan} ========================================================
{yellow}|              Install Best Hacking Tool                 |
{cyan} ========================================================{nc}



{blue}  [ {white}1 {blue}] {green}Mail boomber
{blue}  [ {white}2 {blue}] {green}Nmap

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


def run_python_script(script_name):
    script_path = os.path.join(tools_folder, script_name)
    try:
        subprocess.run(["python", script_path], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")



def main():
    # Automatically switch to the "Tools" folder
    os.chdir(tools_folder)
    
    total_tools = 8  # 工具总数
    logo_print(total_tools)

    while True:
        user_input = input("\033[1;37m┌──(shiter@main)-[~]\n\033[1;37m└─$")

        if not user_input:
            continue
        
        if user_input.lower() == 'x':
            break

        elif user_input.lower() == '2':
            run_python_script("nmap_scan.py")


        elif user_input.lower() == '1':
            run_python_script("MBomb v2.py")


        elif user_input.lower().startswith('about '):
            url_input = user_input[6:]
            about_url(url_input)

        else:
            result = run_command(user_input)
            print(result)


if __name__ == "__main__":
    main()
