theater_location = {
    '001': 'mombasa',
    '002': 'nanyuki',
    '003': 'nairobi',
    '004': 'eldoret',
    '005': 'kisumu',
    '006': 'thika',
}

showtimes = {
    "0900h-1100h": "Early Bird",
    "1115h-1315h": "Regular Viewer",
    "1330h-1530h": "Matinee Goers",
    "1545h-1745h": "Twilight Watchers",
    "1800h-2000h": "Red Carpeters",
    "2015h-2215h": "Night Owls"
}

ticket_prices = {
    "Adults": 800,
    "Seniors": 550,
    "Child": 350,
}

theater_seats = {
    "Cinema1": {
        "A": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"],
        "B": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
        "C": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
        "D": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
        "E": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
        "F": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
        "G": ["X", "X", "O", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
        "H": ["X", "X", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
        "I": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
        "J": ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X"],
        "K": ["X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X"],
        "L": ["O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X"]
    }
}


def display_seats(cinema, showtime):
    seats = theater_seats[cinema]
    print(f"Available seats for {showtimes[showtime]} at {cinema}")
    for row, seats_available in seats.items():
        print(f"Row: {row}: {''.join(seats_available)}")
# def reserve_seat():
# print(theater_seats)