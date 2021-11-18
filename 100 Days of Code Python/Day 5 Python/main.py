
# fruits = ["apple", "Peach", "Pear"]

# for i in fruits:
#     print(i)

# Tugas 1
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# # height = sum(student_heights)
# total_height = 0
# for height in student_heights:
#     total_height += height


# # student = len(student_heights)
# num_student = 0
# for student in student_heights:
#     num_student += 1

# avg_height = round(total_height / num_student)

# print(avg_height)

# Tugas 2
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])


# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score

# print(f"You Highest Score is {highest_score}")

# For Loop Range
# for n in range(1,11, 3):
#     print(n)

# Tugas 3
# total = 0
# for number in range(2,101,2):
#     total += number
# print(total)

# even = 0
# for number in range(1,101):
#     if number % 2 == 0:
#         even += number
#         print(even)

# Tugas 4

# for n in range(1,101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)

# Tugas Final 
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = []

# for char in range(1,nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1,nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1,nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)
# random.shuffle(password)
# print(password)

# password_list = ""

# for char in password:
#     password_list += char

# print(f"Your password is {password_list}")