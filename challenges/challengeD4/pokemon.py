#!/usr/bin/env python3

# imports always go at the top of your code
import requests


def main():

    while True:
        # challenge 1 = add input to ask for a pokemon to look up!
        pokemon = input("What Pokemon would you like to search for? ")
        pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()

        # challenge #2 print the url to the front-default image
        poke_pic = pokeapi["sprites"]["front_default"]
        print(f"Here's what your pokemon looks like: {poke_pic}")

        # challenge 3: Return a count of how many "game_indices" the selected Pokemon has been in
        poke_games = len(pokeapi["game_indices"])
        print(f"Here's how many games {pokemon} has been in: {poke_games}")

        # challenge 4: Print out the "name"s of ALL the selected Pokemon's "moves"
        print(f"Here's all of {pokemon}'s moves!:")
        poke_moves = pokeapi["moves"]
        for move in poke_moves:
            print("Name: ", move["move"]["name"])


main()
