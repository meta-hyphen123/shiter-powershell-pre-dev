



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
tools_folder = os.path.join(current_file_path, 'Tools')


def logo_print(total):
    print("""Shiter PowerShell
版权所有（C） Shiter attack。保留所有权利。

安装最新的 PowerShell，了解新功能和改进！https://github.com/meta-hyphen123/Shiter-Attack-Tools/          
          """)





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
        user_input = input(tools_folder+">")

        if not user_input:
            continue
        
        if user_input.lower() == 'exit':
            break

        elif user_input.lower() == 'ddos':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("ddos_Open.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()


        elif user_input.lower() == 'sql':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("sql.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == 'psyflood':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("psyflood.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == 'other':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("Other Tools.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == 'sniff':

            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("Shiter_Snifer.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
            
        elif user_input.lower() == 'dns-shell':

            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("DNShell.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        elif user_input.lower() == 'all-in-one':

            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("aio.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif user_input.lower() == 'xss':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("XSS_Open.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
            
        elif user_input.lower() == 'web-hacking':
            os.system('cls' if os.name == 'nt' else 'clear')
            run_python_script("wh.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()


        elif user_input.lower() == 'web2attack':
            os.system('cls' if os.name == 'nt' else 'clear')
            xss_folder_path = os.path.join(current_file_path, "Tools/web2attack-master")
            os.chdir(xss_folder_path)
            run_python_script("w2aconsole.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()


        else:
            result = run_command(user_input)
            print(result)


if __name__ == "__main__":
    main()
