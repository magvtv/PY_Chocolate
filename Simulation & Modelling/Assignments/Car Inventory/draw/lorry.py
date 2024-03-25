from textwrap import fill
import tkinter as tk
import random
import json


class DrawLorry:
    def __init__(self):
        self.canvas = canvas
    
    # function to draw the front view of the lorry
    def draw_front_view(self, canvas):
        self.canvas.create_rectangle(50, 50, 250, 100, fill="blue") 
        
        # draw the windscreen
        self.canvas.create_rectangle(70, 60, 120, 90, fill="lightblue") 
        self.canvas.create_rectangle(140, 60, 190, 90, fill="lightblue")
        
        # Draw headlights
        canvas.create_oval(250, 100, 260, 110, fill="yellow")
        canvas.create_oval(250, 140, 260, 150, fill="yellow")
        
        # draw the wheels
        canvas.create_oval(70, 130, 110, 170, fill="black")
        canvas.create_oval(190, 130, 230, 170, fill="black")
        
        # draw side mirrors (left then right)
        canvas.create_rectangle(40, 65, 50, 75, fill="gray") 
        canvas.create_rectangle(250, 65, 250, 75, fill="gray")
        

    def draw_side_view(self, canvas):
        # Draw lorry body
        canvas.create_rectangle(50, 50, 250, 100, fill="blue")

        # Draw windows
        canvas.create_rectangle(70, 60, 100, 80, fill="lightblue")
        canvas.create_rectangle(150, 60, 180, 80, fill="lightblue")

        # Draw wheels
        canvas.create_oval(70, 100, 100, 130, fill="black")
        canvas.create_oval(200, 100, 230, 130, fill="black")

        # Draw side mirrors
        # canvas.create_rectangle(40, 65, 50, 75, fill="gray")  # Left mirror
        canvas.create_rectangle(250, 65, 260, 75, fill="gray")  # Right mirror
        
        
    def draw_rear_view(self, canvas):
        # Draw lorry body
        canvas.create_rectangle(50, 50, 250, 100, fill="blue")

        # Draw rear window
        canvas.create_rectangle(110, 60, 190, 80, fill="lightblue")

        # Draw wheels
        canvas.create_oval(70, 100, 100, 130, fill="black")
        canvas.create_oval(200, 100, 230, 130, fill="black")

        # Draw side mirrors
        canvas.create_rectangle(40, 65, 50, 75, fill="gray")  # Left mirror
        canvas.create_rectangle(250, 65, 260, 75, fill="gray")  # Right mirror
        
    def draw(self, canvas):
        # draw the body
        canvas.rectangle(50, 50, 250, 100, fill="blue")
        
        # draw the windows
        canvas.create_rectangles(70, 60, 100, 80, fill="lightblue")
        canvas.create_rectangles(150, 60, 180, 80, fill="lightblue")
        
        # draw wheels
        canvas.create_oval(70, 100, 100, 130, fill="black")
        canvas.create_oval(200, 100, 230, 130, fill="black")


def show_next_car(canvas, view):
    canvas.delete("all")
    drawer = DrawLorry()
    if view == 'front':
        drawer.draw_front_view(canvas)
    elif view == 'side':
        drawer.draw_side_view(canvas)
    elif view == 'rear':
        drawer.draw_rear_view(canvas)


root = tk.Tk()
root.title("Car Inventory System")

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

show_next_car_button = tk.Button(root, text="Show Next Car (Front View)", command= lambda: show_next_car(canvas, 'front'))
show_next_car_button.pack()

root.mainloop()