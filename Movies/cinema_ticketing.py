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
        ticket_cost = self.number_of_seats * 850        #Assuming KES 850 per seat
        return ticket_cost + snack_cost
    
    
#Subclass for the snack bar
class SnackBar:
    def __init__(self):
        self.menu = {
            'Pringles M': 100,
            'Pringled XL': 250,
            'Urban Bites XL': 300,
            '500ml Sprite': 120,
            '500ml Fanta Passion': 120,
            'Cadbury Lunch Bar': 200,
            'Popcorns': 80,
            'Parle G Biscuits': 120,
            'Skittles': 150
        }
    def fetch_snack_price(self, snack):
        return self.menu.get(snack, 0)

#Abstraction and polymorphism - all details in a generic fashion. sort of like a receipt
def PrintDetails(binger):
    print(f"Payment ID: {binger.id}")
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
        "Margaret Onyancha",
        "maggieonyancha99@gmail.com",
        2,
        "Barbie",
        "2000h-2200h",
        ["Pringles XL", "500ml Fanta Passion", "500ml Fanta Passion"],
        "Nick Karanja",
        "KMC344"
    )
    total_cost1 = binger1.calculate_total_cost(snackbar)
    print("Film Ticket Confirmed: ")
    PrintDetails(binger1)
    print(f"Amount: KES {total_cost1}\n")
    
    




