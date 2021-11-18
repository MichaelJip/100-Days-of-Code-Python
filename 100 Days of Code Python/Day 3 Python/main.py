# water_level = int(input("Water level: "))
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollecoaster!")
# else:
#     print("Go home you to short")

# Tugas 1
# number = int(input("put a number here: "))
# if number % 2:
#     print("This is an odd number")
# else:
#     print("This is an even number")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollecoaster!")
#     age = int(input("What is your age"))
#     if age < 12:
#         print("Pay $5")
#     elif age <= 18:
#         print("Pay $7")
#     else:
#         print("Pay $12")
# else:
#     print("Go home you to short")

# Tugas 2
# height = float(input("input your height in m: "))
# weight = float(input("input your weight in kg: "))

# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")  

# Tugas 3
# year = int(input("Input Years here: "))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollecoaster!")
#     age = int(input("What is your age"))
#     if age < 12:
#         bill = 5
#         print("child Pay $5")
#     elif age <= 18:
#         bill = 7
#         print("teen Pay $7")
#     else:
#         bill = 12
#         print("adult Pay $12")

#     photo = input("Do you want a photo taken? Y or N.")
#     if photo == "Y":
#         bill += 3
#     print(f"your final bill is ${bill}")

# else:
#     print("Go home you to short")

#Tugas 4

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0

# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
    
# if extra_cheese == "Y":
#   bill += 1
  
# print(f"Your final bill is: ${bill}.")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollecoaster!")
#     age = int(input("What is your age"))
#     if age < 12:
#         bill = 5
#         print("child Pay $5")
#     elif age <= 18:
#         bill = 7
#         print("teen Pay $7")
#     elif age >45 and age <= 55:
#         print("Have a free ride")
#     else:
#         bill = 12
#         print("adult Pay $12")

#     photo = input("Do you want a photo taken? Y or N.")
#     if photo == "Y":
#         bill += 3
#     print(f"your final bill is ${bill}")

# else:
#     print("Go home you to short")

# Tugas 5
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))

# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")

# Tugas Final
# print("Welcome to treasure island")
# treasure = input('Your mission is to find the treasure which way you want to go "left" or "right": ')
# if treasure == "left":
#     lake = input('you find a lake would you like to "swim" or "wait": ')
#     if lake == "wait":
#         door = input('You find a door which door will you choose? "red", "blue", or "yellow": ')
#         if door == "yellow":
#             print("You Win!")
#         else: 
#             print("Game Over!")
#     else:
#         print("Game Over!")
# else:
#     print("Game Over!")