# # Define cinema locations and showtimes
# cinema_locations = {
#     "Cinema1": "Nairobi",
#     "Cinema2": "Mombasa",
#     "Cinema3": "Kisumu",
#     "Cinema4": "Nakuru",
#     "Cinema5": "Eldoret",
#     "Cinema6": "Thika",
# }

# showtimes = {
#     "0900": "Morning Show",
#     "1400": "Afternoon Show",
#     "1900": "Evening Show",
# }

# # Define seat availability for each cinema location
# cinema_seats = {
#     "Cinema1": {
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "X"],
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "C": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "D": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "E": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "F": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "G": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "H": ["X", "X", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "I": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "J": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "K": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "L": ["O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"]
#     },
#     "Cinema2": {
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "X"],
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "C": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "D": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "E": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "F": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "G": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "H": ["X", "X", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "I": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "J": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "K": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "L": ["O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"]
#     },
#     "Cinema3": {
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "X"],
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "C": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "D": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "E": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "F": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "G": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "H": ["X", "X", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "I": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "J": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "K": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "L": ["O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"]
#     },
#     "Cinema4": {
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "X"],
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "C": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "D": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "E": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "F": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "G": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "H": ["X", "X", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "I": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "J": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "K": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "L": ["O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"]
#     },
#     "Cinema5": {
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "X"],
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "C": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "D": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "E": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "F": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "G": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "H": ["X", "X", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "I": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "J": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "K": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "L": ["O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"]
#     },
#     "Cinema6": {
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "X"],
#         "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
#         "B": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "C": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "D": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "E": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "F": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "G": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "H": ["X", "X", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "I": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "J": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
#         "K": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
#         "L": ["O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"]
#     },
#     # Define seat availability for other cinema locations
# }

# # Define ticket prices by category
# ticket_prices = {
#     "adult": 800,
#     "senior": 550,
#     "child": 350,
# }

# def display_seating(cinema, showtime):
#     seats = cinema_seats[cinema]
#     print(f"Available Seats for {showtimes[showtime]} at {cinema}:")
#     for row, seats_available in seats.items():
#         print(f"Row {row}: {' '.join(seats_available)}")

# # Main reservation function
# def reserve_seat():
    
#     # Get user's location choice
#     print("Select a cinema location:")
#     for cinema, town in cinema_locations.items():
#         print(f"{cinema} - {town}")
    
#     cinema_choice = input("Enter the cinema number (e.g., Cinema1): ")
    
#     if cinema_choice not in cinema_locations:
#         print("Invalid cinema location. Please try again.")
#         return
    
#     # Get user's showtime choice
#     print("Select a showtime:")
#     for showtime, showtime_name in showtimes.items():
#         print(f"{showtime} - {showtime_name}")
    
#     showtime_choice = input("Enter the showtime (e.g., 0900): ")
    
#     if showtime_choice not in showtimes:
#         print("Invalid showtime. Please try again.")
#         return
    
#     # Display available seats
#     display_seating(cinema_choice, showtime_choice)

#     # Get seat selection
#     row = input("Enter the row (e.g., A, B, L): ").upper()
#     seat_number = int(input(f"Enter the seat number (1-{len(cinema_seats[cinema_choice][row])}): ")) - 1

#     if seat_number < 0 or seat_number >= len(cinema_seats[cinema_choice][row]):
#         print("Invalid seat number. Please try again.")
#         return

#     seat = cinema_seats[cinema_choice][row][seat_number]

#     # Get ticket category
#     print("Select a ticket category (adult/senior/child):")
#     category = input("Enter the category: ").lower()
#     full_name = input("Enter full name: ").title()
    
#     if category not in ticket_prices:
#         print("Invalid category. Please try again.")
#         return

#     # Calculate and display the total price
#     price = ticket_prices[category]
#     print(f"Ticket for \n{showtimes[showtime_choice]} at {cinema_choice} \nSeat: {row}{seat_number + 1} \nFull Name: {full_name} \nCategory: {category.capitalize()} \nTotal: KES {price:.2f}")

# # Start reservation
# reserve_seat()


cinema_locations = {
    'Nairobi': {
        'A': ['o', 'o', 'x', 'o', 'o'],
        'B': ['x', 'x', 'x', 'o', 'o'],
        'C': ['o', 'o', 'o', 'o', 'x'],
    },
    'Mombasa': {
        'A': ['x', 'o', 'o', 'o', 'o'],
        'B': ['x', 'x', 'x', 'o', 'o'],
        'C': ['o', 'o', 'o', 'o', 'o'],
    },
    # Add more cinema locations and rows
}

chosen_location = input("Enter your chosen location: ")
chosen_row = input("Choose a row (A, B, C, ...): ").upper()

if chosen_location in cinema_locations and chosen_row in cinema_locations[chosen_location]:
    available_seats = cinema_locations[chosen_location][chosen_row]
    print(f"Available seats for Row {chosen_row} at {chosen_location}:")
    for i, seat in enumerate(available_seats, start=1):
        if i % 5 == 0:
            print(seat)
        else:
            print(seat, end=' ')
else:
    print("Invalid location or row.")
