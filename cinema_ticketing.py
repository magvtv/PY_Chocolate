# import math
# from fractions import Fraction as Frn
import datetime
import calendar
import random

# print("Sure is lonely at the top")

"""
    This is more of something I should have done long time ago. Still on it and I am not backing out. The purpose, I really need to earn with it. It is Go Time Homie!   
    Understanding that I have to be comprehensive on the Python Intro so that I can head to the examples. I still have 13 days on this. So I am still learning. 

    Back on my boss shit.
        1. So I am thinking of making a function that can check if two numbers are a multiple of each other. Eg. 3 and 9 are multiples of each other. Checking which number is greater and setting it as the greatest value. Done. 
        2. Having a function that can check if a number is even without using multiply, divide or modulo. Checking using add and minus. Even + Even is Even. Odd plus Odd is Even.While loop? Maybe using the same logic of checking prime numbers. Though it used modulo, you can still have it that no even numbers is a prime number. 

        Check if double the number when divided can be divided equally.  

        3. Using python comprehension syntax to produce a list of numbers that the previous one is half of it. Might use map method. Using the short hand lambda notation to make this work.

        3. c) How to produce a list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

        The list adds after every sequence of consecutive even number is added to the very initial. This could be implemented recurisively. 


        4. Program that can sort numbers in a tuple from smallest to largest without using any built in function. 
"""

# 1
# def is_multiple(x, y):
#     if ((x > y) and (x % y == 0)) or ((y > x) and (y % x == 0)):
#         return True
#     else:
#         return False
# print(is_multiple(105, 21))


# 2

# 3
# def double(h):
#     num = [1]
#     for i in range(1, h + 1):
#         num.append(i * 2)
#     print(num)


# List cpmprehension syntax
# h = 9
# double = [2 * x for x in range(1, h + 1)]
# print(double)


# 3. c)

# addList = []
# for x in range(0, 100):
#     if x % 2 == 0:
#         y = x + 2
#         addList.append(y)

# print(addList)
    


# def calculator():
#     start = input("Do you want to use the calc (Yes or No)?  ").lower()
#     if start == "yes":
#         first_num = int(input("Enter first number: "))
#         second_num = int(input("Enter the second number: "))
#         op = input("Enter the sign (+, -, x, /, ): ")
#         if op == "+":
#             print(
#                 "{} + {} = {}".format(first_num, second_num, (first_num + second_num))
#             )
#         elif op == "-":
#             print(
#                 "{} - {} = {}".format(first_num, second_num, (first_num - second_num))
#             )
#         elif op == "x":
#             print(
#                 "{} x {} = {}".format(first_num, second_num, (first_num * second_num))
#             )
#         else:
#             print(
#                 "{} / {} = {}".format(first_num, second_num, (first_num / second_num))
#             )
#     else:
#         print("Goodbye mate!")


# print("Square root tool.")
# num = int(input("Enter +ve number to be square rooted: "))
# if num > 0:
#     result = math.isqrt(num)
#     print("Answer:", result)
# else:
#     num = int(input("Enter +ve number to be square rooted: "))


# print(math.gcd(1701, 3768))
# Primitive approach
# def my_gcd(x, y):
#     if y < x:
#         least = y
#     else:
#         least = x
#     for n in range(1, least + 1):
#         if (x % n == 0) and (y % n == 0):
#             # if n
#             result = n
#             print("GCD of {} and {} is {}".format(x, y, result))


# Euclidean Algorithm - though I am not confident it is flawless
# def euc_gcd(x, y):
#     if y > x:
#         least = y
#         x, least = least, least % x
#     else:
#         least = x
#         y, least = least, least % y
#     return least

# print(euc_gcd(1701, 3768))


# next_author = "George S. Clason"
# authors_review = {
#     "Eva Pompouras": 85,
#     "John Maxwell": 90,
#     "James Clear": 80,
#     "Peter Hollins": 75,
#     "Wilbur Smith": 70,
#     "Robert Kiyosaki": 100,
#     "Napoleon Hill": 97,
#     "MJ Demarco": 95,
# }

# for writer in authors_review:
#     if writer == next_author:
#         print(authors_review)
#         break;
# else:
#     print("No entry of", next_author, "found!")

"""
    I am trying to think of a way to display the numbers from 1 to 100 and then show the total of all the numbers in the range. Using while loop only. Then advance to even showing the number that we are on and the total as it progresses. Success bitch!


    On the bros questions.
        1. Be able to print names after a particular name. Eg. if I say "Visu" I should be able to print the names [Kwasi, Thendu, Alex, Kayanda, Alvan, Ian]. 

    This is me creating any function I want in Python. I want it to be about cars. Of late I have a liking for cars. Especially this German Machine called Audi. 
"""
# start = 0
# stop = 100
# total = 0
# while start <= stop:
#     print("On number {}. Now the total is {}".format(start, total))
#     start += 1
#     total += start

# print("Sum of numbers from 1 to 100 is", total)


# bros = [
#     "Ashfod",
#     "Timo",
#     "Voke",
#     "Kixwii",
#     "Chang",
#     "Visu",
#     "Kwasi",
#     "Thendu",
#     "Alex",
#     "Kayanda",
#     "Alvan",
#     "Ian",
# ]

# print(len(bros))
# bros.sort()
# print(bros)
# for i in bros:
#     if i != "Visu" and i > len(5):
#         print(i)


# def cars():
#     """Talks more about cars. Exotic cars"""
#     audi_cars = ["Deccenium", "PB18 E-Tron", 'R8 Series']

#     ferrari_cars = [
#         "Roma",
#         "SF90 Stradale",
#         "F8 Tributo"
#     ]

#     lamborghini_cars = ["Urus Graphite Capsule", "Aventador Ultimae"]

#     bugatti_cars = ["Chiron Noire"]
#     print("A car for my birthday gift is a ", bugatti_cars())


# cars()


# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x - 1)


# x = fact(3)
# print(x)

# num_list = range(100)
# for i in num_list:
#     new_list = list(filter(lambda x: (x % 2 == 0), num_list))

# print(new_list)


"""
    This is me playing around with lists. I am going to make a list of programming languages that I am a pro in. Adding a nested list of places I want to travel in Kenya. Instead of using extend method can I just add it manually using the + operator? You can surprisingly. 
"""

# travelEurope = [
#     "Italy",
#     "France",
#     "Greece",
#     "Spain",
#     "Norway",
# ]

# print(len(travelEurope))
# gamingLaptops = [
#     "Razor Blade 15",
#     "Alienware M15 R3",
#     "HP Victus 16",
#     "Lenovo Legion 5i Gen 6",
# ]

# for x in gamingLaptops:
#     print("I pray to get a " + x)

# travelAfrica = [
#     "Mauritius",
#     "Egypt",
#     "Ethiopia",
#     "Zambia",
#     "South Africa"
# ]


"""
    Learning about Python tuples. 
"""
# thisTuple = ()
# thisTuple = (
#     "Laundry",
#     "Sleep",
#     "Do Maths",
#     "Zido",
#     "Wash Hair Day",
#     "Prepare clothes",
#     "Rinse the clothes",
#     [23, 2424, 1230],
# )

# thisTuple[7][0] = 400
# print(thisTuple)

"""
    This is me learning more about Python numbers.
    So I am playing with the random module in Python. Basically, what I am doing is, I am creating a guessing number game. From novice to advance. I want to see how it goes.
    Novice: Able to guess within a short range of numbers.
    Intermidiate: Given lives and after finishing their lives, the number is revealed.
    Advance: Able to tell the guesser that they are close to the number.
"""


# x = random.randrange(1, 10)
# guessNumber = int(input("Thinking of a number from 1 to 10. Guess it: "))

# if guessNumber == x:
#     print("Yay!" + guessNumber)
# else:
#     while guessNumber != x:
#         guessNumber = int(input("Try again: "))


"""
    Learning about Python files. Opening a file one must first declare a variable for the opening function. There are shortcut letters to reading, writing a file and appending to the end of the file.
    Something I have not yet understood about files is doing this: clearing all the contents of a given file and then updating the file with something different.
"""

# fp = open("dummy.txt", "r", "w")

# fp.write("IDK THAT BIH  Gunna ft G Herbo\n")
# fp.read()
# fp.close()


"""
    Learning about Exceptional Handling. Catching an exception using try. 

    Starting with a basic program that can output their age from the year they were born. First use basic arithmetic, then use datetime.
    Try using a function that can ask for someones date of birth and output their age (advanced). 
    Ask for the input as dd/mm/yyyy format. Modify the input into a date object so that it is easier to get the date of birth of the user. 10/12/2001 and 2001/12/10
    Fetching the year from the birthdate.
    Output the day they were born and their age. Focusing on the day first, the rest later. Display the day and how old the person is.
    Use comparison of current year and birth year to know whether they have added a year or not. This will need the use of the date and month. If they have not reached their birthdate of birthmonth this year return (year - birthyr) if they have return the above + 1. 
"""
# def triple(num):
#     if not isinstance(num, (int, float)):
#         raise TypeError('Only a number!')
#     else:
#         return num * 3

# print(triple(2/4))


# def divide(a, b):
#     if (a and b) != 0:
#         return a / b

#     elif ((a > b) and a == 0) or ((b > a) and b == 0):
#         return 0
#     else:
#         try:
#             return a / b
#         except ZeroDivisionError:
#             return "You cannot divide {} with 0".format(a)

# print(divide(5734, 10))


# def birthyr():
#     yr = int(input("Which year were you born? "))
#     if yr > 2020:
#         print("You are not from the future!")
#     else:
#         age = 2021 - yr
#         guess = input("Are you " + str(age) + " years old? (Yes/No) ").lower()

#         if guess == "no":
#             print("Then you are " + str(age + 1) + " years old")
#         else:
#             print("I knew it!!!")

# birthyr()


# def formatBirthday(bday):
#     dd, mm, yyyy = bday.split("/")
#     return dd, mm, yyyy


# def fetchBirthDay(bday):
#     dd, mm, yyyy = formatBirthday(bday)
#     bDate = datetime.datetime(int(dd), int(mm), int(yyyy))
#     # month = calendar.month_name[bDate]
#     day = bDate.weekday()
#     return calendar.day_name[day]


# def fetchBirthyear(bday):
#     dd, mm, yyyy = formatBirthday(bday)
#     bDate = datetime.datetime(int(dd), int(mm), int(yyyy))
#     yrstring = ""
#     year = bDate[5:]
#     year = yrstring.join(year)
#     return yrstring


# dd = input("Enter date of the month you were born (dd): ")
# mm = input("Enter the month you were born (mm): ")
# yyyy = input("Enter the year your were born (yyyy): ")

# print(fetchBirthDay("10/1/2002"))


# x = int(input("Enter number: "))
# reverse_number = 0
# while (x > 0):
#     ones = x % 10
#     reverse_number = (10*reverse_number) + ones
#     x = x // 10

# print(f"Reversed ticket number is \"{reverse_number}\"")



# def swap_case(s):
#     answer = []
#     for letter in s:
#         if (letter == letter.upper()):
#             answer.append(letter.lower())
#         elif (letter == letter.lower()):
#             answer.append(letter.upper())
#         else:
#             answer.append(letter)
#     return "".join(answer)

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

# f = input()

# if (f.isdigit()):
#     if (int(f) % 2 == 0):
        
#         print(f"{f} is even")
#     else:
#         print(f"{f} is odd")
# else:
#     print("Input incorrect!")


"""
    Object Oriented Programming in Python.
    A challenge in inheritance, encapsulation, abstraction and polymorphism
"""

import random
import string

#Base class for MovieGoer
class MovieGoer:
    def __init__(self, name, email, number_of_seats, film, show_time, snacks):
        self.id = self.generate_unique_id()
        self.name = name
        self.email = email
        self.number_of_seats = number_of_seats
        self.film = film
        self.show_time = show_time
        self.snacks = snacks
    def generate_unique_id(self):
        characters = string.ascii_uppercase + string.digits
        return "".join(random.choices(characters, k = 10))
    
#Subclass for booking tickets. Instead of concession stand = snack bar
class TicketBooking(MovieGoer):
    def __init__(self, name, email, number_of_seats, film, show_time, snacks, served_by, theatre_job_id):
        super().__init__(name, email, number_of_seats, film, show_time, snacks)
        self.served_by = served_by
        self.theatre_job_id = theatre_job_id
        
    def calculate_total_cost(self, snack_bar):
        snack_cost = sum(snack_bar.fetch_snack_price(snack) for snack in self.snacks)
        ticket_cost = self.number_of_seats * 800        #Assuming KES 800 per seat
        return ticket_cost + snack_cost
    
    
#Subclass for the snack bar
class SnackBar:
    def __init__(self):
        self.menu = {
            "Pringles M": 100,
            "Pringled XL": 250,
            "Urban Bites XL": 300,
            "500ml Sprite": 120,
            "500ml Fanta Passion": 120,
            "Cadbury Lunch Bar": 200,
            "Popcorns": 80,
            "Parle G Biscuits": 120,
            "Skittles": 150
        }
    def fetch_snack_price(self, snack):
        return self.menu.get(snack, 0)

#Abstraction and polymorphism - all details in a generic fashion. sort of like a receipt
def PrintDetails(binger):
    print(f"ID: {binger.id}")
    print(f"Name: {binger.name}")
    print(f"Email: {binger.email}")
    print(f"Film: {binger.film}")
    print(f"Show Time: {binger.show_time}")
    print(f"Seats: {binger.number_of_seats}")
    print(f"Snacks: {', '.join(binger.snacks)}")
    print(f"Served By: {binger.served_by}   {binger.theatre_job_id}")
    

#My usage example
if __name__ == "__main__":
    snackbar = SnackBar()
    binger1 = TicketBooking(
        "James Njenga",
        "njengajames@yahoo.com",
        3,
        "Grand Turismo",
        "1530h, 1730h",
        ["Pringles XL", "Pringles XL", "Pringles XL", "500ml Fanta Passion", "500ml Fanta Passion"],
        "Florence Wanja",
        "KMC293"
    )
    total_cost1 = binger1.calculate_total_cost(snackbar)
    print("Receipt Confirmed: ")
    PrintDetails(binger1)
    print(f"Amount: KES {total_cost1}\n")
    
    




