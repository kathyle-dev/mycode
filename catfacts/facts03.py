#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random  # to get a random cat fact


def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    
    #CUSTOM 01 - TRY OTHER METHODS ON THE REQUEST OBJ
    print(r.headers)
    print(r.status_code)
    print(r.elapsed)

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    for catfact in r.json():
        print(catfact.get("text"))  # the .get() method returns NONE if key not found


def get_random():
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    # CUSTOMIZATION 02 -try getting a SINGLE random fact
    print("This is your random cat fact: " + random.choice(r.json()).get("text"))


get_random()

main()
