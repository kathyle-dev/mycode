#! /usr/bin/env python3
# importing the random module for randomly generating user element
import random

""" THIS IS THE ULTIMATE "WHICH ELEMENTAL BENDER ARE YOU?" QUIZ!! """

# this is a list of all possible elements a person can get from the quiz
elements = [
    "None. You are a mere human with no bending abilities. Whomp Whomp.",
    "Blood. Yikes. You must be the one who chose Mint over Vanilla or Chocolate.",
    "Water. The coolest one of all!",
    "Fire. You're also probably a Slytherin",
    "Earth. But can you Metal bend doe?",
    "Air. You're the second-to-last Airbender!"
]

# this is the list of quiz questions
questions = [
    "(1) What's your favorite color? \n1: Red \n2: Blue \n3. Green \n4. White \n5. Yellow \n6. You didn't list it :( \n",
    "(2) What's your favorite season? \n1: Fall \n2. Spring \n3. Summer \n4. Winter \n5. All of Them! \n6. I hate seasons \n",
    "(3) What's your thoughts on Avatar: The Last Airbender? \n1. Loved it \n2. Hated it \n3. Meh \n4. That live-action movie was awesome! \n5. Haven't watched it \n6. Is that the one with the blue people? \n",
    "(4) Vanilla or Chocolate? \n1. Vanilla \n2. Chocolate \n3. Both \n4. Neither \n5. Mint \n6. Is this for Ice Cream? \n",
    "(5) What's the first thing you'd do with your new abilities? \n1. REVENGE \n2. Join the Avengers \n3. Join the Justice League \n4. Become a movie star \n5. Rob a bank \n6. Code \n",
    "(6) How do you hang toilet paper? \n1. Under \n2. Over \n3. Baby wipes all day \n4. Depends on the TP holder \n5. I don't use TP \n6. However my mom hangs it. \n"
]


# this is a helper function to validate each question
def ask_question(number):
    error_msg = "Sorry bud, You're stuck here until you choose an answer between 1-6."
    while True:
        try:
            answer = input(questions[number]).strip()
            if int(answer) in range(1, 7):
                return answer  # if the answer is between 1-6, this will break the while loop
            else:  # this else is for when it CAN be converted to an int but it is NOT a valid answer i.e. between 1-6
                print(error_msg)
        except:  # this is to catch the exception when the input cannot be converted into an int
            print(error_msg)


# this is a helper function to print the user's element, dramatically
def print_user_element(element):
    drums = 0
    print("DRUMROLL PLEASE!")
    while drums < 5:
        print("rollrollrollrollrolll")
        drums = drums + 1
    print()  # empty new line for read-ability
    print("Your bending element is: " + element)


# this is the main function
def main():
    number = 0
    user_element = ""

    # this loop will take the user through all 6 questions and assign them to an element depending on SPECIFIC answers
    while number < 6:
        answer = ask_question(number)
        if answer == "6" and (number == 2 or number == 4 or number == 5):
            user_element = elements[0]
        elif (answer == "5" and number == 3) or (answer == "1" and number == 4) or (answer == "5" and number == "5"):
            user_element = elements[1]
        number = number + 1

    # if the user completes quiz without any element assigned, one will randomly be assigned now
    if user_element == "":
        user_element = elements[random.randint(0, 5)]

    print_user_element(user_element)
    print("Exiting Quiz. You can't change what you are!!")


main()
