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




print( f'''\007
{yellow}

    |
 ___| ___  ___  ___  ___  ___  ___  ___  ___  ___
|   )|   )|   )|   )|   )|___)|___ |    |   )|   )
|__/ |    |__/ |__/ |__/ |__   __/ |__  |__/||  /
                    |                           {red}v1.33.7

{white}Example invocations:{blue}
  droopescan scan drupal -u URL_HERE
  droopescan scan silverstripe -u URL_HERE
{white}More info:{blue}
  droopescan scan --help
{white}Please see the README file for information regarding proxies.
''')

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
            subprocess.run(["python", "droopescan.py", user_input], check=True)
        except FileNotFoundError:
            print(f"Python interpreter not found. Make sure Python is installed.")
        except subprocess.CalledProcessError as e:
            print(f"Error running Python script: {e}")


