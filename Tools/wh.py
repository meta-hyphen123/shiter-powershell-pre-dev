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
current_file_path = os.path.dirname(os.path.abspath(__file__))
tools_folder = os.path.join(current_file_path)


def logo_print(total):
    print(f'''\007
{yellow}
               _                           
 __      _____| |__    ___  ___ __ _ _ __  
 \ \ /\ / / _ \ '_ \  / __|/ __/ _` | '_ \ 
  \ V  V /  __/ |_) | \__ \ (_| (_| | | | |
   \_/\_/ \___|_.__/  |___/\___\__,_|_| |_|
                                           {purple}v4.5

{cyan} ========================================================
{yellow}|              Install Best Hacking Tool                 |
{cyan} ========================================================{nc}



{blue}  [ {white}1 {blue}] {green}cpscan
{blue}  [ {white}2 {blue}] {green}dsss
{blue}  [ {white}3 {blue}] {green}Struts2scan
{blue}  [ {white}4 {blue}] {green}cmseek
{blue}  [ {white}5 {blue}] {green}droopescan
{blue}  [ {white}6 {blue}] {green}sql
{blue}  [ {white}7 {blue}] {green}DNS-Shell
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
    os.chdir(tools_folder)
    
    total_tools = 8  # 工具总数
    logo_print(total_tools)

    while True:
        user_input = input("\033[1;37m┌──(shiter@main)-[~]\n\033[1;37m└─$")

        if not user_input:
            continue
        
        if user_input.lower() == 'x':
            break

        elif user_input.lower() == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("cps.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()


        elif user_input.lower() == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("dsss.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("S2.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("cmseek.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == '5':

            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("D.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
            
        elif user_input.lower() == '6':

            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("sql.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == '7':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("DNShell.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()




        else:
            result = run_command(user_input)
            print(result)


if __name__ == "__main__":
    main()
