import os
import subprocess

# 颜色定义
red = "\033[1;31m"
yellow = "\033[38;2;255;253;85m"
green = "\033[38;2;255;253;85m"
blue = "\033[38;2;255;253;85m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
violate = "\033[1;37m"
nc = "\033[00m"
white = "\033[1;37m"

pathdog = os.path.dirname(os.path.abspath(__file__))
os.chdir(pathdog)
print(f'''\007
{red}


              _______  ___ _______ ____
             / __/ _ \(_-</ __/ _ `/ _ \.
             \__/ .__/___/\__/\_,_/_//_/
               /_/ v 1.0 - susmithHCK


            {white}

        USAGE:
         -t  --target   - Target web server "example.com"
         -v  --verbose  - Enable verbose mode
         -h  --help     - show this menu

        EXAMPLE:
          python cpscan.py -t targetsite.com -v
{white}
=================================================================
{yellow}     [00]back
{white}=================================================================''')


while True:
    shitermaininput = """
┌──(shiter@main)-[cpscan]
└─$ """

    # 用户输入的参数
    user_input = input(shitermaininput)
    
    if user_input.lower() == '00':
        exit()

    else:
    


        try:
            subprocess.run(["python", "cpscan.py", user_input], check=True)
        except FileNotFoundError:
            print(f"Python interpreter not found. Make sure Python is installed.")
        except subprocess.CalledProcessError as e:
            print(f"Error running Python script: {e}")

