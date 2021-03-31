#!/usr/bin/env python3
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    print("There are these many lines in the vlanconfig.cfg file: ", len(configlist))  # CUSTOMIZATION CODE 03
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

