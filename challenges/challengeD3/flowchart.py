#! /usr/bin/env python3
# this is just for the dramatic welcome text
from colorama import Fore, Back, Style

""" THIS IS THE BASIC ENGINEERING FLOWCHART """

# this is a dict that contains all the questions and answers of the "Basic Engineering" flow chart
flowchart = {
    "questions": ["Does it move? ", "Should it? "],
    "answers": {
        "NY": "Spray some WD-40 on it.",
        "YN": "Wrap it up in duct tape!",
        "OK": "It's doing what it's supposed to!"
    }
}


# this helper function will validate user's input meaning ONLY return Y or N
def validate_input(index):
    user_input = ""
    tries = 0
    while not (user_input == "Y" or user_input == "N"):
        # different prompts depending on "how long" they attenpted to answer the question
        if tries > 6:
            print("\nJUST PRESS 'Q' TO GET US OUTTAH HERE!!! ")
        elif tries > 3:
            print("\nAren't you sick of this question yet? You've been stuck here for a while! Just press 'Y' or 'N'! ")
        elif tries > 0:
            print("\nSorry bud, you have to answer Y or N! ")
        print("\nPress 'Q' to quit at any time.")

        user_input = input(flowchart["questions"][index]).upper().strip()

        # to catch if the user wants to quit the program
        if user_input == "Q":
            pressed_q()

        # to keep track of the amount of times the user tried to answer the question
        tries = tries + 1

    return user_input


# this helper function prints the outputs that match the answer. IF not NY or YN, it MUST be OK
def print_output(answer):
    try:
        output = flowchart["answers"][answer]
    except:
        print("\n" + flowchart["answers"]["OK"])
    else:
        print("\n" + output)

# this helper function prints dramatic welcome text on start of program
def cue_dramatic_welcome():
    print(Fore.LIGHTWHITE_EX + Back.RED + "\n ========== BASIC ENGINEERING ============ \n")
    print("NEED TO KNOW WHAT TO DO? GOOGLE NO MORE! ANSWER THE QUESTIONS BELOW")
    print(Style.RESET_ALL)


# this is a helper function to exit the program
def pressed_q():
    print(Fore.LIGHTWHITE_EX + Back.RED + "\n... Exiting ...")
    exit()

# main runtime function
def main():
    index = 0
    answer = ""
    cue_dramatic_welcome()
    while True:
        answer += validate_input(index)
        index = index + 1
        if len(answer) == 2:
            print_output(answer)
            print("Yay! You've gotten your answer! Now go do it. Goodbye.")
            break


main()