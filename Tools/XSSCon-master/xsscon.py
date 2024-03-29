'''
XSSCon - 2019/2020
This project was created by menkrep1337 with 407Aex team. 
Copyright under the MIT license
'''
import argparse
from lib.helper.helper import *
from lib.helper.Log import *
from lib.core import *
from random import randint
from lib.crawler.crawler import *
epilog="""
Github: https://www.github.com/menkrep1337/XSSCon
Version: 0.5 Final
"""
def check(getopt):
	payload=int(getopt.payload_level)
	if payload > 6 and getopt.payload is None:
		Log.info("Do you want use custom payload (Y/n)?")
		answer=input("> "+W)
		if answer.lower().strip() == "y":
			Log.info("Write the XSS payload below")
			payload=input("> "+W)
		else:
			payload=core.generate(randint(1,6))
	
	else:
		payload=core.generate(payload)
			
	return payload if getopt.payload is None else getopt.payload
	
# ...（之前的代码保持不变）

def start():
    print(logo)
    Log.info("Starting XSSCon...")

    choice = input("Choose an option:\n1. Start XSSCon\n2. About XSSCon\n3. Exit\n> ")

    if choice == '1':
        target_url = input("Enter the target URL (e.g., http://testphp.vulnweb.com): ")
        proxy = input("Set proxy (e.g., {'https':'https://10.10.1.10:1080'}) [Press Enter for None]: ")
        user_agent = input("Request user agent (e.g., Chrome/2.1.1/...) [Press Enter for default]: ") or agent
        payload = input("Do you want to use a custom payload? (Y/n): ")
        
        if payload.lower().strip() == "y":
            custom_payload = input("Write the XSS payload below: ")
        else:
            custom_payload = None

        method = input("Method setting(s):\n\t0: GET\n\t1: POST\n\t2: GET and POST (default)\nEnter the method (0/1/2): ") or '2'
        depth = input("Depth web page to crawl. Default: 2\nEnter the depth: ") or '2'
        cookie = input("Set cookie (e.g., {'ID':'1094200543'}) [Press Enter for default]: ") or '''{"ID":"1094200543"}'''

        core.main(target_url, proxy, user_agent, custom_payload, cookie, int(method))
        crawler.crawl(target_url, int(depth), proxy, user_agent, custom_payload, int(method), cookie)

    elif choice == '2':
        print("""
***************
Project: XSSCon
License: MIT
Author: menkrep1337
Last updates: 2019 May 26
Note: Take your own RISK
****************
""" + epilog)

    elif choice == '3':
        print("Exiting XSSCon.")
        return

    else:
        print("Invalid choice. Exiting.")
        return

if __name__ == "__main__":
    start()
