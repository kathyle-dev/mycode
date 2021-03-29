#! /usr/bin/env python3

# use the dictionary below to pull the appropriate value based on user's inputs

heroes = {
    "wolverine":
        {"real name": "James Howlett",
         "powers": "regeneration",
         "archenemy": "Sabertooth", },
    "harry potter":
        {"real name": "Harry Potter",
         "powers": "he's a wizard",
         "archenemy": "Voldemort", },
    "agent fitz":
        {"real name": "Leopold Fitz",
         "powers": "intelligence",
         "archenemy": "Hydra", }
}
### make sure user's input is error proof & able to loop through the prompts by putting it in a function


def get_user_input():
    # save a user's input to variable "char_name" & char_stat
    char_name = ""
    char_stat = ""
    while not (char_name in heroes):
        char_name = input(" Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz) ").lower()
    while not (char_stat in heroes[char_name]):
        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) ").lower()
    #print hero's info based on user's input
    print(f"{char_name.capitalize()}'s {char_stat} is = " + heroes[char_name][char_stat])


# create a variable that will hold input for user to exit program
user_exit = ""
while not (user_exit == "q"):
    get_user_input()
    user_exit = input("Press 'q' to quit. Press any other key to try again ").lower()
