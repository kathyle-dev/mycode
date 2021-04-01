#!/usr/bin/env python3
from colorama import Fore, Back, Style
import random
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        random_color()
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            random_color()
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

# cutomization 01 -- change the color output on screen -- trying to randomize
def random_color():
    colors = ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"]
    fore_color = random.choice(colors)
    colors.remove(fore_color)
    back_color = random.choice((colors))
        
    print(getattr(Fore, fore_color)) 
    print(getattr(Back, back_color))


# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices

# call our main function
main()

