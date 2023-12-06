"""
might need to broaden the snackbar items. 
realized i can have a brand and their specific items in weight, volume
starting out, will be sure to grow this module. 
kinda works like a database for all the concession stand snacks
snack > brand > item (size, weight)

"""

from textwrap import indent
import json


concession_stand = {
    # frozen chilled snacks
    "Frozen": {
        "Ice Cream": {
            "Haagen-Darz": 635,
            "Dairyland": 400,
            "Coldstone Creamery": 600,
            "London Dairy": 540,
            "Java House": 495,
            "Cream Bell": 440,
            "Lyon's Main": 345,
            "Ooh!": 200,
        },
        # frozen yogurt
        "Planet Yogurt": {
            "Cookie Dough": 345,
            "Pumpkin Pie": 380,
            "Almond Mocha": 400,
            "Toasted Coconut": 485,
            "Mango Foster": 435,
            "Pineapple Guava": 360,
            "Strawberry Banana": 350,
            "Plain Tart": 250,
            "Caramel Pudding": 520,
        },
    },
    # sandwiches
    "Sandwiches": {
        "Vegan": {},
        "Gluten-Free": {},
        "Meat": {
            "Arbys": {
                "Cheese-steak": 365,
                "Bacon Ranch": 390,
                "Crispy Chicken": 450,
                "Corned Beef Reuben": 530,
                "Greek Gyro": 610,
                "Double Beef n Cheddar": 700,
                "Smokehouse Brisket": 750,
                "French Dip n Swiss": 820,
            },
        },
    },
    # gourmets (baked, pies, cakes, muffins, cookies)
    "Gourmet": {
        "Goldbelly": {
            "Party Harer 12 Giants": 840,
            "Beef Tacos": 1115,
            "Signature Italian Beef Sandwich": 1470,
            "Dozen H&H Bagels": 835,
            "Bialyz Dozen": 800,
            "Original Piecaken": 965,
            "Cherry Crumb Pie": 1025,
            "Cecicela Breakfast Basket": 1120,
            "Huckleberry Handpies": 310,
            "Grandma Pizza": 665,
            "Sour Creme Apple Walnut Pie": 525,
        },
    },
    # drinks: olipop, cocacola
    "Drinks": {
        "Olipop": {
            "Ginger Ale": 120,
            "Watermelon Lime": 115,
            "Orange Squeeze": 95,
            "Banana Cream": 120,
            "Ginger Lemon": 95,
            "Cherry Cola": 100,
            "Strawberry Vanilla": 115,
            "Cherry Vanilla": 110,
            "Lemon Lime": 110,
        },
        "Cocacola": {
            "Fanta Blackcurrant": 70,
            "Fanta Passion": 70,
            "Coke Zero": 70,
            "Sprite": 70,
            "Stoney": 70,
            "Coke": 70,
        },
    },
    "KMC Snacks": {
        "Popcorns": {
            "Small": 150,
            "Regular": 210,
            "Large": 285,
        },
        "Potato Crisps": {
            "Small": 190,
            "Regular": 235,
            "XL": 315,
        },
    },
}

# x = json.dumps(concession_stand, indent= 2)
# print(x)