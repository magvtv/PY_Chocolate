# import datetime
# import random
# import calendar



# islands = [
#     'Kauai',
#     'Majorca',
#     'Ambergris Caye',
#     'Grand Cayman',
#     'Bali'
# ]

# bestNetflixSeries = (
#     "Kaleidoscope",
#     "Witcher: Blood & Orgin",
#     "Sandman",
#     "Vikings: Valhalla",
#     "Top Boy",
#     "Peaky Blinders"
# )

# topPlayStationGames = {
#     1: "Fortnite",
#     2: "Gran Turismo 7",
#     3: "God of War: Ragnarok",
#     4: "Horizon: Forbidden West",
#     5: "Classic Spiderman: Myles Morales",
#     6: "Ratchet & Clank: Rift Apart"
# }

# print(len(topPlayStationGames))



# npc = dict(
#     id ="Jade Blum",
#     age = 22,
#     location = "Night City",
#     stableVersion ="Moore Tech Berzerk 1.9",
#     upgradeTo = ["Dylanar Sandevistan", "Zetatech Sandevistan"],
#     cyberDeck=("Raven Microcyber", "Tetratronic"),
# )

# # npc.update({"location": "Netherlands"})
# del npc["cyberDeck"]
# for x in npc.items():
#     print(x)

# del npc["country"]
# x = npc["stableVersion"]
# x = "Arasaka"
# print(x)
# if "cyberware" in npc:
#     print(npc["cyberware"])

# x = npc.items()
# print(x)
# print(npc["country"])
# print(aboutMe.keys())

# cyberware = {
#     "skeleton": ["bionic joints", "dense marrow", "titanium-x"],
#     "nervous": ["nanorelays", "reflex tuner", "kerenzikov", "synaptic accelerator"],
#     "limbs": {
#         "arms": ["projectile launch", "monowire"],
#         "hands": ["ballistic compressor", "smart link"],
#         "legs": "lynx paws",
#     },
#     "eyes": {
#         "ocular": "kiroshi optics",
#         "frontal cortex": ["ex-disk", "heal-on-kill", "self-ice"],
#     },
#     "heart": ["tyrosine injector", "syn-lungs", "biomonitor"],
#     "immunity": ["detoxifier", "shock-n-awe"],
#     "integumentary": (
#         "fireproof coating",
#         "ground plating",
#         "optical camo",
#         "supra-dermal",
#     ),
# }



# gaming_consoles = ({
#     "Microsoft: Xbox Series X",
#     "Sony: PlayStation 5",
#     "Nintendo: Switch",
#     "Microsoft: Series G"
# })

# print(bestNetflixSeries)
# a, b, c, d, e = islands

# def island_tracker():
#     c = "Santorini"
#     print(f"{a} is found in Hawaii")


# x = random.randrange(1, 7)
# print(f"My dice rolls to {x}")
# print(f"Meaning i will play \"{topPlayStationGames[x]}\" on my PS5")


# quotesByWilde = [
#     "some cause happiness wherever they go; others whenever they go",
#     "ambition is the last refuge of failure",
#     "loving oneself: the beginning of lifelong romance",
#     "to expect the unexpected shows a thoroughly modern intellect",
#     "experience is the name we give our mistakes"
# ]


# heraticulus_quotes = (
#     "Change is constant",
#     "Big results need big ambitions",
#     "You cannot encounter prosperity without danger"
# )
# quoteOfTheDay = "{}"

# for x in heraticulus_quotes:
#     print(quoteOfTheDay.format(x))

# favLaptop = "Asus Vivobook Pro"
# favPhone = "Xiaomi Redmi Note 10s"
# favEarbuds = "JBL Live Pro"

# order = 'Laptop: {} \nSmartphone: {} \nEarbuds: {}'
# print(order.format(favLaptop, favPhone, favEarbuds))


# class fastfood ():
#     def outlets():
#         companies = ({
#             "burgers": (
#                 "McDonald's",
#                 "Wendy's",
#                 "Burger King",
#                 "Five Guys"
#             ),
#             "global": (
#                 "Taco Bell",
#                 "Chipotle",
#                 "Moe's",
#                 "Qdoba"
#             ),
#             "pizza": (
#                 "Papa Murphy's",
#                 "Pizza Hut",
#                 "Little Caesars",
#                 "Marco's Pizza"
#             ),
#             "chicken": (
#                 "Chick-Fil-A",
#                 "KFC",

#             ),
#             "sandwich": (
#                 "Arby's",
#                 "Panamera Bread",
#                 "Jersey Mike's",
#                 "Firehouse Subs"
#             ),
#         })

#         return companies


# coursemates = ((
#     "Nathaniel",
#     "PH",
#     "James",
#     "Vincent",
# ))


# youtubers = [
#     "Till Musshoff",
#     "Dre Drexler",
#     "Pewdiepie",
#     "JJ Olatunji",
#     "Sidemen",
#     "Mr Beast",
#     "Uncle Rogers"
# ]

# youtubers[2:5] = ["lokelani", "cocomelon"]
# youtubers.insert(2, "cocomelon")
# youtubers.append("fireship")
# print(youtubers)
# print(type(coursemates))
# print(mpl.__version__)


# def favMeal(food):
#     for x in food:
#         print(x)
#     pass

# mine = list(("Ugali Sukuma Avocado", "Nyamachoma", "Chapati Beans"))
# favMeal(mine)

# homie = lambda forty: forty * 4
# print(homie(5))


# if __name__ == '__main__':
    # n = int(input("Enter Number: ").strip())
    # if (n % 2 == 0) and (n in range(2, 5)):
    #     print("Not Weird")
    # elif (n % 2 == 0) and (n in range(6, 20)):
    #     print("Weird")
    # elif n % 2 == 1:
    #     print("Weird")
    # elif (n % 2 == 0) and (n > 20):
    #     print("Not Weird")
        
# 
# x = range(6, 20, 1)
# print(x)

# class Nomad:
#     def __init__(self, fullName, nationality, industry, places):
#         self.fullName = fullName
#         self.nationality = nationality
#         self.industry = industry
#         self.places = places
        
#     def outline(self):
#         return (
#             f"Names: {self.fullName} \nNationality: {self.nationality} \nIndustry: {self.industry} \nPlaces: {self.places}"
#         )

# person1 = Nomad("PH Magutu", "North American", "Software Development", list(("Kauai", "Austria", "Denmark")))
# person1.places = list(("Kauai, Switzerland, Austria, Spain"))
# del person1
# w = person1.outline()
# print(w)

# class Ammunition:
#     def __init__(self, type, model, country):
#         self.type = type
#         self.model = model
#         self.country = country
#     def showAmmo(self):
#         return (f"Type: {self.type} \nModel: {self.model} \nCountry: {self.country}")
    
# class Knives(Ammunition):
    # pass

# knife1 = Knives("Bowie", None, "United States")
# ammo1 = Ammunition("Assault Rifle", "AMD 65")
# ammo2 = Ammunition("Pistol", "Beretta M9")
# print(knife1.showAmmo())



"""
    Thinking of a manner of implementing inheritance into my small codepiece
"""
# class School:
#     def __init__(self, fullName):
#         self.fullName = fullName

# class Student:
#     def __init__(self, fullName, grade, isBoy):
#         self.fullName = fullName
#         self.grade = grade
#         self.isBoy = isBoy

#     def __str__(self):
#         if (self.isBoy == False):
#             return f"Name: {self.fullName} \nGrade: {self.grade} \nGender: Girl"
#         else:
#             return f"Name: {self.fullName} \nGrade: {self.grade} \nGender: Boy"
    
# class Staff:
#     def __init__(self, fullName, subject, isMan):
#         self.fullName = fullName
#         self.subject = subject
#         self.isMan = isMan
    
#     def __str__(self):
#         if (self.isMan == False):
#             return f"Name: Teacher {self.fullName} \nSubject: {self.subject} \nGender: Lady"
#         else:
#             return f"Name: {self.fullName} \nSubject: {self.subject} \nGender: Gent"
        

# student1 = Student("Emmanuel Apama", 6, True)
# student2 = Student("Ashley Neema", 7, False)
# print(student1)

# teacher1 = Staff("Edwin", "Mathematics, Science", True)
# print(teacher1)


# import numpy as np
# import random as rd

# a = np.rd.rand(6,1) * np.arange(2)
# print(a)

"""
PHASE 2
    Creating a way to read data from csv using python. Accomplished. 
    Store the films in an array
    Select random 3 and say they are premiering in Two Rivers Century Cinemax
"""

"""
import csv
import random

with open("/home/pharoh/Desktop/LEARN/PY/SCICOMP/Data/films.csv", "r") as film:
    csvreader = csv.reader(film)
    for row in csvreader:
        print(row[1])


"""


"""

"""
# tickets = float(input("Enter number of tickets to purchase: "))  
# serialCode = "R81DSD23YW"
# filmTitle = "Creed III"
# currency_rate = 128.97
# USDTicketPrice = 8.35
# KESTicketPrice = int(USDTicketPrice * currency_rate)


# def ticketPriceConverter(currency, price):
#     if currency == "DTK" or currency == "dtk":
#         finalKESPrice = int(price)
#         return f"Ticket Price: KES {((finalKESPrice)):,d}"
#     if currency == "ktd" or currency == "DTK":
#         finalUSDPrice = int(price)
#         return f"Ticket Price: ${((finalUSDPrice)):,d}"

# def totalConverter(currency, price):
#     if currency == "dtk" or currency == "DTK":
#         totalKES = int(price * currency_rate)
#         return f"Total: KES {((totalKES)):,}"
    
#     if currency == "ktd" or currency == "KTD":
#         totalUSD = int(price / currency_rate)
#         return f"Total: ${((totalUSD)):,}"
    

# def receipt():
#     totalPrice = USDTicketPrice * tickets
#     x = ticketPriceConverter("ktd", KESTicketPrice)
#     y = totalConverter("dtk", totalPrice)
#     print(f"Serial Code: {serialCode} \nFilm: {filmTitle} \nTickets: {int(tickets):,d}")
#     print(x)
#     print(y)

# receipt()

"""
    Debugging this issue: 
    Converting the receipt to dollars, change the totalPrice currency to KES and the ticketPrice to USD and the conversion method to KTD in totalConverter only
    Conversion to kenyan shillings, change the totalPrice currency to USD and then the ticketPrice to KES and the conversion method to DTK in totalConverter only
"""





# # QUESTION 3
# def find_rarest_age(student_data):
#     # Create a dictionary to store the counts of each age
#     age_count = {}

#     # Iterate through the student data dictionary and count the occurrences of each age
#     for (name, age) in student_data.items():
#         if age in age_count:
#             age_count[age] += 1
#         else:
#             age_count[age] = 1

#     # Find the least occurring age
#     rarest_age = min(age_count, key=age_count.get)

#     # Print the student names alongside their ages
#     for name, age in student_data.items():
#         print(f"{name}: {age} years old")

#     # Return the least occurring age
#     return rarest_age

# student_data = {"Angela": 20, "Benard": 24, "Catherine": 21, "Damian": 30, "Elaine": 20, "Felix": 24, "Gabriella": 21}

# x = find_rarest_age(student_data)
# print("The rarest age is:", x)



# QUESTION 4
# import math

# class Circle2d:
#     def __init__(self, x=0, y=0, radius=0):
#         self._x = x
#         self._y = y
#         self._radius = radius

#     # Getters and Setters for x, y, and radius
#     def get_x(self):
#         return self._x

#     def set_x(self, x):
#         self._x = x

#     def get_y(self):
#         return self._y

#     def set_y(self, y):
#         self._y = y

#     def get_radius(self):
#         return self._radius

#     def set_radius(self, radius):
#         self._radius = radius

#     # Method to calculate the area of the circle
#     def get_area(self):
#         return math.pi * self._radius**2

#     # Method to calculate the perimeter of the circle
#     def get_perimeter(self):
#         return 2 * math.pi * self._radius

#     # Method to check if a specified point is inside the circle
#     def contains_point(self, x, y):
#         distance = math.sqrt((self._x - x)**2 + (self._y - y)**2)
#         return distance < self._radius

# # Create a circle with center (2, 3) and radius 5
# circle = Circle2d(2, 3, 5)

# # Get the center coordinates and radius
# print("Center: ({}, {})".format(circle.get_x(), circle.get_y()))
# print("Radius: {}".format(circle.get_radius()))

# # Get the area and perimeter
# print("Area: {:.2f}".format(circle.get_area()))
# print("Perimeter: {:.2f}".format(circle.get_perimeter()))

# # Check if a point is inside the circle
# print("Contains Point (4, 4):", circle.contains_point(4, 4))
# print("Contains Point (6, 6):", circle.contains_point(6, 6))


# def most_frequent_word(file_name):
#     word_freq = {}
#     with open(file_name, 'r') as file:
#         for line in file:
#             words = line.strip().split()
#             for word in words:
#                 word = word.lower()  # Convert to lowercase for case-insensitive comparison
#                 if word in word_freq:
#                     word_freq[word] += 1
#                 else:
#                     word_freq[word] = 1
#     # Sort the dictionary by values in descending order
#     sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
#     most_frequent_word = sorted_word_freq[0][0]
#     return most_frequent_word

# # Example usage

# most_frequent = most_frequent_word(file_name)
# print("The most frequent word is:", most_frequent)


# class DigitalNomad:
#     def __init__(self, full_name, gender, nationality, age):
#         self.full_name = full_name
#         self.gender = gender
#         self.nationality = nationality
#         self.age = age
#         self.citizenships = {}
#         self.travel_history = {}
#         self.friends = {}
#         self.portfolio = {}

#     def citizenship(self, country, citizenships):
#         self.citizenships[country] = citizenships

#     def add_travel_history(self, country, cities):
#         self.travel_history[country] = cities

#     def expat(self):
#         expat_friends = {}
#         for country, cities in self.travel_history.items():
#             if country in self.citizenships:
#                 for city in cities:
#                     if city in self.friends:
#                         for friend in self.friends[city]:
#                             if friend not in expat_friends:
#                                 expat_friends[friend] = [country]
#                             else:
#                                 expat_friends[friend].append(country)
#         return expat_friends

#     def add_friend(self, city, friend):
#         if city in self.friends:
#             self.friends[city].append(friend)
#         else:
#             self.friends[city] = [friend]

#     def add_business(self, country, business_type, cities):
#         if country in self.portfolio:
#             self.portfolio[country][business_type] = cities
#         else:
#             self.portfolio[country] = {business_type: cities}

#     def portfolio(self):
#         return self.portfolio


# Create a new DigitalNomad
# dn = DigitalNomad("PH Magutu", "male", "American", 21)

# # Add citizenships
# dn.citizenship("USA", ["American"])
# dn.citizenship("Japan", ["American", "Japanese"])

# # Add travel history
# dn.add_travel_history("USA", 
#     [
#         "New York", "Los Angeles", "San Francisco", "Wiscousin", "Oregon", "Idaho", "Arizona"
#     ]
# )

# dn.add_travel_history("Japan", ["Tokyo", "Kyoto"])

# Add friends
# dn.add_friend("New York", "Alice")
# dn.add_friend("Los Angeles", "Bob")
# dn.add_friend("Tokyo", "Charlie")

# Add businesses
# dn.add_business("USA", "rental", ["New York", "Los Angeles"])
# dn.add_business("Japan", "rental", ["Tokyo", "Kyoto"])
# dn.add_business("Japan", "entertainment", ["Tokyo"])

# Get expat friends
# expat_friends = dn.expat()
# print("Expat Friends:")
# for friend, countries in expat_friends.items():
    # print(f"{friend}: {', '.join(countries)}")

# Get portfolio
# portfolio = dn.portfolio()
# print("\nPortfolio:")
# for country, businesses in portfolio.items():
#     print(f"{country}:")
#     for business, cities in businesses.items():
#         print(f"{business}: {', '.join(cities)}")



# import random
# class Car:
#     def __init__(self, make, model, color, status):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.status = status

#     def __str__(self):
#         return f"{self.color} {self.make} {self.model}"


# class Garage:
#     def __init__(self):
#         self.cars = [
#             Car("Porsche", "911", "Red", "ready to drive"),
#             Car("Koenigsegg", "CCXR", "Black", "under repair"),
#             Car("Audi", "R8", "White", "ready to drive"),
#             Car("BMW", "M5", "Blue", "ready to drive"),
#             Car("Mercedes", "AMG GT", "Silver", "ready to drive"),
#             Car("Aston Martin", "DB11", "Green", "under repair"),
#             Car("Ferrari", "812 Superfast", "Yellow", "ready to drive"),
#             Car("Lamborghini", "Huracan", "Orange", "ready to drive"),
#             Car("McLaren", "720S", "Purple", "ready to drive"),
#             Car("Bugatti", "Chiron", "Gold", "under repair")
#         ]

#     def cars(self):
#         return self.cars
    
#     def check_engine_oil(self, car):
#         print(f"Checking {car} engine oil")
#         x = random.randint(2, 7)

#         if x < 4:
#             print(f"{car} is low on fuel")
#         else:
#             print(f"Engine oil: {x} litres")
#     def replace_tyres(self, car):
#         print(f"Checking tyre pressure in {car}")
#         x = random.randint(30, 35)
#         if x < 32:
#            print(f"Tyre pressure in {car} is low")
#         else: 
#            print(f"Tyre pressure is {x} PSI")
#     def car_wash(self, car):
#         print(f"Cleaning {car}")


#     def available(self):
#         return [car for car in self.cars if car.status == "ready to drive"]
    # def repair(self, car):
    #     print(f"Reparing {car}")
    #     self.check_engine_oil(car)
    #     self.replace_tyres(car)
    #     car.status = 'ready to drive'
    #     print(f"{car} is now ready to drive")

class A:
    def __new__(self):
        print("A's__new__() invoked")
    def __init__(self):
        print("A's__init__() invoked")

class B:
    def __new__(self):
        print("B's__new__() invoked")
    def __init__(self):
        print("B's__init__() invoked")
B()
A()
# print(b)