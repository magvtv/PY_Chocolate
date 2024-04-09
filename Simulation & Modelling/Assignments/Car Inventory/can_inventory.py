import turtle
import tkinter as tk
import random

# setting up turtle screenm with the desired dimensions and background color
turtle.setup(width=1450, height=700)
screen = turtle.Screen()
screen.bgcolor('yellow')
screen.title('Car Inventory')

# seting maximum animation speed
turtle.tracer(1, 0)


# defining details for different types of vehicles
sedan_details = """
The following Sedan is in inventory:
    ID: T9H
    Brand: Tesla
    Model: Model S
    Mileage: 85,000
    Price: USD 90,550.00
    Number of doors: 4
"""

suv_details = """
The following SUV is in inventory:
    id: KS3
    Brand: Kia 
    Model: Sportage
    Mileage: 50,000
    Price: USD 31,000.00
    Passenger Capacity: 5
"""

truck_details = """
The following Truck is in inventory:
    ID: M6A
    Brand: Mercedes Benz
    Model: Actros Chassis
    Mileage: 41,000
    Price: USD 17,320.00
"""


# function to set up the screen 
def draw_initial_details():
    # drawing initial details of the vehicle types
    global sedan_details, suv_details, truck_details
    turtle.penup()
    turtle.goto(-630, 300)
    turtle.write("USED VEHICLE INVENTORY", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 290)
    turtle.write("------------------------------", font=("Calibri", 14, "bold"))

    turtle.goto(-630, 190)
    turtle.write(sedan_details, align="left", font=("Arial", 11, "normal"))

    turtle.goto(-630, 50)
    turtle.write(suv_details, align="left", font=("Arial", 11, "normal"))

    turtle.goto(-630, -90)
    turtle.write(truck_details, align="left", font=("Arial", 11, "normal"))
    turtle.hideturtle()


draw_initial_details()

# function to clear the screen 
def clear_screen():
    for turtle_object in turtle.Screen().turtles():
        turtle_object.clear()


# function to differen types of vehicles individually
def draw_sedan():
    global sedan_details
    clear_screen()
    turtle.penup()
    turtle.goto(-630, 300)
    turtle.write("USED SEDAN INVENTORY", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 290)
    turtle.write("------------------------------", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 190)
    turtle.write(sedan_details, align="left", font=("Arial", 11, "normal"))

    # -----------------------------------------------CAR--------------------------------------------------------#
    # parameters
    a = 20
    b = 80
    u = random.random()
    car_length = a + u * (b - a)

    # turtle object
    car = turtle.Turtle()
    # hiding initial turtle
    turtle.ht()

    # lifts the pen of the turtle (car) and moves to starting point, so no drawing occurs
    car.penup()
    car.goto(-100, 0)

    # random colors for vehicle
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()

    # drawing flowers
    draw_flowers()

    # --------------------initialise drawing of car---------------------- #
    car.speed(0)
    car.pendown()
    car.fillcolor(red_amount, green_amount, blue_amount)
    car.begin_fill()
    car.forward(car_length * 4)  # length
    car.left(90)
    car.forward(car_length / 1.175)  # width
    car.left(90)
    car.forward(car_length * 5)
    car.left(90)
    car.forward(car_length / 1.175)
    car.end_fill()
    # wheel1
    car.left(90)
    car.forward(car_length / 1.25)
    car.right(90)
    car.forward(car_length / 8)
    car.fillcolor('black')
    car.begin_fill()
    car.circle(car_length / 3.45)
    car.end_fill()
    # wheel2
    car.back(car_length / 8)
    car.left(90)
    car.forward(car_length * 2.75)
    car.right(90)
    car.forward(car_length / 8)
    car.fillcolor('black')
    car.begin_fill()
    car.circle(car_length / 3.45)
    car.end_fill()
    # --------upper body-----------#
    car.back(car_length / 8)
    car.left(90)
    car.forward(car_length * 1.45)
    car.left(90)
    car.forward(car_length / 1.175)
    car.left(90)
    car.forward(car_length * 0.75)
    # trapezium
    car.right(60)
    car.forward(car_length * 1.35)
    car.left(60)
    car.forward(car_length * 2.15)
    car.left(60)
    car.forward(car_length * 1.35)
    # middle line
    car.left(120)
    car.forward(car_length * 1.7)
    car.left(90)
    car.forward(car_length * 1.185)
    car.right(90)

    car.hideturtle()
    turtle.update()



def draw_suv():
    global suv_details
    clear_screen()
    turtle.penup()
    turtle.goto(-630, 300)
    turtle.write("USED SUV INVENTORY", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 290)
    turtle.write("------------------------------", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 190)
    turtle.write(suv_details, align="left", font=("Arial", 11, "normal"))

    # ----------------------------------------------SUV------------------------------------------------#
    # parameters
    a = 25
    b = 90
    u = random.random()
    suv_length = a + u * (b - a)

    # turtle object
    suv = turtle.Turtle()

    # hiding initial turtle
    turtle.ht()

    # random colors for vehicle
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()

    # drawing flowers
    draw_flowers()

    suv.penup()
    suv.goto(-100, 0)
    # ----------------initialise drawing of suv------------------- #
    suv.speed(0)
    suv.pendown()
    suv.fillcolor(red_amount, green_amount, blue_amount)
    suv.begin_fill()
    suv.forward(suv_length * 5)  # length
    suv.left(90)
    suv.forward(suv_length / 1.175)  # width
    suv.left(90)
    suv.forward(suv_length * 5)
    suv.left(90)
    suv.forward(suv_length / 1.175)
    suv.end_fill()
    # wheel1
    suv.left(90)
    suv.forward(suv_length / 1.25)
    suv.right(90)
    suv.forward(suv_length / 8)
    suv.fillcolor('black')
    suv.begin_fill()
    suv.circle(suv_length / 3.45)
    suv.end_fill()
    # wheel2
    suv.back(suv_length / 8)
    suv.left(90)
    suv.forward(suv_length * 2.75)
    suv.right(90)
    suv.forward(suv_length / 8)
    suv.fillcolor('black')
    suv.begin_fill()
    suv.circle(suv_length / 3.45)
    suv.end_fill()
    # -----------upper body-----------#
    suv.back(suv_length / 8)
    suv.left(90)
    suv.forward(suv_length * 1.45)
    suv.left(90)
    suv.forward(suv_length / 1.175)
    suv.left(90)
    suv.forward(suv_length * 1.6)
    # trapezium
    suv.right(60)
    suv.forward(suv_length * 1.2)
    suv.left(60)
    suv.forward(suv_length * 2.25)
    suv.left(63)
    suv.forward(suv_length * 1.2)
    # back-wheel
    suv.left(27)
    suv.forward(suv_length * 0.085)
    suv.right(90)
    suv.fillcolor('black')
    suv.begin_fill()
    suv.circle((suv_length / 2.95), extent=180)
    suv.end_fill()
    # middle line
    suv.left(90)
    suv.forward(suv_length * 0.785)
    suv.right(90)
    suv.forward(suv_length * 2.49)
    suv.left(90)
    suv.forward(suv_length * 1.075)

    turtle.update()
    suv.hideturtle()


def draw_truck():
    global truck_details
    clear_screen()
    turtle.penup()
    turtle.goto(-630, 300)
    turtle.write("USED TRUCK INVENTORY", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 290)
    turtle.write("------------------------------", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 190)
    turtle.write(truck_details, align="left", font=("Arial", 11, "normal"))
    # --------------------------------------------TRUCK----------------------------------------------#
    # parameters
    a = 30
    b = 95
    u = random.random()
    truck_length = a + u * (b - a)

    # random colors for vehicle
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()

    # turtle object
    truck = turtle.Turtle()

    # hiding initial turtle
    turtle.ht()

    # drawing flowers
    draw_flowers()

    truck.penup()
    truck.goto(-200, 0)
    # --------------------initialise drawing of truck---------------------- #
    truck.speed(0)
    truck.pendown()
    truck.fillcolor(red_amount, green_amount, blue_amount)
    truck.begin_fill()
    truck.forward(truck_length * 4.5)  # length
    truck.left(90)
    truck.forward(truck_length * 2.875)  # width
    truck.left(90)
    truck.forward(truck_length * 4.5)
    truck.left(90)
    truck.forward(truck_length * 2.875)
    truck.end_fill()
    # wheel1
    truck.left(90)
    truck.forward(truck_length / 1.975)
    truck.right(90)
    truck.forward(truck_length / 10.025)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 2.15)
    truck.end_fill()
    # wheel2
    truck.back(truck_length / 10.45)
    truck.left(90)
    truck.forward(truck_length * 1.285)
    truck.right(90)
    truck.forward(truck_length / 7)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 2.095)
    truck.end_fill()
    # trapezium
    truck.back(truck_length / 7.015)
    truck.left(90)
    truck.forward(truck_length * 2.7)
    truck.left(90)
    truck.forward(truck_length * 0.145)
    truck.right(90)
    truck.forward(truck_length * 1.15)
    truck.right(90)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 2.095)
    truck.end_fill()
    truck.left(90)
    truck.forward(truck_length * 1.75)
    truck.left(90)
    truck.forward(truck_length * 1.35)
    truck.left(60)
    truck.forward(truck_length * 1.75)
    truck.left(120)
    truck.forward(truck_length * 0.875)
    truck.left(90)
    truck.forward(truck_length * 1.5)
    truck.left(150)
    truck.forward(truck_length * 1.75)
    truck.left(30)
    truck.forward(truck_length * 1.425)

    truck.hideturtle()
    turtle.update()


def gencolors():
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()
    # normalized RGB values (0 rep. absence of color and 1 represents the maximum intensity of that component)
    return red_amount,green_amount,blue_amount


def draw_flowers():
    turtle.speed(0)
    turtle.ht()
    turtle.penup()
    turtle.goto(500, -150)
    turtle.pendown()

    for i in range(8):
        turtle.penup()
        turtle.left(180)
        turtle.fd(110)
        turtle.pendown()
        turtle.right(180)

        # flower base
        turtle.fillcolor(gencolors())
        turtle.begin_fill()
        turtle.circle(1, 180)
        turtle.circle(2.5, 110)
        turtle.left(50)
        turtle.circle(6, 45)
        turtle.circle(2, 170)
        turtle.right(24)
        turtle.fd(3)
        turtle.left(10)
        turtle.circle(3, 110)
        turtle.fd(2)
        turtle.left(40)
        turtle.circle(9, 70)
        turtle.circle(3, 150)
        turtle.right(30)
        turtle.fd(1.5)
        turtle.circle(8, 90)
        turtle.left(15)
        turtle.fd(4.5)
        turtle.right(165)
        turtle.fd(2)
        turtle.left(155)
        turtle.circle(15, 80)
        turtle.left(50)
        turtle.circle(15, 90)
        turtle.end_fill()

        # Petal 1
        turtle.left(150)
        turtle.circle(-9, 70)
        turtle.left(20)
        turtle.circle(7.5, 105)
        turtle.setheading(60)
        turtle.circle(8, 98)
        turtle.circle(-9, 40)

        # Petal 2
        turtle.left(180)
        turtle.circle(9, 40)
        turtle.circle(-8, 98)
        turtle.setheading(-83)

        # Leaf 1
        turtle.fd(3)
        turtle.left(90)
        turtle.fd(2.5)
        turtle.left(45)
        turtle.fillcolor(gencolors())
        turtle.begin_fill()
        turtle.circle(-8, 90)
        turtle.right(90)
        turtle.circle(-8, 90)
        turtle.end_fill()
        turtle.right(135)
        turtle.fd(6)
        turtle.left(180)
        turtle.fd(8.5)
        turtle.left(90)
        turtle.fd(8)

        # Leaf 2
        turtle.right(90)
        turtle.right(45)
        turtle.fillcolor(gencolors())
        turtle.begin_fill()
        turtle.circle(8, 90)
        turtle.left(90)
        turtle.circle(8, 90)
        turtle.end_fill()
        turtle.left(135)
        turtle.fd(6)
        turtle.left(180)
        turtle.fd(6)
        turtle.right(90)
        turtle.circle(20, 60)

    # Hide turtle
    turtle.hideturtle()


# the main function that deploys all the above declared functions
# Create buttons using tkinter
root = tk.Tk()
root.geometry("280x100")  # Adjusting the window size
root.title("Buttons")

car_button = tk.Button(root, text="See Sedan", command=draw_sedan, width=10, height=2)  
car_button.pack(side=tk.LEFT,padx=6.5, pady=10)

suv_button = tk.Button(root, text="See SUV", command=draw_suv, width=10, height=2)  
suv_button.pack(side=tk.LEFT,padx=6.5, pady=10)

truck_button = tk.Button(root, text="See Truck", command=draw_truck, width=10, height=2)  
truck_button.pack(side=tk.LEFT,padx=6.5, pady=10)

root.mainloop()
