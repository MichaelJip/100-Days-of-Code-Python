################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope # #

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# Error yang bawah
# print(potion_strength)

# # Global Scope # #
# player_health = str(100)

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()
# print("Player Helath is: " + player_health)

# def game():
#     def drink_potion():
#      potion_strength = 2
#      print(player_health)

#     drink_potion()

# print(player_health)

# # There is no block scope # #

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Spider"]

# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Spider"]
#     if game_level < 5:
#      new_enemy = enemies[0]

#     print(new_enemy)

# create_enemy()


# Modify global scope

# enemies = 1

# def increase_enemies():
# #   global enemies
# #   enemies += 1
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global Constants

# PI = 3.14159
# URL = "https:/www.google.com"



# Final Project

import random
import art 

easy_guess = 10
hard_guess = 5

def number_guess(guess, number, turns):
    if number > guess:
     print("Too low")
     return turns - 1
    elif number < guess:
     print("Too High")
     return turns - 1
    elif number == guess:
     print(f"You are Correct, The answer was {number}")

def diffculty_game():
    player = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if player == 'easy':
        return easy_guess
    else:
        return hard_guess


def game():
    print(art.logos)
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,100)
    # print(f"Correct answer here {number}")

    turns = diffculty_game()

    guess = 0
    while guess != number:
        print(f"You have {turns} attemps remaining to guess the number.")
        guess = int(input("Make a Guess: "))

        turns = number_guess(guess,number,turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")

game()
    



