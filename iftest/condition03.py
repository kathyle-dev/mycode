#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
## CODE CUSTOMIZATION: IF hostname is mtg, print a SECOND line
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")
## add ANOTHER CODE CUSTOM: if the input is NOTHING, print out another string
elif hostname == "":
    print("You didn't type anything in, DUMMY!")
## display that the program is exiting
print("Exiting the script.")

