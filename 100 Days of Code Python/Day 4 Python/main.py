import random
import sys
# random_int = random.randint(1,10)
# print(random_int)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}")

# Tugas 1
# random_flips = random.randint(0,1)

# if(random_flips == 0):
#     print("Tails")
# else:
#     print("Heads")

# state = ["Indonesia","Bali","Jakarta","Medan"]

# state.extend(["Bandung", "Kalimantan"])

# print(state)

# Tugas 2
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# x = len(names)
# random_number = random.randint(0, x)
# person_pay = names[random_number]
# print(person_pay + " is going to pay the meals...")

# state = ["Indonesia","Bali","Jakarta","Medan"]

# num_state = len(state)

# print(state[num_state - 1])

# fruits = ["Straberry", "Apple", "Orange", "Manggo"]
# veges = ["Potatos", "Tomato", "Kale", "Spinach"]

# dirty_dozen = [fruits, veges]

# print(dirty_dozen[1][1])

# Tugas 3
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])

# selected_row = map[vertical -1]
# selected_row[horizontal - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")

# Tugas Final

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps =[rock, paper, scissors]
rps_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if rps_choose >= 3 or rps_choose < 0:
    print("Invalid Input, Instant Lose!!")
    sys.exit()
else:
    print(rps[rps_choose])

computer = random.randint(0,2)
print("Computer choose:")
print(rps[computer])

if rps_choose == 0 and computer == 2:
    print("You Win!")
elif computer == 0 and rps_choose == 2:
    print("You Lose!")
elif rps_choose > computer:
    print("You Win!")
elif computer > rps_choose:
    print("You Lose!")
elif rps_choose == computer:
    print("Draw!")