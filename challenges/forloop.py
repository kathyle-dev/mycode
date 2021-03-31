""" FUNCITON LOOPING CHALLENGE"""

# use the provided list of farms
farms = [
    {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
    {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
    {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}
]

# create a list of not animals
not_animals = ["carrots", "celery"]


# helper function to get list of agriculture
def get_agriculture(index):
    return farms[index]["agriculture"]


# helper function to print list of agriculture
def print_agriculture(agriculture):
    for thing in agriculture:
        print(thing)


# function 1: write a for loop returning all animals from NE farm
def get_animals_ne():
    print_agriculture(get_agriculture(0))


# function 2: Ask a user to choose a farm and return agriculture
def ask_user_farm():
    farm = ""
    farms_obj = {
        "NE": 0,
        "W": 1,
        "SE": 2
    }
    while farm not in farms_obj.keys():
        farm = input("Please choose a farm: NE, SE or W to get all things on the farm ").upper()

    print("These are all the things on farm: " + farm)
    print_agriculture(get_agriculture(farms_obj[farm]))


# function 3: ask a user to choose a farm and only return ANIMALS from that particular farm.
def ask_user_farm_only_animals():
    farm = ""
    farms_obj = {
        "NE": 0,
        "W": 1,
        "SE": 2
    }
    while farm not in farms_obj.keys():
        farm = input("Please choose a farm: NE, SE or W to get ONLY the animals on the farm ").upper()

    agriculture = get_agriculture(farms_obj[farm])
    print("These are the animals on farm: " + farm)
    for thing in agriculture:
        if thing not in not_animals:
            print(thing)


# run it all in the main
def main():
    get_animals_ne()
    ask_user_farm()
    ask_user_farm_only_animals()


main()
