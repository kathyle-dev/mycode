#! /usr/bin/env python3

# the following 3 are pre-written lists to use
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{
    'slappy': 'a',
    'text': 'b',
    'kumquat': 'goggles',
    'user': {'awe    some': 'c', 'name': {'first': 'eyes',
             'last': 'toes'}},
    'banana': 15,
    'd': '    nothing',
    }]

## from each list, pull "eyes", "goggles" and "nothing" and create a print function

#helper function to print quote
def print_quote(eyes,goggles,nothing):
    print(f"My {eyes}! The {goggles} do {nothing}!")

#print from challenge
print_quote(challenge[2][1], challenge[2][0], challenge[3])

#print from trial
print_quote(trial[2]["goggles"], trial[2]["eyes"],trial[3])

#print from nightmare
print_quote(nightmare[0]["user"]["name"]["first"], nightmare[0]["kumquat"], nightmare[0]["d"].strip())

