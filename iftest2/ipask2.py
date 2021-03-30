#!/usr/bin/env python3
import ipaddress
ipchk = input("Apply an IP address: ") # this line now prompts the user for input
#helper function to check if input is a valid ip address
def validate_address(ipchk):
    try:
        ipaddress.ip_address(ipchk)
    except ValueError:
        print("You did not provide proper input.")
    else:
        print("Looks like the IP address was set: " + ipchk)
## if user set IP of gateway
# IF it matches the gateway, immediately print the following ELSE, must check f it is a valid input
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
else:
    validate_address(ipchk)


# print exit string
print("exiting program")
