
# Function with output

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
   
#     return(f"{formated_f_name} {formated_l_name}")

# formated = format_name("angela", "KO")
# print(formated)

# Function have more return di functuin yang sama

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
   
#     return(f"{formated_f_name} {formated_l_name}")

# print(format_name(input("What is your first name "), input("What is your last name ")))

# print(format_name("michael", "jip"))

# formated = format_name("angela", "KO")
# print(formated)

# # Tugas 1
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#         # print("Leap year.")
#       else:
#         return False
#         # print("Not leap year.")
#     else:
#       return True
#     #   print("Leap year.")
#   else:
#     return False
#     # print("Not leap year.")

# def days_in_month(year, month):
#   if month > 12 or month < 1:
#       return "Invalid match"
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(year) and month == 2:
#       return 29
#   return month_days[month - 1]

  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# DocStrings

# def format_name(f_name, l_name):
#     # DocStrings
#     """" Take a first and last name and format it
#     to return the title case version of the name. """
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
   
#     return(f"{formated_f_name} {formated_l_name}")

# format_name()

#  QUiz 1
# def add(n1,n2):
#     return n1 + n2

# def substract(n1,n2):
#     return n1 - n2

# def multiply(n1,n2):
#     return n1 * n2

# def divide(n1,n2):
#     return n1 / n2

# print(add(2, multiply(5, divide(8,4))))

# Tugas Final

import art
import os

def clear():
    os.system('cls')


def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(art.logo)

    first_num = float(input("What's is your first number: "))

    for symbol in operation:
        print(symbol)
    calculator_stop = True


    while calculator_stop:
        operation_symbol = input("Pick an operation above: ")
        second_num = float(input("What's is your second number: "))
        calculatoor_function = operation[operation_symbol]
        answer = calculatoor_function(first_num,second_num)

        print(f"{first_num} {operation_symbol} {second_num} : {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation : ") == 'y':
            first_num = answer
        else:
            calculator_stop = False
            calculator()

calculator()

