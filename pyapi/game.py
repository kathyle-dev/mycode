import random


class Game:
    def __init__(self, **kwargs):
        # start the player in the Hall
        self.currentRoom = "Hall"
        # let the game be initialized with an items and rooms dictionary, that will be given on initialization
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def showInstructions():
        # print a main menu and the commands
        print('''
        RESIDENT ZOMBIES
        ========
        Commands:
          Go [direction]
          Get [item]
          Use [item]
          Examine [item or room]
          Quit
          
          So many zombies. I gotta get outta here. 
        ''')

    def showStatus(self, hero):
        # print the player's current status
        print('---------------------------')
        print('You are in the ' + str(self.currentRoom))
        # print the current inventory
        hero.displayInventory()
        # print player's current health level
        hero.displayHealth()
        # print an item if there is one
        if "item" in getattr(self, "rooms")[getattr(self, "currentRoom")]:
            print("You see a ", getattr(self, "rooms")[getattr(self, "currentRoom")]["item"])

        # print possible directions
        if "paths" in getattr(self, "rooms")[getattr(self, "currentRoom")]:
            paths = getattr(self, "rooms")[getattr(self, "currentRoom")]["paths"]
            for path in paths:
                print("You can go " + path + " to the " + str(
                    getattr(self, "rooms")[getattr(self, "currentRoom")]["paths"][path]))
        print("---------------------------")

    @staticmethod
    def randomCombat(hero, zombie):
        fate = random.choice(["combat", "safe"])
        if fate == "combat":
            print("X X X X X X X X X X X X X X X X X X X X X X X X\n")
            print("Oh no! A zombie has heard you coming and is running towards you!")
            print("\nX X X X X X X X X X X X X X X X X X X X X X X X")
            hero.fight(zombie)

    def startGame(self, hero, zombie):
        self.showInstructions()
        turns = 0
        while True:
            if turns > 3:
                self.randomCombat(hero, zombie)

            self.showStatus(hero)

            # get the player's next 'move'
            # .split() breaks it up into an list array
            # eg typing 'go east' would give the list:
            # ['go','east']
            move = ''
            while move == '':
                move = input('>').strip()

            # split allows an items to have a space on them
            # Get Golden Key is returned ["Get", "Golden Key"]
            move = move.title().split(" ", 1)

            # if they want to quit, break them out of the loop to exit
            if move[0] == "Quit":
                print("Quiting.... The zombies are still out there......")
                break

            # if they type 'go' first
            if move[0] == 'Go':
                room = getattr(self, "rooms")[getattr(self, "currentRoom")]["paths"][move[1]]
                # check that they are allowed wherever they want to go
                if move[1] in getattr(self, "rooms")[getattr(self, "currentRoom")]["paths"]:
                    if room == "Garden" and getattr(self, "rooms")["Garden"]["locked"]:
                        print("Door's locked. Seems like the only way out...")
                    # set the current room to the new room
                    else:
                        setattr(self, "currentRoom", room)
                # there is no door (link) to the new room
                else:
                    print('You can\'t go that way!')

            # if they type 'get' first
            if move[0] == 'Get':
                # if the room contains an item, and the item is the one they want to get
                if "item" in getattr(self, "rooms")[getattr(self, "currentRoom")] and (
                        move[1] == getattr(self, "rooms")[getattr(self, "currentRoom")]['item']):
                    # add the item to their inventory
                    hero.getInventory(move[1], getattr(self, "items")[move[1]])
                    # display a helpful message
                    print("You took the " + move[1] + '!')
                    # delete the item from the room
                    del getattr(self, "rooms")[getattr(self, "currentRoom")]['item']
                # otherwise, if the item isn't there to get
                else:
                    # tell them they can't get it
                    print('Can\'t get ' + move[1] + '!')

            # if they type 'examine' first
            if move[0] == 'Examine':
                # if they typed a room second, and they are in that room display the room's description
                if move[1] in getattr(self, "rooms") and move[1] == getattr(self, "currentRoom"):
                    print(getattr(self, "rooms")[getattr(self, "currentRoom")]["desc"])
                # if they typed an item second, display the item's description
                elif ("item" in getattr(self, "rooms")[getattr(self, "currentRoom")] and move[1] in
                      getattr(self, "rooms")[getattr(self, "currentRoom")]['item']) or move[1] in \
                        hero.inventory[getattr(self, "items")[move[1]]["type"]]:
                    # if the item is a gun, display the current number of bullets
                    if move[1] == "Gun":
                        print(getattr(self, "items")[move[1]]["desc"], getattr(self, "items")[move[1]]["bullets"],
                              " bullets.")
                    # otherwise print normally
                    else:
                        print(getattr(self, "items")[move[1]]["desc"])
                # otherwise, the room or item isn't there to describe
                else:
                    # tell them they can't look at it
                    print("Can't look at the " + move[1] + ". Are you seeing things?")

            # if they type 'use' first
            if move[0] == 'Use':
                # if they have the item, they can use it
                if move[1] in hero.inventory[getattr(self, "items")[move[1]]["type"]]:
                    fate = hero.useItem(move[1], getattr(self, "items")[move[1]]["type"])
                    if move[1] == "Key" and fate == "success":
                        getattr(self, "rooms")["Garden"]["locked"] = False
                # otherwise they can't use what they don't have
                else:
                    print("You don't have a " + move[1] + " to use!")

            turns += 1

            if (len(getattr(hero, "inventory")["weapons"].keys()) + len(
                    getattr(hero, "inventory")["aid"].keys()) == len(
                getattr(self, "items").keys())) and self.currentRoom == "Garden":
                print("You've made it out in one piece!")
                print("You Win.")
