"""THESE ARE CLASSES TO BE USED IN MY ZOMBIE RPG GAME"""
import random


class Player:
    def __init__(self, **kwargs):
        self.health = 20
        for key, value in kwargs.items():
            setattr(self, key, value)

    def displayHealth(self):
        print("Your current health is = ", self.health)

    def heal(self):
        self.health = 20
        print("Your health is back up to", self.health, "for now...")

    def getInventory(self, item, value):
        item_type = value["type"]
        getattr(self, "inventory")[item_type].update({item: value})

    def displayInventory(self):
        # print the current inventory
        weapons = getattr(self, "inventory")["weapons"].keys()
        aid = getattr(self, "inventory")["aid"].keys()
        print('Inventory = Weapons:', list(weapons), "Aid:", list(aid))

    def useItem(self, item, item_type):
        # randomly choose if the player uses item "successfully" or "fails"
        fate = random.choice(["success", "failure"])
        # if it was a gun, check if you can use it.
        if item == "Gun":
            # it has bullets so decrease bullets
            if getattr(self, "inventory")["weapons"]["Gun"]["bullets"] > 0:
                getattr(self, "inventory")["weapons"]["Gun"]["bullets"] -= 1
                print(getattr(self, "inventory")["weapons"][item][fate])
                print("Hope it was worth it. Ammo left = ", getattr(self, "inventory")["weapons"]["Gun"]["bullets"])
            # otherwise they can't use it
            else:
                print("Out of ammo! You better find some.")
                return "failure"

        # it's not a gun so it can be used
        else:
            # print their fate
            print(getattr(self, "inventory")[item_type][item][fate])
            # the sandwich failure is automatic game over!
            if item == "Sandwich":
                if fate == "failure":
                    print("Game Over.")
                    exit()
                else:
                    self.heal()
        return fate

    def fight(self, zombie):
        current_player = "hero"
        while (self.health > 0) and (zombie["health"] > 0):
            fate = random.choice(["success", "failure"])
            weapons = getattr(self, "inventory").get("weapons").keys()
            print('---------------------------')
            print("Here are your available weapons and aid: ", list(weapons))
            print("Current health: YOU =", self.health, "ZOMBIE =", zombie["health"])
            if current_player == "hero":
                if len(list(weapons)) == 0:
                    print("Looks like you didn't pick up any weapons. The zombie bested you!")
                    print("Game Over.")
                    exit()
                else:
                    move = input("Options: USE [weapon], RUN ").strip().title().split(" ", 1)
                    if move[0] == "Use" and move[1] in weapons:
                        print("\nYour move: ", end="")
                        player_fate = self.useItem(move[1], "weapons")
                        if player_fate == "success":
                            zombie["health"] -= random.randrange(6, 16)
                    elif move[0] == "Run" and fate == "success":
                        print("You managed to run away from the zombie...for now.")
                        break
                    elif move[0] == "Run" and fate == "failure":
                        print("You tried to run, but the zombie got hold of your shirt!")
                        self.health -= random.randrange(1, 6)
                    else:
                        print("Invalid option!! Your mistake may cost you... Zombie's turn!")
                current_player = "zombie"
            elif current_player == "zombie":
                print("\nZombie's Move: ", zombie[fate])
                if fate == "success":
                    self.health -= random.randrange(1, 6)
                current_player = "hero"

        if self.health <= 0:
            print("The zombie has defeated you!")
            print("Game Over")
            exit()
        else:
            zombie["health"] = 30
            print("Zombie seems dead. You've made it out alive this time...")