import requests
import os.path
import os
import yaml

"""
btn_press
Function controls the buttons being pressed on the Snom phone
via HTTP API calls.
btn2: string variable defines the pressed key on the keyboard.
"""


def btn_press(btn2):
    print (btn2)
    # Convert keyboard map to phone key map
    for btn in btn2:
        if btn == "c":
            btn = "CANCEL"
        elif btn == "e":
            btn = "ENTER"
        elif btn == "a":
            btn = "OFFHOOK"
        elif btn == "h":
            btn = "ONHOOK"
        elif btn == "r":
            btn = "RIGHT"
        elif btn == "l":
            btn = "LEFT"
        elif btn == "r":
            btn = "RIGHT"
        elif btn == "u":
            btn = "UP"
        elif btn == "d":
            btn = "DOWN"
        elif btn == "+":
            btn = "VOLUME_UP"
        elif btn == "-":
            btn = "VOLUME_DOWN"
        elif btn == "menu":
            btn = "MENU"
        elif btn == "re":
            btn = "REDIAL"
        elif btn == "re":
            btn = "REDIAL"
        elif btn == "dnd":
            btn = "DND"
        elif btn == "m":
            btn = "REC"
        elif btn == "s":
            btn = "SPEAKER"
        elif btn == "head":
            btn = "HEADSET"
        elif btn == "t":
            btn = "TRANSFER"
        elif btn == "hold":
            btn = "F_HOLD"
        elif btn == "<":
            btn = "F1"
        elif btn == ">":
            btn = "F2"
        elif btn == "/":
            btn = "F3"
        elif btn == "":
            btn = "F4"
        elif btn == "?":
            btn = "?"

            print ""
            print "KEY COMMAND LIST"
            print ""
            print "c    -      Simulates pressing the CANCEL key"
            print "e    -      Simulates pressing the ENTER key"
            print "a    -      Simulates lifting up the handset"
            print "hang -      Simulates hanging up the handset"
            print "r    -      Simulates pressing the RIGHT navigation key"
            print "l    -      Simulates pressing the LEFT navigation key"
            print "u    -      Simulates pressing the UP navigation key"
            print "d    -      Simulates pressing the DOWN navigation key"
            print "+    -      Simulates pressing VOLUME UP key"
            print "-    -      Simulates pressing VOLUME DOWN key"
            print "menu -      Simulates pressing the MENU key"
            print "re   -      Simulates pressing the REDIAL key"
            print "dnd  -      Simulates pressing the DND key"
            print "m    -      Simulates pressing the MUTE key"
            print "s    -      Simulates pressing the SPEAKER key"
            print "h    -      Simulates pressing the HEADSET key"
            print "t    -      Simulates pressing the TRANSFER key"
            print "hold -      Simulates pressing the HOLD key"
            print "0    -      Simulates pressing the 0 key"
            print "1    -      Simulates pressing the 1 key"
            print "2    -      Simulates pressing the 2 key"
            print "3    -      Simulates pressing the 3 key"
            print "4    -      Simulates pressing the 4 key"
            print "5    -      Simulates pressing the 5 key"
            print "6    -      Simulates pressing the 6 key"
            print "7    -      Simulates pressing the 7 key"
            print "8    -      Simulates pressing the 8 key"
            print "9    -      Simulates pressing the 9 key"
            print "*    -      Simulates pressing the * key"
            print "#    -      Simulates pressing thr # key"
            print ""
            print "NOTE - SOME BROWSERS REQUIRE %23 FOR # and %2A FOR *"
            print ""
            print "<    -       Simulates pressing the F1 key"
            print ">    -       Simulates pressing the F2 key"
            print "/    -       Simulates pressing the F3 key"
            print "@    -       Simulates pressing the F4 key"
            print ""
            print "NOTE - THE \"F\" KEYS ARE LOCATED UNDER THE MAIN SCREEN"
            print ""
            return

        # Get the phone's config
        username, password, address = parse_config()

        # Post HTTP request to phone
        r = requests.post("http://"+str(username)+":"+str(password)+"@"+str(address)+"/command.htm?key="+str(btn))
        print(r.text)

"""
check_config
The variable checks that the .snom
directory exists on the users
computer and prompts user to input config details if not
"""


def check_config():
    if not os.path.exists(os.path.expanduser('~/.snom/config.yaml')):
        doc = {"config": {"username": '', "password": '', "address": ''}}

        # Prompts user to enter their config details
        doc["config"]["username"] = raw_input("Enter your phone's Username: ")
        doc["config"]["password"] = raw_input("Enter your phone's Password: ")
        doc["config"]["address"] = raw_input("Enter your phone's IP address: ")

        # Creates the directory
        if not os.path.exists(os.path.expanduser('~/.snom/')):
            os.makedirs(os.path.expanduser('~/.snom/'))

        # Writes user inputs to the directory
        with open(os.path.expanduser('~/.snom/config.yaml'), 'w') as outfile:
            yaml.dump(doc, outfile, default_flow_style=False)

"""
parse_config
This variable reads the config file
from the users computer
"""


def parse_config():
    with open(os.path.expanduser('~/.snom/config.yaml'), 'r') as f:
        doc = yaml.load(f)

        username = doc["config"]["username"]
        password = doc["config"]["password"]
        address = doc["config"]["address"]
        return username, password, address

"""
input
This variable requires user input
to communicate with the phone
"""


def input():
    while True:
        press = raw_input("Press a button to use your phone or press ? for help: ")

        btn_press(press)

check_config()
input()
