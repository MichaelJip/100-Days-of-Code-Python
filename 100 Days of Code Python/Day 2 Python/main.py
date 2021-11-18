# Data Types

#String "Hello World"

#print("Hello"[0])

#Integer
#print(10+20)

#Float
#3.14159

#Boolean
#True
#False

# num_char = len(input("Whats is your name? "))
# new_num_char = str(num_char)
# print("your name has " + new_num_char + " Characters")

# type untuk mengetahui tipenya int,char,string,dll

# print(type(num_char))

#print(70 + float("100.5"))
#output 170.5

#Tugas 1
# number = input("two digits number: ")
# result_one = int(number[0])
# result_two = int(number[1])
# result = result_one + result_two
# print(result)

# print(3 + 5)
# print(7 - 4)
# print(3 * 2)
# print(6 / 3)
# 2**3 artinya 2*2*2 atau bisa dibilang 2^3

# Pemdas LR(Left n Right)
# ()
# **
# * /
# + -

# print(3 + 3 * 3 / 3 - 3)

#Tugas 2
# weight = input("Input your weight: ")
# height = input("Input your height: ")

# weight_int = int(weight)
# height_float = float(height)

# bmi = weight_int / height_float ** 2

# bmi_int = int(bmi)
# print(bmi_int)

# print(round(8 / 3))
# print(round(8 / 3, 2))
# print(8 // 3)

# score = 0
# height = 1.8
# isWinning = True
# # f-String
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# Tugas 3
# print((56 - 90 )* 365)

# age = input("Input your age: ")
# old_age = 90 - int(age)

# days = int(365 * old_age)
# weeks = int(52 * old_age)
# months = int(12 * old_age)

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

#Tugas 4
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)

# print(f"Eachh person should pay: ${final_amount}")