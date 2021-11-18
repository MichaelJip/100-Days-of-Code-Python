# Dictionary & Nesting

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The Action of doing something over and over again.",
#     }

# Retrive item dari dictionary
# print(programming_dictionary["Bug"])

# Nambah item di programming_dictionary.
# programming_dictionary["Break"] = "For stop the program"
# print(programming_dictionary)

# Membuat empty dictionary
# empty_dictionary = {}

# menghapus data dalam dictionary
# programming_dictionary = {}

# edit item dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# Looping di dictionary
# for thing in programming_dictionary:
#     print(thing)
#     print(programming_dictionary[thing])

# Tugas 1
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {

# }

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     score = student_scores[key]
#     if score > 90:
#         student_grades[key] = "Outstanding"
#     elif score > 80:
#         student_grades[key] = "Exceeds expecatations"
#     elif score > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"   

# # 🚨 Don't change the code below 👇
# print(student_grades)

# # Nesting
# capital = {
#     "France" : "Paris",
#     "Germany" : "Berlin",
# }

# # Nesting List di dalam dictionary
# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
# }

# # Nesting dictionary dalam dictionary

# travel_log = {
#     "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visited" : 12},
#     "Germany" : { "cities_visited":  ["Berlin", "Hamburg", "Stuttgart"], "cities_not_visited" : ["Brooklyn"]},
# }

# # Nesting dictionary dalam list
# travel_log = {
#     {
#         "country" :"France", 
#         "cities_visited" : ["Paris", "Lille", "Dijon"], 
#         "total_visited" : 12
#     },

#     {
#         "country" :"Germany", 
#         "cities_visited":  ["Berlin", "Hamburg", "Stuttgart"], 
#         "total_visited" : 12
#     },
# }

# Tugas 2
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = country_visited
#     travel_log.append(new_country)

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# Tugas Final
import art
import os

def clear():
    os.system('cls')

print(art.logo)

bid_name = {}
bidding_finish = False

def high_bidder(bid_record):
    high_bid = 0
    winner = ""

    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid {high_bid}")

while not bidding_finish:
    name = input("What is your name: ")
    bid = int(input("How much do you want to bid : $"))
    bid_name[name] = bid
    continue_yes = input("Are there any more bidder 'yes' or 'no'")
    if continue_yes == 'no':
        bidding_finish = True 
        high_bidder(bid_name)
    elif continue_yes == 'yes':
        clear()





