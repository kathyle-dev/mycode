#!/usr/bin/env python3

# create a list containing three items
my_list=["192,168,0.5", 5060, "UP"]


# display the first item in the list
print("This first item in the list (IP): " + my_list[0])

# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]))

# display the third item in the list
print("The last itme in the list (state): " + my_list[2])


#create a new list containing 6 items
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#display all iems in the list using ONE print function
print(f"In order to access ports {str(new_list[0])}, {new_list[1]},  or {str(new_list[2])} I need to {new_list[-1]} into IP address {new_list[3]} or {new_list[4]}.")
