#!/usr/bin/python3
import random
from rpgclasses import Player
from game import Game

"""THIS IS KATHY'S ZOMBIE RPG GAME"""


# dict of possible weapons
items = {
    "Knife": {
        "desc": "This is a rusty knife. Still looks sharp though.",
        "success": "You've lunged at the zombie with your knife! Direct hit to the brain.",
        "failure": "You slipped! You missed the zombie by a hair!",
        "type": "weapons"
    },
    "Gun": {
        "desc": "A good ol' Smith & Wesson. It has ",
        "success": "You've fired a shot! It miraculously hits the heart.",
        "failure": "You've fired a shot and MISSED! Hope the sound doesn't attract all of the zombies",
        "bullets": 6,
        "type": "weapons"
    },
    "Key": {
        "desc": "A key. Maybe it'll open one of these doors?",
        "success": "You try the lock and it worked!",
        "failure": "Door's still locked. Gotta try a different door.",
        "type": "aid"
    },
    "Sandwich": {
        "desc": "It's tuna. Seems edible.",
        "success": "You ate it. Stomach seems ok.",
        "failure": "YIKES! The food had zombie blood. You turned into a zombie.",
        "type": "aid"
    }
}

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'desc': "Just a regular hallway.",
        'paths': {
            'South': 'Kitchen',
            'East': 'Dining Room',
        },
        'item': 'Key'
    },

    'Kitchen': {
        'desc': "Dishes are piled in the sink. Seems like rats have taken over.",
        'paths': {
            'North': 'Hall'
        },
        'item': 'Sandwich',
    },
    'Dining Room': {
        'desc': "The windows are boarded up. I wonder where the people went.",
        'paths': {
            'West': 'Hall',
            'South': 'Garden',
            'North': 'Pantry'
        },
        'item': 'Gun',
    },
    'Garden': {
        'desc': "It's dark out there. No flowers are left.",
        'locked': True,
        'paths': {
            'North': 'Dining Room'
        }
    },
    'Pantry': {
        'desc': "Everything's moldy. Yuck.",
        'paths': {
            'South': 'Dining Room'
        },
        'item': 'Knife',
    }
}

# create a zombie
zombie = {
    "health": 30,
    "success": "The zombie bit you!",
    "failure": "The zombie aimed for you and missed!"
}

hero = Player(inventory={"weapons": {}, "aid": {}})

zombies = Game(items={**items}, rooms={**rooms})

zombies.startGame(hero, zombie)


