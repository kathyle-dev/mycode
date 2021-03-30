## /usr/bin/env python3
# importing the random module for randomly generating user element
import random

### THIS IS THE ULTIMATE "WHICH ELEMENTAL BENDER ARE YOU?" QUIZ!!

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
    "1. What's your favorite color? 1: Red 2: Blue 3. Green 4. White 5. Yellow 6. You didn't list it :(",
    "2. What's your favorite season? 1: Fall 2. Spring 3. Summer 4. Winter 5. All of Them! 6. I hate seasons",
    "3. What's your thoughts on Avatar: The Last Airbender? 1. Loved it 2. Hated it 3. Meh 4. That live-action movie was awesome! 5. Haven't watched it 6. Is that the one with the blue people?",
    "4. Vanilla or Chocolate? 1. Vanilla 2. Chocolate 3. Both 4. Neither 5.Mint 6. Is this for Ice Cream?",
    "5. What's the first thing you'd do with your new abilities? 1. REVENGE 2. Join the Avengers 3. Join the Justice League 4. Become a movie star 5. Rob a bank 6. Code",
    "6. How do you hang toilet paper? 1.Under 2.Over 3. Baby wipes all day 4. Depends on the TP holder 5. I don't use TP 6. However my mom hangs it."
]

#this is a helper function to validate each question
def ask_question(number):
    answer = ""
    tries = 0
    while not int(answer) in range(1,7):
        if tries == 0:
            answer = input(questions[number])
        else:
            answer = input("Sorry bud, You're stuck here until you choose an answer between 1-6. \n" + questions[number])
    return answer
#this is a helper function to print the user's element, dramatically
def print_user_element(element):
    drums = 0
    print("DRUMROLL PLEASE!")
    while drums < 5:
        print("rollrollrollrollrolll")
        drums = drums + 1
    print("Your bending element is: " + element)

#this is the main function
def main():
    number = 0
    user_element = ""
    while number < 6:
        answer = ask_question(number)
        if answer == "6" and number == 2 or number == 4:
            user_element = elements[0]
        elif answer == "5" and number == 3:
            user_element = elements[1]
        elif answer == "2" and number == 5:
            user_element = elements[3]
        else:
            user_element = elements[random.randint(0,5)]
    print_user_element(user_element)


main()