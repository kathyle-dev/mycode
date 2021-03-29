#! /usr/bin/env python3

# use the dictionary below to pull the appropriate value based on user's inputs

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "he's a wizard",
    "archenemy": "Voldemort",},
"agent fitz":
    {"real name": "Leopold Fitz",
    "powers": "intelligence",
    "archenemy": "Hydra",}
        }
### make sure user's input is error proof

#save a user's input to variable "char_name"
hero_names = heroes.keys()
char_name = ""
while !hero_names__contains__(char_name):
    char_name = input(" Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz) ")

# save a user's input to variable "char_stat"
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) ")

print(f"{char_name.capitalize()}'s {char_stat} is = " + heroes[char_name.lower()][char_stat.lower()])
