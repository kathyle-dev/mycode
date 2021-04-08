#! /usr/bin/env python3

import os

#install sl
os.system("sudo apt install sl")
print("sl was installed")

path = os.getcwd() + "/slappy"

# create a new dir called slappy within /mycode
dir = os.path.join(path)
if not os.path.exists(dir):
    os.mkdir(dir)
    print("The slappy directory has been created.")
else:
    print("Slappy directory has already been made here!")

#create a new file "chad_stop_using_that_word.txt" inside this new dir
file = "chad_stop_using_that_word.txt"
with open(os.path.join(path, file), 'w') as fp:
    pass
print('"chad_stop_using_that_word.txt" has been created!')
